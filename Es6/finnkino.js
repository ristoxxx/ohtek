const express = require('express');
const app = express();
const axios = require('axios');

//määritellään datan nouto osoitteet
const urlPosts = "https://www.finnkino.fi/xml/Schedule/?area=1013&dt=11.10.2020";


//määritelään promiset
const promisePosts = axios.get(urlPosts);


//odotetaan kunnes kaikki promiset ovat valmistuneet ja sitten
Promise.all([promisePosts]).then((values) => { //values sisältää molemmat promiset
    //alustetaan muuttujat
    var user                            //käyttäjän tiedot
    var posts                           //viestit
    var combination                     //yhdistelmä yksittäisen käyttäjän tiedoista ja viesteistä
    var list = []                       //lista jolle kootaan kaikkien käyttäjien kaikki tiedot
    //var c = values[1].data.length                       //käyttäjien lukumäärä

                              //                        silmukka joka kerää jokaisen käyttäjän
    //user = values[1].data.filter(p => p.id == i)        //tiedot
    //posts = values[0].data.filter(p => p.ID > 1)   //ja viestit
    //combination = {...user, posts: posts}               //ja muodostaa niistä yhdistelmän
    //list = list.concat(combination)                     //joka lisätään listalle
    posts = values.data.shows

    app.get('/users', function (req, res) {             //muodotetaan endpoint /users ja tulostetaan respondina
        res.json(posts);                                 //kertynyt lista
    })
  });

app.listen(3000);                                       //portti jota sovellus kuuntelee (localhost:3000)
