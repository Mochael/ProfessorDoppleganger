#import userdata
import data
#import test
import requests
#import urllib.request
import Image_properties
import os

#userdata = data.professors[13]




def dif(a, b):
    return abs(a-b)

def main(url):
    userdata = Image_properties.get_data(url)
    minnum = 10.0
    minindex = 0
    for index in range(len(data.professors)):
        score = testing(index, userdata)
        if(score < minnum):
            minindex = index
            minnum = score
    name = os.listdir("ProfImages")[minindex]
    print(name)
    
    return name
    


def testing(index, userdata):
    score = []
    sum = 0.0

    for i in range(len(data.professors[index][0]["faceAttributes"]["hair"]["hairColor"])):
        score.append(dif(data.professors[index][0]["faceAttributes"]["hair"]["hairColor"][i]["confidence"],userdata[0]["faceAttributes"]["hair"]["hairColor"][i]["confidence"]))


    score.append(dif(data.professors[index][0]["faceAttributes"]["smile"], userdata[0]["faceAttributes"]["smile"]))

    if(data.professors[index][0]["faceAttributes"]["gender"] == userdata[0]["faceAttributes"]["gender"]):
        score.append(0.0)

    else:
        score.append(10.0)

    for i in {"beard", "moustache", "sideburns"}:
        score.append(dif(data.professors[index][0]["faceAttributes"]["facialHair"][i], userdata[0]["faceAttributes"]["facialHair"][i]))



    for i in range(len(score)):
        sum += score[i]/len(score)

    return sum

main('https://scontent-iad3-1.xx.fbcdn.net/v/t31.0-8/13323364_1556287674668112_7385276195470315606_o.jpg?oh=1fdebefb6977aac54190f6d68ccfb782&oe=5B1A81AC')
