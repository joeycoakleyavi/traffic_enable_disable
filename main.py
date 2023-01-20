from avi.sdk.avi_api import ApiSession
import os
import sys
import json
import requests
import urllib3

if hasattr(requests.packages.urllib3, 'disable_warnings'):
    requests.packages.urllib3.disable_warnings()
  
if hasattr(urllib3, 'disable_warnings'):
    urllib3.disable_warnings()

def ParseAviParams(argv):
    if len(argv) != 2:
        return
    alert_params = json.loads(argv[1])
    print(str(alert_params))
    return alert_params

def get_api_token():
    return os.environ.get('API_TOKEN')
  
def get_api_user():
    return os.environ.get('USER')
  
def get_api_endpoint():
    return os.environ.get('DOCKER_GATEWAY') or 'localhost'
  
def get_tenant():
    return os.environ.get('TENANT')

def toggle_vs_enabled_disabled(session, vs_uuid, vs_name, state, retries=5):
    if retries <= 0:
        return "Too many retry attempts - aborting!"
    data = {'replace': {'traffic_enabled': state}}
    p_result = session.patch('virtualservice/{}'.format(vs_uuid), data=data)

    if p_result.status_code < 300:
        return '{vs_name} with UUID {vs_uuid} traffic_enabled parameter successfully set to {state}'.format(vs_name=vs_name, vs_uuid=vs_uuid, state=state)
    else:
        return toggle_vs_enabled_disabled(session, vs_uuid, vs_name, state, retries - 1)
    return "Unable to change traffic_enabled parameter for {}".format(vs_name)

if __name__ == "__main__":
    alert_params = ParseAviParams(sys.argv)
    events = alert_params.get('events', [])
    if len(events) > 0:
        token = get_api_token()
        user = get_api_user()
        api_endpoint = get_api_endpoint()
        tenant = get_tenant()

        vs_uuid = events[0]['obj_uuid']
        vs_name = events[0]['obj_name']

        state = False if events[0]['event_id'] == "VIP_DOWN" else True

        try:
            with ApiSession(api_endpoint, user, token=token, tenant=tenant) as session:
                result = toggle_vs_enabled_disabled(session, vs_uuid, vs_name, state)
        except Exception as e:
            result = str(e)
    else:
        result = 'No event data for ControlScriopt'
    
    print(result)