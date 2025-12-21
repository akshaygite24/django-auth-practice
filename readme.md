# Django Authentication And Authorization Learning Project

## About the project
This is a learning project i built while studying django authentication and authorization.

The main goal of this project was to understand how django handles users, permissions, and roles, and how access control works in real application.

UI and design were not priority, Learning backend concept was.


## What I learned and Implemented
- Authentication
    - User Registration
    - Login and Logout
    - Session Based Authentication
    - Protecting Pages using login_required

- Authorization
    - Understanding what user is allowed to do
    - Using django permissions
    - Using groups as roles
    - Manually Checking permissions in view using has_perm()


## Roles & Permissions

- Default User
    - Can view post
    - Can create post ( if permission exist)
    - Can delete their own post

- Moderator
    - can delete any post

- Admin
    - can delete any post
    - can ban users


## Tech Stack
- Python
- Django
- SQLite 

## How to Run the Project
```
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```
