import optparse
import os
import subprocess
import shutil
import config


#get arguments / options
def getOpts() :
    parse = optparse.OptionParser()
    parse.add_option("-b","--branch", dest = "branch",help = "branch to be deployed")
    parse.add_option("-p","--path", dest = "path",help = "path in ur registry")
    (option , args) = parse.parse_args()
    return option

#git hub link (file to be cloned)
path = getOpts().path
gitReg = config.gitVar

deployFolder = config.deplFolder

# try:
#     subprocess.call(['pm2','kill'])

# except:
#     print("could not kill pm2 process")
#     exit(1)

try: 
    os.chdir(deployFolder)
    shutil.rmtree(deployFolder, ignore_errors=True)
    print('=========================================================================================================================')
    print("summary :")
    print(" deleted old code : success")
except: 
    print("no file to delete")
   
   
try:
    os.mkdir(deployFolder)
    os.chdir(deployFolder)
    subprocess.call(['git','clone',gitReg])
    os.chdir(deployFolder+"/"+path)
    print(" cloned latest code : success")
except:
    print("error in clonning")
    shutil.rmtree(deployFolder, ignore_errors=True)
    exit(1)

if(getOpts().branch==None):
    print(os.getcwd())
    currentBranch = subprocess.check_output("git rev-parse --abbrev-ref HEAD",stderr=subprocess.STDOUT, shell=True)
    branch = str(currentBranch).split("'")[1].split("\\n")[0]
else: 
    branch = getOpts().branch

#switch to the branch spacified 
try:
   
    subprocess.call(["git","checkout",branch])
    print(" checked-out "+branch+" : success")
except:
    shutil.rmtree(deployFolder, ignore_errors=True)
    print('please spacify a valid branch')
    exit(1)
    
try:
    os.remove('package-lock.json')
    subprocess.call(["npm","i"])
    print(" installed required packages : success")
except:
    print("error in clonning")
    exit(1)
 
# try:
#     subprocess.call(['pm2','start','server.js','--name api'])
#     print('service started : success')
# except:   
#     print('pm2 could not start ')
#     exit(1)