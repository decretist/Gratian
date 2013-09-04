#! /usr/bin/python
#
# Paul Evans (10evans@cardinalmail.cua.edu)
# 4 September 2013
#
import xml.etree.ElementTree as ET
def main():
    tree = ET.parse('./bsb00009126.xml')
    root = tree.getroot()
    for child in root:
        print child.tag, child.attrib
    header = root[0]
    for child in header:
        print child.tag, child.attrib
    for lg in root.iter('lg'): # <lg> (line group)
        print lg.tag, lg.attrib, lg.text
    ET.dump(header)
if __name__ == '__main__':
    main()
