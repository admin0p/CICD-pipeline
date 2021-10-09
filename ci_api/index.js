const express = require('express')
const app = express()
const cors =  require('cors')
const bodyParser = require('body-parser')
const {getAllBranch,runPipeline} = require('./exec')
const authKey = require('./config')
const {fileop,fileRead} = require('./filelog')

const port = 3000
const logFile = 'logs.txt' 

app.use(bodyParser.urlencoded({extended: true}));
app.set('view engine','ejs');
app.use(express.static('public'));
app.use(cors())

app.get('/', (req, res) => {
    res.render('auth')
    
})

app.get('/auth',(req,res)=>{
    if(req.query.key===authKey){
      return  res.status(200).json({message: "success"})
    }
    res.status(503).json({message: "auth failed"})
})

app.get('/home',auth,(req,res)=>{
    res.render('home')
})

app.get('/backend',auth,async (req,res)=>{
    const branch = await getAllBranch()
    res.render('backend',{branch:branch , key: req.query.key})
})

app.get('/frontend',(req,res)=>{
    res.render('frontend')
})

app.post('/run',auth,async (req,res)=>{
    const data = JSON.parse(Object.keys(req.body)[0])
    console.log(data)
    const {branch,path,deployer}=data
    const result = await runPipeline(branch,path)
    var obj = ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n\n"
                +"time-stamp: "+new Date(Date.now())
                +"\n\ndeployer-name : "+deployer
                +"\n\npath : "+path
                +"\n\nbranch-name : "+branch
                +"\n\nDeploy-logs : "+result+"\n\n\n\n"
    fileop(logFile,obj)
    res.json({logs: obj})
})
app.get('/logs',async (req,res)=>{
    const data =await fileRead("./"+logFile)
    
    res.send(data)
})


//middle ware

function auth(req,res,next){

    if(req.query.key!=authKey){
        return  res.redirect('/')
    }
    next();
}




app.listen(port, () => console.log(`listening on `+port))