#import userdata
import data
import os

userdata = data.professors[5]

score = []


def dif(a, b):
	return abs(a-b)

def main():
	minnum = 0.0
	minindex = 0
	for index in range(len(data.professors)):
		score = testing(index)
		if(score < minnum):
			minindex = index
			minnum = score
			print(score)
	print(minindex)
	return minindex


def testing(index):
	sum = 0.0

	for i in range(len(data.professors[index][0]["faceAttributes"]["hair"]["hairColor"])):
		score.append(dif(data.professors[index][0]["faceAttributes"]["hair"]["hairColor"][i]["confidence"],userdata[0]["faceAttributes"]["hair"]["hairColor"][i]["confidence"]))

	score.append(dif(data.professors[index][0]["faceAttributes"]["smile"], userdata[0]["faceAttributes"]["smile"]))

	if(data.professors[index][0]["faceAttributes"]["gender"] == userdata[0]["faceAttributes"]["gender"]):
		score.append(0.0)

	else:
		score.append(1.0)

	for i in {"beard", "moustache", "sideburns"}:
		score.append(dif(data.professors[index][0]["faceAttributes"]["facialHair"][i], userdata[0]["faceAttributes"]["facialHair"][i]))

	for i in range(len(score)):
		sum += score[i]/len(score)

	return sum

main()

