import os
print('#+'*12)
print('Criador de arquivos')
print('#+'*12)
nomeArq = str(input('Nome dos arquivos: '))
extencArq = str(input('Extenção[EX: py,txt]: '))
quantArq = int(input('Quantidade de arquivos: '))
contador = 0
for c in range(0,quantArq):
	os.system(f'touch {nomeArq}{c}.{extencArq}')
	contador = contador + 1
	print(f'{contador} arquivos criados')
