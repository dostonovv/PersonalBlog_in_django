📁 README.md

# 🧠 Zoirjon's Personal Blog – Django

This is my personal blog project built using Django, designed to be an independent space where I express my thoughts, experiences, and technical journey.  
Unlike standard platforms like Telegram or Medium, this blog lives on my own infrastructure, eventually to be hosted on a Raspberry Pi home server.

## 🧩 Features

- ✍️ Write and publish posts from Django Admin
- 🔎 Search functionality
- ✅ Reactions for each post (like Telegram emojis)
- 🔐 Admin-only access (private dashboard)
- 🎨 Clean, minimalistic frontend (with Tailwind in future updates)
- 🔄 Soon to be open for comments (currently planned)
- ⚙️ Will be integrated into personal server in future (self-hosted setup)

## 🔭 Vision

> "This blog is a living archive of my thoughts —  
> a mirror of my brain. One day, my children or grandchildren  
> will be able to read it and feel like they’re speaking to me."

My ultimate goal is to make this part of my digital legacy and contribute to open-source knowledge.  

## 🚀 Tech Stack

- Backend: Python, Django
- Frontend: HTML/CSS (Tailwind CSS coming soon)
- Database: SQLite (will upgrade to PostgreSQL)
- Hosting: GitHub Pages (temporary) → Raspberry Pi (planned)
- Future Tools: Arduino, Sensors, AIogram for automation bots

## 🛠 Setup

`bash
# Clone the repository
git clone https://github.com/dostonovv/PersonalBlog_in_django.git

# Create virtual environment
python -m venv venv
source venv/bin/activate  # For Windows: venv\Scripts\activate

# Install requirements
pip install -r requirements.txt

# Run the server
python manage.py migrate
python manage.py runserver

Then open your browser and go to:
http://127.0.0.1:8000/

👤 Admin Panel

Accessible at:
http://127.0.0.1:8000/admin/
(Create a superuser with: python manage.py createsuperuser)

📜 License

MIT © Zoirjon Dostonov
See LICENSE for full details.
