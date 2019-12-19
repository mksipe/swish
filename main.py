#!/usr/bin/env python3
import glob, configparser, subprocess, hashlib, sys, config.core.DSP as d
confdir = "./config/*/*.dat"
parser = configparser.ConfigParser()
config = configparser.RawConfigParser(allow_no_value=True)
f = glob.glob(confdir)
class load_data():
  def load_files():
    for i in f:
      parser.read(i)
      parser.sections()
      Type = parser.get('validation', 'type')
      Name = parser.get('validation', 'name')
      try:
        if Type == "core":
          print("Loaded "+Name)
        else:
          if Type == "module":
            print("Loaded "+Name)
          else:
            print("file not loaded "+Name+" Reason: "+Type)
      except:
        print("module loaded.")
        exit
  def load_sections():
      for i in f:
        parser.read(i)
#        s = parser.sections()
#        for i in s:
#          print(s)
  def load_data():
    load_data.load_sections()
    #PTH = parser.get('execution', 'scriptlocation')
    #SH  = parser.get('execution', 'shell')
    #TYP = parser.get('support', 'type')
    #ATH = parser.get('support', 'author')
    #print(PTH)
    #print(SH)
    #print(TYP)
    #print(ATH)


core = 0
module = 0
security = 0
permitted = []
hashed = []

class interpreter():
  print("---[Loading data]---")
  def countextensives():
    c = "core"
    m = "module"
    load_data.load_files()
    f = glob.glob(confdir)
    for i in f:
      config.read(i)
      a = config.get('validation', 'type')
      if a == c:
        global core
        core = core + 1
        print("Adding core ... ")
        permitted.append(i)
      if a == m:
        global module
        module = module + 1
        print("Adding module ... ")
        permitted.append(i)
    print("Cores   : ", core)
    print("Modules : ", module)
  def hashfiles():
    print("---[Hashing Files]---")
    zero = 1
    for i in permitted:
      config.read('./config/core/hashes.asc')
      HASH = config.get('security', i)
      file = i # Location of the file (can be set a different way)
      BLOCK_SIZE = 65536 # The size of each read from the file
      file_hash = hashlib.sha256() # Create the hash object, can use something other than `.sha256()` if you wish
      with open(file, 'rb') as f: # Open the file to read it's bytes
        fb = f.read(BLOCK_SIZE) # Read from the file. Take in the amount declared above
        while len(fb) > 0: # While there is still data being read from the file
          file_hash.update(fb) # Update the hash
          fb = f.read(BLOCK_SIZE) # Read the next block from the file
      #print (i, file_hash.hexdigest()) # Get the hexadecimal digest of the hash
      if HASH == file_hash.hexdigest():
          d.display.center(zero,30,"Succesfully Hashed: " + i)
          zero = zero + 1
          #print(zero)
          hashed.append(i)
      else:
        print(i, "Could not validate hash.")

  def run_files():
    for i in hashed:
      config.read(i)
      FILE = config.get('execution', 'scriptlocation')
      ENV  = config.get('execution', 'shell')
      subprocess.call([ENV, FILE], shell=False )
  def initialize_files():
    load_data.load_data()
    interpreter.countextensives()
    interpreter.hashfiles()

interpreter.initialize_files()

interpreter.run_files()
