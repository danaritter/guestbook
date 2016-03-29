import os
import urllib

import webbrowser 
from google.appengine.ext import vendor
vendor.add('lib')
from rauth import OAuth1Service

from google.appengine.api import users
from google.appengine.ext import ndb

import jinja2
import webapp2

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)


DEFAULT_VERIFICATION_TOKEN = 'default_verification_token'

def verification_token(verification_token=DEFAULT_VERIFICATION_TOKEN)
    


class Verify(webapp2.RequestHandler)    
     



class MainPage(webapp2.RequestHandler):

    def get(self):
    	consumer_key = '32e402c7019a416b6f41c4c6d0acfb07'
        # Create a session
        # Use actual consumer secret and key in place of 'foo' and 'bar'
        service = OAuth1Service(
              name = 'etrade',
              consumer_key = consumer_key,
              consumer_secret = '9fd546af29d9ff761457f05589c1b8ab',
              request_token_url = 'https://etws.etrade.com/oauth/request_token',
              access_token_url = 'https://etws.etrade.com/oauth/access_token',
              authorize_url = 'https://us.etrade.com/e/t/etws/authorize?key={}&token={}',
              base_url = 'https://etws.etrade.com')

        # Get request token and secret    
        oauth_token, oauth_token_secret = service.get_request_token(params = 
                                  {'oauth_callback': 'oob', 
                                   'format': 'json'})

        auth_url = service.authorize_url.format(consumer_key, oauth_token)

        # Get verifier (from google app engine, still working on callback)
        webbrowser.open(auth_url)
        template = JINJA_ENVIRONMENT.get_template('index.html')
        self.response.write(template.render(template_values))
    
        ##verifier = raw_input('Please input the verifier: ')
        
    


        service.get_auth_session(oauth_token, oauth_token_secret, params = {'oauth_verifier': verifier})
        
    
    	# After authenticating a session, use sandbox urls
	    url = 'https://etwssandbox.etrade.com/accounts/sandbox/rest/accountlist.json'
	    resp = session.get(url, params = {'format': 'json'})
   	    self.response.write(resp)
    
    


app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/verify', Verify)
], debug=True)