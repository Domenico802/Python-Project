import re
import os
from datetime import date, datetime, timedelta,time
from pdfminer.high_level import extract_pages, extract_text

#zur Erweiterung: Zugriff auf Drucker um als Beispiel eine Rechnung direkt zu drucken (hier nur Windows)
#import win32print 

#--------------------------------------------------------------------------------
#Liste an Verfügbaren Druckern zeigen 
#System - Windows
#--------------------------------------------------------------------------------
#printers =win32print.EnumPrinters(win32print.PRINTER_ENUM_LOCAL,None,1) 
#print(printers)

#debugging Drucker
#for printer in printers:
#    print(printer[2]) #Nur Namen der Drucker darstellen
#--------------------------------------------------------------------------------

#definierten Pfad angeben welche Datei umbenannt werden soll
filepath = "G:/Documents/Python-Project/read_pdf_test"
os.chdir(filepath) #python braucht / anstatt \ im Pfad

#Datei welche gelesen und danach umbenannt werden soll
file = "Daten_2.pdf"

#--------------------------------------------------------------------------------
#Vorbereitung für automatisches Drucken der Datei um händische Ablage zu machen
#status - nicht getestet da kein Drucker angeschlossen 
#System - Windows
#--------------------------------------------------------------------------------
#file_path = "G:/Documents/Python-Project/read_pdf_test/IMG_20210313_203343.jpg"

#printer_name = "Microsoft Print to PDF" #hier Name des Druckers eintragen 
#file_handle = open(file_path, "rb")
#printer_handle = win32print.OpenPrinter(printer_name)
#Job_Info = win32print.StartDocPrinter(printer_handle,1,(file_path,None,"RAW"))
#win32print.StartPagePrinter(printer_handle)
#win32print.WritePrinter(printer_handle, file_handle.read())
#win32print.EndPagePrinter(printer_handle)
#win32print.EndDocPrinter(printer_handle)
#win32print.ClosePrinter(printer_handle)
#file_handle.close()
#--------------------------------------------------------------------------------


#--------------------------------------------------------------------------------
#Vorbereitung für automatisches Drucken der Datei um händische Ablage zu machen
#status - nicht getestet da kein Drucker angeschlossen und kein Mac
#System - Mac
#Lösung aus https://stackoverflow.com/questions/53777939/how-to-send-a-picture-to-printer-with-python-on-macos
#--------------------------------------------------------------------------------
#os.system("lpr -P YOUR_PRINTER file_name.jpg")
#--------------------------------------------------------------------------------

#pdf als text lesen
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