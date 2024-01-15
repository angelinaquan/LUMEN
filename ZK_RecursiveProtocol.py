from Crypto_func import keccak_256

def recursive_protocol(args):
    print("------------------------------")
    print("[recursive_protocol]")
    return recursive_protocols(args)
def recursive_protocols(args):
    n = len(args)
    if n == 1:
        return args[0]
    else:
        mid = n // 2
        left = recursive_protocols(args[:mid])
        right = recursive_protocols(args[mid:])
        return keccak_256(str(left) + str(right))


#test
#print(recursive_protocol(["a", "b", "c", "d"]))


