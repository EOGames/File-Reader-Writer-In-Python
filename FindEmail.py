emailArray = [
    'xyz@gmail.com',
    'noob@gmail.com',
    'free@gmail.com',
    'crazyShitter@gmail.com',
    'totallyrubbish@gmail.com'
]
with open('emailList','w') as file:
    for em in emailArray:
        file.write(em +'\n')

with open ('emailList','r') as file:
    list = file.readlines() 
   # print(list)
    for l in list:
        print(l.rstrip())
        if 'crazy' in l:
            print("DANG it have Crazy "+l)
            break


