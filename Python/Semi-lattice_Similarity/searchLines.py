# -*- coding: utf-8 -*-
'''
Created on 9 mars 2016

@author: virgilt
'''

import regularExpression as regex
import sys

#créer un fichier pour chaque mot placer en attribut. SI une expression est recherchée, il faut utiliser :
#'une expression'
regex.rechercherMots(sys.argv[1:])
