# Quickbite

A Django web application simulating an online food ordering system. This backend-focused project is currently in progress and serves as a learning platform for Django development.

## Features (Current)

- Django project scaffolded with reusable app structure
- Admin dashboard setup
- Models and views for Restaurants and Menu Items
- URL routing for browsing restaurant menus

## Upcoming Features

- Users can start an order session
- Add/remove items from cart
- Checkout and view previous orders
- Order management via admin panel

## Tech Stack

- Python
- Django
- SQLite (development)
- HTML/CSS (basic for now)

## Project Structure

```
quickbite/
├── manage.py
├── db.sqlite3
├── restaurants/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── admin.py
│   └── templates/
├── quickbite/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── README.md
```

## Setup Instructions

1. Clone the repository:
   ```
   git clone https://github.com/npancini/quickbites.git
   cd quickbites
   ```

2. Create a virtual environment and install Django:
   ```
   python3 -m venv venv
   source venv/bin/activate
   pip install django
   ```

3. Run migrations and start the server:
   ```
   python manage.py migrate
   python manage.py runserver
   ```

4. Open your browser and go to `http://127.0.0.1:8000/`

## Learning Goals

- Practice Django’s MVT architecture
- Work with model relationships
- Implement order/cart logic and form validation
- Build scalable backend systems