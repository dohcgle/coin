## Криптовалюталар ҳақида маълумот берувчи сайт
## Верстка free-css.com сайтидан олинган. Backend Django 3 да ёзилган. Маълумотлар омбори SQLITE3 яратилган.
## Лойиҳада Бош сахифа, Биз хақимизда, Валюта, Гуруҳ, Богланиш саҳифалари яратилган.
## Валюта, Гуруҳ, Боғланиш саҳифалари динамик килиб ишланган. Турли роботлардан ҳимоя қилиш мақсадида Captcha дан фойдаланилган.
## Лойиханинг админ панелидан фойдаланиш аккаунти
> admin панель 
>> login: ulugbek <br> 
>> password: django123

# Django, SQLITE3, Nginx ва Gunicornларни Ubuntu Server 20.04га ўрнатиш ва созлаш
1. Ubuntu учун зарурий пакетларни ўрнатиш
### Django ни Python 3 билан созлаш учун куйидагини ёзинг:
> sudo apt update <br>
> sudo apt install python3-pip python3-dev libpq-dev nginx curl

### Лойиҳа учун Python виртуал муҳитини яратиш
> sudo -H pip3 install --upgrade pip <br>
> sudo -H pip3 install virtualenv

#### virtualenv ўрнатилгандан сўнг, лойиҳа учун каталог яратиш ва унга кириш керак
> mkdir ~/myprojectdir <br>
> cd ~/myprojectdir
####  Лойиҳа каталигида куйидаги буйруқ ёрдамида Python виртуал муҳитини яратинг
> virtualenv myprojectenv
####  Виртуал мухитини активлаштиринг
> source myprojectenv/bin/activate
####  Виртуал муҳитини тўғри ишга туширган бўлсангиз (myprojectenv) - кўринишда бўлади.
#### Энди Django, Gunicorn урнатинг:
> pip install django gunicorn

### Django лойиҳани github кўчириб олиш ва созлаш
> git clone https://github.com/dohcgle/coin.git
#### Статитик файлларни йигиш ва бир жойга тўплаш
> ./manage.py collectstatic
#### Django 8000 портини ишлатади, шунинг учун биз шу портга рухсат очишимиз керак
> sudo ufw allow 8000

#### Энди биз лойихани ишлашини тестдан утказиб куришимиз мумкин бунинг учун куйидаги буйрукни теринг
> ./manage.py runserver 0.0.0.0:8000

#### Кейинги кадам Gunicorn лойихага хизмат курсатиш жараёнини текширишимиз керак, бунинг учун coin.wsgi турган катологга киришимиз ва куйидаги буйрукни теришимиз керак
> gunicorn --bind 0.0.0.0:8000 coin.wsgi
#### Тестлаш жараёни муваффакиятли якунлангандан кейин ctrl+c билан серверни тухтатамиз ва куйидаги буйрукни териб, виртуал мухитдан чикамиз.
> deactivate

### Gunicorn socket ва systemd хизмат файлларини яратиш
### systemd файлини яратинг ва унга қуйидагиларни ёзинг
> sudo nano /etc/systemd/system/gunicorn.socket
```
[Unit]
Description=gunicorn socket

[Socket]
ListenStream=/run/gunicorn.sock

[Install]
WantedBy=sockets.target
```

### Энди gunicorn.service файлини яратинг ва унга қуйидагиларни ёзинг
> sudo nano /etc/systemd/system/gunicorn.service
```
[Unit] 
Description=gunicorn daemon
Requires=gunicorn.socket
After=network.target

[Service]
User=ulugbek
Group=www-data
WorkingDirectory=/home/ulugbek/myprojectdir/coin
ExecStart=/home/ulugbek/myprojectdir/myprojectenv/bin/gunicorn \
          --access-logfile - \
          --workers 3 \
          --bind unix:/run/gunicorn.sock \
          coin.wsgi:application

[Install]
WantedBy=multi-user.target
```

### systemd файли тайёр бўлди, сақланг ва уни ёпинг.
### Энди Gunicorn сокетни активлаштиришимиз ва ишга туширишимиз мумкин:
> sudo systemctl start gunicorn.socket <br>
> sudo systemctl enable gunicorn.socket
### Gunicorn ўзгартиришлар киритсангиз, уни ўчириб кайта ёқинг
>sudo systemctl daemon-reload <br>
> sudo systemctl restart gunicorn
### Энди Nginx сервери ва Gunicorn алоқаларини созлаймиз
### Nginx каталигида sites-available блокини яратамиз ва унга қуйидаги командаларни ёзамиз
> sudo nano /etc/nginx/sites-available/myproject

``` 
server { 
    listen 8000; 
    server_name server_domain_or_IP; 
    location = /favicon.ico { access_log off; log_not_found off; } 
    location /static/ { <br>
        root /home/ulugbek/myprojectdir/coin;
    } 
    location / { 
        include proxy_params; <br>
        proxy_pass http://unix:/run/gunicorn.sock; 
    } 
} 
```

### Файлни сақланг ва ёпинг. Энди файлларни сайтлар каталогига улаб уни активлаштиришимиз мумкин.
> sudo ln -s /etc/nginx/sites-available/myproject /etc/nginx/sites-enabled

## Ниҳоят биз Django лойиҳани Nginx ва Gunicorn ёрдамида Ubuntu server 20.04 ўрнатишни ўргандик.

### Йуриқнома https://www.digitalocean.com/community/tutorials/how-to-set-up-django-with-postgres-nginx-and-gunicorn-on-ubuntu-20-04-ru мақоласи асосида тайёрланди












