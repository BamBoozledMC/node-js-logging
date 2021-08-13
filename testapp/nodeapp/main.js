console.log('hi')
var {PythonShell} = require('python-shell');

let options = {
  mode: 'text',
  pythonOptions: ['-u'], // get print results in real-time
  scriptPath: './python/',
};

PythonShell.run('main.py', options, function (err, results) {
  if (err) throw err;
  console.log('results: %j', results);
  console.log('finished');
});

console.log('Hello World!');
