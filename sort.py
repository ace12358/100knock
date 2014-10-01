#!usr/bin/python
#-*-coding:utf-8-*-

def bublesort(list):
	n = len(list)
	for i in range(n, 0, -1):
		for j in range(1, i):
			if(list[j-1]>list[j]):
				temp = list[j-1]
				list[j-1] = list[j]
				list[j] = temp
	return list
def main():
	a = [5,4,3,2,1]
	print a
	bublesort(a)
	print a
if __name__ == "__main__":
	main()
