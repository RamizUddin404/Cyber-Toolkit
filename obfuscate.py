import marshal, base64, zlib, os

def obfuscate(file_path):
    with open(file_path, 'r') as f:
        code = f.read()
    
    # Compilation and encoding
    # We add a header to maintain your branding even in the obfuscated file
    header = f"# ENCRYPTED BY: RAMIZ UDDIN ULTIMATE OBFUSCATOR\n# SOURCE PROTECTED. DO NOT TAMPER.\n"
    
    # Marshal -> Zlib -> Base64
    compiled_code = compile(code, '', 'exec')
    marshalled = marshal.dumps(compiled_code)
    compressed = zlib.compress(marshalled)
    encoded = base64.b64encode(compressed)
    
    obfuscated_code = header + f"import marshal,zlib,base64;exec(marshal.loads(zlib.decompress(base64.b64decode({encoded}))))"
    
    with open(file_path, 'w') as f:
        f.write(obfuscated_code)

def protect_all():
    print("[*] Starting Code Protection Process...")
    files = [f for f in os.listdir('.') if f.endswith('.py') and f not in ['obfuscate.py', 'cyber_deps.py']]
    for f in files:
        print(f"[+] Protecting: {f}")
        obfuscate(f)
    print("[!] All files protected successfully.")

if __name__ == "__main__":
    protect_all()
