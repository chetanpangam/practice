import xml.etree.cElementTree as etree

str_xml = "<feed xml:lang='en'> \
    <title>HackerRank</title> \
    <subtitle lang='en'>Programming challenges</subtitle> \
    <link rel='alternate' type='text/html' href='http://hackerrank.com/'/> \
    <updated>2013-12-25T12:00:00</updated> \
</feed>"

# tree= etree.ElementTree(etree.fromstring(str_xml))
tree = etree.parse('files/feed.xml')

root = tree.getroot()
print(root)

print(f"Root: {root.tag}")
print(f"Length : {len(root)}")

for child in root:
    print(f"Child : {child.tag}")

print(f"Root Attribute : {root.attrib}")
print(tree.findall('{http://www.w3.org/2005/Atom}author'))
print(tree.findall('.//{http://www.w3.org/2005/Atom}author'))


for element in root.iter():
    print(f"Tag : {element.tag}")
    if element.attrib:
        print(len(element.attrib))
        print(f"Atrributes: {element.attrib}")