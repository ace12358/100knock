#!/usr/bin/python
#-*-coding:utf-8-*-

import sys 
import re
from test54 import *
re_marks = re.compile(u"[。、「」『』]|。")
dst = ""
srcs = ""
noun_cnt = 0 
verb_cnt = 0
not_stand_cnt = 0
text = main()
for sent in text:
        for Ch in sent:
                for w in Ch.morphs:
                        if w.pos == "名詞":
                                noun_cnt += 1
			if w.pos1 == "非自立":
                                not_stand_cnt += 1
                        if re_marks.search(w.surface.decode("utf-8")) is None:
                                        dst += w.surface
                for w in sent[Ch.dst].morphs:
			if w.pos == "動詞":
                                verb_cnt += 1
			if w.pos1 == "非自立":
                                not_stand_cnt += 1
                        if re_marks.search(w.surface.decode("utf-8")) is None:
                                srcs += w.surface
                if verb_cnt != 0 and noun_cnt != 0 and not_stand_cnt==0:
                        print dst + "\t" + srcs
                dst = ""
                srcs = ""
                noun_cnt = 0 
                verb_cnt = 0 
		not_stand_cnt = 0
