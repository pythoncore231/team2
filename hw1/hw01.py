"""git practice"""

import hashlib

string_to_hash = hashlib.sha512(b'You can hash only latin symbols')
hashed_string = string_to_hash.hexdigest()

print hashed_string
