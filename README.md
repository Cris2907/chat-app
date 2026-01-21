# Chat App

A real-time chat application built with Flask and Socket.IO.

## Project Structure

```
chat-app/
├── app/
│   ├── __init__.py      # Application factory and configuration
│   ├── app.py           # Main application entry point
│   ├── models.py        # Database models
│   └── sockets.py       # Socket.IO event handlers
├── migrations/          # Database migrations
├── requirements.txt     # Python dependencies
├── .env                 # Environment variables (not committed)
├── .gitignore          # Git ignore rules
└── README.md           # This file
```

## Setup Instructions

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/Cris2907/chat-app.git
cd chat-app
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Configure environment variables:
   - Copy `.env` and update the values as needed
   - Change `FLASK_SECRET_KEY` to a secure random value in production

### Running the Application

Start the development server:
```bash
python app/app.py
```

Or using Flask CLI:
```bash
flask run
```

The server will start on `http://localhost:5000`

## Development

### Adding New Features

- **Models**: Add database models in `app/models.py`
- **Socket Events**: Add Socket.IO event handlers in `app/sockets.py`
- **Routes**: Add HTTP routes in the application factory (`app/__init__.py`)

### Database Migrations

Database migration support can be added using Flask-Migrate:
```bash
pip install flask-migrate
```

## Technologies Used

- **Flask**: Web framework
- **Flask-SocketIO**: WebSocket support
- **Python-SocketIO**: Socket.IO implementation
- **Eventlet**: Async networking library

## License

See LICENSE file for details.