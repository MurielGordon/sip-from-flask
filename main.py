# sip-from-flask

import os
from app_file_upload import app
import urllib.request
from flask import Flask, flash, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename

app = Flask(__name__)
# the above solved the inescapable 'No file type' error. Error appeared whether or not the correct file type was submitted.
# new error message is:
# "RuntimeError: This session is unavailable because no secret key was set. Set the secret_key on the...
# ...application to something unique and secret."
# above error fixed; new error is:
# "NameError: name 'UPLOAD_FOLDER' is not defined" 

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def upload_form():
    return render_template('upload.html')

@app.route('/', methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
        flash('No image selected for uploading')
        return redirect(request.url)
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        #print('upload_image filename: ' + filename)
        flash('Image successfully uploaded and displayed below')
        return render_template('upload.html', filename=filename)
    else:
        flash('Allowed image types are -> png, jpg, jpeg, gif')
        return redirect(request.url)
    
@app.route('/display/<filename>')
def display_image(filename):
    #print('display_image filename: ' + filename)
    return redirect(url_for('static', filename='uploads/' + filename))

if __name__ == "__main__":
    app.secret_key = 'secret key'
    app.config['SESSION_TYPE'] = 'filesystem'
    app.debug = True
    # added lines 49 - 51
    app.run()