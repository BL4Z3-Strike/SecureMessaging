from app import socketio

@socketio.on('message')
def handle_message(msg):
    socketio.send(msg)
