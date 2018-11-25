FROM ubuntu:18.04
RUN apt update && apt install -y apache2  && apt install -y unzip && apt install -y wget
RUN a2enmod rewrite
RUN DEBIAN_FRONTEND=noninteractive apt-get install -yq php libapache2-mod-php php-cli php-mysql php-zip php-ldap php-curl php-gd php-odbc php-pear php-xml php-xmlrpc php-mbstring php-snmp php-soap php-in$
RUN service apache2 restart
RUN cd /var/www/html && rm index.html && wget https://download.prestashop.com/download/releases/prestashop_1.7.4.4.zip
RUN cd /var/www/html && unzip prestashop_1.7.4.4.zip
RUN chown -R www-data:www-data /var/www/html && chmod -R 755 /var/www/html
EXPOSE 8080 80 20 21 22
