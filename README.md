# 📝 Blog API

## 📌 Overview
The **Blog API** is a RESTful API built with Django and Django REST Framework (DRF). It allows users to create, retrieve, update, and delete blog posts while supporting authentication, pagination, search, and filtering features.

## 🚀 Features
- ✅ **User Authentication** (JWT-based login & registration via Djoser)
- ✅ **Post Management** (Create, Read, Update, Delete blog posts)
- ✅ **Pagination** for optimized API responses
- ✅ **Search & Ordering Filters** for better content retrieval
- ✅ **MultiParsers Support** (handling different content types)
- ✅ **Secure API Endpoints** with JWT authentication

## 🛠️ Tech Stack
- **Backend:** Django, Django REST Framework (DRF)
- **Authentication:** JWT (via Djoser)
- **Database:** PostgreSQL / SQLite
- **Filtering & Pagination:** DRF SearchFilter, OrderingFilter, and built-in pagination

## 📂 Installation & Setup
### 1️⃣ Clone the Repository
```bash
git clone https://github.com/Imperialemmy/blog-api.git
cd blog-api
```

### 2️⃣ Create & Activate Virtual Environment
```bash
python -m venv env
source env/bin/activate  # On Windows use `env\Scripts\activate`
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Run Database Migrations
```bash
python manage.py migrate
```

### 5️⃣ Create Superuser
```bash
python manage.py createsuperuser
```

### 6️⃣ Start the Development Server
```bash
python manage.py runserver
```
The API will be available at `http://127.0.0.1:8000/`.

## 🔑 Authentication
### Obtain Access Token
```bash
POST /api/token/
```
Payload:
```json
{
  "username": "your_username",
  "password": "your_password"
}
```
Response:
```json
{
  "access": "your_access_token",
  "refresh": "your_refresh_token"
}
```

### Use Token for Authenticated Requests
Include the token in your headers:
```bash
Authorization: Bearer your_access_token
```

## 📝 API Endpoints
| Method | Endpoint | Description |
|--------|---------|-------------|
| `POST` | `/api/auth/users/` | Register a new user |
| `POST` | `/api/token/` | Obtain JWT token |
| `GET` | `/api/posts/` | List all blog posts |
| `POST` | `/api/posts/` | Create a new blog post |
| `GET` | `/api/posts/{id}/` | Get details of a blog post |
| `PUT` | `/api/posts/{id}/` | Update a blog post |
| `DELETE` | `/api/posts/{id}/` | Delete a blog post |
| `GET` | `/api/posts/?search=query` | Search blog posts |
| `GET` | `/api/posts/?ordering=-date_created` | Order blog posts by latest |

## 🌍 Deployment
The API is **live** and can be accessed at:
🔗 [Live API URL](#) *(Replace with actual link)*

## 🤝 Contributing
Contributions are welcome! Feel free to fork this repository, open issues, and submit pull requests.

## 📜 License
This project is licensed under the **MIT License**.

---

### 📧 Contact
For any questions or collaborations, reach out via GitHub: [Imperialemmy](https://github.com/Imperialemmy)

---

This README provides all necessary details for users and developers to get started with your Blog API. Let me know if you need any modifications! 🚀

