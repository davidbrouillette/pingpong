const express = require('express');
const bodyParser = require('body-parser');
const fs = require('fs');

const Stats = require('./stats.model');
const Game = require('./game.model');
const Player = require('./player.model');


const app = express();

app.use(bodyParser.json());

app.get('/', (request,response)=>{
    response.send('test');
});

app.post('/saveGame', (request, response) =>{
    const newGame = new Game(response.body);

    fs.appendFileSync('games.json', JSON.stringify(newGame));

    response.json({"success":"true"});
});


app.listen(3002, ()=>{
    console.log('Listening on port 3002');
})