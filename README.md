# 📖 SocialSync

A Django-based social media platform where users can register, follow others, and engage with posts through likes and comments.

## 🚀 Features
- 🔹 User authentication (login/logout/signup)
- 🔹 User profile creation
- 🔹 Follow/unfollow functionality
- 🔹 Post creation & feed display
- 🔹 Comments and likes on posts
- 🔹 Suggested users to follow

##  Installation & Setup

1. **Clone the repository**  
   ```bash
   git clone https://github.com/your-username/social_book.git
   cd social_book

2. **Create & activate a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # macOS/Linux
   venv\Scripts\activate     # Windows

3. **Apply database migrations**
   ```bash
   python manage.py migrate

4. **Run the development server**
   ```bash
   python manage.py runserver

The app will be available at http://127.0.0.1:8000/.
