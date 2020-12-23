# CS50x final project
This application is my final project for the course CS50x by Harvard.
After submission, I will continue to work on this project to add features and other enhancements.

## Description
(no-name) is a self-hosted web app that allows you to create an online image gallery and securely share it with friends and family.
No passwords are required, you only need an e-mailaddress to login.
It was made with sharing pictures of your children in mind, but can also be used as regular image gallery.

## Tech stack
- Python
- Flask
- Bootstrap
- PostgreSQL

## Features

### v0.1 goals
- [X] allow admin to invite users via their own email address
- [X] protect main page
- [X] main page displays pictures from a folder, using [masonry](https://masonry.desandro.com/)
- [x] display pictures chronologically
- [ ] allow family and friends to upload individual pictures/videos from gallery view
- [ ] use wsgi server on own server / Heroku to host application


### expansion goals

- [x] allow users to invite others to follow their gallery
- [ ] send a notification to all users that a new picture has been uploaded
- [ ] allow users to "heart" pictures
- [ ] allow users to comment on pictures

## Installation

1. Clone the repo:
```
git clone https://github.com/BastienVH/CS50x-Final-Project.git
```
2. Navigate to the folder in your CLI:
```
cd CS50x-Final-Project
```
3. Create a python 3 virtual environment:
Windows: `py -3 -m venv venv`
Linux: `python3 -m venv venv`

4. Activate your virtual environment:
Windows: `venv\Scripts\activate`
Linux: `. venv/bin/activate`

5. install the requirements with pip:
```
pip install -r requirements.txt
```
6. Run the program (only for testing):
```
flask run
```