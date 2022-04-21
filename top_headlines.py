from flask import Flask, render_template
import requests
import secrets

app = Flask(__name__)


@app.route('/')
def welcome():
    """
    handle welcome request
    :return:
    """
    return render_template('welcome.html')


@app.route('/name/<input_name>')
def hello(input_name):
    """
    handle hello request
    :param input_name:
    :return:
    """
    return render_template('name.html', name=input_name)


@app.route('/headlines/<input_name>')
def headlines(input_name):
    """
    handle headlines request
    :param input_name:
    :return:
    """
    # do request Top Stories
    url = "https://api.nytimes.com/svc/topstories/v2/technology.json"
    querystring = {"api-key": secrets.api_key}
    payload = ""
    headers = {'Content-Type': 'application/json'}

    # analyze response data
    response = requests.request("GET", url, data=payload, headers=headers, params=querystring)
    result = response.json()
    return render_template('headline.html', first_headline=result[0]['title'], second_headline=result[1]['title'],
                           third_headline=result[2]['title'], fourth_headline=result[3]['title'],
                           fifth_headline=result[4]['title'])
    # return render_template('headline.html', first_headline='This is first', second_headline='This is second',
    #                        third_headline='This is thrid', fourth_headline='This is fourth',
    #                        fifth_headline='This is fifth', name=input_name)


if __name__ == '__main__':
    app.run()
