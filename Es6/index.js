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
function userPosts(posts){
    let uPosts = posts
    .filter(p => p.userId == 4);
    return uPosts;
}

function abFilter(users){
    let su = users
    .filter(e => e.id != null)
    .filter(e => e.id >= 4);
    return su;
}



app.get('/', function (req, res) {
    let suodatettu = abFilter(users);
    let viestit = userPosts(posts);
    //res.json(suodatettu);
    res.json(viestit);
})

app.get('/hei', function (req, res) {
        res.send('hello!');
})
 
app.listen(3000);