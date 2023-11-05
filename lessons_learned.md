## In which we document every single thing we learned with very little organization
1. You can avoid tagalong files from other git working trees if you use the FIRST set of instructions (create new repo on command line) in a new GitHub repo instead of the SECOND set (push existing repo from command line)
2. Nice markdown documentation for these .md files here: https://tinyurl.com/y3s7kmjk
Secret key generation: https://tinyurl.com/4ysuy5dk
3. app.secret_key variable must be set in app_file_upload.py script AND in the if __name__ == "__main__": condition in main.py
4. app.config['SESSION_TYPE'] = 'filesystem' added to if __name__ == "__main__": condition seems to do [something with where variables are stored in flask sessions.](https://tinyurl.com/2p9awsuv) Found it in an example of ways to spice up the name/main condition. Doesn't seem to be hurting anything ¯\\_(ツ)_/¯
5. Adding app.debug = True to the name/main condition in main.py also seems like good practice but can also be removed without hurting the fuctioning of the program.
6. "[folder name] not defined" type error messages can be the result of a folder path being different than you think. Suggested way to find the true path of a folder or file: https://tinyurl.com/4wuzy2xw
7. UPLOAD_FOLDER variable needs to be defined in the unpload_image(): function in main.py for the thing to work: https://tinyurl.com/w92x7dxd
8. ...and app.config needed to be removed from the file.save line 
9. UPLOAD_FOLDER variable as defined in main.py MUST be the true path for the folder. Cannot use relative path. Not sure why.
10. UPLOAD_FOLDER variable as defined in app_file_upload.py can be either true path or relative path. Not sure why there is more wiggle room here.

## The error messages and their corresponding fixes