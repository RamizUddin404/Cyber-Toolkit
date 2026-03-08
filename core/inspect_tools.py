import marshal, zlib, base64, dis

def decode_and_inspect(encoded_str):
    data = base64.b64decode(encoded_str)
    decompressed = zlib.decompress(data)
    code_obj = marshal.loads(decompressed)
    print("--- Disassembly ---")
    dis.dis(code_obj)
    print("\n--- Constants ---")
    for i, const in enumerate(code_obj.co_consts):
        print(f"{i}: {const}")
    print("\n--- Names ---")
    for i, name in enumerate(code_obj.co_names):
        print(f"{i}: {name}")

print("Inspecting net_map.py:")
decode_and_inspect(b'eJyVUk9PE0EUn92d3ZaW+CeAGBAc8U9cjEYsmFARgxRjQ2hMFwyykM3STkpjd7uZbTXsRaMHe8QYox5MPHjRD+Bn8FilRDPh5sF4M/AFnJlSrGljwkvmzZvfm3nvzfu9H6BJ5L19N8HUS2AAQ5oFpL5LRDLkPkBkQ2FaafiWoQHjiwDYYQCWlSEwthcCgZyUk3T1Fz+kMlJTFpUthWf5KLKY+460DFpkiOUZkxoxTbWBG3JbVFkA6VBrlEZVh0Cs/TvYFlX/ojmgaymqZgrYJsFovzlyLXbVuX4QCTQkJBio79Ppman5mQS6eS+O0lNzySW0kEgkU8HIgaL2m5cdHVK56FPNX/dL2KGqR/Juiaplz8NElyh0bQf7/CeIAhotFYsFaw3bWUxIlIGQLX+SqcdgG2rPkk+SlVwNHtuGHdXIyRpEzKjc2hh9FX8efzGxcakaOVWDQ8Kr1+CwME5swYFd3qdMc9P3ef5U53l/Bgw2SYYyLqNmrJkBpZUBQxNT1s2skAFm5eJ/eeZ8meEGmo603mRzFW6bseMfziOpICrIvuKYwyuI8EispQp2s0E/R1K49LBI7qM520Pnp9J30Ly9WsB6oBkZ272BqDw+TvhYB5pNPHTRDkLmjFvCZEXXCP8AVfOuVy7RSGZ9FRMriz2fRgl2ig+wOBDeRaKJtOQop0oQKQqhCim7pItZndwxvcchI6TvnfwVnn6/UL1wu3Y2uR3qrCw+ffT6zGZocBONfIslv8SStdjs57sNwtdqsJfzrG/BbsKD0bBlOXbetSxdFSVQWMo7WAyMyMgv8LmyrA9AvKhXFJ5witlyAU+S4+zIS/XPMfVbkSTpJzi8A1VpcOcIlHp2I0CKfFeilaVNpfdN19ueqtIr4vwBXYHbQw==')

print("\n\nInspecting local_map.py:")
decode_and_inspect(b'eJyVUs9PE0EUnt2d3ZYt/gogBgRX1MTFaMSCCRUxQDFpkB66YpCFbNZ2Uhq7PzK71bAXjR7sEWOMejDx4EX/AP8Gj1WWmGy4eTDeCPwDzkxprWljwkt25r1vZt57+77vJ2gx/mDfT5PlNdCAxi0AXN85zGn8AMB8ExVIJKxCDaaWATDjAKwKI2DiIIUCilyRU8XfNMjmuZYqIvkEWuUzq6I3D3I8aLMRUm2Ca+TUxQau8R1RYQnkYu1ZGl0dBcnO72BHVPyLFoEqZSMxX0YmDsYH9bEbyevWzcNYICnMgqH6Ppebn7k7n1Zm76eU3MxiZkVZSqcz2WDsUFkH9auWCiPe8SLJ2/B8ZEWii0u2H4kV10VY5SJomxby6J8oEYgSvuOUjXVkFhDGCQJC8nnTZHkKdqD0IvMsUy2G8OQO7KrJZ0KoEKd6e3P8Tepl6tXU5pWafDaEI+xUDeEoc05vw6F9Oqd869CbPH+p89zUgEaUpAmTvNKKtTIgtDOgSUxlvcSLaWCBd/7LM+VLjzfQnNx+k+gq3rFi1z+cy9kgwci+ZumjawqmmchIBWQXgj6K3HHyZlnJIv+xgx8qi6YbSFretG8pET85iamgA8nErnLZDGL6vO0jvKZKmLYeiSXbrfiRnN94gLBRQK4XJTCynEeIBZjOD0usID5BSWIUshYiAVds3EO8I/Rg7oA9QsXAB/47PPdxqXZpNrwwtxPrri4/f/L2/FZseEsZ+5HMfEtmwuTC13sNqtdD2E8ZVrdhL+6mqeOGYZkl2zBUkbUQQb9kISYVVpFeoIoyjE+Avah3FJ+ynEKljKbxKRLSVr2LZNkVOI77BY7tQZEb3j8OOHmPh1zfrgxgd3VlS+h/1/O+ryb0s0x/AEBb2f8=')
