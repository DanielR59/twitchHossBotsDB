from oauth2client.service_account import ServiceAccountCredentials
import gspread
import re
scope = ["https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive.file",
        "https://www.googleapis.com/auth/drive"
]
creds = ServiceAccountCredentials.from_json_keyfile_name("GoogleDriveConfig.json",scope)
client = gspread.authorize(creds)

DriveSheet = client.open("BotsHoss Twitch").sheet1.get_all_records(head=1) #Primer Celda es encabezado

#Tomamos los datos unicamente del bot Hoss (actual atacante en Twitch)

bots_names = set() #Evitamos duplicados
for element in DriveSheet:
    aux = list(element.values())
    filtro1 = re.search("hoss(.*)",aux[0])
    filtro2 = re.search("h[0].*",aux[0])
    if filtro1 or filtro2:
       bots_names.add(aux[0])

bots_names = list(bots_names)
bots_names.append("BANLISTEND")

#Escribimos el archivo final para el script
with open("banlist.txt", 'w') as output:
    for row in bots_names:
        output.write(str(row) + '\n')

