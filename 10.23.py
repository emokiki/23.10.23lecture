""" import os

fp = "temp.txt"

file = open(fp,"w")

if os.path.exists(fp) :
    print("ok")
else : 
    print("error")

file.close() """


""" #
import os
fp="temp.txt"

if os.path.exists(fp):
    f=open(fp, "r")
    for line in f :
        print(line)
        
else : 
    f=open(fp,"w")
    for i in range(100) :
        f.write(str(i)+ "\n")
    
     """
""" import os

fp = "new.txt"

f= open(fp, "w")
f.close()

os.remove(fp)
print("complete")

 """

""" import os
def dir_print(p) :
    files = os.listdir(p)
    for f in files :
        print(f)

fp = "new.txt"

f=open(fp,"w")
f.close()

dir_print("./")
print("-------------------\n\n")
dir_print("./") """

""" 
import os
fp = "new.txt"

f=open(fp,"w")
f.close()

os.rename(fp,"new1.txt")
print("complete")

 """
""" 
import os
fp="new.txt"
tp = "new1.txt"


f=open(fp,"w")
f.close()

if os.path.exists(tp) :
    print("exist, smae name file")
    os.remove(tp)
else : 
    os.rename(fp,"new1.txt")
    print("complete")
     """
""" 
import os

def dir_print(p) :
    files = os.listdir(p)
    for f in files :
        print(f)

fp="new.txt"
tp = "new1.txt"

f=open(fp,"w")
f.close()

dir_print("./")
print("-------------------\n\n")

if os.path.exists(tp) :
    print("exist, smae name file")
    os.remove(tp)
else : 
    os.rename(fp,"new1.txt")
    print("complete")
     """


#with
#f = open("temp.txt", "r")
with open("temp.txt", "r") as f :
    print(f.read())
    
    #for i in range(110) : 
    #   res = f.readline()
    #print(res)