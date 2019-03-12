import base64

f = open('xpdf.txt','w')

x = open('xpdf-tools-win-4.01.zip','rb').read()

b = base64.b64encode(x)

f.write(b.decode('utf8'))

f.close()