# 🏥 Hospital Administration System

A full-stack web application to manage hospital operations including staff management, appointment booking, and attendance tracking — built with Python, Flask, and MySQL.

-----

## 🚀 Live Demo

> 🔗 [Coming Soon — Deploying on Render](#)

-----

## 📌 Features

- 🔐 **Role-Based Authentication** — Separate dashboards for Admin, Doctor, and Staff
- 📋 **Patient Management** — Add, update, and view patient records
- 📅 **Appointment Scheduling** — Book and manage appointments with automated workflows
- 👨‍⚕️ **Staff Management** — Manage doctor and staff profiles and assignments
- 📊 **Admin Dashboard** — Overview of hospital operations at a glance
- 📱 **Responsive UI** — Works across desktop and mobile devices

-----

## 🛠️ Tech Stack

|Layer   |Technology                               |
|--------|-----------------------------------------|
|Backend |Python, Flask                            |
|Database|MySQL, SQLAlchemy                        |
|Frontend|HTML5, CSS3, Bootstrap                   |
|Auth    |Session-based / Role-Based Access Control|
|Tools   |Git, VS Code                             |

-----

## 📂 Project Structure

```
Hospital-Administrations/
│
├── app.py                  # Main Flask application
├── models.py               # Database models (SQLAlchemy)
├── requirements.txt        # Python dependencies
│
├── templates/              # HTML templates
│   ├── admin/
│   ├── doctor/
│   └── staff/
│
├── static/                 # CSS, JS, Images
│   ├── css/
│   └── js/
│
└── README.md
```

-----

## ⚙️ Getting Started

### Prerequisites

- Python 3.8+
- MySQL
- pip

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/NithishKumar420/Hospital-Administrations.git
cd Hospital-Administrations

# 2. Install dependencies
pip install -r requirements.txt

# 3. Configure your database
# Update DB credentials in app.py or config.py

# 4. Run the application
python app.py
```

Then open your browser and go to `http://localhost:5000`

-----

## 👤 Default Login Credentials (Demo)

|Role  |Username|Password |
|------|--------|---------|
|Admin |admin   |admin123 |
|Doctor|doctor  |doctor123|
|Staff |staff   |staff123 |


> ⚠️ Change credentials before deploying to production!

-----

## 📸 Screenshots

> *(Add screenshots of your dashboard, login page, and patient management screen here)*

-----

## 🙋‍♂️ Author

**Nithish Kumar P**

- 🌐 Portfolio: [freelancerportfoliowebsiteexample.netlify.app](https://freelancerportfoliowebsiteexample.netlify.app)
- 💼 GitHub: [@NithishKumar420](https://github.com/NithishKumar420)
- 📧 Email: litnithish@gmail.com

-----

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

-----

⭐ If you found this project useful, please consider giving it a star!