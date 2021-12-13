from flask import Flask, jsonify
from flask import request
from flask_cors import cross_origin

import os
import json
import joblib
import time

import nltk

from score import vader, lda, score

# download required sources
nltk.download('vader_lexicon')
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')
nltk.download('tagsets')
nltk.download('stopwords')
nltk.download('words')
nltk.download('punkt')


app = Flask(__name__)

lda_model = joblib.load('LDA_model.jbl')
dictionary = joblib.load('dictionary.jbl')
removed_words = joblib.load('removed_words.jbl')

@app.route('/', methods=['GET'])
@cross_origin()
def health_check():
    return 'OK'


@app.route('/predict', methods=['POST'])
@cross_origin()
def predict():
    global lda_model

    # flask always has a "request" object that contains the input data.
    request_input = request.get_json()

    text = request_input.get('text')

    tokenized_sentences, vader_scores = vader(text)

    sentence_lda_scores = lda(tokenized_sentences, lda_model, dictionary, removed_words)

    return score(vader_scores, sentence_lda_scores)
    

@app.errorhandler(Exception)
def handle_exception(error):
    response = jsonify({'msg': 'Internal server error'})
    response.status_code = 500
    return response

if __name__ == '__main__':
    app.run('localhost', port=5000)