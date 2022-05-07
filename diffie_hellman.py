p = int(input("Enter Prime Number (p): "))
q = int(input("Enter Primitive root of p (q): "))
a = int(input("Choose Private Key for Alice: "))
b = int(input("Choose Private Key for Bob: "))

A = q**a % p
B = q**b % p

S_a = B**a % p
S_b = A**b % p

if S_a == S_b:
    print("ALice and Bob can communicate with each other!!!")
    print(f"They share a secret no = {S_a}")
else:
    print("ALice and Bob cannot communicate with each other!!!")