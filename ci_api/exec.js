const { stdout } = require('process');
const util = require('util')
const exec = util.promisify(require('child_process').exec)
const spawn = util.promisify(require('child_process').spawn)



const getAllBranch = async ()=>{
    var branches = [];
    try{
        const {stdout,stderr} =await exec('cd /root/api/server/find-backend && git branch -r')
       const branch = stdout.split("origin/")
       for(var i=2;i<branch.length;i++){
       branches.push(branch[i].split('\n')[0]) 
       }
       return(branches)
    }catch(e){
        console.log(e)
        return(1)
    }


}




const runPipeline = async (branch,path)=>{

    try{
    const {stdout,stderr} = await exec('cd ../script/ && python3 ci.py -p '+ path + ' -b ' + branch) 
    return stdout;

}
catch(e){
    console.log(e)
    return(1)
}

}

module.exports = {getAllBranch : getAllBranch , runPipeline: runPipeline }


