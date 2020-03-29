from flask import Flask, render_template, jsonify
from flask_socketio import SocketIO, emit
from flask_cors import CORS
    
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, cors_allowed_origins='*')

@app.route('/')
def index():
    print('called')
    return jsonify({'called': True})

@socketio.on('connect')
def test_connect():
    print('Client connected')
    return jsonify({'Client connected': True})


@socketio.on('disconnect')
def test_disconnect():
    print('Client disconnected')
    return jsonify({'Client disconnected': True})

@socketio.on('play video')
def play_video(message):
    print('play video')
    emit('play video', broadcast=True)

@socketio.on('pause video')
def pause_video(message):
    print('pause video')
    emit('pause video', broadcast=True)

if __name__ == '__main__':
    socketio.run(app)