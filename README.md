# 🧠 Zoirjon's Personal Blog – Django

This is my personal blog project built using Django — an independent space where I express my thoughts, experiences, and technical journey.  
Unlike standard platforms like Telegram or Medium, this blog lives on my own infrastructure, and will soon be hosted on a Raspberry Pi home server.

---

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Django](https://img.shields.io/badge/Django-5.0-green)
![License](https://img.shields.io/badge/License-MIT-yellow)

---

## 🧩 Features

- ✍️ Write and publish posts from Django Admin
- 🔎 Search functionality
- ✅ Reactions for each post (like Telegram emojis)
- 🔐 Admin-only access (private dashboard)
- 🎨 Clean, minimalistic frontend (Tailwind CSS planned)
- 💬 Comments system (coming soon)
- ⚙️ Self-hosted setup on Raspberry Pi (planned)

---

## 🔭 Vision

> "This blog is a living archive of my thoughts —  
> a mirror of my brain. One day, my children or grandchildren  
> will be able to read it and feel like they’re speaking to me."

My ultimate goal is to make this part of my digital legacy and contribute to open-source knowledge.

---

## 🚀 Tech Stack

- **Backend**: Python, Django
- **Frontend**: HTML, CSS (Tailwind CSS planned)
- **Database**: SQLite (PostgreSQL planned)
- **Hosting**: GitHub Pages → Raspberry Pi (future)
- **Future Integration**: Arduino, Sensors, AIOgram (bots, automation)

---

## 🛠 Setup

```bash
# Clone the repository
git clone https://github.com/dostonovv/PersonalBlog_in_django.git

# Navigate into project directory
cd PersonalBlog_in_django

# Create virtual environment
python -m venv venv
# Activate (Windows)
venv\Scripts\activate
# or (Linux/macOS)
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Apply migrations
python manage.py migrate

# Run the server
python manage.py runserver
