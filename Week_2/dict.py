cat=dict(name="kitty",age=5)
print(cat)

cat={"name":"kitty","age":5}
print(cat)

cat={"name":"kitty","age":5}
print(cat['name'])
print(cat.get("name"))
print(cat.get("gender","Not found"))

cat['age']=7
 print(cat['age'])

cat.pop('age')
print(cat)

for i,j in cat.items():
    print(i,j)
