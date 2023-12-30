from flask import Flask,request
import requests
from pymessenger import Bot
app = Flask(__name__) #creating the Flask class object

VERIFYTOKEN ='haile_chatbot'
PAGE_ACCESS_TOKEN = "EAACmsTvt5ZB8BO0x6hv2qcpZAdLh3DeJXQsuZBLcknfOWq1SCf88OU1g4A4ENFx4Vp9J8nojgLFssPujYQI3Vh5Lb0gbRvT8PQl3AnUh6OVdC0GwIXwZAXs3AJRwJZCHpQ0FmePUWf1DyHa2AGSz9gQwfG1RihqfJ2LZCaQL7UL7ZBUOw37Mo6repe7saqAmgeFGZBukClgJ2kTsJ8ZArhgZDZD "
bot =Bot(PAGE_ACCESS_TOKEN)

def handling_message(text):
 adjusted_msg =text
 if adjusted_msg =="hi" or adjusted_msg == "Hi":
  response ="hello"
 elif adjusted_msg =="what's up " or adjusted_msg == "What's up ":
   response ="I am great"
 else:
    response="i am pleasure to"
    return response

@app.route('/', methods=["POST" , "GET"])
def web_hook():
    if request.method == 'Get':
        if request.args.get('hub.verify_token') ==VERIFYTOKEN:
            return request.args.get(hub.challenge)
        else:
            return "unable to connect fb"
    elif request.method =="Post":
        data= request.json
        process= data['entry'][0]['messaging']
        for msg in process :
            text=msg['message']['text']
            sender_id=msg['sender']['id']
            response=handling_message(text)
            bot.send_text_message(sender_id,response)
        return "message post"
    else:
        return "ok"
    if _name_ == '_main_':
        app.run()







