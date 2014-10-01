#!/usr/bin/python
# -*-coding:utf-8*-

from optparse import OptionParser
parser = OptionParser()

from test42_def import test42
from test43_def import test43
from test44_def import test44
from test45_def import test45
from test46_def import test46

parser.add_option("-a", "--t42",action="store", type="int", help="excute_test42")
parser.add_option("-b", "--t43",action="store", type="int", help="excute_test43")
parser.add_option("-c", "--t44",action="store", type="int", help="excute_test44")
parser.add_option("-d", "--t45",action="store", type="int", help="excute_test45")
parser.add_option("-e", "--t46",action="store", type="int", help="excute_test46")

(options ,args) = parser.parse_args()

if options.t42 == 1:
	test42()
if options.t43 == 1:
	test43()
if options.t44 == 1:
	test44()
if options.t45 == 1:
	test45()
if options.t46 == 1:
	test46()
