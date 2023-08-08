
acronyms = {"LOL": "laugh out loud", "IDK": "I dont know", "TBH": "to be honest"}

acronyms['SMH'] = "So much hate"

del acronyms["LOL"]

definition = acronyms.get("BTW")

if definition:
    print(definition)
else: 
    print("Key doesn't exist")

sentence = "IDK" + " what happened " + "TBH"
translation = acronyms.get("IDK") + " what happened " + acronyms.get("TBH")

print(sentence)
print(translation)