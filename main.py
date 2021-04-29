from flask import Flask, render_template, request, make_response
from ast import literal_eval
from Bowling import BowlingChallenge

app = Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['POST', 'GET'])
def form():
    if request.method == 'GET':
        response = make_response(render_template('form.html'))
        add_header(response)
        return response
    if request.method == 'POST':
        form_data = request.form

        #_filename = ''

        bowl = BowlingChallenge()
        #giveninputScores = bowl.readInput(_filename)
        allStrikes = False

        # Accept list of scores as input from form.html
        inputRolls = bowl.convertStringstoInt(form_data['projectFilepath'])
        #inputRolls = literal_eval(form_data['projectFilepath'])

        if len(inputRolls) <= 21:

            finalScore, table = bowl.bowling_score(inputRolls)

            # Set allStrikes flag to True if all elements of input list are 10
            if all(elem == 10 for elem in inputRolls):
                allStrikes = True

            # Show output only if 0<=finalScore<=300 and table is not empty and (allStrikes is False or allStrikes is
            # True and number of rolls is 12)
            if (0 <= finalScore <= 300 and (allStrikes is True and len(inputRolls) == 12) and len(table) != 0) or (
                    0 <= finalScore <= 300 and allStrikes is False and len(table) != 0):
                response = make_response(render_template('index.html', title='Bowling Scoreboard', result=table))
                add_header(response)

            # Error if allStrikes is True and number of inputs > 12
            elif (len(inputRolls) > 12 and allStrikes is True) or finalScore == 0:
                response = make_response(render_template('err.html'))
                add_header(response)
            else:
                response = make_response(render_template('err.html'))
                add_header(response)
        else:
            response = make_response(render_template('err.html'))
            add_header(response)
        return response


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'no-cache, no-store'
    response.headers['Pragma'] = 'no-cache'
    return response


if __name__ == "__main__":
    app.run(host="localhost", port=5000)
