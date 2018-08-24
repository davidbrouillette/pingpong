// import wpi from 'wiring-pi';

// function setupGPIO(){
//     wpi.setup('wpi');
//     var pin = 0;
//     wp1.pinMode(pin, wpi.OUTPUT);
//     var value = 1;


// }

const Gpio = require('pigpio').Gpio;

const button = new Gpio(4,{
    mode: Gpio.INPUT,
    pullUpDown: Gpio.PUD_DOWN,
    edge: Gpio.EITHER_EDGE
});

button.on('interrupt', (level) => {
    console.log(level);
})