const chalk = require('chalk');
const Gpio = require('pigpio').Gpio;

const GPIOSetup = (clientSocket) => {
	const button = new Gpio(4, {
		mode: Gpio.INPUT,
		pullUpDown: Gpio.PUD_UP,
		edge: Gpio.FALLING_EDGE
	});

	button.enableAlert();
	button.glitchFilter(250);

	button.on('alert', (level, tick) => {
		try{
			console.log(chalk.green("In button Interrupt"));
			console.log(chalk.green(level));
			console.log("--");
			if(level === 0){
				clientSocket.emit('buttonPressed', 'button1');
			}
		} catch(e){
			console.error(e);
		}
		
	}, 2000);
	
	return button;
}

module.exports = GPIOSetup;
