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
			if s_element.attrib["id"] == "1":
				for ds_element in s_element.iter("dependencies"):
					if "type" in ds_element.attrib:
						if ds_element.attrib["type"] == "basic-dependencies":
							for g_element in ds_element.iter("governor"):
								if "idx" in g_element.attrib:
									if g_element.attrib["idx"] == "4":
										for d_element in g_element.getparent().iter("dependent"):
											print d_element.text
#	print build_text_list(root)
