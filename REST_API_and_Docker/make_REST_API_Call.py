import requests
# import json

payload = {'input_sentence': "I love this movie and i would watch it again and again!"}
# payload = {'input_sentence': "I like this movie, However its good to watch one time only."}
# payload = {'input_sentence': "I don't like this movie, as it had bad plot and bad acting."}
url = 'http://127.0.0.1:8080/get_sentiment'
# url = 'http://127.0.0.1:8080/'

result = requests.post(url, data=payload)

if __name__=='__main__':
    print(result.text)