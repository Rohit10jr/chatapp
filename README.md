# Django FullChat Project

![Django](https://img.shields.io/badge/Django-4.x-brightgreen)
![Python](https://img.shields.io/badge/Python-3.x-blue)
![Channels](https://img.shields.io/badge/Channels-4.x-orange)
![License](https://img.shields.io/badge/License-MIT-red)

The Django Chatrooms Project is a real-time chat application built with Django Channels and WebSockets. It provides a modern and interactive way for users to engage in group chats in real-time.

![Chatrooms Project Screenshot](/screenshot.png)

## Table of Contents

1. [Features](#features)
2. [Getting Started](#getting-started)
   - [Installation](#installation)
   - [Configuration](#configuration)
3. [Usage](#usage)
4. [Contributions](#contributions)
5. [License](#license)
6. [Acknowledgments](#acknowledgments)
7. [Contact](#contact)

## Features

- **Real-Time Chat:** Engage in real-time group chats with multiple users.
- **User Authentication:** Secure registration, login, and user profile management.
- **Multiple Chatrooms:** Create, join, and manage chatrooms for various topics.
- **Message History:** View chat history and scroll through previous messages.
- **User Typing Indicator:** See when other users are typing in real-time.
- **Customizable:** Add or modify chatrooms and personalize user profiles.
- **Responsive Design:** Access the chatrooms from different devices.

## Getting Started

Follow these steps to get your Django Chatrooms Project up and running:


### Installation

1. Clone the repository:
```
git clone https://github.com/Rohit10jr/fullchat.git
```
2. Create a virtual environment and activate it:
```
python -m venv venv
source venv/bin/activate
```
3. Install the project dependencies:
```
pip install -r requirements.txt
```
4. Apply database migrations:
```
python manage.py migrate
```
5. Start the development server:
```
python manage.py runserver
```
6. Access the chatrooms at http://localhost:8000.

## Configuration

Customize your project settings by modifying the chatrooms/settings.py file. This includes database settings, WebSocket configuration, and other options.

## Usage

Register and log in to create your user profile.
Explore existing chatrooms and join them.
Engage in real-time conversations with other users in your chatroom.
Create your chatroom or manage existing ones.
View message history and see when others are typing in real-time.

## Contributions

Contributions to the Django Chatrooms Project are welcome. To contribute, please follow these guidelines:
Fork the repository and create a new branch for your feature or bug fix.
Submit a pull request with a detailed description of your changes.

## Acknowledgments

This project was developed using Django, Channels, and WebSockets, taking inspiration from various open-source chat applications.
