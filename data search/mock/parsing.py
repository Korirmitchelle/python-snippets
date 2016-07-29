import json
from pprint import pprint
var=int(raw_input("Enter ID\n"))
if var!=0:
    with open('data.json') as json_data:
        data=json.load(json_data)
        for r in (data['Users']):
            if (r['id'] == var):
                print (r['id'])
                print (r['first_name'])
                print (r['last_name'])
                print (r['email'])
                print (r['gender'])
else:
    print("ID must enter a number")