import React from 'react';
import Score from './score.jsx';
import "./app.css";
import io from 'socket.io-client';

class App extends React.Component{
    constructor(props){
        super(props);
		
        this.state = {
            score1: 0,
            score2: 0,
            socket: null
        }

        this.addPoint = this.addPoint.bind(this);
    }
    
    componentWillMount(){
		const socket = io('http://localhost:1337');
		socket.on('connected', (data) => {
			console.log(`from server through socketio: ${JSON.stringify(data)}`);
		});
		socket.on('buttonPressed', (data) => {
			console.log(`In buttonPressed event: ${data}`);
			if(data === "button1"){
				this.setState({
					score1: this.state.score1 + 1
				});
			} else if(data === "button2"){
				this.setState({
					score2: this.state.score2 + 1
				});
			}
		});
		
		this.setState({
			socket:socket
		});
	}

    addPoint(e){
        let newP1Score = this.state.score1;
        let newP2Score = this.state.score2;

        if(e.target.id === "one"){
            newP1Score = this.state.score1 + 1;
        } else if (e.target.id === "two"){
            newP2Score = this.state.score2 + 1;
        }
        
        this.setState({
            score1: newP1Score,
            score2: newP2Score
        });
    }
	
    render(){
        return (
            <div className="app-container">
                <div className="scores-container">
                    <Score
                        scoreToDisplay={this.state.score1}
                    />
                    <Score
                        scoreToDisplay={this.state.score2}
                    />
                </div>
                <button id="one" onClick={this.addPoint}>Player 1 Plus 1</button>
                <button id="two" onClick={this.addPoint}>Player 2 Plus 1</button>
            </div>
        )
    }
}

export default App;
