#!/usr/bin/env bash
# script that creates a bunch of file that prepary the web server
# to deploy web static and install nginx if its not installed
if [ ! -d /etc/nginx/ ];
then
	sudo apt-get update
	sudo apt-get install -y nginx
fi

special="test"
if [ ! -d /data/ ];
then
	sudo mkdir -p /data/web_static/{releases/$special,shared}
fi

sudo chown -R ubuntu:ubuntu /data/

text="<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>"
echo $text >> /data/web_static/releases/$special/index.html

if [ -L /data/web_static/current ];
then
	rm /data/web_static/current
	ln -s /data/web_static/releases/$special /data/web_static/current
else
	ln -s /data/web_static/releases/$special /data/web_static/current
fi

replace="server_name _;"
text2="	server_name _;\n	location\/hbnb_static\/ {\n	alias \/data\/web_static\/current\/;\n	}"
sudo sed -i "s/$replace/$text2/" /etc/nginx/sites-available/default
sudo service nginx restart
