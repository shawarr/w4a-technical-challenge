from flask import Flask, session, render_template, send_from_directory, request
import os, time

app= Flask(__name__)
app.secret_key=os.getenv("KEY")
@app.get('/')
def index():
    if 'login_time' in session and time.time() - session.get('login_time') <= 10:
        return "Logged in successfully", 200
    else:
        return render_template('invalid_session.html')

@app.get('/src/<path:filename>')
def serve_files(filename):
    return send_from_directory("static",filename)

@app.get('/login')
def login():
    return render_template('login.html')

@app.post('/auth')
def auth():
    json_data= request.get_json()
    username= json_data.get('username')
    password= json_data.get('password')
    if username == os.getenv('USER') and password == os.getenv('PASS'):
        session['login_time'] = time.time() 
        return {"ok": True}, 200
    else:
        session.clear()
        app.logger.warning("Invalid credentials")
        return {"ok": False, "message": "Invalid credentials"}  , 401
