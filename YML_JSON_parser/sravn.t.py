import json
import yaml
import time
start_time = time.clock()
with open('sravn.yml') as f:       
    dataMap = yaml.safe_load(f) 
    print (json.dumps(dataMap))
print(time.clock()-start_time)