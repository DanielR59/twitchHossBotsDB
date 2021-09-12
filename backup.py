import os
import sys
import shutil
def read_to_list(file):

    with open(file,'r') as f:
        file_list = f.read()

    file_list = file_list.split(sep='\n')
    file_list = list(filter(None,file_list))
    file_list.remove("BANLISTEND")
    return file_list

banlist = read_to_list("banlist.txt")
backup = read_to_list("banlist.backup.txt")

#checamos si es el mismo archivo
if (len(banlist) == len(backup)) and (banlist==backup):
    print("Los archivos son iguales :D")
    sys.exit()

#checamos si el numero de elementos disminuyó
if len(banlist) < len(backup):
    print("Copiando el backup al archivo original")
    shutil.copyfile("./banlist.backup.txt","./banlist.txt")

if len(banlist) > len(backup):
    print("Actualizando el backup")
    for element in banlist:
        if element not in backup:
            backup.append(element)

    backup.append("BANLISTEND")
    with open("banlist.backup.txt", 'w') as output:
        for row in backup:
            output.write(str(row) + '\n')
    print("Backup actualizado :D")