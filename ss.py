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