Τσιλιβάκος Γιώργος π20193

import request
from datetime import datetime
hmera = datetime.now().day
mhnas = datetime.now().month
if mhnas==1 or mhnas==3 or mhnas==5 or mhnas==7 or mhnas==8 or mhnas==10 or mhnas==12:
   meresmhna=31
if mhnas==2 or mhnas==4 or mhnas==6 or mhnas==9 or mhnas==11:
   meresmhna=30
if mhnas == 2:   
   meresmhna=28                 

meraarx=1
while hmera >= meraarx   and meresmhna >= meraarx:
      x= request.get('https://api.opap.gr/draws/v3.0/1100/draw-date/2021-{M}-{D}/2021-{M}-{D}/draw-id'.format(M=mhnas,D=meraarx))
      print (x)
      
      
      
