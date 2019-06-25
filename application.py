from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

@app.route("/")
def main():
    return render_template('index.html')

@app.route('/getCoursesData')
def getCoursesData():
    return send_from_directory('data/', 'AA_courses.csv', as_attachment=True)

if __name__ == "__main__":
    app.run()