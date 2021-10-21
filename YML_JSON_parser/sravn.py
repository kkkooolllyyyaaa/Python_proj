import json
import yaml
with open('sravn.yml') as f:       
    dataMap = yaml.safe_load(f) 
    print (json.dumps(dataMap))