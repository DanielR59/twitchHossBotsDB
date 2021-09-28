import sys
import shutil
import sys
def read_to_list(file : str) -> list:

    with open(file,'r') as f:
        file_list = f.read()

    file_list = file_list.split(sep='\n')
    file_list = list(filter(None,file_list))
    file_list.remove("BANLISTEND")
    return file_list


def backup_updater(original_file_list : list, backup_file_list : list, filename : str):
    #checamos si es el mismo archivo
    if (len(original_file_list) == len(backup_file_list)) and (original_file_list.sort()==backup_file_list.sort()):
        print("Los archivos son iguales :D")
        return 1

    #checamos si el numero de elementos disminuyó
    if len(original_file_list) < len(backup_file_list):
        print("Copiando el backup al archivo original")
        shutil.copyfile("./"+ filename+ ".backup","./"+filename)
    #Si el numero aumentó actualizamos el backup
    if len(original_file_list) > len(backup_file_list):
        print("Actualizando el backup")
        for element in original_file_list:
            if element not in backup_file_list:
                backup_file_list.append(element)

        backup_file_list.append("BANLISTEND")
        with open(filename+".backup", 'w') as output:
            for row in backup_file_list:
                output.write(str(row) + '\n')
        #print("Backup actualizado :D")

if __name__ == '__main__':
    try: 
        filename = sys.argv[1]
    except:
        print("Necesito el archivo perro")
        sys.exit(1)

    banlist = read_to_list(filename)
    backup = read_to_list(filename +".backup")
    backup_updater(banlist,backup,filename)
   
