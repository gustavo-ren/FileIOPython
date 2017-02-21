'''
Created on 28 de jan de 2017

@author: Gustavo
'''
arq=open("C:\\Users\\Gustavo\\Desktop\\v2.txt", "w+")

arq.write("Who wants to be king")
print(arq.closed)
arq.close()
print (arq.closed)