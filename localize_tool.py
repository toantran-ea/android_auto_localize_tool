#!/usr/bin/python
# -*- coding: UTF-8 -*-

# The MIT License (MIT)

# Copyright (c) 2015 @ Toan Tran

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

"""This script is to make the life of Android developer much easier when doing localization for apps."""


__author__ = 'Toan Tran'
__copyright__   = "Copyright 2015, Toan Tran"

import os
import sys
import xml.etree.ElementTree as ET
import goslate
import codecs
from xml.dom.minidom import parseString


EXCEPTION_LIST = ('°',)
SUPPORT_LANG_CODES = ('af', 'sq', 'ar', 'az', 'eu', 'bn', 'be', 'bg', 'ca', 'zh-CN', 'zh-TW', 'hr', 'cs', 'da', 'nl', 'en', 'eo', 'et', 'tl', 'fi', 'fr', 'gl', 'ka', 'de', 'el', 'gu', 'ht', 'iw', 'hi', 'hu', 'is', 'id', 'ga', 'it', 'ja', 'kn', 'ko', 'la', 'lv', 'lt', 'mk', 'ms', 'mt', 'no', 'fa', 'pl', 'pt', 'ro', 'ru', 'sr', 'sk',
 'sl', 'es', 'sw', 'sv', 'ta', 'te', 'th', 'tr', 'uk', 'ur', 'vi', 'cy', 'yi',)

def load_strings_file(language_code):
	tree = ET.parse('strings.xml')
	root = tree.getroot()
	translated_resources_root = ET.Element("resources")
	untransalated_resources_root = ET.Element("resources")
	for child in root:
		if child.text is not None  and  child.text.encode('utf-8') not in EXCEPTION_LIST:
			try:
				translated_text = translate_to(child.text.encode('utf-8'), language_code)
				name = child.attrib['name']
				print name, '-->', translated_text
				ET.SubElement(translated_resources_root, tag="string", name=name).text = translated_text
			except:
				ET.SubElement(untransalated_resources_root, tag="string", name=name).text = child.text.encode('utf-8')
				print ">>>>>>>> can not translate text " + child.text.encode('utf-8')

	to_file(translated_resources_root, 'translated_strings.xml')
	to_file(untransalated_resources_root, 'untranslated_strings.xml')

			
def to_file(root_element, output_xml_file_name):
	xmlstr = parseString(ET.tostring(root_element, encoding='utf-8')).toprettyxml(indent="   ")
	with codecs.open('temp.xml', 'w', 'utf-8') as f:
		f.write(xmlstr)
	temp_out_tree = ET.parse("temp.xml")
	os.remove('temp.xml')
	temp_out_tree.write(output_xml_file_name,encoding='utf-8', xml_declaration=True,method='xml')

def translate_to(text, lang_code):
	gs = goslate.Goslate()
	return gs.translate(text, lang_code)

def validate_lang_code(language_code):
	return language_code in SUPPORT_LANG_CODES

if __name__ ==  '__main__':
	# accept only 1 argument as language code to translate into
	if len(sys.argv) != 2:
		print "Usage: python localize_tool.py <target_language_code>\n" + "For example: python localize_tool.py en \n" + "The result will be 2 files named <translated_strings.xml> and <untranslated_strings.xml>."
		exit(1)
	else:
		target_language_code = sys.argv[1]
		if validate_lang_code(target_language_code):
			load_strings_file(target_language_code)
		else:
			print "Invalid language code provided: " + target_language_code
