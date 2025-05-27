from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/status')
def status():
    return render_template('status.html')

@app.route('/logs')
def logs():
    return render_template('logs.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
