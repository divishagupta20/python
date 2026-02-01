import random
import os
import shutil
import json
import csv
from datetime import datetime,timedelta
import time
import re
x = random.randint(1,10)
print(x)
print(random.choice(["hj",1,"hft",True]))

print(os.getcwd())

os.mkdir('foldr')




shutil.copyfile('source.txt','destination.txt')

dic = {"hello":1,"ogg":2}
print(dic)
string = json.dumps(dic)

print(string)

d = json.loads(string)
print(d)

now = datetime.now()

print(now)

yesterday = now - timedelta(days=1)
print(yesterday)

print(time.time())
#time.sleep(2)
print(time.time())


pattern = r'\d+'
text= "hello 1234 is 456"
match = re.search(pattern,text)
print(match.group())
