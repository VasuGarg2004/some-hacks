import json
import hashlib as hl
m = hl.sha256()

# Get the secret Ids to a list
with open('secret-id.txt') as file1:
    secretIds = [line.rstrip() for line in file1]

# Get possible dep codes to a list
with open('dep.txt') as file2:
    deps = [line.rstrip() for line in file2]

# define output dict
validSecretIds = {}

# run a loop over deps for rolls in given range
for dep in deps:
    for i in range(10001-10200, 20001-20200, 30001-30200):
        # concatenate roll number and find last 6 digits of sha256 hash
        m.update(b"21" + dep + i)
        str = m.hexdigest()

        sid = str[len(str) - 6:]

        # Verify against given list to approve roll as well as ID and store them in dict
        for secretId in secretIds:
            if sid == secretId:
                validSecretIds["21" + dep + i] = secretId

# output obtained data
with open("Valid-Secret-Ids.json", "w") as outfile:
    json.dump(validSecretIds, outfile)