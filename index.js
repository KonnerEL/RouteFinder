const PORT = process.env.PORT || 5000
const express = require('express');
const app = express();

const router = express.Router();

app.use(express.static(__dirname));

app.get('/',(req,res)=>{
    try {      
        res.sendFile('index.html'); 
    } catch(e) {
        console.log('Error:', e.stack);
    }
})

app.get('/python',(req,res)=>{
    try {      
        var source = req.query.source
        var target = req.query.target
        const { spawn } = require('child_process');
        const pythonProcess = spawn('python', ['./main.py', source, target]);

        pythonProcess.stdout.on('data', (data) => {
            res.send(data.toString());
        });
    } catch(e) {
        console.log('Error:', e.stack);
    }
})

///////////////////PORT SERVER////////////////////
app.listen(8080, () => {
  console.log(`Listening on 8080`)
})
/////////////////////////////////////////////////




