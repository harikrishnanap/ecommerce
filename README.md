# 🛒 Django Ecommerce Project

A simple ecommerce website built with Django, featuring product categories, search, cart management, and checkout.

## 🚀 Features

- Category-wise product listing
- Product detail pages
- Search functionality
- Add to cart, remove from cart
- Checkout page
- Admin dashboard for product management
- Slug-based SEO URLs
- Pagination support

## 🔧 Tech Stack

- Backend: Django, Python
- Frontend: HTML, CSS, Bootstrap
- Database: SQLite

## 📸 Screenshots

(Add screenshots of homepage, product detail, cart, etc.)

## 📁 Project Structure

```bash
ecommerce/
├── ecommerce/          # Django project folder (settings.py, urls.py, wsgi.py)
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── shop/               # Django app for handling ecommerce logic
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── views.py
│   └── urls.py
│
├── static/             # Static files (CSS, JS, images)
│   └── style.css
│
├── templates/          # HTML templates
│   ├── base.html
│   └── shop/
│       ├── index.html
│       ├── category.html
│       └── product.html
│
├── db.sqlite3          # SQLite DB file
├── manage.py           # Django's CLI utility

