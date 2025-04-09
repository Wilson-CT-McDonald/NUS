const http = require('http')
const PORT =  5000
const fs = require('fs')
const { error } = require('console')
const path = require('path')

const server = http.createServer(
    (request,response) => {
        let file_path = path.join(__dirname,'public',request.url==='/'?'home.html' : request.url + 'html')

        fs.readFile(file_path,(error,data)=> {
            if(error) {
                response.writeHead(200,{'content-type': "text/html"})
                response.end('<h1>404 Not Found</h1>')
            } else {
                response.writeHead(200,{'content-type': "text/html"})
                response.end(data)
            }
        })


        // if(request.url==='/') {
        //     response.writeHead(200,{'content-type': "text/html"})
        //     response.end('<h1>Home Page</h1> <p>This is HTML response</p>')
        // } else if(request.url==='/about') {
        //     response.writeHead(200,{'content-type': "text/html"})
        //     response.end('D:\Documents\Git Repo\NUS\Mod-10\node\public\about.html')
        // } else {
        //     response.writeHead(200,{'content-type': "text/html"})
        //     response.end('<h1>404 Not Found</h1>')
        // }
    }
)

server.listen(PORT, ()=>{
    console.log('server is running at ${PORT}')
})