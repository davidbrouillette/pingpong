import React from "react";
import Paper from "@material-ui/core/Paper";
import Grid from "@material-ui/core/Grid";
import Avatar from "@material-ui/core/Avatar";
import Chip from "@material-ui/core/Chip";
import AlbumIcon from "@material-ui/icons/Album";
import { withStyles } from "@material-ui/core";

const StyledPaper = ({ isServer, ...props }) => {
    const Styled = withStyles({
        root: {
            backgroundColor: isServer ? "#c2185b" : "transparent",
            color: "#fff",
            fontSize: "25vw"
        }
    })(Paper);
    return <Styled {...props} />;
};

const StyledPaperNoBackground = withStyles({
    root: {
        backgroundColor: "transparent"
    }
})(Paper);

const StyledLeftChip = withStyles({
    root: {
        width: "100%",
        justifyContent: "center",
        flexFlow: "row-reverse"
    }
})(Chip);

const StyledRightChip = withStyles({
    root: {
        width: "100%",
        justifyContent: "center"
    }
})(Chip);

class ActiveGame extends React.Component {
    render() {
        const { scoreLeft, scoreRight, serveLeft, serveRight } = this.props;

        return (
            <div className="activegame-component">
                <Grid
                    container
                    direction="row"
                    justify="space-around"
                    alignItems="stretch"
                    spacing={8}
                    className="activegame-container">
                    <Grid item xs={6} className="score-container">
                        <StyledPaper className="score" isServer={serveLeft}>
                            <div>{scoreLeft}</div>
                        </StyledPaper>
                    </Grid>
                    <Grid item xs={6} className="score-container">
                        <StyledPaper className="score" isServer={serveRight}>
                            <div>{scoreRight}</div>
                        </StyledPaper>
                    </Grid>
                    <Grid item xs={6}>
                        <StyledPaperNoBackground className="server-indicator-left-container">
                            <StyledLeftChip
                                avatar={
                                    <Avatar>
                                        <AlbumIcon />
                                    </Avatar>
                                }
                                label="Left Player"
                                className="server-indicator-left"
                                color="secondary"
                            />
                        </StyledPaperNoBackground>
                    </Grid>
                    <Grid item xs={6}>
                        <StyledPaperNoBackground className="server-indicator-right-container">
                            <StyledRightChip
                                avatar={
                                    <Avatar>
                                        <AlbumIcon />
                                    </Avatar>
                                }
                                label="Right Player"
                                className="server-indicator-right"
                                color="secondary"
                            />
                        </StyledPaperNoBackground>
                    </Grid>
                </Grid>
            </div>
        );
    }
}

export default ActiveGame;
