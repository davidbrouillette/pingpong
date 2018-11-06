import React, { Component } from "react";
import io from "socket.io-client";
import { MuiThemeProvider, createMuiTheme } from "@material-ui/core/styles";
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
            scoreLeft: 0,
            scoreRight: 0,
            currentServer: "serverLeft",
            socket: null
        };
    }

    componentWillMount() {
        const socket = io("http://localhost:1337");
        socket.on("connected", (data) => {
            console.log(`from server through socketio: ${JSON.stringify(data)}`);
        });
        socket.on("scoreLeft", (data) => {
            let newScoreLeft = this.state.scoreLeft + 1;
            let newServer = {};
            let totalScore = newScoreLeft + this.state.scoreRight;
            let mod = totalScore > 21 
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
                scoreLeft: newScoreLeft,
                ...newServer
            });
        });
        socket.on("scoreRight", (data)=>{
            let newScoreRight = this.state.scoreScore + 1;
            let newServer = {};
            let totalScore = newScoreRight + this.state.scoreLeft;
            let mod = totalScore > 21
                ? 2
                : 5;
            if (totalScore % mod === 0) {
                newServer = {
                    currentServer: this.state.currentServer === "serverLeft"
                        ? "serverRight"
                        : "serverLeft"
                }
            }
            this.setState({
                scoreRight: newScoreRight,
                ...newServer
            });
            
        });

        this.setState({
            socket: socket
        });
    }

    render() {
        return (
            <MuiThemeProvider theme={theme}>
                <div className="App">
                    <ActiveGame scoreLeft={20} scoreRight={17} serveLeft={false} serveRight={true} />
                </div>
            </MuiThemeProvider>
        );
    }
}

export default App;
