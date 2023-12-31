## In which we document every single thing we learned with very little organization
1. You can avoid tagalong files from other git working trees if you use the FIRST set of instructions (create new repo on command line) in a new GitHub repo instead of the SECOND set (push existing repo from command line)
2. Nice markdown documentation for these .md files here: https://tinyurl.com/y3s7kmjk
3. Secret key generation: https://tinyurl.com/4ysuy5dk
4. app.secret_key variable must be set in app_file_upload.py script AND in the if __name__ == "__main__": condition in main.py
5. app.config['SESSION_TYPE'] = 'filesystem' added to if __name__ == "__main__": condition seems to do [something with where variables are stored in flask sessions.](https://tinyurl.com/2p9awsuv) Found it in an example of ways to spice up the name/main condition. Doesn't seem to be hurting anything ¯\\_(ツ)_/¯
6. Adding app.debug = True to the name/main condition in main.py also seems like good practice but can also be removed without hurting the fuctioning of the program.
7. "[folder name] not defined" type error messages can be the result of a folder path being different than you think. Suggested way to find the true path of a folder or file: https://tinyurl.com/4wuzy2xw
8. UPLOAD_FOLDER variable needs to be defined in the unpload_image(): function in main.py for the thing to work: https://tinyurl.com/w92x7dxd
9. ...and app.config needed to be removed from the file.save line 
10. UPLOAD_FOLDER variable as defined in main.py MUST be the true path for the folder. Cannot use relative path. Not sure why.
11. UPLOAD_FOLDER variable as defined in app_file_upload.py can be either true path or relative path. Not sure why there is more wiggle room here.


## The error messages and their corresponding fixes
> "No file type" -- inescapable outcome regardless of type of file added, no file added.
- Fix: added **app = Flask(__name__)** under the import code block.
> "RuntimeError: This session is unavailable because no secret key was set. Set the secret_key on the application to something unique and secret."
- Fix: Generated secret key in terminal using the following commands:
- >python3
- >import os
- >os.urandom(12)
- Added the following lines to if __name__ == "__main__": condition in main.py:
- >app.secret_key = 'secret key'
- >app.config['SESSION_TYPE'] = 'filesystem'
- >app.debug = True
- Set secret key variable in main.py and app_file_upload.py
> "NameError: name 'UPLOAD_FOLDER' is not defined" 
- Fix: Find true folder path in terminal using the following commands:
- >python3
- >import os
- >os.path.abspath("src/examplefile.txt")
- Optional: replace relative path with true path for UPLOAD_FOLDER in app_file_upload.py
- Not optional: add UPLOAD_FOLDER _**with**_ true path as variable to **if file and allowed_file(file.filename):** if statement in _def upload_image():_ function.  
- Also not optional: file.save line in main.py needs a refresh:
- > old: **file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))**
- > new: **file.save(os.path.join(UPLOAD_FOLDER, filename))**