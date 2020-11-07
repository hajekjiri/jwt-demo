from authlib.jose import jwt
import time

def issue_jwt( filename='key.pem' ):
  """
    issue_jwt: create jwt based on rsa key file
    @input: filename
    @output: jwt string
  """

  encoded_jwt = None

  iat_time = int( time.time() ) #when was this jwt issued
  nbf_time = iat_time + 1 #valid in one second
  exp_time = nbf_time + 60 * 3 # expires in three minutes
  
  header = { 'alg' : 'RS256' }
  payload = {
    'iss' : 'Issuer name',
    'sub' : 'Subject name',
    'aud' : 'Audience name',
    'exp' : exp_time,
    'nbf' : nbf_time,
    'iat' : iat_time,
    'jti' : 'JWT ID'
  }

  with open( filename, 'r' ) as f:
    key = f.read()
    encoded_jwt = jwt.encode( header, payload, key )

  return encoded_jwt

def validate_jti( claim, jti ):

  correct = 'JWT ID'

  if len( correct ) != len( jti ):
    return False

  for i,j in zip( jti, correct ):
    if i != j:
      return False

  return True

def verify_jwt( encoded_jwt, filename='pubkey.pem' ):
  """
    @input: jwt to decode, filename with public key
    @output: decoded jwt str
  """

  ret_val = ""
  
  options = {
    'iss' : {
      #for multiple issuers you can use `values`
      'values' : ['Issuer name', 'Another issuer'],
      #tells jwt whether it has to check for issuer
      'essential' : True
    },
    'sub' : {
      #for one subject you can use `value`
      'value' : 'Subject name',
      'essential' : True
    },
    'aud' : {
      'value' : 'Audience name',
      'essential' : True
    },
    'exp' : {
      'essential' : True
    },
    'nbf' : {
      'essential' : True
    },
    'iat' : {
      'essential' : True
    },
    'jti' : {
      'essential' : True,
      #you can define your own function for validation
      'validate' : validate_jti
    }
  }

  with open( filename, 'r' ) as f:
    pubkey = f.read()
    #here we decode claims for validation
    claims = jwt.decode( encoded_jwt, pubkey, claims_options=options )
    #and finally we validate every claim
    claims.validate()
    ret_val = claims.__str__()

  return ret_val

if __name__ == "__main__":
  s =  issue_jwt()
  #we'll wait for one second since the token isn't valid yet
  time.sleep( 1 )
  print( verify_jwt( s ) )
