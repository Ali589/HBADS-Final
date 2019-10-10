import xml.etree.ElementTree as ET
tree = ET.parse('zxc.xml')

def brightness():
    root = tree.getroot()
    x = root[0][1].text
    return str(x)

def contrast():
    ro = tree.getroot()
    y = ro[1][1].text
    return str(y)
def saturation():
    roo = tree.getroot()
    z = roo[2][1].text
    return str(z)

def confirm(a,b,c):
    root = tree.getroot()
    root[0][1].text = str(a)
    root[1][1].text = str(b)
    root[2][1].text = str(c)
    tree.write('zxc.xml')