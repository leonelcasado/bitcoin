#!/usr/bin/env python
# N�o esque�am de colocar no diret�rio para cgi e dar
# direito de execu��o
import sys
print 'Content-type: text/plain\n'
print sys.version
print '\nPath das bibliotecas:'
print '\n'.join(sys.path)
