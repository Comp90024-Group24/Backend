from flask import Flask
import couchDBUtil as dbUtil

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route('/postTest', methods=["POST"])
def postTest():
    result = [{'cityName': 'London', 'twitterCount': 1000}, {'cityName': 'New York', 'twitterCount': 2000}]
    return result


@app.route('/getTest', methods=["GET"])
def getTest():
    result = [{'cityName': 'London', 'twitterCount': 1000}, {'cityName': 'New York', 'twitterCount': 2000}]
    return result


# Get the number of tweets posted by each city
@app.route('/city_num', methods=["GET"])
def getCityTwitterCounts():
    db = dbUtil.getDB()
    view = dbUtil.getView(db, 'city/city_num')
    data = []
    for row in view:
        rowInfo = {'cityName': row.key, 'twitterCount': row.value}
        data.append(rowInfo)
    return data

# Get the number of tweets posted in each language
@app.route('/lang_num', methods=["GET"])
def getLanguageTwitterCounts():
    db = dbUtil.getDB()
    view = dbUtil.getView(db, 'lang/lang_num')
    data = []
    for row in view:
        rowInfo = {'language': row.key, 'twitterCount': row.value}
        data.append(rowInfo)
    return data

# Get the number of tweets posted in each language
@app.route('/month_num', methods=["GET"])
def month_num():
    db = dbUtil.getDB()
    view = dbUtil.getView(db, 'month/month_num')
    data = []
    for row in view:
        rowInfo = {'month': row.key, 'twitterCount': row.value}
        data.append(rowInfo)
    return data

# Get urban opposition
@app.route('/city_polarity', methods=["GET"])
def city_polarity():
    db = dbUtil.getDB()
    view = dbUtil.getView(db, 'polarity/city_polarity')
    data = []
    for row in view:
        rowInfo = {'cityName': row.key, 'polarity': row.value}
        data.append(rowInfo)
    return data

#GET
@app.route('/polarity_month_average', methods=["GET"])
def polarity_month_average():
    db = dbUtil.getDB()
    view = dbUtil.getView(db, 'polarity_month/polarity_month_average')
    data = []
    for row in view:
        rowInfo = {'month': row.key, 'polarity': row.value}
        data.append(rowInfo)
    return data



if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port='8000')
