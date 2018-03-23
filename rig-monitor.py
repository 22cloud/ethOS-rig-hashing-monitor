#!/usr/bin/python

# Author: Pepe Ramirez
# Link: https://github.com/peperamirez89/ethOS-rig-hashing-monitor
# Date: 02/15/2018

import os
import sys
import time
import datetime
import commands

gLogFile = "/home/ethos/Rig-monitor/rig-monitor-log.log" #Log path

def GetHashes():
    hashesStats = commands.getstatusoutput(
        "\grep -m 1 miner_hashes /var/run/ethos/stats.file")
    if (hashesStats[0] != 0):
        return 0
    return hashesStats[1][13:]


def DumpActivity(dumpStr):
    try:
        pLogFile = open(gLogFile, "a")
        pLogFile.write("%s\n" % (dumpStr))
        pLogFile.close()
    except:
        print "File write error in - " + gLogFile


##########
#  Main  #
##########

while 1:
    time.sleep(420) #IfYouKnowWhatIMean
    hashes = GetHashes()
    restart = None
    gpuHashes = hashes.split(' ')
    for gpuHash in gpuHashes:
        if (gpuHash == "00.00" or gpuHash == "0"):
            restart = True
    if restart:
        DumpActivity(str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))+" - [Rig rebooted] - [Hashes] : {"+str(gpuHashes)+"}")
        os.system("sudo reboot")