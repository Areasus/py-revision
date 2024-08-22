import json

# x =  '{ "name":"Santosh G.C.", "age":26, "address":"LaMACHAUR 19"}'
x = { "name":"Santosh G.C.", "age":26, "address":"LaMACHAUR 19"}

# parse x:
# convert into JSON:
y = json.dumps(x)  #converts into json
# y = json.loads(x)  #parse json

# the result is a Python dictionary:
print(y)
# print(y["age"])

try:
  print(x)
except:
  print("Something went wrong")
finally:
  print("The 'try except' is finished")