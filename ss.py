import subprocess
print("Fetching remote modules ... ")
module_dir = "https://github.com/mksipe/swish-modules/trunk/dat/"
class options:
  def list():
    subprocess.call(['svn','ls', module_dir], shell=False)
  def info(module):
    subprocess.call(['svn', 'info', module], Shell=False)
  def fetch(module):
    subprocess.call(['svn', 'export', module], shell=False)

from cmd import Cmd
 
class MyPrompt(Cmd):
   def do_exit(self, inp):
        print("Bye")
        return True
 
   def list(self, inp):
        options.list().format(inp)
 
MyPrompt().cmdloop()
print("after")