

function parseTopicGame(message){
    let jsonData = JSON.parse(message);
    let reset = jsonData.reset
        ? "true"
        : "ERROR";

    return {
        reset: reset
    }
}

module.exports = parseTopicGame;
