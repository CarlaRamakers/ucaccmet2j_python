import json
with open('ucaccmet2j_python/precipitation.json')as file:
    precipiation = json.load(file)

preci = []
for line in precipiation:
    seattle = line['station']
    if seattle == 'GHCND:US1WAKG0038':
         preci.append(line)
    else: line = '' 

month_list = [0,0,0,0,0,0,0,0,0,0,0,0]
number = 0
months = 0
for line in preci:
    date = str(line['date'])
    sep_date = date.split(sep='-')
    month = int(sep_date[1])
    value = line['value']
    month_list[month-1]= month_list[month-1] + value

with open('ucaccmet2j_python/results.json','w',encoding='utf-8')as file:
    json.dump(month_list,file,indent=4)   

suma = 0
for lines in preci:
    value = lines['value'] 
    if 'value' in lines:
        suma = suma + value
    else: suma = 0
print(suma)
