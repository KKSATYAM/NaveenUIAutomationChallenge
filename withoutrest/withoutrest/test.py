import requests

BASE_URL='https://scaling-lamp-55p4qpv956j3r9q-8000.app.github.dev/'
ENDPOINT='get/'

def get_all_employee_data():
    response=requests.get(BASE_URL+ENDPOINT)
    # print(response.json())
    print(response.status_code)

# get_all_employee_data()
def post_all_employee_data():
    response=requests.post(BASE_URL+ENDPOINT)
    # print(response.content)
    print(response.status_code)

post_all_employee_data()
