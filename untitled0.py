import hashlib 
from simplecrypt import encrypt , decrypt 

value = "peter:hellow"


def SHA256():
    result = hashlib.sha256(value.encode())
    print("SHA256 Data = " ,result.hexdigest())

SHA256()

def MD5():
    result = hashlib.md5(value.encode())
    print("MD5  = " , result.hexdigest())
MD5()

message = "Rohan1"
hexstring = ""

def encryption():
    global hexstring
    cypher_code = encrypt('AIM',message)
    hexstring = cypher_code.hex()
    print("encrypt = " , hexstring)
encryption()

def decryption():
    global hexstring
    byte_string = bytes.fromhex(hexstring) 
    original_r = decrypt('AIM',byte_string)
    final = original_r.decode("utf-8")
    print("decrypt = ", final)

decryption()
    

    
    