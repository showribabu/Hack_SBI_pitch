from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def home():
    return render_template('index.html')

# @socketio.on('status_update')
# def handle_status_update(message):
#     updated_status = process_status_update(message)
#     emit('updated_status', updated_status)

if __name__ == '__main__':
    socketio.run(app)
