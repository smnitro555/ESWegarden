# ESW Egarden - An Effort for Hydroponics to be Automated with a Raspberry-Pi

import ConfigParser
import RPi.GPIO as GPIO

Config = ConfigParser.ConfigParser()
Config.read('config.ini')
systems = []

def ConfigSectionMap(section):
    dict1 = {}
    options = Config.options(section)
    for option in options:
        try:
            dict1[option] = Config.get(section, option)
            if dict1[option] == -1:
                DebugPrint("skip: %s" % option)
        except:
            print("exception on %s!" % option)
            dict1[option] = None
    return dict1

numSystems = len(Config.sections())

for i in range(numSystems):
    print "Looking at System %d" % (i + 1)
    sectionString = 'System' + str(i + 1);
    try:
        type = Config.get(sectionString,'Type')
        print "System Type is: %s" % (type)  # TO Fix
        status = Config.get(sectionString, 'Status')
        print "System Status is: %d" % (status) #TO Fix
        pumpPin = Config.get(sectionString, 'PumpPin')
        print "System Pump Pin is: %d" % (int(pumpPin))  # TO Fix
        waterLevelPin = Config.get(sectionString, 'WaterLevelPin')
        print "System Water Level Detection Pin is: %d" % (int(waterLevelPin))  # TO Fix
    except:
        print 'Bad Naming of Sections in Config File, Continuing Haphazardly'

    # Starting the systems based of System Type
    if (type == 'NFT'):
        x = NFT(pumpPin,waterLevelPin)
        systems.append(x)
    elif (type == 'Drip'):
        # Drip System has unique parameters for it, so parsing for the more information
        try:
            onTime = Config.get(sectionString, 'onTime')
            print "System will be On This Much Time per Hour (minutes): %d" % (int(onTime))  # TO Fix
        except:
            print 'Bad Naming of Drip System Timer in Config File, Continuing Haphazardly'
    elif type == 'EbbNFlow':

    else:
        print 'System type did not Match known types. Check Spelling of System Type'
