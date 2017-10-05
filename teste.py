#!/usr/bin/env python
# Não esqueçam de colocar no diretório para cgi e dar
# direito de execução
import sys
print 'Content-type: text/plain\n'
print sys.version
print '\nPath das bibliotecas:'
print '\n'.join(sys.path)
