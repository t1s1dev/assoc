from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

@app.route("/")
def main():
    return render_template('index.html')

@app.route('/getData/<path:filename>')
def get_data(filename):
    return send_from_directory('./static/data/', filename)

@app.route('/saveData')
def save_data():
    with open("test.txt","wb") as fo:
    	fo.write("This is Test Data")

if __name__ == "__main__":
    app.run()
