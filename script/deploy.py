import optparse
import os
import subprocess
import shutil

#temp folder
foldername = "temp-jifhijhfidsjfjhsfhsfvsdfvdsgcdvscudsbc"

#get arguments / options
def getOpts() :
    parse = optparse.OptionParser()
    parse.add_option("-b","--branch", dest = "branch",help = "branch to be deployed")
    parse.add_option("-p","--path", dest = "path",help = "path in ur registry")
    (option , args) = parse.parse_args()
    return option

#git hub link (file to be cloned)
path = getOpts().path
f = open("./config","rt")
gitReg = f.read()

#make the temp folder
try:
    currentDir = os.getcwd()
    #print('u are in '+currentDir)
    os.mkdir(foldername)
    os.chdir(currentDir + "/" + foldername)
except: 
    print("internal error .... please run the command again")
    shutil.rmtree(currentDir + "/" + foldername, ignore_errors=True)
    exit(1)
   
#clone repo into the temp folder
try:
    print('========================================================')
    result = subprocess.check_output("git clone "+gitReg,stderr=subprocess.STDOUT,shell=True)
    print(result)
except  :
    shutil.rmtree(currentDir + "/" + foldername, ignore_errors=True)
    print("please add ur ssh registry link in the config file") 
    exit(1)

#get the path that needs to be deployed
try:        
    os.chdir(currentDir + "/" + foldername + "/" + path)
except:
    print("eneter valid loaction path")
    shutil.rmtree(currentDir + "/" + foldername, ignore_errors=True)
    exit(1)

#print('u are in '+ os.getcwd())

#check if any branch is spacifies if not deploy the current branch 
if(getOpts().branch==None):
    currentBranch = subprocess.check_output("git rev-parse --abbrev-ref HEAD",stderr=subprocess.STDOUT, shell=True)
    branch = str(currentBranch).split("'")[1].split("\\n")[0]
else: 
    branch = getOpts().branch

#switch to the branch spacified 
try:
    print('========================================================')
    result=subprocess.check_output("git checkout "+getOpts().branch, stderr=subprocess.STDOUT, shell=True)
    print(result)
except:
    shutil.rmtree(currentDir + "/" + foldername, ignore_errors=True)
    print('please spacify a valid branch')
    exit(1)

#deploy to the server

#Note: edit the ssh host 
# subprocess.call(['ssh','root@165.232.189.212',"pm2 kill && cd /root/api/server && rm -rf *"])
# subprocess.Popen("bash -O extglob -c 'scp -r !(node_modules) root@165.232.189.212:/root/api/server'",stderr=subprocess.STDOUT,shell=True).communicate()
# subprocess.call(['ssh','root@165.232.189.212', "cd /root/api/server && rm -rf package-lock.json && npm install &&  pm2 start server.js --name api && exit"])#add pm2 start 


#subprocess.call(['pm2','kill'])

shutil.rmtree('/home/admin0p/Desktop/apidepl/server', ignore_errors=True)
os.mkdir('/home/admin0p/Desktop/apidepl/server')
subprocess.call(['cp','-r','.','/home/admin0p/Desktop/apidepl/server'])
os.chdir('/home/admin0p/Desktop/apidepl/server')
os.remove('package-lock.json')
subprocess.call(['npm','install'])

#subprocess.call(['pm2','start','server.js','--name','api'])


shutil.rmtree(currentDir + "/" + foldername, ignore_errors=True)