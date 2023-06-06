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

    # Обчислення кількості фільмів для кожного актора та актриси
    actor_counts = data['Actor'].value_counts()
    actress_counts = data['Actress'].value_counts()

    # Об'єднання кількостей фільмів акторів та актрис у один DataFrame
    actor_actress_counts = pd.concat([actor_counts, actress_counts], axis=1)
    actor_actress_counts.columns = ['Actor', 'Actress']
    actor_actress_counts = actor_actress_counts.fillna(0)

    # Отримання топ-10 акторів та актрис за кількістю фільмів
    top_actors = actor_actress_counts.nlargest(10, 'Actor')
    top_actresses = actor_actress_counts.nlargest(10, 'Actress')

    # Побудова графіка для акторів
    plt.bar(top_actors.index, top_actors['Actor'])
    plt.xlabel('Actor')
    plt.ylabel('Number of Films')
    plt.title('Top 10 Actors by Number of Films')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('static/actors_plot.png')  # Зберегти графік акторів як зображення у папці 'static'
    plt.close()

    # Побудова графіка для актрис
    plt.bar(top_actresses.index, top_actresses['Actress'])
    plt.xlabel('Actress')
    plt.ylabel('Number of Films')
    plt.title('Top 10 Actresses by Number of Films')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('static/actresses_plot.png')  # Зберегти графік актрис як зображення у папці 'static'
    plt.close()

    return render_template('index.html')

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
    app.run()
