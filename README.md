# Записи фільмів

Програма, яка дозволяє додавати записи про фільми у SQLite базу даних через консоль, або через веб-сервіс на flask

## Запуск через cli.py
### Додати запис:
`python cli.py add "Test 3" 1991 "scifi" 2,34,12 3 "Max Payne"`
### Подивитися існуючі записи:
`python cli.py list`
### Відфільтрувати записи по категорії фільму:
`python cli.py find horror`
### Повернути кількість фільмів по категоріям:
`python cli.py report`

## Запуск через app.py
`python app.py`
### Додати запис:
`curl -X POST http://127.0.0.1:5000/films      -H "Content-Type: application/json"      -d '{"name": "Test Name 2", "year": 2065, "category": "scifi", "duration": "2,1,13", "rating": 3, "actors":"actor1,actor2,actor3"}'`
### Подивитися існуючі записи:
`curl http://127.0.0.1:5000/films`
### Відфільтрувати записи по категорії фільму:
`curl http://127.0.0.1:5000/films?category=scifi`
### Повернути кількість фільмів по категоріям:
`curl http://127.0.0.1:5000/report`

## Формат даних
data.db, один запис: Ім'я фільму;рік;категорія;довжина фільму (годин:хвилин:секунд);рейтинг;список акторів

## Розгортання

### Розгортання коду
```
cd ~
git clone https://github.com/vlad-tkalenko/Best_films.git
cd Best_films
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
pip install gunicorn
pip freeze > requirements.txt
```
### Підняти gunicorn
```gunicorn -w 2 -b 127.0.0.1:8000 app:app```
### Налаштувати автоматичний запуск через systemd
```
sudo cp deploy/bestfilms.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable --now bestfilms
sudo systemctl status bestfilms
```
### Налаштувати nginx
```
sudo cp deploy/nginx.conf /etc/nginx/sites-available/bestfilms
sudo ln -s /etc/nginx/sites-available/bestfilms /etc/nginx/sites-enabled/
sudo rm /etc/nginx/sites-enabled/default
sudo nginx -t                      
sudo systemctl reload nginx
```
### Отримати https сертифікат (після створення домену)
```
sudo snap install --classic certbot
sudo ln -s /snap/bin/certbot /usr/local/bin/certbot
sudo certbot --nginx -d api.papagaichik.pp.ua
```
Після всіх команд, сайт відкривається за [url](https://api.papagaichik.pp.ua/films)
