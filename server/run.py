from app import create_app, socketio
import os

flask_app = create_app()

app = flask_app  # 👈 IMPORTANT for Vercel

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    socketio.run(flask_app, host='0.0.0.0', port=port, debug=True)