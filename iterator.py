import os

for filename in os.listdir("ProfImages"):
    name = filename.split(" ")
    url = "https://github.com/Mochael/ProfessorDoppleganger/blob/master/ProfImages/"+name[0]+"%20"+name[1]+"?raw=true"
    with open("names.txt", "a") as f:
        f.write(url+"\n")

