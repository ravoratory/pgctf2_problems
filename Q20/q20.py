import random
from string import ascii_letters, digits

def encode(r: str) -> str:
    random.seed(len(r))
    t1 = f"{ascii_letters}{digits}_{{}}"
    t2 =  ''.join(random.sample(t1, len(t1)))
    return ''.join(map(lambda s: t2[t1.find(s)], list(r)))


def decode(c: str) -> str:
    # Let's implement!
    return ''
