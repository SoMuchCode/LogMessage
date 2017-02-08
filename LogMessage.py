#!/usr/bin/env python
#
# LogMessage class
#  For writing (appending) to a log file
#  version 0.1
#
# Python 3.6
# CLM 20170208
#
# To initialize LogMessage
# message = LogMessage('log.txt')
#
# To read the log
# message.read()
#
# To write to the log
# message.write('whatever you want to log.')
#


class LogMessage:
    def __init__(self, fileName):
        self.fn = fileName
    def read(self):
        file = open(self.fn,'r')
        for linE in file:
            print(linE, end = '')
        file.close()
    def write(self, texT):
        try:
            self.appendMe = texT
            file = open(self.fn,'a')
            file.write('\n')
            file.write(self.appendMe)
            file.close()
        except IOError as errorCaught:
            try:
                self.appendMe = texT
                file = open(self.fn,'w')
                file.write(self.appendMe)
                file.close()
            except Exception as errorCaught:
                print('Error: ' , errorCaught)
        except Exception as errorCaught:
            print('Error: ' , errorCaught)

# Initialize LogMessage class
message = LogMessage('log.txt')


## Example code to show how it works

# Add time-stamps to the logs
try:
    import datetime
except:
    print('Error: Can not load module: datetime')

def timeStamped(fmt='%Y%m%d-%H:%M:%S'):
    return datetime.datetime.now().strftime(fmt)

# Time to log something
message.write(timeStamped()+' '+'Log Message To Write')
message.write(timeStamped()+' '+'Another Log Message To Write')
message.write(timeStamped()+' '+'And another Log Message To Write')

# Read the log
var = message.read()
print(var)
