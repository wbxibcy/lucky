from flask import Flask, render_template, jsonify
# from random import randint
from ran import ra

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

data = {
        '1' : '小明',
        '2' : '小红',
        '3' : '小玉',
        '4' : '小小红',
        '5' : 'mqm',
        '6' : '电次',
        '7' : '帕瓦',
        '8' : '秋'
    }


@app.route('/', methods=['GET'])
def give():
    # return jsonify({'data':data})
    return render_template('index.html')


@app.route('/data', methods=['GET'])
def date():
    return jsonify({'data':data})


@app.route('/lucky', methods=['GET'])
def result():
    num = ra()
    return jsonify({'result':data[str(num)]})


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port='8080')
