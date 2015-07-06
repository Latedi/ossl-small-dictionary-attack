#!/usr/bin/env python
import os
def getsortkey(tuple):
        return tuple[1]
 
chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789 !\"#$%&'-./:;<>=?@[]\\^_`{}|~\n\t"
res = []
for file in os.listdir("./out"):
        data = os.popen("cat ./out/" + file).read()
        good = 0
        bad = 0
        for c in data:
                if c in chars:
                        good += 1
                else:
                        bad += 1
        res.append((file, (good, bad)))
 
res.sort(key=getsortkey)
for r in res:
        print r[0] + "\t" + str(r[1][0]) + "\t" + str(r[1][1])
print str(len(res))
