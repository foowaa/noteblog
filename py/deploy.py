import os

markdown_dir = r"../md"
base_dir = r"../public"
http_dir = r"../public/articles"
index_dir = r"../public/pages"

isExist_markdown = os.path.exists(markdown_dir)
isExist_base = os.path.exists(base_dir)
isExist_http = os.path.exists(http_dir)
isExist_index = os.path.exists(index_dir)


if not isExist_markdown:
	os.makedirs(markdown_dir)
if not isExist_base:
	os.makedirs(base_dir)
if not isExist_http:
	os.makedirs(http_dir)
if not isExist_index:
	os.makedirs(index_dir)
		
		

