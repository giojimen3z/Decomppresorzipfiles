import zipfile


def unzip_file(path, password, destination):
    # Nombre del archivo zip protegido con contraseña
    zip_file = path

    # Contraseña del archivo zip
    password = password

    # Ruta de destino para los archivos extraídos
    destination = destination

    # Descomprimir el archivo zip con contraseña
    try:
        with zipfile.ZipFile(zip_file) as zip_ref:
            zip_ref.extractall(destination, pwd=password.encode('utf-8'))
        print('Archivo descomprimido exitosamente.')
    except zipfile.BadZipFile:
        print('Error: Archivo zip dañado.')
    except RuntimeError:
        print('Error: Contraseña incorrecta.')