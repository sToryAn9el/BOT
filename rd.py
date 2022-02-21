#!/usr/bin/python

def banner():
	print '====================================================='
	print '|!!|	     Duplicate Entry Remover		|!!|'
	print '|!!|	        It is Me ZeeX_IND		|!!|'
	print '====================================================='

banner()
	
inpt=raw_input('Masukin List bang :')
oupt=raw_input('Masukin nama result bang :')
	
if __name__ == '__main__':
	f = open(oupt,'w+')
	flag = False
	print 'Wait bentar cok..'
	with open(inpt) as fp:
		for line in fp:
			for temp in f:
				if temp == line:
					flag = True
					print('Duplicate Found.. Removing This Shit..!!')
					break
			if flag == False:
				f.write(line)
			elif flag == True:
				flag = False
			f.seek(0)
		f.close()
print '.../done'
