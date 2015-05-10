import json
import math
from fpl import fpl
from flask import Flask, request, send_file, jsonify, render_template

app = Flask(__name__)
VERSION = 1
CURRENT_YEAR = "2015"
NULL_RETURN = 'FPLAPI Version {}.<br>Learn more at <a href="http://github.com/svmatthews/fplapi">github.com/svmatthews/fplapi</a>.'.format(VERSION)

def calculate_rate(base, rate, size):
    amount = base + (rate * int(size))
    return amount

def nice_amount(num):
    nice = '${:,}'.format(num)
    return nice

@app.route('/', methods=['GET'])
def index():
    return NULL_RETURN

@app.route('/api', methods=['GET'])
def api():
    # if the query includes arguments, do something with them
    if (request.args):

        year = request.args.get('year')
        household_size = request.args.get('size')
        base = fpl[year]['base']
        rate = fpl[year]['rate']

        income = calculate_rate(base, rate, household_size)

        return jsonify({
            'request': {
                'year': year,
                'household_size': household_size
            },
            'info': {
                'year_base': base,
                'year_rate': rate
            },
            'amount': income,
            'amount_nice': nice_amount(income)
        })

    # otherwise return a version number and learn more
    else: 
        return NULL_RETURN

if __name__ == '__main__':
    app.run(debug=True)