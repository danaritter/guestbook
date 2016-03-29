import os
import urllib
import logging
import traceback
import webbrowser 

from rauth import OAuth1Service

import webapp2


def getSession():
    # Create a session
    # Use actual consumer secret and key in place of 'foo' and 'bar'
    service = OAuth1Service(
              name = 'etrade',
              consumer_key = 'foo',
              consumer_secret = 'bar',
              request_token_url = 'https://etws.etrade.com/oauth/request_token',
              access_token_url = 'https://etws.etrade.com/oauth/access_token',
              authorize_url = 'https://us.etrade.com/e/t/etws/authorize?key={}&token={}',
              base_url = 'https://etws.etrade.com')

    # Get request token and secret    
    oauth_token, oauth_token_secret = service.get_request_token(params = 
                                  {'oauth_callback': 'oob', 
                                   'format': 'json'})

    auth_url = service.authorize_url.format(consumer_key, oauth_token)

    # Get verifier (direct input in console, still working on callback)
    webbrowser.open(auth_url)
    verifier = input('Please input the verifier: ')

    return service.get_auth_session(oauth_token, oauth_token_secret, params = {'oauth_verifier': verifier})



class MainPage(webapp2.RequestHandler):

    def get(self):
    	session = getSession()
    	# After authenticating a session, use sandbox urls
	url = 'https://etwssandbox.etrade.com/accounts/sandbox/rest/accountlist.json'
	resp = session.get(url, params = {'format': 'json'})
   	self.response.write(resp)
    
    


app = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)