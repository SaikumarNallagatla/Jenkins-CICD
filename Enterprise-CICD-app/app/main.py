from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return {"message": "Hello from Enterprise CI/CD Pipeline!", "status": "success"}

@app.route('/health')
def health_check():
    return {"status": "healthy"}

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)