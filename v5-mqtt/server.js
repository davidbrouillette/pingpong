const path = require('path');
const express = require('express');
const chalk = require('chalk');
const morgan = require('morgan');
var mqtt = require('mqtt');
const socketIO = require('socket.io');

const parseTopicScore = require('./score.topic');

const parseTopicGame = require('./game.topic');

const parseTopicServe = require('./serve.topic');

const PORT = process.env.PORT || 1337;
const app = express();
const server = require('http').createServer(app);

const SocketSetup = require('./socketSetup.js');

var io = socketIO(server);
var clientSocket = null;
SocketSetup(server, io, clientSocket);


var client = mqtt.connect('http://192.168.86.37:1883');

client.on('connect', ()=>{
    client.subscribe('/pingpong/score', (err)=>{
        if(err){
            console.log(err);
            return;
        } 
    });
    client.subscribe('/pingpong/game', (err)=>{
        if(err){
            console.log(err);
            return;
        } 
    });
    client.subscribe('/pingpong/serve', (err)=>{
        if(err){
            console.log(err);
            return;
        } 
    });
});

client.on('message', (topic, message) => {
    if(topic === '/pingpong/score'){
        let data = parseTopicScore(message.toString());
        
        if(data.player !== "ERROR" && data.action !== "ERROR"){
            io.emit('score', JSON.stringify(data));
        }
        client.publish('/pingpong/score/ack', '{"received":"true"}');
    }
    if(topic === '/pingpong/game'){
        let data = parseTopicGame(message.toString());
        if(data.reset !== "ERROR"){
            io.emit('game', JSON.stringify(data));
        }
    }
    if(topic === '/pingpong/serve'){
        let data = parseTopicServe(message.toString());
        if(data.server !== "ERROR" && data.action !== "ERROR"){
            io.emit('serve', JSON.stringify(data));
        }
    }
});


app.use('/build',express.static(path.join(__dirname, 'build')));

app.use(morgan('dev'));

app.get('/', (request,response) => {
    response.sendFile(path.join(__dirname, 'build/index.html'));
});

server.listen(PORT, () => {
    console.log(chalk.cyan(`Listening intently on port ${PORT}`));
});


