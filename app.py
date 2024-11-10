from flask import Flask
from automa import automa_bp

app = Flask(__name__)
app.register_blueprint(automa_bp, url_prefix='/automa')

@app.route('/')
def hello():
    return "Hello, World!"

if __name__ == '__main__':
    app.run(debug=True)