file = open('file.txt', 'w')
file.write("hi , I am Jatin Kishore M")
file.seek(0)
fileR = open('file.txt', 'r+')
for each in fileR:
    print(each)

fileR.close
