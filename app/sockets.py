"""
Socket.IO event handlers.
"""
from flask_socketio import emit, join_room, leave_room
from app import socketio


@socketio.on('connect')
def handle_connect():
    """Handle client connection."""
    print('Client connected')
    emit('connected', {'data': 'Connected to server'})


@socketio.on('disconnect')
def handle_disconnect():
    """Handle client disconnection."""
    print('Client disconnected')


# TODO: Add more socket event handlers here
# Example:
# @socketio.on('message')
# def handle_message(data):
#     """Handle incoming message."""
#     emit('message', data, broadcast=True)
