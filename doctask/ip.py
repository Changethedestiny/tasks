import re
l=[]
f = open("input.txt")
data=f.read().replace(" ", "").replace('\n','')
y=data.replace("details."," ")
    # z= re.findall("AMQ8441:DisplayClusterQueueManager", y)
x=y.replace("AMQ8441:DisplayClusterQueueManager","\n")
print(x)
# print(data)
            
