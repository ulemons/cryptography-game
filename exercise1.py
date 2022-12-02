bank = "ABCDEFGHIJKLMNOPQRSTUVWXYZ abcdefghijklmnopqrstuvwxyz,'?!.$*&0123456789@:+"


def encrypt(message, key):
    pass

def decrypt(message, key):
    pass
    
assert encrypt("test",2) == "vguv"
assert encrypt("encrypted message",42) == "+I@MTKO+:7H+NN8B+"
assert encrypt("This may result as very difficult message, also because as the length increase also the complexity to decrypt this message increases",144) == "PdeoWiXuWnaoqhpWXoWranuW ebbeZqhpWiaooXcawWXhokWYaZXqoaWXoWpdaWhajcpdWejZnaXoaWXhokWpdaWZkilhatepuWpkW aZnulpWpdeoWiaooXcaWejZnaXoao"


assert decrypt("vguv",2) == "test"
assert decrypt("+I@MTKO+:7H+NN8B+",42) == "encrypted message"
assert decrypt("PdeoWiXuWnaoqhpWXoWranuW ebbeZqhpWiaooXcawWXhokWYaZXqoaWXoWpdaWhajcpdWejZnaXoaWXhokWpdaWZkilhatepuWpkW aZnulpWpdeoWiaooXcaWejZnaXoao",144) == "This may result as very difficult message, also because as the length increase also the complexity to decrypt this message increases"
