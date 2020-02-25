#Создайте собственную программу «Адресная книга», работающую из командной строки и позволяющую просматривать, добавлять, изменять, удалять или искать контактные
#данные ваших знакомых. Кроме того, эта информация также должна сохраняться на диске для последующего доступа.
#Это достаточно простая задача, если думать о ней в терминах, которые мы до сих пор
#проходили
import shelve
class Address_book():
    data = {}
    def __init__(self,name,phone):
        self.name = name
        self.phone = phone
        Address_book.data[name] = phone
    def adding(self):
        cortage = shelve.open('adbook')
        Address_book.data[self.name] = self.phone
        cortage[self.name] = self.phone
        cortage.close()
    @staticmethod
    def show():
        cortage = shelve.open('adbook')
        for i in cortage.items():
            print(i)
        cortage.close()
    @staticmethod
    def get():
        cortage = shelve.open('adbook')
        name = input("Чей номер нужен?: ")
        print(cortage[name])
        cortage.close()
    @staticmethod
    def delete(): # self здесь не нужен, так как staticmethod не принимает никаких обязательных аргументов, по типу объекта класса или самого класса.
        cortage = shelve.open('adbook')
        name = input("Кого удалить?: ")
        if name.lower() == 'никого':
            pass
        else:
            del cortage[name]
    @staticmethod
    def change():
        cortage = shelve.open('adbook')
        name,number_phone = input("Чей номер поменять?: "), int(input("Номер: "))
        cortage[name] = number_phone
        cortage.close()
Address_book('Maxim', 79069739733).show()
# Готово!