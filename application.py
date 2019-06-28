from flask import Flask, render_template, send_from_directory
from flask import request
from werkzeug.utils import secure_filename
from app import app
import os

app = Flask(__name__)

APP_ROOT = os.path.dirname(os.path.abspath(__file__))
UPLOAD_PATH = '/static'
UPLOAD_DIR= os.path.join(APP_ROOT, UPLOAD_PATH)

@app.route("/")
def main():
    return render_template('index.html')

@app.route("/edit")
def edit():
    return render_template('edit.html')

@app.route('/getData/<path:filename>')
def get_data(filename):
    return send_from_directory('./static/data/', filename)

@app.route('/saveData')
def save_data():
    with open("test.txt","wb") as fo:
        fo.write("This is Test Data")

if __name__ == "__main__":
    app.run()

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
  if request.method == 'POST':
    f = request.files['file']
    f.save(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(f.filename)))
  return 'file uploaded successfully'