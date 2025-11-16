from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello():
    # A simple greeting message
    message = "Hello from my first containerized application!"
    
    # Let's try to get a version number from an environment variable
    app_version = os.environ.get('APP_VERSION', 'unknown')
    
    return f"<h1>{message}</h1><p>Application Version: {app_version}</p>"

if __name__ == "__main__":
    # We run on port 5000, which is a common port for web development
    app.run(debug=True, host='0.0.0.0', port=5000)