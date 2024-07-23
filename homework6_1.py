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
	def __init__(self, phone_number:str):
              if not phone_number.isdigit() or len(phone_number) != 10: # Лише 10 цифр
                      raise ValueError("Номер телефону має складатись з 10 цифр.") # В іншому випадку помилка
              super().__init__(phone_number)
       
class Record: # Клас для зберігання інформації про контакт (ім'я та номер телефону).
       def __init__(self, name: str):
            self.name = Name(name)
            self.phones = []

       def add_phone(self, phone: str) -> None: # додавання
              self.phones.append(Phone(phone))

       def remove_phone(self, phone): # видалення
              for number in self.phones:
                     if number.value == phone:
                          self.phones.remove(number)
                          return 
              raise ValueError
           
       def edit_phone(self, phone:str, new_phone:str) -> None: # зміна
              for number in self.phones:
                     if number.value == phone:
                           number.value = new_phone
                           return
              raise ValueError("Номер телефону не знайдено.")
           
       def find_phone(self, phone): # пошук
              for number in self.phones:
                     if number.value == phone:
                         return phone
              raise ValueError("Номер телефону не знайдено.")

       def __str__(self):
           return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict): # Клас для зберігання всіх контатів

       def add_record(self, record: Record): # Метод додавання контакту
              name = record.name.value
              self.data.update({name: record})

       def find(self,name): # Метод для знаходження та перевірки контакту
              return self.get(name)
       
       def delete(self,name): # Метод для видалення контакту
              del self[name]

       def __str__(self):
              return "\n".join(str(record) for record in self.data.values())
       
