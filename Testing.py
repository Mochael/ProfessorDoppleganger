#import userdata
import data
import os

userdata = data.professors[4]

score = []


def dif(a, b):
	return abs(a-b)

def main():
	maxnum = 0.0
	maxindex = 0
	for index in len(data.professors):
		num = testing(index)
		if(num > maxnum):
			maxindex = index
			maxnum = num

	return maxindex


def testing(index):
	sum = 0.0

	for i in data.professors[index][0]["faceAttributes"]["hair"]["hairColor"]:
		score.append(dif(i["confidence"], userdata[0]["faceAttributes"]["hair"]["hairColor"][i]["confidence"]))

	score.append(dif(data.professors[index][0]["faceAttributes"]["smile"], userdata[0]["faceAttributes"]["smile"]))

	if(data.professors[index][0]["faceAttributes"]["gender"] == userdata[0]["faceAttributes"]["gender"]):
		score.append(1)

	else:
		score.append(0)

	for i, val in data.professors[index][0]["faceAttributes"]["facialHair"]:
		score.append(dif(val, userdata[0]["faceAttributes"]["facialHair"][i]))

	for i in score:
		sum += score[i]/len(score)

	return sum



