#!/usr/bin/python
# -*- coding: UTF-8 -*-

# This script is to make the life of Android developer much easier when doing localization for apps.

import goslate
import xml.etree.ElementTree as ET
from xml.dom.minidom import parseString

EXCEPTION_LIST = ('°',)

def load_strings_file():
	tree = ET.parse('strings.xml')
	root = tree.getroot()
	translated_resources_root = ET.Element("resources")
	untransalated_resources_root = ET.Element("resources")
	for child in root:
		if child.text is not None  and  (child.text.encode('utf-8') not in EXCEPTION_LIST):
			try:
				translated_text = translate_to_english(child.text.encode('utf-8'))
				name = child.attrib['name']
				print name, '-->', translated_text
				ET.SubElement(translated_resources_root, tag="string", name=name).text = translated_text
			except:
				print ">>>>>>>> can not translate text " + child.text.encode('utf-8')
	xmlstr = parseString(ET.tostring(translated_resources_root, encoding="utf-8")).toprettyxml(indent="   ")
	with open("a_strings.xml", "w") as f:
		f.write(xmlstr.encode("utf-8"))

			

def translate_to_english(text):
	gs = goslate.Goslate()
	return gs.translate(text, 'en')

if __name__ ==  '__main__':
	load_strings_file()
