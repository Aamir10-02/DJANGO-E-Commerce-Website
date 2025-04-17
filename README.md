# 🛍️ DjangoShop - Modern E-Commerce Platform  
**A Full-Featured Online Store Built with Django**  


A complete e-commerce solution featuring user authentication, payment processing, order management and admin dashboard. Built with Django and PostgreSQL, deployed on Railway.

**Live Demo:** [https://djangoecom.store/](https://djangoecom.store/)

---

## 🌟 Key Features  
### 👤 User Features  
- 🔐 Secure registration/login with password reset
- 🛒 Shopping cart with persistent storage
- 💳 PayPal & credit card payments integration
- 📦 Order tracking (shipped/unshipped status)
- 📝 Editable user profiles & shipping addresses
- 🔄 Password update functionality

### 🛠️ Admin Features  
- 📊 Dashboard with sales analytics
- 📦 Order management system
- 👥 User management interface
- 📦 Product inventory control
- 🚚 Shipping status updates

---

## 🚀 Deployment  
[![Deploy on Railway](https://railway.app/button.svg)]
**Hosted on [Railway](https://railway.app)** with PostgreSQL database

---

## 🛠️ Installation  

### Prerequisites  
- Python 3.8+
- PostgreSQL
- Virtual Environment

```bash
# Clone repository
git clone https://github.com/Aamir10-02/DJANGO-E-Commerce-Website.git
cd DJANGO-E-Commerce-Website

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate  # Windows

# Install dependencies
pip install -r requirements.txt

# Configure environment
cp .env.example .env
# Update .env with your credentials
Database Setup

python manage.py migrate
python manage.py createsuperuser
Run Locally

python manage.py runserver
Visit http://localhost:8000

⚙️ Configuration
Required Environment Variables (.env):


SECRET_KEY=your_django_secret
DEBUG=True
DB_URL=postgresql://user:password@localhost:5432/dbname
PAYPAL_CLIENT_ID=your_paypal_id
PAYPAL_SECRET=your_paypal_secret
🚂 Railway Deployment
Create new Railway project

Add PostgreSQL plugin

Set environment variables:

SECRET_KEY

DEBUG (False in production)

DATABASE_URL (auto-set by PostgreSQL plugin)

PAYPAL_CLIENT_ID

PAYPAL_SECRET

Deploy!

🖥️ Usage
User Registration

Create account → Verify email → Login

Shopping Experience

Browse products → Add to cart → Checkout → Payment

Profile Management

Update personal info → Change password → Manage addresses

Admin Dashboard

/admin → Manage orders, users, products

🧩 Tech Stack
Backend: Django, Python

Database: PostgreSQL

Frontend: HTML, CSS, JAVASCRIPT

Payments: PayPal REST API

Hosting: Railway

Security: CSRF protection, password hashing



📜 License
MIT License - See LICENSE for details

🙏 Acknowledgments
Django Software Foundation

PayPal Developer Network

Bootstrap Community

Railway Deployment Platform

Created with ❤️ by Aamir Saiyad