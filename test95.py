import xml.sax
import xml.sax.handler
import sys

class Handler(xml.sax.handler.ContentHandler):
	def __init__(self):
		self.frag = False
		self.title_name = "" 
	def startElement(self, name, attrs):
		if name == "redirect":
			print self.title_name.encode("utf-8") + "\t" + attrs.getValue("title").encode("utf-8")
		if name == "title":
			self.frag = True

	def endElement(self, name):
		if name == "title":
			self.frag = False
		
	def characters(self, content):
		if self.frag:
			self.title_name = content
		#	print content

def main():
	parser = xml.sax.make_parser()
	parser.setContentHandler(Handler())
	parser.parse(sys.argv[1])
	return
	
if __name__=="__main__":
	main()
