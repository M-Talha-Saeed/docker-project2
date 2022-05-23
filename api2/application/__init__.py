from flask import Flask, request, Response
import random

app = Flask(__name__)

@app.route('/get/place', methods = ['GET'])
def get_place():
    place = ['portugal', 'spain', 'america', 'italy']
    randomnum = random.randint(0, 3)
    return Response(place[randomnum], mimetype= 'text/plain')

if __name__ == '__main__':
    app.run(port = 5001, debug = True, host = '0.0.0.0')

