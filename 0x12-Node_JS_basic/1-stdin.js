process.stdout.write('Welcome to Holberton School, what is your name?\n');

process.stdin.on('readable', () => {
  const INPUT = process.stdin.read();
  if (INPUT) process.stdout.write(`Your name is: ${INPUT}`);
});

process.stdin.on('end', () => {
  process.stdout.write('This important software is now closing\n');
});
