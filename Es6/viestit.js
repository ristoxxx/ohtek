const http = require('http');
//const jsonFile = require('./events.json');
//let events = jsonFile['data'];
//let e = events[80];
//let nimi = e.id;
const fetch = require('node-fetch');

const httpPromise = fetch('http://jsonplaceholder.typicode.com/users');
Promise.httpPromise.then((values) => {
    console.log(values);
  });
//const users = require('./users.json');
//const posts = require('./posts.json');
//let nimi = users.length;
//console.log(users.length);



const hostname = '127.0.0.1';
const port = 3000;

const server = http.createServer((req, res) => {
  res.statusCode = 200;
  res.setHeader('Content-Type', 'text/plain');
  res.end('Helo World ' + ' !' + nimi);
});
server.listen(port, hostname, () => {
  console.log(`Server running at http://${hostname}:${port}/`);
});