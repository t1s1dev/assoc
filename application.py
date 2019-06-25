from flask import Flask, render_template, send_file

app = Flask(__name__)

@app.route("/")
def main():
    return render_template('index.html')

@app.route('/getCoursesData')
def getCoursesData():
    return send_file('index.html')

if __name__ == "__main__":
    app.run()
