from flask import Flask, render_template, jsonify, session, json, Response
from flask_socketio import SocketIO, emit, join_room, leave_room, send
from flask_cors import CORS
    
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, cors_allowed_origins='*')

users = {}

@app.route('/')
def index():
    print('called')
    return jsonify({'called': True})

@socketio.on('connect', '/user')
def test_connect():
    print('Client connected')
    return jsonify({'Client connected': True})

@socketio.on('create', '/user')
def on_create(data):
    # Data should be in json format for example -> {'username' : 'Taranjit'}
    username = data['username']
    # Generate a five digit room Id below is just an example
    room = 'ABCDE'
    join_room(room)

    users[room] = [ username ]
    
    emit('call_me', users[room], room=room)
    
    print('on_create')
    return room

@socketio.on('join', '/user')
def on_join(data):
    # Data should be in json format for example -> {'username' : 'Taranjit', 'room' : 'ABCDE'}
    username = data['username']
    room = data['room']
    join_room(room)

    users[room].append(username)
    
    emit('call_me', users[room], room=room)

    print('on_join')
    return room

@socketio.on('start')
def on_start(data):
    # Data should be in json format for example -> {'username' : 'Taranjit', 'room' : 'ABCDE'}
    username = data['username']
    room = data['room']
    join_room(room)

if __name__ == '__main__':
    socketio.run(app)