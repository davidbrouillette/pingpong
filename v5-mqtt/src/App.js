import React, { Component } from "react";
import { MuiThemeProvider, createMuiTheme } from "@material-ui/core/styles";
import io from "socket.io-client";
import ActiveGame from "./pages/activeGame";

import "./App.css";

const theme = createMuiTheme({
    palette: {
        primary: {
            light: "#534bae",
            main: "#1a237e",
            dark: "#000051",
            contrastText: "#fff"
        },
        secondary: {
            light: "#fa5788",
            main: "#c2185b",
            dark: "#8c0032",
            contrastText: "#fff"
        }
    }
});

class App extends Component {
    constructor(props) {
        super(props);

        this.state = {
            player1: 0,
            player2: 0,
            currentServer: "serverLeft",
            socket: null
        };
    }

    componentWillMount() {
        
        const socket = io("http://localhost:1337");
        socket.on("connected", (data) => {
            console.log(`from server through socketio: ${JSON.stringify(data)}`);
        });
        socket.on("serve", (data)=>{
            let jsonData = JSON.parse(data);
            if(jsonData.action === "set" && (jsonData.server === "player1" || jsonData.server === "player2")){
                    let newServer = jsonData.server === "player1"
                        ? "serverLeft"
                        : "serverRight"
                    this.setState({
                        currentServer: newServer
                    });
            }
        })
        socket.on("game", (data) =>{
            let jsonData = JSON.parse(data);
            if(jsonData.reset){
                this.setState({
                    player1: 0,
                    player2: 0,
                    currentServer: "serverLeft",
                });
            }
        })
        socket.on("score", (data) => {
            let jsonData = JSON.parse(data);
            let newScore = this.state[jsonData.player];
            let totalScore = this.state.player1 + this.state.player2;
            let newServer = {};

            if(jsonData.action === "add") {
                newScore +=  1;
                totalScore++;
            } else if (jsonData.action === "subtract" && newScore > 0){
                    newScore -= 1;
                    totalScore--;
            }
            
            let mod = totalScore > 40
                ? 2
                : 5;
            if(totalScore % mod === 0){
                newServer = {
                    currentServer: this.state.currentServer === "serverLeft" 
                        ? "serverRight"
                        : "serverLeft"
                }
            }
            
            this.setState({
                [jsonData.player]: newScore,
                ...newServer
            });

        });

        this.setState({
            socket: socket
        });
    }

    render() {
        let leftServe = this.state.currentServer === "serverLeft";
        let rightServe = this.state.currentServer === "serverRight";

        return (
            <MuiThemeProvider theme={theme}>
                <div className="App">
                    <ActiveGame scoreLeft={this.state.player1} scoreRight={this.state.player2} serveLeft={leftServe} serveRight={rightServe} />
                </div>
            </MuiThemeProvider>
        );
    }
}

export default App;
