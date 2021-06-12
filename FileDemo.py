# open to write
texFile = open("xmltxt.txt","w")
texFile.write("First content!")
texFile.close()
# open to append
texFile = open("xmltxt.txt","a")
texFile.write("Now the file has more content!")
texFile.close()
# open to read
texFile = open("xmltxt.txt","r")
print(texFile.read())


# create file
import os
if not (os.path.exists("demofile.txt")):
    newFile = open("demofile.txt","x")
    print("emofile.txt created")
    newFile.close()
    
    # open to write
    newFile = open("demofile.txt","w")
    newFile.write("Now the new file has content!")
    newFile.close()

    # open to append
    newFile = open("demofile.txt","a")
    newFile.write("The new file has more content!")
    newFile.close()

    # open to append
    newFile = open("demofile.txt","r")
    print(newFile.read())

else:
  # open to append
  newFile = open("demofile.txt","a")
  newFile.write("The new file has more content!")
  newFile.close()

  # open to append
  newFile = open("demofile.txt","r")
  print(newFile.read())