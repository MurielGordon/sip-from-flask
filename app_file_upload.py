# sip-from-flask

from flask import Flask

UPLOAD_FOLDER = '<true_path_info>/static/uploads'
# true path found using
# >>>python3
# >>>import os
# >>>os.path.abspath("src/examplefile.txt")
## this UPLOAD_FOLDER can be either the true path or the more vague '/static/uploads'. No idea why

app = Flask(__name__)
app.secret_key = 'secret key'
# recommended method for secret key generation:
# >>>python3
# >>> import os
# >>> os.urandom(12)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1280 * 1280