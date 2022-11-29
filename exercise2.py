PUBLIC_G = 5
PUBLIC_P = 47

def get_public_key(secret):
    pass

def get_private_key(secret, public_key):
    pass

assert get_public_key(123) == 39
assert get_private_key(123, 2) == 21

assert get_public_key(302) == 16
assert get_private_key(302, 18) == 4

assert get_public_key(1502) == 36
assert get_private_key(1502, 18) == 6