import time
localtime = time.asctime( time.localtime(time.time()) )
execTime = localtime
file = open("readme.txt", 'w')
file.write("Kept code alive at : ")
file.write(str(execTime))
file.close()
# opens and writes text to the readme.txt
#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