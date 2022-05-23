from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/', methods=['GET'])
@app.route('/place/activity', methods = ['GET'])
def get_holiday():
    place = requests.get('http://service_2:5001/get/place').text
    activity = requests.get('http://service_3:5002/get/activity').text
    generate = place + ' ' + activity
    task = requests.post ('http://service_4:5003/post/task', data = generate).text
    return render_template('home.html', title='holiday generator', place = place, activity=activity, task=task)

if __name__ == '__main__':
    app.run(port=5000, debug=True, host = '0.0.0.0')
