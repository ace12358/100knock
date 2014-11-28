import kyotocabinet as kc
import sys
from collections import defaultdict

class KyotoCabinet(kc.DB):
    def __del__(self):
        self.close()

    def open(self, *args, **kwds):
        if not super(KyotoCabinet, self).open(*args, **kwds):
            raise IOError("Open error: {0}".format(super(KyotoCabinet, self).error()))

    def set(self, *args, **kwds):
        if not super(KyotoCabinet, self).set(*args, **kwds):
            raise IOError("Set error: {0}".format(super(KyotoCabinet, self).error()))

    def close(self, *args, **kwds):
        if not super(KyotoCabinet, self).close(*args, **kwds):
            raise IOError("Close error: {0}".format(super(KyotoCabinet, self).error()))

    def cursor(self, *args, **kwds):
        cur = super(KyotoCabinet, self).cursor(*args, **kwds)
        cur.jump()
        while 1:
            rec = cur.get_str(True)
            if not rec: break
            yield rec
        cur.disable()


if __name__ == "__main__":

    db = KyotoCabinet()
    db.open("sample.kch", kc.DB.OWRITER | kc.DB.OCREATE)
    for line in open(sys.argv[1]):
        itemList = line.strip().split("\t")
        bigram = (itemList[1], itemList[2])
        #bigram = " ".join(itemList[1:3])
        prob = float(itemList[0])
        #print bigram,prob
        db.set(bigram, prob)

    dic = defaultdict(lambda:0.0)
    for rec in db.cursor():
        db_bigram= str("%s %s") %(rec[0].split("', '")[0][2:], rec[0].split("', '")[1][:-2])
        dic[db_bigram] = float(rec[1])

    sentences = sys.stdin.readlines()

    for sent in sentences:
        score = 1.0
        tok_list = sent.strip().split()
        for i in range(len(tok_list)-1):
            bigram = u"%s %s" %(tok_list[i],tok_list[i+1])
            bigram = bigram.strip()
            score *= dic[bigram]
        print score
