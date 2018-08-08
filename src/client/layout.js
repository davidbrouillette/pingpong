import React from 'react';
import Score from './score.js';
import ServeIndicator from './scoreIndicator.js';

const Layout = ({indicator, active}) => {
	return (
		<div className="layout-component">
			<div className={active ? "current-serve default" : "default"}>
				{ indicator }
			</div>
		</div>
	)
}

export default ServeIndicator;
