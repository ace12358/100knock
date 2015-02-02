import xml.sax
import xml.sax.handler
import sys

class Handler(xml.sax.handler.ContentHandler):
	def __init__(self):
		self.frag = False 
	def startElement(self, name, attrs):
		if name == "title":
			self.frag = True

	def endElement(self, name):
		if name == "title":
			self.frag = False
		
	def characters(self, content):
		if self.frag:
			print content

def main():
	parser = xml.sax.make_parser()
	parser.setContentHandler(Handler())
	parser.parse(sys.argv[1])
	return
	
if __name__=="__main__":
	main()
