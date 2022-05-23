from flask import Flask, request, Response
import random

app = Flask(__name__)

@app.route('/get/activity', methods=['GET'])
def get_activity():
    activity = ['kayaking', 'snowboarding', 'jetskiing', 'skiing']
    randomnum = random.randint(0, 3)
    return Response(activity[randomnum], mimetype= 'text/plain')

if __name__ == '__main__':
    app.run(port=5002, debug=True, host='0.0.0.0')