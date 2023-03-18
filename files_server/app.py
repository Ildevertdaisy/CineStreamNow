
import os
from flask import Flask, request, send_from_directory
from werkzeug.utils import secure_filename
import asyncio

UPLOAD_FOLDER = 'uploads'
POSTERS_FOLDER = 'posters_path'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'jpeg', 'gif', 'mp4', 'mp3', 'ts'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['POSTERS_FOLDER'] = POSTERS_FOLDER

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/files/upload", methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return "No file part", 400
    file = request.files['file']
    if file.filename == '':
        return "No selected file", 400
    if file and allowed_file(file.filename):
        extracted_filename = file.filename.split('.')[0]
        associated_file_folder = secure_filename(extracted_filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], associated_file_folder)
        os.makedirs(file_path, exist_ok=True)
        file.save(os.path.join(file_path, file.filename))
        asyncio.sleep(10)
        return f"File saved at: {os.path.join(file_path, file.filename)}", 200
    else:
        return "File type not allowed", 400

@app.route("/files/upload/posters_path", methods=['POST'])
def upload_poster_path():
    if 'file' not in request.files:
        return "No file part", 400
    file = request.files['file']
    if file.filename == '':
        return "No selected file", 400
    if file and allowed_file(file.filename):
        extracted_filename = file.filename.split('.')[0]
        associated_file_folder = secure_filename(extracted_filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], app.config['POSTERS_FOLDER'],  associated_file_folder)
        os.makedirs(file_path, exist_ok=True)
        file.save(os.path.join(file_path, file.filename))
        asyncio.sleep(10)
        return f"File saved at: {os.path.join(file_path, file.filename)}", 200
    else:
        return "File type not allowed", 400
    

#Route pour récupérer un fichier


if __name__ == "__main__":
    app.run(debug=True)