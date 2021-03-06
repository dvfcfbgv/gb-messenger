import React, { Component } from 'react'
import { withApollo } from 'react-apollo'
import { withStyles } from '@material-ui/core'
import ChatroomToolbox from './ChatroomToolbox.js/ChatroomToolbox'

class MainPanel extends Component {
	render() {
		if (!this.props.chatroomId) return null
		return (
			<div className={this.props.className}>
				<ChatroomToolbox chatroomId={this.props.chatroomId} />
			</div>
		)
	}
}

const styles = theme => ({})

export default withApollo(withStyles(styles)(MainPanel))
