import json

# create a simple JSON array
jsons = '{"key1":"value1","key2":"value2","key3":"value3"}'

# change the JSON string into dict
jsonObject = json.loads(jsons)
print(type(jsonObject))
# print the keys and values
for key in jsonObject:
    value = jsonObject[key]
    print("The key and value are {} = {}".format(key, value))
