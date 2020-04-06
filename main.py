from flask import Flask, render_template, request, send_from_directory
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
  if request.method == 'POST' and \
    request.files and 'photo' in request.files:
    photo = request.files['photo']
    filename = secure_filename(photo.filename)
    path = os.path.join('uploads', filename)
    photo.save(path)
    fout = open("pictures.txt", 'a')
    fout.write(filename + '<br />')
    fout.close()
  return render_template('index.html')

@app.route('/view')
def view():
  fin = open("pictures.txt", 'r')
  photos = fin.readlines()
  photos = [photo.strip() for photo in photos]
  fin.close()
  return render_template('view.html', photos=photos)

@app.route('/photos/<filename>')
def get_file(filename):
  return send_from_directory('uploads', filename)

app.run(host='0.0.0.0', port=8080)