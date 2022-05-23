from flask import Flask, request, Response

app = Flask(__name__)

@app.route('/post/task', methods=['POST'])
def post_task():
    generate = request.data.decode('utf-8')
    final_task = generate.split()
    if final_task[0] == 'portugal' and final_task[1] == 'skiing':
        task = 'go to ski at serra da estrela'
    elif final_task[0] == 'portugal' and final_task[1] == 'jetskiing':
        task = 'jetskiing in lagos'
    elif final_task[0] == 'portugal' and final_task[1] == 'snowboarding':
        task = 'snowbaord at the mountains near a town called Loriga'
    elif final_task[0] == 'portugal' and final_task[1] == 'kayaking':
        task = 'kayak and explore the algarve regions in portugal'
    elif final_task[0] == 'spain' and final_task[1] == 'skiing':
        task = 'ski on the mountains of sierra nevada'
    elif final_task[0] == 'spain' and final_task[1] == 'jetskiing':
        task = 'jetskiing in barcelona'
    elif final_task[0] == 'spain' and final_task[1] == 'snowboarding':
        task = 'snowboard at the formigal resort'
    elif final_task[0] == 'spain' and final_task[1] == 'kayaking':
        task = 'kayak on the guadalquivir River, Seville'
    elif final_task[0] == 'america' and final_task[1] == 'skiing':
        task = 'ski in aspen United States'
    elif final_task[0] == 'america' and final_task[1] == 'jetskiing':
        task = 'jetski at the miami south beach'
    elif final_task[0] == 'america' and final_task[1] == 'snowboarding':
        task = 'snowboard at the park city in the utah olympic park'
    elif final_task[0] == 'america' and final_task[1] == 'kayaking':
        task = 'kayak at the juniper Run, Ocala National Forest'
    elif final_task[0] == 'italy' and final_task[1] == 'skiing':
        task = 'ski at the mountains in dolomites'
    elif final_task[0] == 'italy' and final_task[1] == 'jetskiing':
        task = 'jetski at the marine reserves in italy'
    elif final_task[0] == 'italy' and final_task[1] == 'snowboarding':
        task = 'snowboard in livigno in italy'
    elif final_task[0] == 'italy' and final_task[1] == 'kayaking':
        task = 'kayak in venice'
    else:
        task = "No Holiday could be generated"

    return Response(task, mimetype = 'text/plain')

if __name__ == '__main__':
    app.run(port=5003, debug=True, host='0.0.0.0')