# VITTS

VITTS is a web application designed to support visually impaired teachers in monitoring and managing classroom dynamics effectively. VITTS intelligently identifies specific student actions such as standing, sleeping, or raising hands, and provides auditory feedback to the teacher via Text-to-Speech (TTS) technology.

## Features

 - **Action Detection**: Utilizes YOLOv5 computer vision model to detect the appropriate actions or behaviours of students in videos.
 - **Student Action Identification**: Identifies specific student actions such as standing, sleeping, or raising hands.
 - **Auditory Feedback**: Provides auditory feedback to the teacher via Text-to-Speech (TTS) technology.
 - **Web Interface**: User-friendly web interface for easy interaction.

## Installation

1. Clone the repository:
   git clone https://github.com/your_username/visually_impaired.git
2. Install dependencies:
   pip install -r requirements.txt


3. Set up the MySQL database:

 - Install and start XAMPP.
 - Access phpMyAdmin through your web browser (usually at `http://localhost/phpmyadmin`).
 - Create a new database named `vitts`.
 - Update database settings in `settings.py` file to use the appropriate database credentials.

4. Start both the Apache and MySQL servers:

 - Open XAMPP control panel.
 - Start both the Apache and MySQL servers from the control panel.

5. Run migrations:
   python manage.py migrate

6. Start the development server:
   python manage.py runserver

7. Access the web application at `http://localhost:8000` in your browser.

## Usage

1. Log in to the VITTS web application using your credentials.
2. Navigate to the Upload section and upload your video.
3. VITTS will begin monitoring classroom dynamics in real-time.
4. Receive auditory feedback regarding specific student actions.

## Technologies Used

VITTS utilizes the following technologies:

- **Python**: Programming language used for backend development.
- **Django**: Web framework used for building the web application.
- **JavaScript**: Programming language used for frontend interactions.
- **HTML/CSS**: Markup and styling languages used for designing the user interface.
- **MySQL**: Relational database management system used for data storage.
- **XAMPP**: Apache distribution containing MySQL, PHP, and Perl used for local development environment setup.
- **YOLOv5**: State-of-the-art object detection model used for real-time monitoring of classroom dynamics.










