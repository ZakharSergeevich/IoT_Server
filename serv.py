from flask import Flask
import datetime

app = Flask(__name__)

@app.route("/")
def hello():
   now = datetime.datetime.now()
   timeString = now.strftime("%Y-%m-%d %H:%M")
   templateData = {
      'title' : 'HELLO!',
      'time': timeString
      }
   return render_template('main.html', **templateData)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=2000, debug=True)