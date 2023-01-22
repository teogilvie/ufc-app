#export FLASK_APP=api.py && export FLASK_DEBUG=1 && flask run
#Find out why .flaskenv won't read

from flask import Flask, request
from UFC_Stat_Comparison import fight_prediction
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

fighterInfo = [{'f1fn': 'jiri',
                'f1ln': 'prochazka',
                'f2fn': 'glover',
                'f2ln': 'teixeira'}
                ]

@app.route('/prediction', methods=['GET', 'POST'])
def predict_fight():
    if request.method == 'POST':
        f1fn = request.json['f1fn']
        f1ln = request.json['f1ln']
        f2fn = request.json['f2fn']
        f2ln = request.json['f2ln']
        fighterInfo.append({'f1fn': f1fn, 'f1ln': f1ln, 'f2fn': f2fn, 'f2ln': f2ln})
        prediction = fight_prediction(f1fn, f1ln, f2fn, f2ln)
        return {'winner': prediction}
    
 

@app.route('/test')
def test_link():
    prediction = 'Success'
    return {'winner': prediction}

