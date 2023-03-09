# with open('ReadFile.txt', 'r') as file:
#     print (file.read())
    

with open ('ReadFile.txt','r') as file:
    backupFile = file.read()
    print(backupFile + " its From Back Up File")

with open ('ReadFile.txt','w') as file:
    file.write( backupFile +'\n Yo Its Added By Code')

with open ('ReadFile.txt','r') as file:
    newInfo = file.read()
    print(newInfo + " New Edited File")
