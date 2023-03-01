new_file= open('fails.txt', 'w', encoding='utf-8')
new_file.write('python')
new_file.close()


new_file= open('fails.txt', 'w', encoding='utf-8')
file_content = new_file.read()
print(file_content)

new_file.close()




file = open('data.txt', 'w')
file.write('kaut kas')
file.close()