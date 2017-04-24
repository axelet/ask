cd /home/box/web
rm /etc/nginx/sites-enabled/default
ln -s /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/default
/etc/init.d/nginx restart
rm /etc/gunicorn.d/hello.py
ln -s /home/box/web/etc/hello.py /etc/gunicorn.d/hello.py
/etc/init.d/gunicorn restart
django-admin startproject ask
cd /home/box/web/ask
python manage.py startapp qa
#sudo /etc/init.d/mysql start