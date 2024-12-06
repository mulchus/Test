import rollbar
from environs import Env

env = Env()
env.read_env()
ROLLBAR_ACCESS_TOKEN = env('ROLLBAR_ACCESS_TOKEN')

rollbar.init(
  access_token=ROLLBAR_ACCESS_TOKEN,
  code_version='1.0',
  environment='dev',
)

# report_message
rollbar.report_message('Rollbar is configured correctly', 'info')

# report_error
# try:
#     a = None
#     a.hello()
# except:
#     rollbar.report_exc_info()


# Example of error data enrichment (optional)
def payload_handler(payload, **kw):
    # Adding info about the user affected by this event (optional)
    # The 'id' field is required, anything else is optional
    payload['data']['person'] = {
        'id': '1234',
        'username': 'testuser',
        'email': 'user@email',
    }

    # Example of adding arbitrary metadata (optional)
    payload['data']['custom'] = {
        'trace_id': 'aabbccddeeff',
        'feature_flags': [
            'feature_1',
            'feature_2',
        ],
    }

    return payload


rollbar.events.add_payload_handler(payload_handler)

try:
    a = None
    a.hello()
except:
    rollbar.report_exc_info()
