path=${pwd}
echo $path
python3 manage.py makemigrations
python3 'manage.py' 'migrate'
service httpd restart
