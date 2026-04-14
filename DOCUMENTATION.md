# MyBlog - Project Documentation 🚀

Welcome to the official documentation for **MyBlog**, a premium blogging platform built with Django. This document provides a comprehensive guide to understanding, installing, and extending the MyBlog ecosystem.

---

## 1. Project Overview

### Project Name: MyBlog
**MyBlog** is a modern, high-performance web application designed for writers and readers. It prioritizes user experience through a "premium" aesthetic while maintaining robust backend functionality.

*   **Purpose**: To provide a clean, distraction-free environment for sharing insights and stories.
*   **Problem Solved**: Replaces cluttered, generic blogging platforms with a sleek, social-media-inspired interface that supports real-time interaction (likes) and community building (comments).
*   **Key Features**:
    *   **Post CRUD**: Full lifecycle management of blog entries.
    *   **Dynamic Likes**: Heart-based liking system with AJAX real-time updates.
    *   **Comment Threads**: Nested discussions on every post.
    *   **User Identities**: Personalized profiles with bios and dynamic avatars.
    *   **Advanced Search**: Topic and author discovery via a sleek search interface.

---

## 2. Technology Stack

### Backend
*   **Django 5.1.7**: The primary web framework (Python).
*   **Django-Decouple**: For secure environment variable management.
*   **WhiteNoise**: For efficient serving of static files in production.

### Frontend
*   **HTML5 & CSS3**: Custom styles with advanced CSS variables and glassmorphism.
*   **Bootstrap 5.3**: For responsive layout grids.
*   **Google Fonts**: *Outfit* (Headings) and *Inter* (Body).
*   **JavaScript (Fetch API)**: For asynchronous (AJAX) interactions.

### Database
*   **SQLite**: Development database.
*   **PostgreSQL**: Recommended production database (via `dj-database-url`).

---

## 3. System Architecture

MyBlog follow the standard **MVT (Model-View-Template)** architecture:

1.  **Request**: User clicks a button (e.g., "Like").
2.  **URL Dispatcher**: Matches the request to a specific view in `blog/urls.py`.
3.  **View**: `blog/views.py` processes logic, interacts with the Database through Models.
4.  **Model**: `blog/models.py` handles the data structure and business logic.
5.  **Template**: Django renders the HTML using data from the view and returns it to the client.

---

## 4. Project Structure

```text
My_Blog_Django-main/
├── blog/                   # Main Application Folder
│   ├── migrations/         # Database migration files
│   ├── models.py           # Database schemas (Post, Profile, Comment)
│   ├── views.py            # Business logic and request handling
│   ├── urls.py             # App-specific URL routing
│   ├── forms.py            # Form definitions for posts and contact
│   └── ...
├── myblog/                 # Project Configuration Folder
│   ├── settings.py         # Global settings (DB, Middleware, Apps)
│   ├── urls.py             # Main URL routing
│   ├── wsgi.py             # Web Server Gateway Interface
│   └── ...
├── static/                 # CSS, Images, and JS
├── templates/              # HTML files (base, blog, accounts)
├── .env                    # Secret environment variables (Ignored by Git)
├── manage.py               # Django utility command line tool
├── requirements.txt        # List of Python dependencies
└── README.md               # Quick-start guide
```

---

## 5. Installation and Setup Guide

### Prerequisites
*   Python 3.10+
*   pip (Python package manager)

### Step-by-Step Setup
1.  **Clone the Repo**:
    ```bash
    git clone https://github.com/surendrareddysabbella9-bot/MyBlog.git
    cd My_Blog_Django-main
    ```
2.  **Create Virtual Environment**:
    ```bash
    python -m venv venv
    venv\Scripts\activate  # Windows
    source venv/bin/activate  # macOS/Linux
    ```
3.  **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```
4.  **Set Up Environment**: Create a `.env` file and add your `SECRET_KEY`.
5.  **Run Migrations**:
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```
6.  **Start Server**:
    ```bash
    python manage.py runserver
    ```

---

## 6. Configuration

### settings.py Details
*   **Decoupled Keys**: All sensitive data is fetched using `config()`.
*   **Static/Media**: 
    *   `STATIC_ROOT` is set to `staticfiles/`.
    *   `MEDIA_ROOT` handles user-uploaded profile pictures in `media/profile_pics/`.
*   **WhiteNoise**: Middleware is injected to handle static files without a separate web server like Nginx during deployment.

---

## 7. Application Workflow

### Authentication Flow
1.  User visits `/register/` and creates an account.
2.  Django encrypts and saves the user.
3.  User logs in via `/login/`.
4.  Upon login, a `Profile` model is automatically accessed/created via `get_or_create` in the profile view.

### The "Like" Lifecycle
1.  User clicks the Heart button.
2.  JavaScript (Fetch) sends a POST request to `/post/<id>/like/`.
3.  The view toggles the user's presence in the `likes` ManyToMany field.
4.  The view returns a JSON response with the updated count.
5.  JavaScript updates the UI instantly without page reload.

---

## 8. Database Design (Models)

| Model | Key Fields | Purpose |
| :--- | :--- | :--- |
| **User** | username, password, email | Default Django auth model. |
| **Profile** | user (OneToOne), bio, picture | Extends user data for blog identity. |
| **Post** | author, title, content, likes | The core blog content entity. |
| **Comment** | post, author, content | Feedback and discussion engine. |

---

## 9. Deployment Guide (Render)

1.  **Build Command**:
    ```bash
    pip install -r requirements.txt && python manage.py collectstatic --no-input && python manage.py migrate
    ```
2.  **Start Command**:
    ```bash
    gunicorn myblog.wsgi:application
    ```
3.  **Common Issue**: `ModuleNotFoundError: No module named 'app'`.
    *   **Fix**: Ensure your start command points to `myblog.wsgi`, NOT `app:app`.

---

## 10. Future Enhancements
*   **Social Auth**: Allow login via Google/GitHub.
*   **Rich Text Editor**: Integrated CKEditor for beautiful post drafting.
*   **Newsletter**: Email integration to notify followers of new posts.

---

## 11. Conclusion
**MyBlog** is a robust foundation for a professional blogging network. By combining Django's powerful backend with a bespoke, CSS-driven frontend, it delivers a state-of-the-art experience out of the box.

Documentation authored by **Antigravity AI** for **Surendra Reddy Sabbella**.
