# -*- coding: 850 -*-
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests, re
from bs4 import BeautifulSoup

query = raw_input("Ingrese query SQLI: ")


#url
url = 'http://www.google.com/search'
 
#Parametros de busqueda
payload = { 'q' : str (query), 'start' : '0' }
 
#Configuracion de  User-Agent
my_headers = { 'User-agent' : 'Mozilla/11.0' }
 
#Obteniendo la respuesta de los datos ingresados
r = requests.get( url, params = payload, headers = my_headers )
 
#Create a Beautiful soup Object of the response r parsed as html
soup = BeautifulSoup( r.text, 'html.parser' )
 
#Getting all h3 tags with class 'r'
h3tags = soup.find_all( 'h3', class_='r' )
 
#Finding URL inside each h3 tag using regex.
#If found : Print, else : Ignore the exception
for h3 in h3tags:
    try:
        print( re.search('url\?q=(.+?)\&sa', h3.a['href']).group(1) )
    except:
        continue
 
 
#End
