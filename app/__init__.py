"""
Flask application factory and configuration.
"""
from flask import Flask
from flask_socketio import SocketIO

socketio = SocketIO()


def create_app(config_name='default'):
    """
    Application factory pattern.
    
    Args:
        config_name: Configuration to use (default, development, production, testing)
    
    Returns:
        Flask application instance
    """
    app = Flask(__name__)
    
    # Load configuration
    app.config.from_prefixed_env()
    
    # Initialize extensions
    socketio.init_app(app, cors_allowed_origins="*")
    
    # Register blueprints (to be added later)
    
    return app
