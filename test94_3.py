import xml.sax
import xml.sax.handler
import sys

class Handler(xml.sax.handler.ContentHandler):
	def startElement(self, name, attrs):
		print "Start: " + name

	def endElement(self, name):
		print "End: " + name
		
	def characters(self, content):
		print "character:" + content
		return

def main():
	parser = xml.sax.make_parser()
	parser.setContentHandler(Handler())
	parser.parse(sys.argv[1])
	return
	
if __name__=="__main__":
	main()
