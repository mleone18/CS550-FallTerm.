import sys
Firstname = ["stinky","lumpy","buttercup","gidget","crusty","greasy","fluffy","cheeseball","chim chim","poopsie","flunky","booger","pinky","zippy","goober","doofus","slimy","loopy","snotty","falafel","dorkey","squeezit","oprah","skipper","dinky",
"zsa zsa"]

Lastfirst = ["diaper","toilet","bubble","girdle","barf","lizard","waffle","cootie","monkey","potty","liver","banana","rhino","burger","hamster","toad","gizzard","pizza","gerbil","chicken","pickle","chuckle","tofu","gorilla","stinker"]

Lastlast = ["head", "mouth", "face", "nose", "tush", "breath", "pants", "shorts", "lips", "honker", "butt", "brain", "tushie", "chunks", "hiney", "biscuits", "toes", "buns", "fanny", "sniffer", "sprinkles", "kisser", "squirt", "humperdinck", "brains", "juice"]

name = input('name: ')
fullname = name.rstrip().lower().split(" ")

indexFirstname = ord(fullname[0][0])-97
indexLastfirst =  ord(fullname[1][0])-97
indexLastlast = ord(fullname[1][-1])-97


print(Firstname[indexFirstname] + Lastfirst[indexLastfirst] + Lastlast[indexLastlast])
