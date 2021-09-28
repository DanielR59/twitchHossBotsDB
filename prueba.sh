#!/bin/bash

cadena="Los archivos son iguales :D"
output=$(python3 backup.py $1 2>&1)
echo "$(date) : $output" >> status.log
if [ "$output" == "$cadena" ]
then
  
    return
else
    echo "Actualizando los datos a Github :3"
    git add $1
    git commit -m "Actualizacion base de datos"
    git push origin main

fi
