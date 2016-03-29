from rauth import OAuth1Service
import webbrowser 

def getSession():
    
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

    # Get verifier (direct input in console, still working on callback)
    webbrowser.open(auth_url)
    verifier = raw_input('Please input the verifier: ')

    return service.get_auth_session(oauth_token, oauth_token_secret, params = {'oauth_verifier': verifier})

# Create a session
session = getSession()

# After authenticating a session, use sandbox urls
url = 'https://etwssandbox.etrade.com/accounts/sandbox/rest/accountlist.json'

resp = session.get(url, params = {'format': 'json'})

print(resp)