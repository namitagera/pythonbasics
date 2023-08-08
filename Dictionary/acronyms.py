acronyms = ["LOL", "IDK", "SMH"]
acronyms.append("BFN")
acronyms.append("IMHO")
acronyms.remove("IDK")
del acronyms[3]

if "LOL" in acronyms:
    print("Wors is in the list")
else:
    print("Word is not in the list")

print(acronyms)

for acronym in acronyms:
    print(acronym)


