import random
import string

class GeneratorsUtils:
    def __init__(self):
        pass
    
    def id_client_generator(self):
        randomints = "".join(random.choice(string.digits ) for _ in range(7))
        randomstrs = "".join(random.choice(string.ascii_uppercase) for _ in range(1))
        generate = f"AP{randomstrs}{randomints}"
        return generate
    
    def id_account_generator(self):
        randomints = "".join(random.choice(string.digits ) for _ in range(9))
        randomstrs = "".join(random.choice(string.ascii_uppercase) for _ in range(3))
        generate = f"N{randomstrs}{randomints}"
        return generate