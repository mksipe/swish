import subprocess, configparser
parser = configparser.ConfigParser()
module_dir = "https://github.com/mksipe/swish-modules/trunk/dat/"
class options:
  def list():
    subprocess.call(['svn','ls', module_dir], shell=False)
  def info(module):
    subprocess.call(['svn', 'cat', 'https://github.com/mksipe/swish-modules/trunk/dat/'+module], shell=False)
  def fetch(module):
    subprocess.call(['svn', 'export', 'https://github.com/mksipe/swish-modules/trunk/dat/'+module], shell=False)
  def subfetch(module):
      subprocess.call(['svn', 'export', module], shell=False)

from cmd import Cmd
 
class MyPrompt(Cmd):
  prompt = 'SS> '
  intro = "swish store - Type ? to list commands"

  def do_exit(self, inp):
        print("Bye")
        return True
  def do_list(self, inp):
        options.list()
  def do_info(self, inp):
        txt = input("SS[Search]>")
        options.info(txt)
  def do_install(self, inp):
        txt = input("SS[Install]>")
        subprocess.call(["cd config/modules/"], shell=False)
        options.fetch(txt)
        parser.read(txt)
        parser.sections()
        asc = parser.get("download", 'checksum')
        run = parser.get("download",'runfile')
        subprocess.call(["cd run/"], shell=False)
        options.subfetch(run)
        subprocess.call(["cd ../../tmp"], shell=False)
        options.subfetch(asc)
        subprocess.call(["cat", txt.strip(".dat")+".asc", ">>", "../config/hashes.asc" ], shell=False)

MyPrompt().cmdloop()
print("after")