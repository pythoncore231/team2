import hashlib

string2hash = hashlib.sha512(b'You can hash only latin symbols')
hashedString = string2hash.hexdigest()

print(hashedString)