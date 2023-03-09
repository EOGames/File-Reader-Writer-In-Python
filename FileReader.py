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

with open ("newfile.txt",'a') as file: #it will create new file if its not their and will apend stuff u need means will not delete stuff #like w (write) do
    file.write("Its Added By Code")
    file.write("\n Its Secound line")
    file.write ("\n \t New Line And Tabbed")


with open ('newfile.txt','r') as file:
    print(file.read())


