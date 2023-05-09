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

sudo touch /data/web_static/releases/$special/index.html
text="<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>"
echo "$text" | sudo tee /data/web_static/releases/$special/index.html

sudo ln -sf /data/web_static/releases/$special /data/web_static/current

sudo chown -R ubuntu:ubuntu /data/

replace="server_name localhost;"
text2="server_name localhost;\n	location \/hbnb_static\/ {\n		alias \/data\/web_static\/current\/;\n	}"
sudo sed -i "s/$replace/$text2/" /etc/nginx/sites-available/default
sudo service nginx restart
