var mqtt = require('mqtt');


const MqttClient = () => {
    var client = mqtt.connect('ws://192.168.86.37:9001');

    client.on('connect', ()=>{
        client.subscribe('/pingpong/score', (err)=>{
            if(err){
                console.log(err);
                return;
            }
            client.publish('/pingpong/score/ack', 'true');
        });
    });

    client.on('message', (topic, message) => {
        if(topic === '/pingpong/score'){
            console.log(message.toString());
            client.end();
        }
    });
}

export default MqttClient