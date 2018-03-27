from flask import request, make_response, Flask
from route_decorators import url_verification, validate_response
from lunch_handler import create_lunch_event

VERIFICATION_TOKEN = 'verification token from slack workspace'
app = Flask(__name__)


@app.route('/event_endpoint', methods=['POST'])
@url_verification
@validate_response('token', VERIFICATION_TOKEN, 'json')
def events_route():
    """
    Any event based response will get routed here.
    Decorates first make sure it's a verified route and this isn't a challenge event
    Lastly forwards event data to route director
    """

    return make_response('', 200)


@app.route('/lunch', methods=['POST'])
@validate_response('token', VERIFICATION_TOKEN, 'values')
def random_lunch():
    """
    Endpoint for getting random lunch event.
    Sends the notification to whichever channel the user
    was in when running the slash-command
    """
    req = request.values
    lunch_val = create_lunch_event(req)
    return make_response(lunch_val, 200)

if __name__ == '__main__':
    app.run(port=5000, debug=True)