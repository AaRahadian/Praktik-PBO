from template_engine import \
    parse_template, \
    compile_template

fl = open('dokumen/template.html','r')
template_text = fl.read()
fl.close()

data_parameter = {
    'nama' : 'Muhamad Rahadian Santoso',
    'buah': ['Jeruk', 'Semangka', 'Durian']
}

# Kompilasi template
tokens = parse_template(template_text)

output = compile_template(tokens, data_parameter)
print(output)