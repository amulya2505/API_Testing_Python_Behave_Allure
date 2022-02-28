import json
from behave import *
import requests
from utils  import config
from utils  import create_body
from utils  import response


request_headers = {}
response = {}
response_codes = {}
request_body = {}


@when('when user sets the url for {param}')
def step_impl(context, param):
    global url
    if (context.config.userdata['env'] == 'local'):
        url = config.LOCAL_URL + param
        request_headers['Content-Types'] = config.CONTENT_TYPE
    else:
        url = config.PROD_URL 
        request_headers['Content-Types'] = config.CONTENT_TYPE
    print(url)


@step(u'set the asr body for in with "{params2}"')
def step_impl(context,params2):
    request_body['POST'] = create_body.reqbody(params2)


@then('should see a valid response {param}')
def step_impl(context,param):
    print(request_headers)
    print(request_body)
    response = requests.post(url=url, headers=request_headers, json=request_body['POST'])
    statuscode = response.status_code
    response_codes['POST'] = statuscode
    print(response)
    json_data = json.loads(response.text)
    textresponse = json_data["key"]

    assert response_codes['POST'] == config.SUCCESS_CODE
# validate reponse which you want to pass from feature file and then refer to response.py file
    assert textresponse == response.reponse[param] 
    

# make sure the names of the steps are same as defined in the feature file.
# behave also detects the duplicacy in the names in steps file, One has to keep the names different for different functions and it can be tricky sometimes
