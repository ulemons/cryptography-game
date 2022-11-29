def encrypt(message, key):
    pass

def decrypt(message, key):
    pass

assert encrypt("test",2) == "vguv"
assert encrypt("encrypted message",42) == "CLAPWNRCB7KCQQ8EC"
assert encrypt("This may result as very difficult message, also because as the length increase also the complexity to decrypt this message increases",144) == "Vjkuboc,btguwnvbcubxgt,bfkhhkewnvboguucig?bcnuqbdgecwugbcubvjgbngpivjbkpetgcugbcnuqbvjgbeqorngzkv,bvqbfget,rvbvjkuboguucigbkpetgcugu"


assert decrypt("vguv",2) == "test"
assert decrypt("CLAPWNRCB7KCQQ8EC",42) == "encrypted message"
assert decrypt("Vjkuboc,btguwnvbcubxgt,bfkhhkewnvboguucig?bcnuqbdgecwugbcubvjgbngpivjbkpetgcugbcnuqbvjgbeqorngzkv,bvqbfget,rvbvjkuboguucigbkpetgcugu",144) == "This may result as very difficult message, also because as the length increase also the complexity to decrypt this message increases"