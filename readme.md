# Обрезка ссылок с помощью Битли

Код предназначен для:
- создания коротких bitly-ссылок из длинных URL
- получения статистики по кликам по bitly-ссылкам

Для работы необходим токен сервиса https://bitly.com

### Как установить
Для работы необходим установленный python3
1. Скачать архив и распаковать.

2. Получить токен сервиса bitly.com
https://support.bitly.com/hc/en-us/articles/230647907-How-do-I-generate-an-OAuth-access-token-for-the-Bitly-API-

3. Файл .env.example переименовать в .env, в `BYTLY_TOKEN` подставить полученный токен
 ```
   BYTLY_TOKEN = a3256343452643efd32453432765209as
   ```

4. Установить виртуальное окружение и установить зависимости
```
pip -m venv venv
```
```
pip install -r requirements.txt
```

### Использование
Используется консольный ввод.

1. Создать короткую ссылку bitly:
```
python main.py https://google.com    
For https://google.com Bitlink id = bit.ly/3kz0YGv
```

2. Вывести количество переходов по кликам по битли-ссылке:
```
python main.py https://bit.ly/3kz0YGv 
Count of clicks: 11
```

### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).