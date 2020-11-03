const express = require('express');
const app = express();
const axios = require('axios');

//määritellään datan nouto osoitteet
const urlPosts = "https://jsonplaceholder.typicode.com/posts";
const urlUsers = "https://jsonplaceholder.typicode.com/users";

//määritelään promiset
const promisePosts = axios.get(urlPosts);
const promiseUsers = axios.get(urlUsers);

//odotetaan kunnes kaikki promiset ovat valmistuneet ja sitten
Promise.all([promisePosts, promiseUsers]).then((values) => { //values sisältää molemmat promiset
    //alustetaan muuttujat
    var user                            //käyttäjän tiedot
    var posts                           //viestit
    var combination                     //yhdistelmä yksittäisen käyttäjän tiedoista ja viesteistä
    var list = []                       //lista jolle kootaan kaikkien käyttäjien kaikki tiedot
    var c = values[1].data.length                       //käyttäjien lukumäärä

    for (i = 1; i < c; i++ ) {                          //silmukka joka kerää jokaisen käyttäjän
    user = values[1].data.filter(p => p.id == i)        //tiedot
    posts = values[0].data.filter(p => p.userId == i)   //ja viestit
    combination = {...user, posts: posts}               //ja muodostaa niistä yhdistelmän
    list = list.concat(combination)                     //joka lisätään listalle
    }

    app.get('/users', function (req, res) {             //muodotetaan endpoint /users ja tulostetaan respondina
        res.json(list);                                 //kertynyt lista
    })
  });

app.listen(3000);                                       //portti jota sovellus kuuntelee (localhost:3000)