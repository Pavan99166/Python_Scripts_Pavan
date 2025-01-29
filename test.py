mydict={
"name":"pavan",
"id":123,
"domain":["devops", "cloud engineer", "SRE"],
"tools":{"os":["linux", "windows"], "cloud":"aws"}
} 

print(mydict)
print(mydict["name"])
print(mydict["domain"])
print(mydict["domain"][1])
print(mydict["tools"]["os"])
print(mydict["tools"]["os"][0])
