from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)
from weblio import *

app = Flask(__name__)

line_bot_api = LineBotApi('OCns1AwjeI3wfAyD/+KKlQr1bXaBBPT44nuERvxLE+/MZKkUI6/eMnTc9PKaJn/LXEcMXnzMcuhc2Km5GZePWGViDbdSwAUCiinAYTDIFtqv5lvlPN8UTv0a6U4wWBWqirBobPiWaWtizW+Vw4sKxwdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('426b62b84070433c13e91a1b77df5d9b')

@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=Research(event.message.text))
        )


if __name__ == "__main__":
    app.run()
