from flask import Flask, render_template, request, redirect, url_for
import pandas as pd
import os

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

    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    if file and allowed_file(file.filename):
        filename = 'film.csv'
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        return redirect(url_for('visualize'))
    return redirect(url_for('index'))

@app.route('/visualize')
def visualize():
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], 'film.csv')
    if os.path.exists(filepath):
        data = pd.read_csv(filepath, encoding='latin1', delimiter=';')

        return render_template('visualize.html', data=data.to_dict('records'))
    return render_template('visualize.html', data=None)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() == 'csv'

if __name__ == '__main__':
    app.run(debug=False, threaded=True, port=8002)
