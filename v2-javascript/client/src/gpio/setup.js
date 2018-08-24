import wpi from 'wiring-pi';

function setupGPIO(){
    wpi.setup('wpi');
    var pin = 4;
    wpi.pinMode(pin, wpi.IN);
    wpi.pullUpDnControl(pin, wpi.PUD_UP)

	while true{
		buttonPressed = wpi.input(4);
		if(!buttonPressed){
			alert("buttonpressed");
		}
	}
}
