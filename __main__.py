'''
Created on Feb 29, 2024

Created by: ZhengLinLei
'''

from tool.RSAwienerHacker import hack_RSA
from tool.RSAvulnerableKeyGenerator import generateKeys
import argparse
import sys


if __name__ == "__main__":
    if len(sys.argv) < 2 or sys.argv[1] not in ["crack", "generate"]:
        print("Example of use: python {} [crack|generate]".format(sys.argv[0]))
        exit(-1)

    if sys.argv[1] == "generate":
        print("\n ==== Generating RSA keys ==== \n\n")
        loop = 1
        bits = 1024

        if len(sys.argv) >= 3:
            bits = int(sys.argv[2])
        if len(sys.argv) == 4:
            loop = int(sys.argv[3])

        for i in range(loop):
            e,n,d = generateKeys(bits)
            print ("-------- Public Key --------")
            print("e =")
            print(e)
            print("-")
            print("n =")
            print(n)
            print("-")
            print ("--------- Private Key --------")
            print("d =")
            print(d)
            print("-----------------------")
        exit(0)


    parser = argparse.ArgumentParser()
    parser.add_argument('crack', help='crack')
    parser.add_argument('-c', help='Cypher text')
    parser.add_argument('-e', help='Public key', required=True)
    parser.add_argument('-n', help='N', required=True)
    args = parser.parse_args()
    try:
        c = int(args.c) if args.c is not None else None
        e = int(args.e)
        n = int(args.n)
    except:
        print("Error parsing arguments: Type -h for help.")
        exit(-1)
        
    d = hack_RSA(e, n)

    if d is not None:
        print("Private key: ", d)
    else:
        print("Wiener attack failed.")
    
    if c is None:
        exit(0)

    decrypted_m = pow(c, d, n)

    print("Decrypted message: ", decrypted_m)
