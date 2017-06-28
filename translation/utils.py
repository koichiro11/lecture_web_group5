# coding:utf-8

import requests
import json

import google_api


def translate_text_with_model(text, source, target, model="nmt"):
    """
    :param text: source text
    :param source: source language
    :param target: target language
    :param model: using model (defualt:nmt)
    :return:
    """
    # set token here
	token = google_api.google_api_key
    url = "https://translation.googleapis.com/language/translate/v2"

    payload = {
	            'target': target,
	            'source': source,
	            'q': text,
	            'model': model,
	            'key': token
            	}

    headers = {
            	'Content-Type': 'application/json',
                    # 'Authorization': 'Bearer ' + token,
            }

    response = requests.get(url, params=payload, headers=headers)

    # JSON decode
    jObj = json.loads(response.text)

    # print(jObj)
    return jObj
