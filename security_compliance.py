from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Secure Agri-Lending Platform"

if __name__ == '__main__':
    app.run(ssl_context='adhoc')
