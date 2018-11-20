
function parseTopicScore(message){
    let jsonData = JSON.parse(message);
    let player = jsonData.player
        ? jsonData.player
        : "ERROR";

    let action = jsonData.action
        ? jsonData.action
        : "ERROR";

    return {
        player: player,
        action: action
    }
}

module.exports = parseTopicScore;