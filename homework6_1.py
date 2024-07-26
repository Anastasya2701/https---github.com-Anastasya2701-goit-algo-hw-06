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
	def __init__(self, phone):
              if not phone.isdigit() or len(phone) != 10: # Лише 10 цифр
                      raise ValueError("Номер телефону має складатись з 10 цифр.") # В іншому випадку помилка
              super().__init__(phone)
       
class Record: # Клас для зберігання інформації про контакт (ім'я та номер телефону).
       def __init__(self, name):
            self.name = Name(name)
            self.phones = []

       def add_phone(self, phone): # додавання
              self.phones.append(Phone(phone))

       def remove_phone(self, phone): # видалення
              for number in self.phones:
                     if number.value == phone:
                          self.phones.remove(number)
                          return 
              raise ValueError
           
       def edit_phone(self, old_phone, new_phone): # зміна
              for number in self.phones:
                     if number.value == old_phone:
                         number = Phone(new_phone)
                         break
                     else:
                         raise ValueError
           
       def find_phone(self, phone): # пошук
              for number in self.phones:
                     if number.value == phone:
                         return number
              return None

       def __str__(self):
           return f"Contact name: {self.name.value}, phones: {'; '.join(number.value for number in self.phones)}"

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
       
# Створення нової адресної книги
book = AddressBook()

    # Створення запису для John
john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")

    # Додавання запису John до адресної книги
book.add_record(john_record)

    # Створення та додавання нового запису для Jane
jane_record = Record("Jane")
jane_record.add_phone("9876543210")
book.add_record(jane_record)

    # Виведення всіх записів у книзі
     
print(book)

    # Знаходження та редагування телефону для John
john = book.find("John")
john.edit_phone("1234567890", "5555555555")

print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

    # Пошук конкретного телефону у записі John
found_phone = john.find_phone("5555555555")
print(f"{john.name}: {found_phone}")  # Виведення: John: 5555555555

    # Видалення запису Jane
book.delete("Jane")
