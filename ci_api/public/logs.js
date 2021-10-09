const getLogs = async ()=>{
    try{
        const logData = await axios.get(localStorage.getItem('baseURL')+"logs?key="+key)
        return logData.data
    }
    catch(e){
        alert("could not get log")
    }
}

