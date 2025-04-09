const os = require('os')
const path = require('path')

console.log('Hello World');

console.log(os.type())
console.log(os.version())
console.log(os.homedir())
console.log('-------------')
console.log('Directory: ',__dirname)
console.log('File Name: ',__filename)

const {add,mul} = require('./math')

console.log('addition: ',add(3,5))