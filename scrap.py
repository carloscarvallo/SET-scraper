import requests
import csv
import json

set_url = 'https://servicios.set.gov.py/eset-publico/ciudadano/recuperar'

# loop through all URLs
id_range = 10000000
id = 1

with open ('datos.csv','w') as csvfile:
   writer=csv.writer(csvfile)
   for id in range(id_range):
       payload = {"cedula": id}
       result = requests.get(set_url, params=payload)
       res_json = result.json()
       id+=1

       if(res_json["presente"] == False):
            print("No existe el nro de cedula")
       else:
           line = ""
           for key,value in res_json['resultado'].items():
                line += [key, value]
           print(line)
           writer.writerow(line)
       