import os

name = os.environ["USERNAME"]
print(name)
system=os.environ["COMPUTERNAME"]
print(system)
vari=os.environ.get("Gond")
print(vari)
unknown=os.environ["Gond"]
print(unknown)

