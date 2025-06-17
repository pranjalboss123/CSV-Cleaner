import os
from flask import Flask, render_template, request, send_file
from werkzeug.utils import secure_filename
from main import run_full_pipeline

app = Flask(__name__)
UPLOAD_FOLDER = 'input'
OUTPUT_FILE = 'output/final_cleaned_output.csv'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return "No file part in request", 400

    file = request.files['file']
    if file.filename == '':
        return "No selected file", 400

    filename = secure_filename(file.filename)
    filepath = os.path.join(UPLOAD_FOLDER, filename)
    file.save(filepath)

    # Here runs the agents .
    run_full_pipeline(filepath)

    return render_template('result.html', filename=filename)

@app.route('/download')
def download_file():
    return send_file(OUTPUT_FILE, as_attachment=True)

if __name__ == '__main__':
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)
    app.run(debug=True)
