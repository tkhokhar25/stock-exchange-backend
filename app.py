from flask import Flask, render_template, jsonify, session
from flask_socketio import SocketIO, emit, join_room, leave_room
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

@socketio.on('create')
def on_create(data):
    # Data should be in json format for example -> {'username' : 'Taranjit'}
    username = data['username']
    # Generate a five digit room Id below is just an example
    room = 'ABCDE'
    join_room(room)
    # TODO: send the room ID to the client

@socketio.on('join')
def on_join(data):
    # Data should be in json format for example -> {'username' : 'Taranjit', 'room' : 'ABCDE'}
    username = data['username']
    room = data['room']
    join_room(room)

if __name__ == '__main__':
    socketio.run(app)