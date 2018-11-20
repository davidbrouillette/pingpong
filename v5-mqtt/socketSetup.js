
const SocketSetup = (server, io, clientSocket) => {
	io.on('connection', function(socket){
		clientSocket = socket;
        
        console.log("Connected to client");
        clientSocket.emit('connected', {"connected":"true"});
		
		clientSocket.on('disconnect', ()=>{
			console.log("client disconnected");
        });	
	});
}

module.exports = SocketSetup;
