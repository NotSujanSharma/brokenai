import jwt
import datetime

def generate_jwt(user_id):
    secret_key = "not a good secret key"

    # Payload data you want to encode within the JWT
    payload = {
        "user_id": user_id,
        "exp": datetime.datetime.utcnow() + datetime.timedelta(days=1),
        "iat": datetime.datetime.utcnow(), 
    }

    # Generate the JWT
    token = jwt.encode(payload, secret_key, algorithm="HS256")

    # Since jwt.encode() returns a byte string, decode it to get the string representation
    #token_str = token.encode('utf-8')

    return token

def decode_jwt(token):
    secret_key = "not a good secret key"
    try:
        decoded_token = jwt.decode(token, secret_key, algorithms=["HS256"])
        return decoded_token
    except:
        return None

def authorized(token):
    #check if token is jwt or not
    if(token is None):
        return False
    
    #Verify the signature of the JWT
    decoded_token = decode_jwt(token)
    if(decoded_token is not None):
        return True
    else:
        return False
        
def get_username(token):
    decoded_token = decode_jwt(token)
    if(decoded_token is not None):
        return decoded_token['user_id']
    else:
        return None


