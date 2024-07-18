from collections import UserDict

class Field: #Базовий клас для полів запису 
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):   #Клас для зберігання імені контакту. Обов'язкове поле.
    def __init__(self, value):
           self.value = value
           super().__init__(value)		              

class Phone(Field): #Клас для зберігання номеру телефона. Має валідацію формату.
		def __init__(self, phone_number):
                        if len(phone_number) != 10: # Лише 10 цифр
                               raise ValueError("Номер телефону має складатись з 10 цифр.") # В іншому випадку помилка
                        super().__init__(phone_number)
       
class Record: # Клас для зберігання інформації про контакт (ім'я та номер телефону).
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone): # додавання
           for phone in self.phones:
                  if phone.value == phone:
                         return
                  self.phone.append(Phone(phone))

    def remove_phone(self, phone): # видалення
           for phone in self.phones:
                  if phone.value == phone:
                         self.phones.remove(phone)
                         return 
                  raise ValueError
           
    def edit_phone(self, old_phone, new_phone): # зміна
           for phone in self.phones:
                  if phone.value == old_phone:
                         phone.value = new_phone
                         return
                  raise ValueError
           
    def find_phone(self, phone): # пошук
           for phone in self.phones:
                  if phone.value == phone:
                         return phone
                  raise ValueError

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict): # Клас для зберігання всіх контатів
       def __init__(self):
              self.data = {}
              super().__init__()

       def add_record(self, contact): # Метод додавання контакту
              self.data[contact.name.value] = contact

       def find(self,contact): # Метод для знаходження та перевірки контакту
              return self.data.get(contact)
       
       def delete(self, contact): # Метод для видалення контакту
              del self.data[contact.name.value]

       def __str__(self):
              return "\n".join(str(record) for record in self.data.values())