import os

try:
    os.system('cd /devl/midi && git pull && cd -')

except:
    print "Unable to pull updates from Github."
