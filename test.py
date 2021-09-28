from oauth2client.service_account import ServiceAccountCredentials
import gspread
import re

def read_bots_from_excel(client, google_sheet_column : int, filtros : list = []):
    
    DriveSheet = client.open("BotsHoss Twitch").sheet1.col_values(google_sheet_column)
    DriveSheet.pop(0)
    bots_names = set(DriveSheet) #Evitamos duplicados
    if not filtros:
        bots_names = list(bots_names)
        bots_names.append("BANLISTEND")
        return bots_names

    final_list = []
    for element in bots_names:      
        for filtro in filtros:
            re_match = re.search(filtro,element)
            if re_match:
                final_list.append(element)
                break
    final_list.append("BANLISTEND")
    return final_list

def write_output(file : str , output_list : list):
    with open(file,'w') as output:
        for row in output_list:
            output.write(str(row) + '\n')

if __name__ == '__main__':

    scope = ["https://www.googleapis.com/auth/spreadsheets",
            "https://www.googleapis.com/auth/drive.file",
            "https://www.googleapis.com/auth/drive"
    ]
    creds = ServiceAccountCredentials.from_json_keyfile_name("GoogleDriveConfig.json",scope)
    client = gspread.authorize(creds)


    bots_names = read_bots_from_excel(client, 1, ['hoss(.*)','h[0].*'])
    bots_names2 = read_bots_from_excel(client, 2)
    write_output("banlist.txt",bots_names)
    write_output("banlist_otrosBots.txt",bots_names2)
