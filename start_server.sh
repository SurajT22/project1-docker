#This is a shell scripts
export host export MYSQL_DATABASE=starwarsdb
export MYSQL_USER=root
export MYSQL_ROOT_PASSWORD=root # REPLACE with your password
export MYSQL_HOST=127.0.0.1

python manage.py runserver