import json
with open('ucaccmet2j_python/precipitation.json')as file:
    precipiation = json.load(file)

preci = []
for line in precipiation:
    seattle = line['station']
    if seattle == 'GHCND:US1WAKG0038':
         preci.append(line)
    else: line = ''
suma = 0
for lines in preci:
    value = lines['value'] 
    if 'value' in lines:
        suma = suma + value
    else: suma = 0

seattle_list = [0,0,0,0,0,0,0,0,0,0,0,0]
number = 0
months = 0
for line in preci:
    date = str(line['date'])
    sep_date = date.split(sep='-')
    month = int(sep_date[1])
    value = line['value']
    seattle_list[month-1]= (seattle_list[month-1] + value)

count= -1
relative_seattle = []
for divided in seattle_list:
    count = count +1
    relative_seattle.append(seattle_list[count]/suma)



preci = []
for line in precipiation:
    cincinnati = line['station']
    if cincinnati == 'GHCND:USW00093814':
         preci.append(line)
    else: line = ''
sumas = 0
for lines in preci:
    value = lines['value'] 
    if 'value' in lines:
        sumas = sumas + value
    else: sumas = 0

cincinnati_list = [0,0,0,0,0,0,0,0,0,0,0,0]
number = 0
months = 0
for line in preci:
    date = str(line['date'])
    sep_date = date.split(sep='-')
    month = int(sep_date[1])
    value = line['value']
    cincinnati_list[month-1]= (cincinnati_list[month-1] + value)

count= -1
relative_cincinnati = []
for divided in cincinnati_list:
    count = count +1
    relative_cincinnati.append(cincinnati_list[count]/sumas)



preci = []
for line in precipiation:
    maui = line['station']
    if maui == 'GHCND:USC00513317':
         preci.append(line)
    else: line = ''
sumasa = 0
for lines in preci:
    value = lines['value'] 
    if 'value' in lines:
        sumasa = sumasa + value
    else: sumasa = 0

maui_list = [0,0,0,0,0,0,0,0,0,0,0,0]
number = 0
months = 0
for line in preci:
    date = str(line['date'])
    sep_date = date.split(sep='-')
    month = int(sep_date[1])
    value = line['value']
    maui_list[month-1]= (maui_list[month-1] + value)


count= -1
relative_maui = []
for divided in maui_list:
    count = count +1
    relative_maui.append(maui_list[count]/sumasa)
print(relative_maui)



preci = []
for line in precipiation:
    sandiego = line['station']
    if sandiego == 'GHCND:US1CASD0032':
         preci.append(line)
    else: line = ''
sumao = 0
for lines in preci:
    value = lines['value'] 
    if 'value' in lines:
        sumao = sumao + value
    else: sumao = 0

sandiego_list = [0,0,0,0,0,0,0,0,0,0,0,0]
number = 0
months = 0
for line in preci:
    date = str(line['date'])
    sep_date = date.split(sep='-')
    month = int(sep_date[1])
    value = line['value']
    sandiego_list[month-1]= (sandiego_list[month-1] + value)

count= -1
relative_sandiego = []
for divided in sandiego_list:
    count = count +1
    relative_sandiego.append(sandiego_list[count]/sumao)

relative_monthly_precipitation = {'Cincinnati':relative_cincinnati,
                                  'Seattle':relative_seattle,
                                  'Maui': relative_maui,
                                  'San Diego': relative_sandiego}

print(relative_monthly_precipitation)
with open('ucaccmet2j_python/results.json','w',encoding='utf-8')as file:
    json.dump(relative_monthly_precipitation,file,indent=4)