import hashlib as hl
m = hl.sha256()

# m.update(b"21ME10093")
# str = m.hexdigest()

# secretId = str[len(str)-6:]

with open('secret-id.txt') as file:
    secretIds = [line.rstrip() for line in file]

