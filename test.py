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

bots_names = []
for element in DriveSheet:
    aux = list(element.values())
    filtro = re.search("hoss(.*)",aux[0])
    if filtro:
       bots_names.append(aux[0])

bots_names = set(bots_names) #Eliminamos duplicados
#Escribimos el archivo final para el script
with open("banlist.txt", 'w') as output:
    for row in bots_names:
        output.write(str(row) + '\n')

