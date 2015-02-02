#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import xml.sax, xml.sax.saxutils

base = xml.sax.saxutils.XMLGenerator
class SampleHandler4J(base):
    def startElement(self, tag, attrs):
        if tag != u'title':
            base.startElement(self, tag, attrs)
    def endElement(self, tag):
        if tag != u'title':
            base.endElement(self, tag)

file = open(sys.argv[1], "w")
xml.sax.parse('SampleS.xml', SampleHandler4J(file, 'utf-8'))
