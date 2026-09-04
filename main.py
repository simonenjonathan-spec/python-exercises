x = 42
y = 13.37
text = "hello, world!"
isit = True
noitisnt = False
# boolean
none = None

ids = [1, 2, 3]
task = {"id": 1, "task": "chilla hela helgen"}

todos = [
    {"id": ids[0], "task": "åka tåg"},
    {"id": ids[1], "task": "chilla hela helgen"}
]

print("Saker jag behöver göra:\n")
for todo in todos:
    print(f"{todo["id"]}. {todo["task"]}")

#num = [1, 2, 3, 4, 5]
#for n in range(x):
#    num.append(n)
#print(num) 