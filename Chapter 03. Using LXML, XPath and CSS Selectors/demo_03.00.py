from lxml import etree

xml = open("food.xml", "rb").read()
tree = etree.XML(xml)

print(f"=>> {tree}")
print("_"*20)
print(f"=>> {type(tree)}")
print("_"*20)

for element in tree.iter():
    print(f"    =>> {element.tag} - {element.text}")