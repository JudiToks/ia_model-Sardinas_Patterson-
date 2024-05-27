from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():  # put application's code here
    return render_template('index.html')

@app.route('/predict', methods=['GET'])
def predict():  # put application's code here
    return render_template('result.html')

if __name__ == '__main__':
    app.run()
