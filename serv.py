from flask import Flask, render_template, request, url_for
import datetime
app = Flask(__name__)

sensor = 0

@app.route("/sensor/", methods=["POST"])
def number():
    content = request.get_json()
    sens = content['sens'] 
    global sensor   
    sensor = sensor + int(sens)
    print (content)
    return 'JSON posted'

@app.route("/")
def hello():
   now = datetime.datetime.now()
   timeString = now.strftime("%Y-%m-%d %H:%M")
   templateData = {
      'title' : 'HELLO!',
      'time': timeString,
      'counter': str(sensor) 
      }
   return render_template('main.html', **templateData)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=2000, debug=True)