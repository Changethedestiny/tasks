# import re
# import pandas as pd
# from itertools import chain
# import csv
# fi=open("input.txt","r")
# lst=[]
# final_heads=[]
# final_values=[]
# dic={}
# for i in fi:
#     data=i.replace(" ", "").replace('\n','')
#     d=data.replace("details."," ")
#     w=d.replace("AMQ8441:DisplayClusterQueueManager","\n")
#     z=w.replace(",","jaya").replace(".","sree").replace("()","(full)")
#     y=z.replace(")",",").replace(","," ").replace("("," ")
#     x=y.replace("sree", ".").replace("jaya", ",").replace("full","none")
#     sp=x.split()
#     head=sp[::2]
#     lst.append(head)
#     v=sum(lst,[])
#     value=sp[1::2]
#     di=dict(zip(head,value))
#     final_values.append(di)
# for j in v:
#     if j not in final_heads:
#         final_heads.append(j)
# with open('sample4.csv', 'w', encoding='UTF8', newline='') as f:
#         writer = csv.DictWriter(f, fieldnames=final_heads)
#         writer.writeheader()
#         writer.writerows(final_values)
# df=pd.read_csv('sample4.csv')
# df.fillna('NULL',inplace=True)
# df.to_csv('sample4.csv', index=False)
# print("data is stored in sheet")
# import re
# l=[]
# f = open("input.txt")
# data=f.read().replace(" ", "").replace('\n','')
# y=data.replace("details."," ")
#     # z= re.findall("AMQ8441:DisplayClusterQueueManager", y)
# x=y.replace("AMQ8441:DisplayClusterQueueManager","\n")
# with open('dump.txt','w') as f:
#     f.write(str(x)+'\n')


import csv
import re
import pandas as pd
f = open("input.txt")
data=f.read().replace(" ", "").replace('\n','')
y=data.replace("details."," ")
    # z= re.findall("AMQ8441:DisplayClusterQueueManager", y)
x=y.replace("AMQ8441:DisplayClusterQueueManager","\n")
with open("dump".txt','w') as f:
    # f.write(str(x)+'\n')

fi=open("input.txt","r"):
lst=[]
final_heads=[]
final_values=[]
dic={}
for i in fi:
    z=i.replace(",","n").replace(".","b").replace("( )","(noe)")
    y=z.replace(")",",").replace(","," ").replace("("," ")
    x=y.replace("b", ".").replace("n", ",").replace("noe","()")
    sp=x.split()
    head=sp[::2]
    lst.append(head)
    v=sum(lst,[])
    value=sp[1::2]
    di=dict(zip(head,value))
    print(di)
    final_values.append(di)
for j in v:
    if j not in final_heads:
        final_heads.append(j)
with open('sample4.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=final_heads)
    writer.writeheader()
    writer.writerows(final_values)
df=pd.read_csv('sample4.csv')
df.fillna('NULL',inplace=True)
df.to_csv('sample4.csv', index=False)
print("data is stored in sheet")