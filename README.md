Flask Movie Data Visualization
This is a Flask web application that allows users to upload a CSV file containing movie data and visualizes the top actors and actresses based on the number of films they have appeared in.

Prerequisites
Make sure you have the following installed before running the application:

Python 3.x
Flask
pandas
matplotlib
Installation
Clone the repository to your local machine.

Navigate to the project directory.

Install the required dependencies using the following command:

pip install -r requirements.txt

Usage
Place your movie data CSV file in the uploads folder. The file should have the following format:
Columns: 'Actor', 'Actress', 'Title', 'Year', 'Genre', 'Director', 'Country'
Use ';' as the delimiter.
Run the Flask application using the following command: python app.py

Open your web browser and visit http://localhost:5000 to access the application.

Click on the "Upload a CSV File" button and select your movie data CSV file.

The application will process the file and display the following:

A table with the uploaded data, available on the "Visualization" page.
A bar chart displaying the top 10 actors based on the number of films they have appeared in.
A bar chart displaying the top 10 actresses based on the number of films they have appeared in.
Візуалізація даних про фільми за допомогою Flask
Це веб-додаток Flask, який дозволяє користувачам завантажувати CSV-файл, що містить дані про фільми, і візуалізує найкращих акторів та актрис на основі кількості фільмів, в яких вони знялися.

Необхідні умови
Перед запуском програми переконайтеся, що у вас встановлено наступне:

Python 3.x
Flask
pandas
matplotlib
Встановлення
Клонуйте сховище на вашу локальну машину.

Перейдіть до каталогу проекту.

Встановіть необхідні залежності за допомогою наступної команди:

pip install -r requirements.txt

Використання
Помістіть CSV-файл з даними вашого фільму до теки uploads. Файл повинен мати наступний формат:
Стовпці: 'Актор', 'Актриса', 'Назва', 'Рік', 'Жанр', 'Режисер', 'Країна'
Використовуйте ';' як роздільник.
Запустіть додаток Flask за допомогою наступної команди: python app.py

Відкрийте веб-браузер і перейдіть за адресою http://localhost:5000, щоб отримати доступ до програми.

Натисніть на кнопку "Завантажити файл CSV" і виберіть файл CSV з даними вашого фільму.

Програма обробить файл і відобразить наступне:

Таблицю з завантаженими даними, доступну на сторінці "Візуалізація".
Гістограму, що відображає 10 найкращих акторів за кількістю фільмів, в яких вони знялися.
Гістограму, що відображає 10 найкращих акторок за кількістю фільмів, у яких вони знялися.
