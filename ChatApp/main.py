from flask import Flask, render_template
from flask_socketio import SocketIO, send

app = Flask(__name__)
app.config['SECRET'] = 'secret!123'

socketio = SocketIO(app, cors_allowed_origins = '*')

@socketio.on('message')
def handle_message(message):
    print('received message : '+message)
    if message != 'User connected!':
        send(message, broadtcast=True)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    socketio.run(app, debug=True, host='192.168.0.110')

