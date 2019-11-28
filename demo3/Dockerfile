FROM php:7.1-apache

RUN a2enmod rewrite

WORKDIR /var/www/html

ENV DEBIAN_FRONTEND noninteractive
RUN apt-get -qq update && apt-get -qq -y --no-install-recommends install \
  curl \
  unzip \
  libfreetype6-dev \
  libjpeg62-turbo-dev \
  libmcrypt-dev \
  libpng-dev \
  libjpeg-dev \
  libmemcached-dev \
  zlib1g-dev \
  imagemagick \
  git \
  && docker-php-ext-install -j$(nproc) iconv mcrypt \
  pdo pdo_mysql mysqli gd \
  &&  docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-dir=/usr/include/ \
  &&  curl -sL https://deb.nodesource.com/setup_12.x | bash \
  && apt-get install -y nodejs 

RUN cd /var/www && git clone https://github.com/omeka/omeka-s.git html \
&& cd html\
&& npm install\
&& npm install --global gulp-cli\
&& gulp init

COPY ./database.ini /var/www/html/config/database.ini

RUN chown -R www-data:www-data /var/www/html