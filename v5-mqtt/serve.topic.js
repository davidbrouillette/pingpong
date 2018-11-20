
function parseTopicServe(message){
    let jsonData = JSON.parse(message);
    let action = jsonData.action
        ? jsonData.action
        : "ERROR";

    let server = jsonData.server
        ? jsonData.server
        : "ERROR";

    return {
        action: action,
        server: server
    }
}

module.exports = parseTopicServe;
