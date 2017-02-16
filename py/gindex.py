#python3 code
#md2html.py
import mistune
import codecs
from http.server import SimpleHTTPRequestHandler
import socketserver
import json
import math
import os
import shutil

with open('../config/config.json','r') as config_file:
    config = json.load(config_file)
    items_of_every_page = config['items_of_every_page']
    css = config['css']
    blog_title = config['title']

titles = []
descriptions = []
links = []
with open('../config/index','r', encoding = 'utf8') as f:
	n = 0
	while True:
		line  = f.readline().strip('\n')
		if not line:
			break
		if line != '---':
			n += 1
			if (n%3) == 1:
				titles.append(line)
			elif (n%3) == 2:
				descriptions.append(line)
			else:
				links.append(line)
		else:
			pass

	if n == 0:
		raise Exception('No enough items in index!')
	if (n%3) != 0:
		raise Exception("The number of titles, descriptions and links mismatches!")

number_of_md = math.ceil(n/(3.0*items_of_every_page))
pages, remainder = divmod(n/3, items_of_every_page)


for i in range(number_of_md):
	with open(os.path.join('../md/',str(i)+'.md'), 'w', encoding = 'utf8') as f:
		f.write("<title>%s</title>\n"%blog_title)
		f.write("## %s\n"%blog_title)
		if i<pages:
			items_of_the_page = items_of_every_page
		else:
			items_of_the_page = int(remainder)
		for j in range(items_of_the_page):
			f.write("### [%s](%s)\n"%(titles.pop(), links.pop()))
			f.write("%s\n"%descriptions.pop())
		if number_of_md != 1:
			if i == 0:
				f.write("\n")
				f.write("* [Next](/pages/1)")
			elif i != number_of_md-1:
				f.write("\n")
				f.write("* [Next](/pages/%d\n"%(i+1))
				f.write("\n")
				f.write("* [Prev](/pages/%d\n"%(i-1))
			else:
					if number_of_md == 2:
						f.write("\n")
						f.write("* [Prev](/)")
					else:
						f.write("\n")
						f.write("* [Prev](/pages/%d)"%(i-1))


mk = mistune.Markdown()
if os.path.exists('../public/pages'):
	shutil.rmtree('../public/pages/')
	os.makedirs('../public/pages')
else:
	os.makedirs('../public/pages')
for i in range(number_of_md):
	with open(os.path.join('../md/',str(i)+'.md'),'r', encoding='utf8') as f1:
		s = f1.read()
		html = mk(s)
		os.makedirs(os.path.join(r'../public/pages', str(i)))
		with open(os.path.join('../public/pages/',str(i), 'index.html'), 'w', encoding = 'utf8') as f2:
			f2.write(html)
			with open(css, 'r') as css_file:
				css_content = css_file.read()
				f2.write('<style>'+css_content+'</style>')
shutil.move("../public/pages/0/index.html", "../public/index.html")

os.chdir('../public')
PORT = 8888
Handler = SimpleHTTPRequestHandler
httpd = socketserver.TCPServer(("",PORT), Handler)
print("Successful!")
httpd.serve_forever()

