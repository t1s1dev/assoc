from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

@app.route("/")
def main():
    return render_template('index.html')

@app.route('/getData/<path:filename>')
def getData(filename):
    return send_from_directory('./static/data/', filename)

if __name__ == "__main__":
    app.run()
