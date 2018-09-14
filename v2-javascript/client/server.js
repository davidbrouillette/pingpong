const path = require('path');
const express = require('express');
const chalk = require('chalk');
const morgan = require('morgan');

const PORT = process.env.PORT || 1337;
const app = express();
const server = require('http').createServer(app);
const SocketSetup = require('./socketSetup.js');

app.use('/dist',express.static(path.join(__dirname, 'dist')));

app.use(morgan('dev'));

app.get('/', (request,response) => {
    response.sendFile(path.join(__dirname, 'index.html'));
});

var sockets = SocketSetup(server);


server.listen(PORT, () => {
    console.log(chalk.cyan(`Listening intently on port ${PORT}`));
});
