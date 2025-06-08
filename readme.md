# 🕑 Symplique Solutions - Reminder API

A Django REST Framework-based API for user registration, authentication, and personal reminders.

---

## 🚀 Features

- **User Registration:** Register new users and receive an authentication token.
- **Token Authentication:** Secure endpoints using DRF's token authentication.
- **Create Reminders:** Authenticated users can create reminders (email or SMS type).
- **View Reminders:** Authenticated users can view their own reminders.
- **Admin Panel:** Manage reminders and users via Django admin.

---

## 🗂️ Project Structure

```
.
├── api/
│   └── urls.py
├── core/
│   ├── settings.py
│   └── urls.py
├── home/
│   ├── admin.py
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   └── migrations/
├── db.sqlite3
├── manage.py
├── requirements.txt
├── readme.md
└── .gitignore
```

---

## ⚙️ Requirements

- Python 3.8+
- Django 5.2.2
- djangorestframework 3.16.0

Config venv and activate
```sh 
python -m venv venv
venv/Script/activate
```
Install all dependencies:

```sh
pip install -r requirements.txt
```

---

## 🛠️ Setup & Usage

1. **Apply Migrations**
    ```sh
    python manage.py migrate
    ```

2. **Create a Superuser** (optional, for admin access)
    ```sh
    python manage.py createsuperuser
    ```

3. **Run the Development Server**
    ```sh
    python manage.py runserver
    ```

- **API root:** [http://127.0.0.1:8000/api/](http://localhost:8000/api/)
- **Admin panel:** [http://127.0.0.1:8000/admin/](http://localhost:8000/admin/)

---

## 📚 API Endpoints

| Endpoint                | Method | Description             | Auth Required |
|-------------------------|--------|-------------------------|--------------|
| `/api/register/`        | POST   | Register a new user     | No           |
| `/api/login/`           | POST   | Obtain auth token       | No           |
| `/api/reminder/`        | GET    | List your reminders     | Yes          |
| `/api/reminder/create/` | POST   | Create a new reminder   | Yes          |

---

## 💡 Usage Examples

### Register

```http
POST /api/register/
Content-Type: application/json

{
  "username": "testuser",
  "email": "test@example.com",
  "password": "yourpassword"
}
```

**Response**
```json
{
  "message": "User created",
  "token": "yourauthtoken"
}
```

---

### Login

```http
POST /api/login/
Content-Type: application/json

{
  "username": "testuser",
  "password": "yourpassword"
}
```

**Response**
```json
{
  "token": "yourauthtoken"
}
```

---

### Create Reminder

```http
POST /api/reminder/create/
Authorization: Token yourauthtoken
Content-Type: application/json

{
  "message": "Doctor appointment",
  "date": "2024-06-10",
  "time": "15:00:00",
  "reminder_type": "email"
}
```

---

### List Reminders

```http
GET /api/reminder/
Authorization: Token yourauthtoken
```

**Response**
```json
[
  {
    "message": "Doctor appointment",
    "date": "2024-06-10",
    "time": "15:00:00",
    "reminder_type": "email"
  }
]
```

---

## 📝 Models

See [`home.models.ReminderModel`](home/models.py) for the reminder schema.

---

## 🛡️ Admin

- Reminders are manageable via the Django admin at `/admin/`.
- See [`home.admin.ReminderModelAdmin`](home/admin.py).

---

## ⚙️ Settings

- Token authentication is enabled by default in `core/settings.py`.
- Timezone is set to `Asia/Kolkata`.

---


