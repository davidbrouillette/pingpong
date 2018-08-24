import React from 'react';
import Score from './score.jsx';
import wpi from 'wiring-pi';
import "./app.css";

class App extends React.Component{
    constructor(props){
        super(props);

        this.state = {
            score1: 0,
            score2: 0
        }

        this.addPoint = this.addPoint.bind(this);
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

	componentDidMount(){
		wpi.setup('wpi');
		var pin = 4;
		wpi.pinMode(pin, wpi.IN);
		wpi.pullUpDnControl(pin, wpi.PUD_UP)

		while(true){
		
			buttonPressed = wpi.input(4);
			if(!buttonPressed){
				alert("buttonpressed");
			}
		}
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
