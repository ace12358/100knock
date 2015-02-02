#!/usr/bin/python
# coding:utf-8

import sys
import argparse
from lxml import etree

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


if __name__ == "__main__":
	args = getArgs()
	tree = etree.parse(args.xml_file)
	root = tree.getroot() # ルート要素を取得(Element型)
	#print etree.tostring(tree)

	#タグをとテキストをすべて表示
	for s_element in root.iter("sentence"):
		if "id" in s_element.attrib:
			if s_element.attrib["id"] == "2":
				for w_element in s_element.iter("token"):
					if "id" in w_element.attrib:
						if w_element.attrib["id"] == "5":
							for t_element in w_element.iter("word"):
								print t_element.text

	build_text_list = root.XPath("//text()")
#	print build_text_list(root)
