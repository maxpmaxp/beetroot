print('NEW')
new_file = open('new_file2', 'w+')
new_file.write('abcdefg')
print(f'Cursor: Symbol #{new_file.tell()}')
new_file.write('\nabcdefg')
print(f'Cursor: Symbol #{new_file.tell()}')
new_file.seek(1)
new_file.write('456')
print(f'Cursor: Symbol after write #{new_file.tell()}')
print(new_file.read(3))
print(f'Cursor: Symbol after read #{new_file.tell()}')
new_file.write('456')
print(f'Cursor: Symbol after write #{new_file.tell()}')
new_file.close()





