from app.extract_file import unzip_file

basePath = "/Users/jaijimenez/Desktop/lab1/Lab 1/Extractinfo/"
zipVar = ""
pathAux = ""
destination = ""
flag = ""
passwordPosition = 0
password = ""
passwords = ["9", "08", "376", "8372", "68589", "481272", "0044984", "44063984", "543233354", "9116259440",
             "03189880826"]

for i in range(9, -1, -1):
    pathAux = basePath
    destination = basePath
    password = passwords[passwordPosition]
    zipVar = "flag_99" + str(i) + ".zip"
    if i == 9:
        pathAux += zipVar
        destination = basePath

    if i != 9:
        flag += "flag/"
        pathAux += flag + zipVar
        destination += flag
    print(pathAux)
    print(destination)
    unzip_file(pathAux, password, destination)
    passwordPosition += 1
