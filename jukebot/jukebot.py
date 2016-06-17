from flask import Flask, request
from fbmsgbot.bot import Bot
from config.info import TOKEN

token = TOKEN
app = Flask(__name__)
bot = Bot(TOKEN)

@app.route('/webhook', methods=['GET', 'POST'])
def listen():
    """
    NOTE request.args returns a multilist AKA a dict {k: []} where 
    values are lists
    """

    # Handle initial facebook authentication
    if request.args.get('hub.verify_token') == token:
        return request.args.get('hub.challenge')

    message = bot.messages_for_request(request)

    return "hello world"

if __name__ == "__main__":
    app.run(port=8000)