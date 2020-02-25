import os
import shutil
def list_files(startpath):
   for root, dirs, files in os.walk(startpath): # корень, директории, файлы
       if dir!= '.git':
           level = root.replace(startpath, '').count(os.path.sep) # считает кол-во разделителей на моей оц(//)
           indent = ' ' * 4 * level # увеличивает табулярные оступы в level раз (зависит от кол-ва разделителей путей в пути)
           print('{}{}/'.format(indent, os.path.basename(root)))
           subindent = ' ' * 4 * (level + 1)
           for f in files:
               print('{}{}'.format(subindent, f))

print(os.getcwd())
os.chdir(r"C:\Users\Max\Documents\My Games\Sid Meier's Civilization 5")
print(list_files(os.getcwd()))
#https://dev-gang.ru/article/python-vvedenie-v-modul-os-ojxgrmcxi3/
