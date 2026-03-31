from flask import Flask, render_template, request, redirect
import pymysql

app = Flask(__name__)

# Database connection
db = pymysql.connect(
    host="localhost",
    user="root",
    password="Mysql@123",
    database="socialmedia"
)


# -------------------------------
# DASHBOARD
# -------------------------------
@app.route("/")
def max():

    cursor = db.cursor()

    # Total users
    cursor.execute("SELECT COUNT(*) FROM users")
    user_count = cursor.fetchone()[0]

    # Total posts
    cursor.execute("SELECT COUNT(*) FROM posts")
    post_count = cursor.fetchone()[0]

    # Total engagement
    cursor.execute("SELECT AVG(likes + comments + shares) FROM engagement")
    engagement = cursor.fetchone()[0]

    if engagement is None:
        engagement = 0 

    return render_template(
        "max.html",
        user_count=user_count,
        post_count=post_count,
        engagement=engagement
    )


# -------------------------------
# ADD USER
# -------------------------------
@app.route("/add_user", methods=["POST"])
def add_user():

    user_id = request.form["user_id"]
    username = request.form["username"]
    email = request.form["email"]
    country = request.form["country"]
    join_date = request.form["join_date"]

    cursor = db.cursor()

    sql = """
    INSERT INTO users (user_id, username, email, country, join_date)
    VALUES (%s,%s,%s,%s,%s)
    """

    values = (user_id, username, email, country, join_date)

    cursor.execute(sql, values)
    db.commit()

    return redirect("/")


# -------------------------------
# ADD POST
# -------------------------------
@app.route("/add_post", methods=["POST"])
def add_post():

    user_id = request.form["user_id"]
    content = request.form["content"]
    hashtags = request.form["hashtags"]

    cursor = db.cursor()

    sql = """
    INSERT INTO posts (user_id, content, post_date, hashtags)
    VALUES (%s,%s,NOW(),%s)
    """

    values = (user_id, content, hashtags)

    cursor.execute(sql, values)
    db.commit()

    return redirect("/")


# -------------------------------
# ADD ENGAGEMENT
# -------------------------------
@app.route("/add_engagement", methods=["POST"])
def add_engagement():

    post_id = request.form["post_id"]
    likes = request.form["likes"]
    comments = request.form["comments"]
    shares = request.form["shares"]

    cursor = db.cursor()

    sql = """
    INSERT INTO engagement (post_id, likes, comments, shares)
    VALUES (%s,%s,%s,%s)
    """

    values = (post_id, likes, comments, shares)

    cursor.execute(sql, values)
    db.commit()

    return redirect("/")


# -------------------------------
# RUN SERVER
# -------------------------------
if __name__ == "__main__":
    app.run(debug=True)