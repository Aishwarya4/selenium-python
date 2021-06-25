# file = open("E:\\file_handling.txt",'w')
# file.write("Aishwarya\n")
# file.write("Parab")
# file.close()
# file = open("E:\\file_handling.txt",'r')
# print(file.read())#read all content of the file at once
# print(file.read(3)) #read given number of charcters
# print(file.readlines())#read all content of the file at once in return in array
# print(file.readline())#read first line
# file = open("E:\\file_handling.txt",'a')
# print(file.write("\n Msc Part I"))
# file.close()
file = open("E:\\file_handling.txt", 'r')
for line in file:
    print(line)