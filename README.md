# Memory Lane (my CS50x final project)
This application is my final project for the course CS50x by Harvard.
After submission, I will continue to work on this project to add features and other enhancements.

## Description
Memory Lane is a self-hosted web app that allows you to create an online image gallery and securely share it with friends and family.
No passwords are required, you and your friends login using a magic link sent to your email.
It was made with sharing pictures of your children in mind, but can also be used as regular image gallery.

## Tech stack
- Language: Python
- Framework: Flask
- CSS framework: Bootstrap
- Database: PostgreSQL
- [Remix Icon](https://remixicon.com/) 

## Features
- A setup process that runs on first launch to specify the admin user
- Protected so only invited people can view the gallery
- A responsive masonry-style gallery that sorts images from new to old
- Add individual images straight from the gallery view or multiple images from the upload-page
- Invite-page to invite multiple people at the same time

## Roadmap

### v0.1 goals
- [X] allow admin to invite users via their own email address
- [X] protect main page
- [X] main page displays pictures from a folder, using [masonry](https://masonry.desandro.com/)
- [x] display pictures chronologically
- [X] allow family and friends to upload individual pictures/videos from gallery view
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