# 🛒 Ecommerce Django Project

A full-stack ecommerce web application built using **Django**. Users can browse products, add them to cart, and place orders. Admins can manage products and orders from the Django admin panel.

---

## 🚀 Features

* 🏬 Product listing & detail pages
* 🔍 Category filtering
* 🛒 Add to Cart / Update Cart / Remove Items
* 💳 Checkout system
* 📦 Order creation with OrderItems
* 👤 User authentication (login required for cart & checkout)
* 🧑‍💼 Admin panel with order + product management
* 📱 Fully responsive UI (mobile + desktop)

---

## 🖼️ Screenshots

> 📌 Replace these with your actual screenshots (save images inside a `/screenshots` folder)

### 🏠 Home Page

![Home](screenshots/home.png)

### 📦 Product Page

![Product](screenshots/product.png)

### 🛒 Cart Page

![Cart](screenshots/cart.png)

### ✅ Order Success

![Success](screenshots/success.png)

---

## 🛠️ Tech Stack

* **Backend:** Django (Python)
* **Frontend:** HTML, CSS, Bootstrap
* **Database:** SQLite (default)
* **Authentication:** Django Auth

---

## ⚙️ Installation

```bash
# Clone the repository
git clone https://github.com/Usman851/ecommerce-django.git
cd ecommerce-django

# Create virtual environment
python -m venv env

# Activate env (Windows)
env\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py makemigrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Run server
python manage.py runserver
```

---

## 🔐 Admin Panel

Access admin at:

```
http://127.0.0.1:8000/admin/
```

You can:

* Add products
* View orders
* See ordered items inside each order

---

## 📁 Project Structure

```
ecommerce-django/
│
├── store/            # Main app
├── templates/        # HTML templates
├── static/           # CSS, JS, images
├── media/            # Uploaded product images
├── db.sqlite3        # Database (ignored in git)
├── manage.py
└── requirements.txt
```

---

## 🧪 Future Improvements

* 💳 Payment integration (Razorpay/Stripe)
* ❤️ Wishlist feature
* 🔎 Advanced search & filters
* 📦 Order tracking system
* 📧 Email notifications

---

## 🤝 Contributing

Pull requests are welcome. For major changes, please open an issue first.

---

## 📄 License

This project is open-source and free to use.

---

## 👨‍💻 Author

**Shaik Usman**

* GitHub: [https://github.com/Usman851](https://github.com/Usman851)

---

## ⭐ Support

If you like this project, give it a ⭐ on GitHub!
