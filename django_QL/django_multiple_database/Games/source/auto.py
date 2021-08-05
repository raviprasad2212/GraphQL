pyfile = open('conf.py', 'r', encoding="utf-8")
lines = pyfile.readlines()
print(lines[16])


index_value = 17
with open('conf.py', 'r+') as fd:
        contents = fd.readlines()
        data = "import os\nimport sys\nimport sphinx_rtd_theme\nsys.path.insert(0, os.path.abspath('../..'))\nroot_dir = os.getcwd()\nremove_source = root_dir.strip('source')\nremove_doc = remove_source.strip('doc/')\nadd_modules = '/modules'\nget_module_path = remove_doc + add_modules"
        main_modules = "for r,d,f in os.walk(r'/{}'.format(get_module_path)):\n    sys.path.append(r)"
        contents.insert(index_value, data+"\n"+main_modules)  # new_string should end in a newline
        fd.seek(0)  # readlines consumes the iterator, so we need to start over
        fd.writelines(contents)  # No need to truncate as we are increasing filesize
        index_value = index_value+1


index_value = 99
with open('conf.py', 'r+') as fd:
        contents = fd.readlines()
        d = "html_theme = 'sphinx_rtd_theme'"
        contents.insert(index_value, d+"\n")  # new_string should end in a newline
        fd.seek(0)  # readlines consumes the iterator, so we need to start over
        fd.writelines(contents)  # No need to truncate as we are increasing filesize
        index_value = index_value+1









# print(get_module_path)

# #/home/ravi/Desktop/NewCRM/NX-CRMService/modules'
# for r,d,f in os.walk(r'/{}'.format(get_module_path)):
#     sys.path.append(r)