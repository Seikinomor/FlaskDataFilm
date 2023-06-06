# Flask Movie Data Visualization

This is a Flask web application that allows users to upload a CSV file containing movie data and visualizes the top actors and actresses based on the number of films they have appeared in.

## Prerequisites

Make sure you have the following installed before running the application:

- Python 3.x
- Flask
- pandas
- matplotlib

## Installation

1. Clone the repository to your local machine.
2. Navigate to the project directory.
3. Install the required dependencies using the following command:


pip install -r requirements.txt

## Usage
Place your movie data CSV file in the uploads folder. The file should have the following format:
Columns: 'Actor', 'Actress', 'Title', 'Year', 'Genre', 'Director', 'Country'
Use ';' as the delimiter.
Run the Flask application using the following command:
python app.py
Open your web browser and visit http://localhost:5000 to access the application.
Click on the "Upload a CSV File" button and select your movie data CSV file.
The application will process the file and display the following:
A table with the uploaded data, available on the "Visualization" page.
A bar chart displaying the top 10 actors based on the number of films they have appeared in.
A bar chart displaying the top 10 actresses based on the number of films they have appeared in.

I hope this helps! Let me know if you have any further questions.

