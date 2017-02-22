import re

class Bucket:
    def __init__(self, count, down):
        self.count = count
        self.words = []
        self.up = None
        self.down = down

    def remove(self, word):
        if word in self.words:
            self.words.remove(word)

    def make_up(self, word):
        self.up = Bucket(self.count + 1, self)
        self.up.words.append(word)
        return self.up

def word_counter(text, retCount):
    textList = re.split("[^a-zA-Z_0-9']", text.lower()) # use regexes to parse out words
    textList = [word for word in textList if word] # remove all captured null strings
    bucketMap = {}
    bottomBucket = Bucket(0, None)
    retList = []

    if not textList:
        return ["" for i in range(retCount)] # if no words, return list of empty strings of size retCount
    for word in textList:
        bucket = bucketMap.get(word, bottomBucket)
        bucket.remove(word)
        if bucket.up:
            bucket.up.words.append(word)
            bucketMap[word] = bucket.up
        else:
            newBucket = bucket.make_up(word)
            bucketMap[word] = newBucket
            topBucket = newBucket
    while retCount:
        if len(topBucket.words) < retCount:
            retList += topBucket.words
            retCount -= len(topBucket.words)
            if topBucket.down:
                topBucket = topBucket.down
            else:
                retList += ["" for i in range(retCount)]
                retCount = 0
        else:
            retList += [topBucket.words[i] for i in range(retCount)]
            retCount = 0
    return retList
