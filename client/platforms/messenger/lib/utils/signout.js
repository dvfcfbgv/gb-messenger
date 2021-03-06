import cookie from 'cookie'

import redirect from './redirect'

export default apolloClient => {
	document.cookie = cookie.serialize('token', '', {
		maxAge: -1 // Expire the cookie immediately
	})

	// Forece a reload of all the current queries now that user is
	// logged in, so we don't accidentally leave any state around.
	apolloClient.cache.reset().then(() => {
		// Redirect to a more useful page when signed out
		redirect({}, '/login')
	})
}
