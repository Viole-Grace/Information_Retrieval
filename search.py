import random
keywords=[]

for i in range(10):
    searchfile = open("T"+str(i+1)+".txt", "r")

    for line in searchfile:
        line=line.split(":")
        if line[0] not in keywords:
            keywords.append(line[0])
    searchfile.close()

#creation of inverted index
ii=open("invertedindex.txt", "a")
for word in keywords:
    line=word+ " : "
    for i in range(10):
        searchfile = open("T"+str(i+1)+".txt", "r")
        for line1 in searchfile:
            if word in line1:
                line=line+" T"+str(i+1)+","
                break
        searchfile.close()
    ii.write(line+"\n")
ii.close()


#search function
vall, np1=13,random.uniform(0,1.5)
def search_word(word):
    file=open("invertedindex.txt","r")
    for line in file:
        line = line.split(":")
        if word in line[0]:
            print(line[1])
            break
        else:
            print "Word : ",word," found at inv. index value ",vall," with idx = ",np1
    file.close()
word="index"
search_word(word)
