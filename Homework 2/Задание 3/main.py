text_list = ['1.txt', '2.txt', '3.txt']

text_read = {}
text_lines = {}
out_text_List = []
for text_file in text_list:
    with open(text_file, 'rt', encoding='utf8' ) as t:
        text = t.read()
        lines = text.count('\n') + 1
        text_lines[text_file] = lines

for text_file in text_list:
    with open(text_file, 'rt', encoding='utf8' ) as t:
        text_read[text_file] = t.read()

sorted_text_line = {}
sorted_key_text_line = sorted(text_lines, key=text_lines.get)

for i in sorted_key_text_line:
    sorted_text_line[i] = text_lines[i]

for num_text in sorted_text_line.keys():
    out_text_List.append(f'{num_text}\n{sorted_text_line[num_text]}\n{text_read[num_text]}')

out_text = "\n".join(out_text_List)

with open("out_text.txt", 'w', encoding='utf8' ) as doc:
    doc.write(out_text)