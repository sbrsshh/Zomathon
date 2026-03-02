from app import create_app, socketio
import os

flask_app = create_app()

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    socketio.run(flask_app, host='127.0.0.1', port=port, debug=True, allow_unsafe_werkzeug=True)
