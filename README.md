<h1 align="center">All-in-One University App – Revolutionizing Student Life </h1>

## Overview
All-In-One is a *University Management System* built using *Django (Python), HTML, CSS, and JavaScript*. This project helps manage university-related tasks such as student records, faculty details, course management, and more.

## Features
- *User Authentication* (Admin, Faculty, Students)  
- *Student and Faculty Management*  
- *Course Registration & Management*  
- *Attendance Tracking*  
- *Exam & Results Management*  
- *Notices & Announcements*  
- *Responsive UI*

## Technologies Used
- *Backend:* Python (Django Framework)  
- *Frontend:* HTML, CSS, JavaScript  
- *Database:* SQLite / MySQL (configurable)

## Installation
Follow these steps to set up the project locally:

1. *Clone the repository*
   
   git clone https://github.com/shaikat020/all-in-one-university.git
   cd All-In-One-University
   

2. *Create a virtual environment (optional but recommended)*
   
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   

3. *Install dependencies*
   
   pip install -r requirements.txt
   

4. *Apply migrations*
   
   python manage.py migrate
   

5. *Create a superuser (admin account)*
   
   python manage.py createsuperuser
   

6. *Run the server*
   
   python manage.py runserver
   

7. *Open in browser*
   
   http://127.0.0.1:8000
   

## Project Structure

all-in-one-university/
│-- university_app/
│   ├── migrations/
│   ├── static/
│   ├── templates/
│   ├── views.py
│   ├── models.py
│   ├── urls.py
│   ├── admin.py
│-- db.sqlite3
│-- manage.py
│-- requirements.txt
│-- .gitignore
│-- README.md


## Contributors
Md Rakibul Hassan

## Contributing
Feel free to contribute! Fork the repository, make changes, and submit a pull request.

## License
This project is licensed under the *MIT License*.

## Contact
For queries or suggestions, contact: *tahsin.azad.skt@gmail.com*
