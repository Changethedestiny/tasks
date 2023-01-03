import csv
fieldnames = ['CLUSQMGR', 'CHANNEL', 'CLUSTER', 'SSLCIPH','STATUS','LION','JAYA','DEFTYPE']  
rows = [
{'CLUSQMGR': 'QM3', 'CHANNEL': 'TO.QM3.S', 'CLUSTER': 'DEMO', 'SSLCIPH': 'TRIPLE_DES_SHA_US', 'STATUS': 'INACTIVE', 'LION': '()'},
{'CLUSQMGR': 'QM3,MQ1', 'CHANNEL': 'TO.QM3', 'CLUSTER': 'DEMO', 'SSLCIPH': '.', 'STATUS': 'INACTIVE', 'JAYA': '-none'},
{'CLUSQMGR': 'QM1', 'CHANNEL': 'TO.QM1', 'CLUSTER': 'DEMO', 'DEFTYPE': 'CLUSSDRB', 'SSLCIPH': '()', 'STATUS': 'RUNNING'}
] 
for i in rows:
        for j in i.values():
                
                        

# with open('countries.csv', 'w', encoding='UTF8', newline='') as f:
#         writer = csv.DictWriter(f, fieldnames=fieldnames)
#         writer.writeheader()
#         writer.writerows(rows)

