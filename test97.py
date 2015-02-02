import xml.sax
import xml.sax.handler
import sys
import re

class Handler(xml.sax.handler.ContentHandler):
	def __init__(self):
		self.frag = False
		self.frag_category = False
		self.category = ""
	def startElement(self, name, attrs):
		if name == "title":
			self.frag = True
		if name == "text":
			self.frag_category = True

	def endElement(self, name):
		if name == "title":
			self.frag = False
		if name == "text":
			self.frag_category = False
	def characters(self, content):
		if self.frag:
			self.title_name = content
	#		print "title:" + content.encode("utf-8")
		if self.frag_category:
			re_category_pattern = re.compile(r"\{\{Commonscat\|(.+)\}\}")
			match = re_category_pattern.search(content)
			if match:
				print "title: " + self.title_name.encode("utf-8")
				print "english title: " + match.group(1).split("|")[0]
				print
def main():
	parser = xml.sax.make_parser()
	parser.setContentHandler(Handler())
	parser.parse(sys.argv[1])
	return
	
if __name__=="__main__":
	main()
