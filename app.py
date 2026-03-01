from flask import Flask
import os
import socket

app = Flask(__name__)

@app.route('/')
def hello():
    hostname = socket.gethostname()
    return f"""
    <html>
        <head>
            <title>DevOps Flask App</title>
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    margin: 40px;
                    text-align: center;
                    background-color: #f0f0f0;
                }}
                .container {{
                    background-color: white;
                    padding: 20px;
                    border-radius: 10px;
                    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
                }}
                h1 {{ color: #333; }}
                .info {{ color: #666; margin-top: 20px; }}
            </style>
        </head>
        <body>
            <div class="container">
                <h1>🚀 Hello DevOps World!</h1>
                <p>This Flask app is running in a Docker container!</p>
                <div class="info">
                    <p><strong>Hostname:</strong> {hostname}</p>
                    <p><strong>Environment:</strong> {os.getenv('FLASK_ENV', 'production')}</p>
                </div>
            </div>
        </body>
    </html>
    """

@app.route('/health')
def health():
    return {"status": "healthy", "message": "App is running smoothly!"}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)