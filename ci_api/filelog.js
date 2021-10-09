
const util = require('util')
const fs = require('fs')
const writeFile = util.promisify(fs.appendFile)
const readFile = util.promisify(fs.readFile);


const fw = async (fpath,buffer)=>{
   try{
       const data = await writeFile(fpath,buffer)
   }
    catch(e){
        console.log("error in write==== "+e)
    }
}

const fileop = async (file,str)=>{
try{
   // const readData =await readFile(file);
    //const data = JSON.parse(readData)
    //data.push(str);
    const stat = fs.statSync(file).size / (1024 * 1024)
    console.log(stat)
   if(stat > 1.5){
   const unlink = fs.unlinkSync(file)

   }
   fw(file,str)
}
catch(e){
    console.log("creating file")
    fw(file,str)
}

}

const fileRead = async (file) =>{
    try{
        const data = await readFile(file);
       
        return (data)

    }catch(e){
        console.log(e)
        return ("no file")
    }
}


module.exports = {fileop : fileop , fileRead: fileRead }



