const {spawn} = require('child_process');

// spawn new child process to call the python script
 const python = spawn('cmd.exe', ['/c', 'cd python & python -u main.py']);
 // collect data from script
 python.stdout.on('data', (data) => {
  console.log(data.toString());
});
python.stderr.on('data', (data) => {
  console.log(data);
});
 // in close event we are sure that stream from child process is closed
 python.on('exit', (code, signal) => {
  console.log(`Child exited with code ${code} and signal ${signal}`);
});
python.stdin.end();
