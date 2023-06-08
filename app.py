from flask import Flask, render_template, request, redirect, url_for
import pandas as pd
import os
import matplotlib.pyplot as plt

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = 'film.csv'
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)
            return redirect(url_for('visualize'))

    # Завантаження даних з файлу з правильним роздільником
    data = pd.read_csv("film.csv", encoding='latin-1', delimiter=';')

    # Отримання фільмів, у яких знімалася Bardot Brigitte
    bardot_movies = data[data['Actress'] == 'Bardot, Brigitte']

    # Групування фільмів за роком випуску та підрахунок кількості фільмів за кожен рік
    bardot_movies_by_year = bardot_movies.groupby('Year').size()

    # Виведення назв фільмів актриси Brigitte Bardot по роках у консоль
    for year, movie_count in bardot_movies_by_year.items():
        movies = bardot_movies[bardot_movies['Year'] == year]['Title'].tolist()
        print(f"Рік: {year}, Кількість фільмів: {movie_count}, Фільми: {', '.join(movies)}")

    # Побудова графіка
    plt.plot(bardot_movies_by_year.index, bardot_movies_by_year.values)
    plt.xlabel('Year')
    plt.ylabel('Number of Films')
    plt.title('Bardot Brigitte Movies by Year')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('static/bardot_movies_plot.png')  # Зберегти графік у папці 'static'
    plt.close()

    return render_template('index.html', bardot_movies=bardot_movies)


@app.route('/visualize')
def visualize():
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], 'film.csv')
    if os.path.exists(filepath):
        data = pd.read_csv(filepath, encoding='latin1', sep=';')
        return render_template('visualize.html', data=data.to_html())
    return render_template('visualize.html', data=None)


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() == 'csv'


if __name__ == '__main__':
    app.run(debug=False, threaded=True, port=8002)
