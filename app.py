# File: app.py

from flask import Flask
import os

# Create an instance of the Flask application
app = Flask(__name__)

# Define a route for the root URL '/'
@app.route('/')
def hello():
    # A simple greeting message to display
    message = "Hello World! This application is running inside a Docker container."
    
    # A good practice is to be able to identify the application version at runtime.
    # We read it from an environment variable set by our container platform later.
    app_version = os.environ.get('APP_VERSION', 'unknown')
    
    # Return an HTML response
    return f"""
        <h1>{message}</h1>
        <p>Application Version: {app_version}</p>
        <p>This pipeline was executed by Jenkins.</p>
    """

# This block allows us to run the app directly using 'python app.py'
if __name__ == "__main__":
    # Run the app, making it accessible from outside the container (host='0.0.0.0')
    app.run(host='0.0.0.0', port=5000)