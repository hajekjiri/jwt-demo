from authlib.jose import jwt
import time

def issue_jwt( file_name='key.pem' ):

  encoded_jwt = None

  iat_time = int( time.time() ) #when was this jwt issued
  nbf_time = iat_time + 3 #valid in three seconds
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

  with open( file_name, 'r' ) as f:
    key = f.read()
    encoded_jwt = jwt.encode( header, payload, key )

  return encoded_jwt
