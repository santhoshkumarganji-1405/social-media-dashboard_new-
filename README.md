# 📊 Social Media Analytics Dashboard

A simple web-based dashboard built using **Flask** and **MySQL** to track social media users, posts, and engagement metrics.

---

## 🚀 Features

* 📈 Dashboard showing:

  * Total Users
  * Total Posts
  * Average Engagement (Likes + Comments + Shares)
* 👤 Add new users
* 📝 Add new posts
* ❤️ Track engagement (likes, comments, shares)
* 🔄 Real-time updates using Flask routes

---

## 🛠️ Technologies Used

* Python
* Flask
* MySQL
* PyMySQL
* HTML (Templates)

---

## 📂 Project Structure

```
project/
│── app.py
│── templates/
│     └── max.html
│── static/
│── database.sql
│── README.md
```

---

## ⚙️ Installation & Setup

### 1. Clone the repository

```
git clone https://github.com/your-username/social-media-dashboard.git
cd social-media-dashboard
```

### 2. Install dependencies

```
pip install flask pymysql
```

### 3. Setup MySQL Database

Create a database:

```
CREATE DATABASE socialmedia;
```

Create tables:

```
CREATE TABLE users (
    user_id INT PRIMARY KEY,
    username VARCHAR(50),
    email VARCHAR(100),
    country VARCHAR(50),
    join_date DATE
);

CREATE TABLE posts (
    post_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    content TEXT,
    post_date DATETIME,
    hashtags VARCHAR(255)
);

CREATE TABLE engagement (
    id INT AUTO_INCREMENT PRIMARY KEY,
    post_id INT,
    likes INT,
    comments INT,
    shares INT
);
```

---

### 4. Update Database Credentials

In `app.py`, update:

```
db = pymysql.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="socialmedia"
)
```

---

### 5. Run the application

```
python app.py
```

Open in browser:

```
http://127.0.0.1:5000/
```

---

## 📊 Dashboard Overview

* Total Users → Count from users table
* Total Posts → Count from posts table
* Engagement → Average of likes + comments + shares

---

## 🔮 Future Improvements

* User authentication (login/signup)
* Data visualization (charts using Chart.js)
* Edit/Delete functionality
* API integration
* Deployment on cloud (Heroku / AWS)

---

## 🤝 Contributing

Feel free to fork this repo and improve the project.

---

## 📄 License

This project is open-source and free to use.

---

## 👨‍💻 Author

**Santhosh Ganji**

---

⭐ If you like this project, don't forget to star the repo!
