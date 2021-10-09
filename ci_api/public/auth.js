

const get = async ()=>{
    try{
        const response =await axios.get(window.location.href+'auth',{params :{key : key} })
        localStorage.setItem('baseURL',window.location.href)
      return(response.data)
    }
    catch(e){
        console.log(e)
         return(1)    
    }
}

const authenticate = async () =>{
    const result = await get();
    if(result!==1){  
    localStorage.setItem('deployer',deployer)
    localStorage.setItem('key',key)
       window.location.assign(localStorage.getItem('baseURL')+'home?key='+key)
       console.log(response)
       return 0
    }
   localStorage.removeItem('key');
   window.location.reload()
}

authenticate()