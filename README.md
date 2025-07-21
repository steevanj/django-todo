````markdown
# 📝 Django TODO App

A simple TODO web application built with Django, where users can:

- ✍️ Sign up and log in
- ✅ Add daily tasks
- 🛠️ Edit existing tasks
- ❌ Delete tasks
- 🔐 Sign out securely

---

## 🚀 Features

- User authentication (signup, login, logout)
- Add, edit, delete tasks
- User-specific task filtering
- Bootstrap-based responsive UI

---

## 🛠️ Tech Stack

- Python 3.x
- Django 5.x
- SQLite (default)
- HTML, Bootstrap 5

---

## ⚙️ Installation

1. **Clone the Repository**

```bash
git clone https://github.com/steevanj/django-todo.git
cd django-todo
````

2. **Create Virtual Environment**

```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

3. **Install Dependencies**

```bash
pip install -r requirements.txt
```

4. **Run the Server**

```bash
python manage.py migrate
python manage.py runserver
```

5. Visit `http://127.0.0.1:8000` in your browser 🎉

---

## 🧪 Sample Credentials (optional)

You can create your own account or register a test user during signup.

---

## 📁 Project Structure

```
django-todo/
├── todoapp/              # Main app with views/models
├── templates/            # HTML files (login, signup, todo)
├── static/               # CSS files
├── db.sqlite3            # Database file
├── manage.py             # Django management script
├── requirements.txt      # Python dependencies
└── .gitignore            # Ignored files
```

---

## 🛡️ License

This project is licensed under the MIT License.

---

## 🙋‍♂️ Author

**Steevan J**
Passionate Django Developer 💻 | [GitHub](https://github.com/steevanj)

---

## 🌟 Show some love
