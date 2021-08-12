console.log('hi')
const {spawn} = require('child_process');

// spawn new child process to call the python script
 const python = spawn('python', ['test.py']);
 // collect data from script
 python.stdout.on('data', function (data) {
  console.log('Pipe data from python script ...');
  var textChunk = data.toString('utf8');// buffer to string
  console.log(textChunk);
 });

python.on('message', (message) => {
  console.log(message)
})

 // in close event we are sure that stream from child process is closed
 python.on('close', (code) => {
 console.log(`child process close all stdio with code ${code}`);
});

console.log('Hello World!');
