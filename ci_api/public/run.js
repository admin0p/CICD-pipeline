const config = {
    headers: {
      'Content-Type': 'application/x-www-form-urlencoded'
    }
}

const runpipeline = async (branch,path) =>{
    try{
        const response = await axios.post(localStorage.getItem('baseURL')+"run?key="+key,
        {branch: branch,
        path:'find-backend/server',
        deployer: localStorage.getItem('deployer')},config)
       return(response.data)
    }
    catch(err){
        console.log(err)
        return 1
    }
}