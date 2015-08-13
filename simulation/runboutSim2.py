#!/usr/bin/env python

from boututils import shell, launch, getmpirun
import sys, os, ConfigParser, shutil, fileinput
from datetime import *
from guifunctions import *


currentDir = os.getcwd()
config = currentDir + '/config/config.ini'

parser = ConfigParser.ConfigParser()
parser.read(config)
exe = parser.get('exe', 'path')
archive = parser.get('archive', 'path')
MPIRUN = getmpirun()
nargs = len(sys.argv)
runid = sys.argv[1] # First argument is the Archive ID to load
restart = sys.argv[2]

print runid

if nargs < 3:
    # prints help if arguements aren't given
    print("Format is: ")
    print("  %s <run id> [directory]")
    print("     directory - optional, default is 'tmp'")
    sys.exit(1)

# Unless an arguement is given a temporary folder is created to run in
if nargs > 3:
    directory = sys.argv[3]
else:
    directory = 'tmp'


# Confirms location of BOUT++ archive
try:
    archive = os.environ["BOUTARCHIVE"]
except KeyError:
    # No environment variable. Use default
    archive = '/hwdisks/home/jh1479/BOUT-dev/archive/'

# Checks for a valid archive ID
def rundirectory(runid):   
    if os.path.exists(runid):
        print 'Valid runid', runid
    else:
        print 'Invalid runid', runid
        sys.exit(0)


# Makes a new directory called "tmp"
shell("mkdir " + directory) 
sourcedirectory = rundirectory(runid)



# Inport inputs into the temporary directory ???
inputfiles = os.listdir(runid)
for runfiles in inputfiles:
    filepath = os.path.join(runid, runfiles)
    if os.path.isfile(filepath):
        shutil.copy(filepath, directory)
        
######################################################################
#ADD ANY CHANGES TO HEADINGS THAT NEED TO BE MADE HERE IF THEY COME UP
######################################################################
changeHeading(directory + '/BOUT.inp', '[timing]', '')
changeHeading(directory + '/BOUT.inp', '[TWOfluid]', '[2fluid]')
######################################################################   

cmd = exe + ' -d ' + directory + '/'
#print("Command = '%s'" % cmd)
if restart == 'y':
    launch(cmd + ' restart', nproc = 5, nice = 10)
else:
    launch(cmd, nproc = 5, nice = 10, pipe=False)


# Save files from tmp into the loaded archive file and allows for addition of notes

inputfiles = os.listdir(directory)
for runfiles in inputfiles:
    filepath = os.path.join(directory, runfiles)
    if os.path.isfile(filepath):
        shutil.copy(filepath, runid)

shutil.rmtree('tmp')
sys.exit(0)