import os
from flask import Flask, jsonify, request
from flask_cors import CORS


from dotenv import load_dotenv
load_dotenv()

CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")

from reloadly_core.core.enums.Environment  import Environment
from reloadly_giftcard.giftcard.sdk.client.GiftcardAPI import GiftCards

giftcardAPI = GiftCards(clientId=CLIENT_ID, clientSecret=CLIENT_SECRET, environment=Environment.GIFTCARD_SANDBOX)

countryCode = "US"
FETCHRESPONSE = giftcardAPI.products().getByISO(countryCode)

app = Flask(__name__)
app.config.from_object(__name__)
CORS(app, resources={r'/*': {'origins': '*'}})


@app.route('/', methods=['GET'])
def all_giftcards():
   response_object = {'status': 'success'}
   if request.method == 'GET':
     response_object['giftcards'] = FETCHRESPONSE
   return jsonify(response_object)


if __name__ == "__main__":
  app.run()