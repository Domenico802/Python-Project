import re
import os
from datetime import date, datetime, timedelta,time
from pdfminer.high_level import extract_pages, extract_text

#definierten Pfad angeben welche Datei umbenannt werden soll
os.chdir("G:/Documents/Python-Project/read_pdf_test")

#Datei welche gelesen und danach umbenannt werden soll
file = "Daten_2.pdf"
text = extract_text(file)

#debugging
#print(text) 

pattern = re.compile("\d{2}.\d{2}.\d{4}") 
matches = pattern.findall(text) # suche nach pattern ZahlZahl.ZahlZahl.ZahlZahlZahlZahl in file text 

#debugging
#print("matches:")
#print(matches)
#debugging
#print("Länge der Liste:")
#print(len(matches))

i = 0

#check ob es mehrere Datumsangaben gibt
if(len(matches) > 1):
    min_time_diff = None
    for temp_date in matches: #alle Datumsangaben durchgehen
        date_obj = datetime.strptime(temp_date,"%d.%m.%Y") #konvertieren zu datetime objekt damit man differenz bilden kann
        time_diff = datetime.today() - date_obj
        #debugging
        #print(time_diff.days)
        if min_time_diff is None or time_diff < min_time_diff: #raussuchen des index in Liste matches mit counter um Datum aus kürzest zurückligender Vergangenheit zu speichern
            min_time_diff = time_diff
            i=i+1
    #debugging        
    #print("Niedrigster Abstand:", min_time_diff.days)  
    #print("i", i)  
    matches = str(matches[i-1]) #da counter mit 0 initialisiert wird muss hier ein index nach vorne gesprungen werden in der matches Liste. Konvertierung zu string um replace anwenden zu können
    stripped = matches.replace(".","")
else:
    matches = "".join(matches)
    stripped = matches.replace(".","")



#debugging
#print("stripped")
#print(stripped)
os.rename(file, stripped + "_" + file)