#!/usr/bin/env python3
import glob, sys, configparser, subprocess
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
            end
          end
      except:
        print("There was an error processing "+Name+".")
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
  def load_lang_support():
    load_data()
    dir = "./config/languages/r33/run.py"
    print("---(Languages)---File Support Check---")
    support = [
      "Python_3",
      "Shell",
    ]
    for i in f:
      run = parser.get('support', 'type')
      get = parser.get('execution','scriptlocation' )
      if i in support:
        if i == run:
          print("Accepted filetype; Adding to config ... "+run)
      else:
        print("Rejected filetype; Rolling over ... "+run)

        
load_data.load_files()
load_data.load_data()
load_data.load_lang_support()


