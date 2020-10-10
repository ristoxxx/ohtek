//const Redux = require('redux');
const fetch = require('node-fetch');
const express = require('express');
const app = express();
const users = require('./users.json');
const posts = require('./posts.json');
const axios = require('axios');
const { response } = require('express');

const url = "https://jsonplaceholder.typicode.com/posts";
const urlb = "https://jsonplaceholder.typicode.com/users";

const promise = axios.get(url);
const promiseb = axios.get(urlb);

Promise.all([promise, promiseb]).then((values) => {
    const user = values[1].data.filter(p => p.id == 3)
    const posts = values[0].data.filter(p => p.userId == 3)
    const combination = {...user, posts: posts}
    app.get('/users', function (req, res) {
        res.json(combination);
        //res.json(viestit);
    })
  });
//promise.then(response => {
//    const notes = response.data
//    console.log(notes[1])
//})

//promiseb.then(response => {
//    const notesb = response.data
//    console.log(notesb[1])
//})

//const get_data = async url => {
//  try {
//    const response = await fetch(url);
//    const json = await response.json();
//    return json;
//  } catch (error) {
//    console.log(error);
//  }
//};

//const post = get_data(url);
//console.log(post);

//fetch('https://jsonplaceholder.typicode.com/posts')
//  .then(response => response.json())
//  .then(data => {
//      console.log(data);
//        const pos = data;
//        app.get('/hei', function (req, res) {
//            res.json(pos);
//    })
//  })
  //.catch(err => ...)

function idFilter(minNumber = '1', maxNumber = '1') {
    return function (user) {
        console.log('moi');
        let { id } = user.id; // object destructuring
        return id && 4 <= id && id <= 8;
    }
}
function userPosts(posts, x){
    let uPosts = posts
    .filter(p => p.userId == x);
    return uPosts;
}

function abFilter(users, y){
    let su = users
    .filter(e => e.id != null)
    .filter(e => e.id == y);
    return su;
}

function luoTuloste(users, posts, z) {
    let suodatettu = abFilter(users, z);
    let viestit = userPosts(posts, z);
    return {...suodatettu, posts: viestit };
//let lisatty = {...suodatettu, posts: viestit };
}
let lisa = luoTuloste(users, posts, 6);
let li = luoTuloste(users,posts,7);
let lisatty = {...lisa, ...li};

app.get('/', function (req, res) {
    res.json(lisatty);
    //res.json(viestit);
})


 
app.listen(3000);