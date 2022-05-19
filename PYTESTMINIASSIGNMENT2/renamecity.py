print("Rename key city to location in the following dictionary: ")
sampleDict = {

  "name": "Kelly",

  "age":25,

  "salary": 8000,

  "city": "New york"

}
value=sampleDict["city"]
del sampleDict["city"]
sampleDict["location"]=value
print(sampleDict)
print()
