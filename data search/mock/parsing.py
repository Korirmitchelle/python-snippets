import json
from pprint import pprint
var = raw_input("Please enter id: ")
with open('data.json') as data_file:
    var = json.load(data_file)
    pprint(var)
    var["id"] 