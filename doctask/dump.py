import csv
import re
import pandas as pd
f = open("input.txt")
data=f.read().replace(" ", "").replace('\n','')
y=data.replace("details."," ")
    # z= re.findall("AMQ8441:DisplayClusterQueueManager", y)
x=y.replace("AMQ8441:DisplayClusterQueueManager","\n")
with open('dump.txt','w') as f:
    f.write(str(x)+'\n')