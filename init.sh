sudo rm -r /etc/nginx/sites-enabled/*
sudo ln -s /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/test.conf
sudo /etc/init.d/nginx restart
sudo rm -r /etc/gunicorn.d/*
sudo ln -s /home/box/web/etc/hello.py   /etc/gunicorn.d/hello.py
sudo /etc/init.d/gunicorn restart
