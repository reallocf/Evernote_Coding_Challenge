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

    def listify(self, retCount):
        retList = []
        while retCount:
            if len(self.words) < retCount:
                retList += self.words
                retCount -= len(self.words)
                if self.down:
                    self = self.down
                else:
                    retList += ["" for i in range(retCount)]
                    retCount = 0
            else:
                retList += [self.words[i] for i in range(retCount)]
                retCount = 0
        return retList

def word_counter(text, retCount):
    textList = re.split("[^a-zA-Z_0-9']", text.lower()) # use regexes to parse out words
    textList = [word for word in textList if word] # remove all captured null strings
    bucketMap = {}
    bottomBucket = Bucket(0, None)

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
    return topBucket.listify(retCount)

# Justification for O(n) time:
#
# text.lower() will be O(n) - where n is the number of characters in the string -
# because it performs a constant time operation (an if statement) n times
#
# re.split() will be O(n) - where n is the number of characters in the string -
# because it performs a constant time operation (a couple if statements) n times
#
# removing the captured null strings will be O(n) - where n is the number of words
# in the string - because it performs a constant time operation (an if statement)
# n times
#
# returning an empty list will be O(n) - where n is retCount - because it performs
# a constant time operation (creating an empty string) n times
#
# looping through textList and filling the buckets will be O(n) - where n is the
# number of words in the string - because it performs a constant time operation
# (getting a value from a hashmap, a couple of if statements, removing/adding to a
# list, creating a bucket, and/or adding a new element to a hashmap - note that
# some of these are amortized) n times
#
# listify will be a O(n) operation - where n is retCount - because it performs a
# constant time operation (a couple if statements and adding elements to a list)
# n times
#
# The whole function will perform independent O(n) operations a constant number of
# times, so the overall time complexity is O(n)
#
# Note that the number of words and the retCount can both approach the total number
# of characters, so they must also be included in our analysis of time complexity
#
