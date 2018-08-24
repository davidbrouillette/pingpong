import React from 'react';
import ReactDOM from 'react-dom';
import App from './components/app.jsx';
import io from 'socket.io-client';

const socket = io('http://localhost:1337');
socket.on('news', function(data){
    console.log(`from server through socketio: ${data}`);
});

ReactDOM.render(
    <App />,
    document.getElementById('react-app-root')
);