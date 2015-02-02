#!/usr/bin/python
#coding:utf-8

import sys
import argparse
import xml.sax
from xml.sax.handler import ContentHandler
def getArgs():
    # パーサーの生成
    parser = argparse.ArgumentParser(description="100本ノック91-100 xml")

    # オプション引数の追加
    parser.add_argument(
        "-f", "--file",
        dest="xml_file",
        required=True,
        help="xml形式のファイル"
    )
    return parser.parse_args()

class printNameHandler(ContentHandler):
    def __init__(self, writer=sys.stdout):
        self._writer = writer
        self._node = []
        ContentHandler.__init__(self)

    def startElement(self, name, attrs):
        self._node.append(name)

    def endElement(self, name):
        self._node.pop()

    _name_node = [u'built-in', u'type', u'name']
    def characters(self, data):
        if self._node == self._name_node:
            self._writer.write(u'%s\n' % data)
if __name__ == "__main__":
	args = getArgs()
	parser = xml.sax.make_parser()
	parser.setContentHandler(printNameHandler())
	parser.parse(open(args.xml_file))
