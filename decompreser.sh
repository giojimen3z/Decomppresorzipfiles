#!/bin/bash

# Nombre del archivo zip protegido con contraseña
zip_file="/Users/jaijimenez/Desktop/lab1/Lab 1/Extractinfo/flag_999.zip"

# Contraseña del archivo zip
password="9"

# Ruta de destino para los archivos extraídos
destination="/Users/jaijimenez/Desktop/lab1/Lab 1/Extractinfo/"

# Verificar si el archivo zip existe
if [ ! -f "$zip_file" ]; then
    echo "Error: El archivo zip $zip_file no existe."
    exit 1
fi

# Crear el directorio de destino si no existe
if [ ! -d "$destination" ]; then
    mkdir -p "$destination"
fi

# Descomprimir el archivo zip con contraseña
unzip -P "$password" "$zip_file" -d "$destination"

# Verificar si se extrajeron correctamente los archivos
if [ $? -eq 0 ]; then
    echo "Archivo descomprimido exitosamente."
else
    echo "Error: Contraseña incorrecta o archivo dañado."
    exit 1
fi
