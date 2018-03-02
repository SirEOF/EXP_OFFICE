import sys
if sys.argv[1]:
	f = open('tmp.txt','r')
	s = f.read()
	f.close()
	newtx = s.replace('UURRLL',sys.argv[1])
	f = open('1.txt','w')
	f.write(newtx)
	f.close()
else:
	print 'please choose a domain'