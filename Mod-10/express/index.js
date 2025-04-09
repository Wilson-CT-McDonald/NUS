const express = require('express')
const app = express()
const PORT = 5000
const path = require('path')

app.set("view engine","pug")
app.set("views","./views")

app.get('/:name',(request,response) => {
    //response.send('Welcome to express')
    //response.sendFile(path.join(__dirname,"home.html"))
    response.render("home",{name:request.params.name})
})

app.get('/about',(request,response) => {
    //response.send('About Page')
    response.sendFile(path.join(__dirname,"about.html"))
})

app.listen(PORT,()=>{
    console.log('SERVER IS RUNNING AT ${PORT}')
})