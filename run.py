import json
import math
from fpl import fpl
from flask import Flask, request, jsonify

app = Flask(__name__)
VERSION = 1
CURRENT_YEAR = '2015'
NULL_RETURN = 'FPLAPI Version {}.<br>Learn more at <a href="http://github.com/codeforamerica/fplapi">github.com/codeforamerica/fplapi</a>.'.format(VERSION)
CURRENT_USER_INCOME = 0.0
ALLOWED_INCOME_TYPES = ('annual', 'monthly')

def calculate_fpl_percentage(user_income_type, user_income, base_income):
    user_income = user_income*12 if user_income_type == ALLOWED_INCOME_TYPES[1] else user_income
    return round(100*(user_income/base_income), 2)

def calculate_rate(base, rate, size):
    amount = base + (rate * (int(size) - 1))
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

        # if no year is specified, default to CURRENT_YEAR
        if (request.args.get('year')):
            year = request.args.get('year')
        else:
            year = CURRENT_YEAR

        base = fpl[year]['base']
        rate = fpl[year]['rate']

        # if no household size is specified, return an error
        # TODO: return a different reponse with all household size info
        if (request.args.get('size')):
            household_size = request.args.get('size')
        else:
            return 'No household size specified in URL. Example: <code>size=4</code>.'

        # If no income is specified, carry on with the computations
        if (request.args.get('income')):
            user_income = float(request.args.get('income'))
        else:
            user_income = CURRENT_USER_INCOME

        # If no income type is specified, set annual as default type
        if (request.args.get('income_type') and request.args.get('income_type') in ALLOWED_INCOME_TYPES):
            user_income_type = request.args.get('income_type')
        else:
            user_income_type = ALLOWED_INCOME_TYPES[0]

        income = calculate_rate(base, rate, household_size)
        fpl_percentage = calculate_fpl_percentage(user_income_type, user_income, income)

        return jsonify({
            'request': {
                'year': year,
                'household_size': household_size,
                'income': user_income
            },
            'info': {
                'year_base': base,
                'year_rate': rate
            },
            'amount': income,
            'amount_nice': nice_amount(income),
            'fpl_percentage': fpl_percentage
        })

    # otherwise return a version number and learn more
    else:
        return NULL_RETURN

if __name__ == '__main__':
    app.run(debug=True)

def start():
    return app