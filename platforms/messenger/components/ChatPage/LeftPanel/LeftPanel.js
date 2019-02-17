import React, { Component } from 'react'
import { withApollo } from 'react-apollo'
import { withStyles } from '@material-ui/core'

import Chatrooms from './Chatrooms/Chatrooms'
import PanelNavBar from './PanelNavBar/PanelNavBar'

class MainPanel extends Component {
	render() {
		return (
			<div className={this.props.className}>
				<PanelNavBar />
				<Chatrooms username={this.props.username} />
			</div>
		)
	}
}

const styles = theme => ({})

export default withApollo(withStyles(styles)(MainPanel))
