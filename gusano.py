# primer argumento es el archivo y el segundo numero de copias. ['gusano.py', '2']

import shutil
import sys

if len(sys.argv) == 2:
    for num in range(0, int(sys.argv[1])):
        shutil.copy(sys.argv[0], sys.argv[0] + f'{num}.py')

else:
    print('Envia dos parametros')

# python gusano.py + numero de veces asi es como se ejecuta este programa
