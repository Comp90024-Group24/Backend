from flask import Flask, jsonify, make_response
import requests

app = Flask(__name__)

def get_document_count():
    url = "http://172.26.134.204:5984/twitter_all/_design/Lang/_view/lang_num"
    response = requests.get(url, auth=('user', 'pwd'))
    if response.status_code != 200:
        app.logger.error('GET /tasks/ {}'.format(response.status_code))
        return None, "Error: Unexpected response {}".format(response)
    data = response.json()
    try:
        return data['rows'][0]['value'], None
    except (KeyError, IndexError):
        return None, "Error: Could not parse CouchDB response"

@app.route('/document_count')
def document_count():
    count, error = get_document_count()
    if error:
        return make_response(jsonify({'error': error}), 400)
    else:
        return jsonify({"document_count": count})

if __name__ == '__main__':
    app.run(debug=True,debug=True,host='0.0.0.0',port='8000')
