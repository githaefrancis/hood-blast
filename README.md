# Hood Blast

## Description

A django web application that allows a user to keep up with what is happening in the neighbourhood. A user has to update the neighbourhood they live in after signing up. A user can view posts and business form their neighbourhood.

## Author

Francis Githae

## BDD
- User signs up.
- User completes signup by confirming email.
- User updates their profile to indicate their neighbourhood.
- User views posts and businesses from their neighbourhood.
- User can add a new post or business
- User can update their neighbourhood if they move.


## Admin Dashboard
-Admin adds and removes neighbourhoods through the admin dashboard.

> path /admin


## Tools and Technologies

- Python-Programming language
- Django - Web app framework.
- Postgresql -For the database
- Bootstrap5 -For styling and responsiveness.


## Setting up the project locally

1. Clone the repository
```bash
git clone git@github.com:githaefrancis/hood-blast.git
```

2. Navigate to the project folder
```
cd hood-blast
```
3. Create and activate the virtual environment

```bash
python3 -m venv virtual

source virtual/bin/ activate
```

4. Install dependencies from the requirements.txt

```bash
pip install -r requirements.txt
```
5. Create database


6. Create .env file

```bash
export DB_NAME=<name_of_db>

export DB_USER='db_user'

export DB_PASSWORD='db_password'
export SECRET_KEY='secret_key'


export DEBUG='False'

export DB_HOST='127.0.0.1'

export MODE='dev'

export ALLOWED_HOSTS='.localhost','.heroku.com','.127.0.0.1'

export DISABLE_COLLECTSTATIC=1

cloudinary_api_key=<cloudinary secret key>
cloudinary_secret=<cloudinary secret>
cloud_name=<cloudinary cloud name>
```

7. Load .env

```bash 
source .env
```

8. Migrate models

```
python3 manage.py migrate
```
9. Run tests

```
python3 manage.py test
```

10. Run the app

```
python3 manage.py runserver

```


## Livelink

[Hood Blast](https://hood-blast.herokuapp.com/)

## Contact

Email: mureithigithae@gmail.com

## License

This project is under the MIT License [click here for more information](LICENSE)

&copy; 2022 Francis Githae

