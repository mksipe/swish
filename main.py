#!/usr/bin/env python3
import glob, configparser, subprocess
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
      if a == m:
        global module
        module = module + 1
        print("Adding module ... ")
    print("Cores   : ", core)
    print("Modules : ", module)
  def initialize_files():
    load_data.load_data()
    interpreter.countextensives()
  def run_files():
    for i in f:
      config.read(i)
      FILE = config.get('execution', 'scriptlocation')
      ENV  = config.get('execution', 'shell')
      subprocess.call([ENV, FILE], shell=False )

interpreter.initialize_files()

interpreter.run_files()
