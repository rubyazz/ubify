# Project Name: Ubify
## Overview
This project aims to create a personalized music service, similar to Spotify. It is built using Django, Docker, FastAPI, Celery, DRF, Pillow, django-ckeditor, and grappeli. The application allows users to search for songs and albums, create playlists, and pay for premium features. It also provides a platform for artists to showcase their music, create profiles, and interact with their fans.

## Features

- User authentication using JWT tokens
- Search functionality for songs and albums
- Payment gateway integration
- Custom user models with different roles (singer, listener)
- Profile management for singers
- Likes functionality for users
- APIs for artists, albums, songs, and likes
- Admin panel for managing users, songs, and albums

## Technologies Used

- **Django**: A Python-based web framework for building web applications
- **FastAPI**: A modern, fast (high-performance) web framework for building APIs
- **Celery**: A task queue used for asynchronous processing
- **DRF**: A powerful and flexible toolkit for building APIs
- **Pillow**: A Python Imaging Library that adds image processing capabilities to your Python interpreter
- **django-ckeditor**: A rich text editor for Django
- **grappeli**: A customizable, responsive, and lightweight administrative interface for Django

## Installation and Usage

To run the project locally, follow these steps:

1. Clone the repository to your local machine.
2. Install the dependencies using `pip install -r requirements.txt`
3. Create a PostgreSQL database.
4. Set up the environment variables in a `.env` file.
5. Migrate the database using `python3 manage.py migrate`
6. Create a superuser account using `python3 manage.py createsuperuser`
7. Start the development server using `python3 manage.py runserver`

## APIs
The project provides the following APIs:

- `/api/token/`: Token Obtain Pair API for user authentication
- `/users/api/register/`: User registration API
- `/api/general/`: API for retrieving all singers, albums, and songs
- `/api/artists/list/`: API for retrieving all singers
- `/api/albums/list/`: API for retrieving all albums
- `/api/songs/list/`: API for retrieving all songs
- `/users/api/likes/`: API for retrieving all liked songs of a user

## Contributing
We welcome contributions from anyone who is interested in improving this project. If you'd </br> like to contribute, please follow these steps:

1. Fork the repository to your own GitHub account.
2. Create a new branch for your feature or bugfix.
3. Write your code and tests.
4. Submit a pull request explaining your changes.

## License
This project is licensed under the MIT License. Feel free to use, modify, and distribute the </br> code as you see fit.
