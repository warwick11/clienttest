import requests
import json

url ='https://httpbin.org/get'
LINE_ACCESS_TOKEN= 'X2cOT4rC4BPy3C42mpBttRpOBZYFSH5olp+aqGy1V/Ltca6BEQ9wI66xWouCaCYfXXCgSpX2K9l/UCu5h4fPFLgOp4/v9ijNiERzYSEOMG+h3nE5ADrBhT3Et8J8QNAofbsEeg0nBTA4m+ih4NEqSgdB04t89/1O/w1cDnyilFU='
replaytoken=''

headers={
    'Content-Type': 'application/json; charset=UTF-8',
    'Authorization': 'Bearer ' + LINE_ACCESS_TOKEN
}

payload={
    'replyToken': event.replyToken,
    'messages': [{
    'type': 'text',
    'text': 'test'
      }]
}

reponse = requests.post(url)
print(reponse)