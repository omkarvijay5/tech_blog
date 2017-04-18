my technical blog by using django rest framework and angularjs

setup guidelines

1. git clone https://github.com/omkarvijay5/tech_blog.git

2. cd tech_blog

3. create an environment

4. pip install -r requirements.txt

5. create a postgres database and user. If you want to use the existing setup then do following
   postgres username: 'tech_blog' password: 'tech_blog' db name: tech_blog_dev
   source utils/.env
   If you want to use different database credentials change utils/.env file

6. python manage.py migrate

7. python manage.py collectstatic

8. python manage.py runserver
   