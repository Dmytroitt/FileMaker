import os
print('#+'*12)
print('File maker')
print('#+'*12)
nomeArq = str(input('File names: '))
extencArq = str(input('Extension[EX: py,txt]: '))
quantArq = int(input('Number of files: '))
contador = 0
for c in range(0,quantArq):
	os.system(f'touch {nomeArq}{c}.{extencArq}')
	contador = contador + 1
	print(f'did {contador} files')
