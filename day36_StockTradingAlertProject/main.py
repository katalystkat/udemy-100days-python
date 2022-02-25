STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
stockapi_key = "5TW9PX71OPIWJ59R"
news_api_key = "bc396939bd2d486e89c1114c2869b98d"
account_sid = "AC7ae818f5b0b79d62d5cb67c8636db01a"
auth_token = "43d09420ef8491cd5af44c7383460e94"
phone_number = "+18607757217"

import requests
def get_news():
    news_url = NEWS_ENDPOINT
    news_parameters = dict(apiKey=news_api_key, q=COMPANY_NAME, language="en", pageSize=10)
    news_request = requests.get(news_url, params=news_parameters)
    stock_news = news_request.json()
    stock_articles_titles = [stock_news["articles"][n]["title"] for n in [0,3]]
    print(stock_articles_titles)
    stock_articles_descriptions = [stock_news["articles"][n]["description"] for n in [0,3]]
    print(stock_articles_descriptions)

# replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
url = STOCK_ENDPOINT
stocks_parameters= {
    "function" : "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "outputsize":"compact",
    "apikey": stockapi_key
}
r = requests.get(url, params=stocks_parameters)
data = r.json()

yesterday_close= data["Time Series (Daily)"]["2022-02-23"]["4. close"]
yesteryesterday_close = data["Time Series (Daily)"]["2022-02-22"]["4. close"]
five_below = 0.95*(float(yesteryesterday_close))
five_above = 1.05*(float(yesteryesterday_close))
if five_below <= float(yesterday_close) <= five_above:
    print("We are within 5%")

if float(yesterday_close)> five_above:
    print("Whoa, we're experiencing some >5% action today... let's see why")
    get_news()
if float(yesterday_close) < five_below:
    print("Oopsies, we're experiencing some <5% action since yesterday.. Let's see why")
    get_news()


## STEP 1: Use https://newsapi.org/docs/endpoints/everything
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
#HINT 1: Get the closing price for yesterday and the day before yesterday. Find the positive difference between the two prices. e.g. 40 - 20 = -20, but the positive difference is 20.
#HINT 2: Work out the value of 5% of yerstday's closing stock price. 



## STEP 2: Use https://newsapi.org/docs/endpoints/everything
# Instead of printing ("Get News"), actually fetch the first 3 articles for the COMPANY_NAME. 
#HINT 1: Think about using the Python Slice Operator



## STEP 3: Use twilio.com/docs/sms/quickstart/python
# Send a separate message with each article's title and description to your phone number. 
#HINT 1: Consider using a List Comprehension.



#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

