const path = require('path');
const express = require('express');
const chalk = require('chalk');
const morgan = require('morgan');

const PORT = process.env.PORT || 1337;
const app = express();

app.use('/dist',express.static(path.join(__dirname, 'dist')));

app.use(morgan('dev'));

app.get('/', (request,response) => {
    response.sendFile(path.join(__dirname, 'index.html'));
});

app.listen(PORT, () => {
    console.log(chalk.blue(`Listening intently on port ${PORT}`));
});
