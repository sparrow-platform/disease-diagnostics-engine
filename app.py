
from __future__ import print_function # In python 2.7
from flask import Flask, session, render_template, make_response, jsonify, request, send_from_directory, g, url_for
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
import json
from sklearn.naive_bayes import GaussianNB
import numpy as np
import pickle as pkl
from sklearn.externals import joblib
import pandas as pd
from decimal import Decimal
from werkzeug.utils import secure_filename
import logging
from flask import escape
from flask_expects_json import expects_json
import math
import operator
from more_itertools import unique_everseen
from uuid import uuid4

import os
import uuid
import requests
import sys

from helper import vector_cos5, isValid, isInDB, get_model, findFeatures, findSymptom, findDisease, syInData





app = Flask(
    __name__
)



class SetEncoder(json.JSONEncoder):
    def default(self, obj):
       if isinstance(obj, set):
          return list(obj)
       return json.JSONEncoder.default(self, obj)



def get_model():
    model_file = 'data/all-files-for-ml/' + 'all_mnb' + '.pkl'
    mnb = joblib.load(open(model_file, 'rb'))
    data = pd.read_csv("data/all-files-for-ml/all_x.csv")
    df = pd.DataFrame(data)
    cols = df.columns
    features = cols # = symptoms
    features_raw = [str(features[x]) for x in range(len(features))]
    # convert feature array into dict of symptom: index
    feature_dict = {}
    for i,f in enumerate(features):
        feature_dict[f] = i
    return mnb, features, feature_dict

MODEL, LABELS, LABELS_DICT = get_model()



@app.route('/api/labels', methods = ['GET'])
def labels():
    features_for_select = []
    for i,f in enumerate(LABELS):
        features_for_select.append({ "value": f, "label": f })
    return jsonify(features_for_select)



@app.route('/api/sySuggest', methods = ['POST'])
def sySuggest():
    data = request.get_json(silent=True)
    symp = escape(data.get('symptom'))
    print(symp)

    # load the weights
    new_vecs = np.load('data/all-files-for-ml/' + '10_epochs_0.6_similarity.npy')
    similarity_score = 0.6

    d = pd.read_csv('data/all-files-for-ml/' + 'Dictionary.csv')
    dic = {}
    for i in d.index:
        dic[d.Key.loc[i]] = d.Values.loc[i]

    results = []

    syInDataset = syInData()

    symptom = np.load('data/all-files-for-ml/' + 'symptom.npy')

    # loop through the symptoms in the data set and find the symptoms with cosine similarity greater than 'similarity_score'
    for i in set(symptom):
    #.reshape(1, -1)
        if i in syInDataset and symp in dic:
            XA = new_vecs[dic[i]]
            XB = new_vecs[dic[symp]]

            similarity = vector_cos5(XA, XB)

            if (similarity) > similarity_score:
                # remove the same symptom from the list of outputs
                if i != symp:
                    syStr = findSymptom(i, lang='ENG')
                    if len(syStr) != 0:
                        results.append({"label":syStr, "value": i})
                    else:
                        results.append({"label":i, "value": i})
        else:
            continue


    return jsonify(results)


schema = {
  'type': 'object',
  'properties': {
    "symptoms": {
      "type": "array",
      "items": {
        "type": "string"
      }
    },
    "text": {
      "type": "string",
    }
  }
}

availableLang = {'en': 'ENG', 'de': 'GER'}



@app.route('/api/predict', methods = ['POST'])
@expects_json(schema) # if payload is invalid, request will be aborted with error code 400
def predict():
    lang = escape(request.args.get('lang'))
    data = request.get_json(silent=True)
    search = data.get('symptoms')
    text = data.get('text')

    #if text: search = getConcepts(text)

    if lang is None or lang not in list(availableLang.keys()):
        lang = 'en'

    langCode = availableLang[lang]


    if len(search) == 0:
        return jsonify({})

    sample = np.zeros((len(LABELS),), dtype=np.int)
    sampe = sample.tolist()

    for i, cui in enumerate(search):
      if isValid(cui):
        if isInDB(cui):
          sample[LABELS_DICT[cui]] = 1
        else:
          print("skipping " + cui)
      else:
        print("CUIs must consist of the letter 'C' "+ "followed by 7 digits: " + cui)

    sample = np.array(sample).reshape(1,len(sample))
    results = MODEL.predict_proba(sample)[0]

    results_ordered_by_probability = map(lambda x: {
        "disease": findDisease(x[0], langCode),
        "disease_cui": x[0],
        "prob": round(Decimal(x[1] * 100), 3),
        "sy": findFeatures(x[0], langCode)
    }, sorted(zip(MODEL.classes_, results), key=lambda x: x[1], reverse=True))

    prediction = results_ordered_by_probability[:15]

    return jsonify(prediction)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)