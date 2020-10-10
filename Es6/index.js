const express = require('express');
const app = express();
const users = require('./users.json');
const posts = require('./posts.json');

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




app.get('/', function (req, res) {
    let suodatettu = abFilter(users, 5);
    let viestit = userPosts(posts, 5);
    let lisatty = {...suodatettu, posts: viestit };
    res.json(lisatty);
    //res.json(viestit);
})

app.get('/hei', function (req, res) {
        res.send('hello!');
})
 
app.listen(3000);