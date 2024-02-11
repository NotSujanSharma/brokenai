import jwt
import datetime

def generate_jwt(user_id):
    # Your "secret" key that will be used to encode the JWT
    secret_key = "meisujansharmathegreat"

    # Payload data you want to encode within the JWT
    payload = {
        "user_id": user_id,  # Example user ID
        "exp": datetime.datetime.utcnow() + datetime.timedelta(days=1),  # Expiration time
        "iat": datetime.datetime.utcnow(),  # Issued at
    }

    # Generate the JWT
    token = jwt.encode(payload, secret_key, algorithm="HS256")

    # Since jwt.encode() returns a byte string, decode it to get the string representation
    #token_str = token.encode('utf-8')
    return token

def decode_jwt(token):
    secret_key = "meisujansharmathegreat"
    try:
        decoded_token = jwt.decode(token, secret_key, algorithms=["HS256"])
        return decoded_token
    except:
        return None

def authorized(token):
    #check if token is jwt or not
    if(token is None):
        return False
    
    #Veryfy the signature of the JWT
    decoded_token = decode_jwt(token)
    if(decoded_token is not None):
        return True
    else:
        return False


