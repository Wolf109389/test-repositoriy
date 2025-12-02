import os

class Book:
    def __init__(self, name=None, pages=0, genre=None, 
                 desciption=None, year=0, author=None, 
                 price=0, quantity=0, number_of_sales=0,
                 ):
        self.__name = name
        self.test_pages(pages)
        self.__genre = genre
        self.description = desciption
        self.__year = year
        self.__author = author
        self.price = price
        self.quantity = quantity
        self.number_of_sales = number_of_sales

    def test_pages(self, pages=0):
        if pages < 0:
            self.__pages = 0
        else:
            self.__pages = pages

    def __str__(self):
        return f"Name: {self.__name}\tPages: {self.__pages}\tGenr: {self.__genre}\t  Author: {self.__author}\t Price: {self.price}\tCount: {self.quantity}\t"
    
    def get_name(self):
        return self.__name
    
    def get_author(self):
        return self.__author
    
    def get_year(self):
        return self.__year
    
    def get_genre(self):
        return self.__genre
    
    def __del__(self):
        print(f'Book "{self.__name}" deleted')
    
class BookShop:
    def __init__(self):
        self.__books = []

    def add_book(self, book=None):
        if book != None:
            self.__books.append(book)

    def search_book(self, type_search):
        found = []
        not_found = ""
        if type_search == "1":
            not_found = "Не знайдено книг із такою назвою"
            search = input("Яку книгу бажаєте знайти: ").lower()
            found = [f for f in self.__books
                     if f.get_name() and search in f.get_name().lower()
                    ]
            
        elif type_search == "2":
            not_found = "Не знайдено книг цього року"
            try:
                search = input("Книги якого року бажаєте знайти: ")
                found = [f for f in self.__books
                         if f.get_year() == int(search)
                        ]
            except:
                print("Введіть щось інше..")

        elif type_search == "3":
            not_found = "Не знайдено книг цього автора"
            search = input("Книги якого автора бажаєте знайти: ").lower()
            found = [f for f in self.__books
                     if f.get_author() and search in f.get_author().lower()
                    ]
            
        else:
            not_found = "Не знайдено книг із таким жанром"
            search = input("Книги з яким жанром бажаєте знайти: ").lower()
            found = [f for f in self.__books
                     if f.get_genre() and search in f.get_genre().lower()
                    ]

        return found, not_found
    
    def buy_book(self):
        search = input("Яку книгу бажаєте купити: ").lower()
        found = [f for f in self.__books
                 if f.get_name() and search in f.get_name().lower()
                ]
        
        verify, *_ = found or [None]
        if verify:
            answ = input(f'1. Yes\n2. No\nВи хочете купити "{verify.get_name()}"? ').lower()
            if answ == "1":
                self.remove_book(verify)
        else:
            print("Не знайдено такої книги..")

    def get_info(self):
        info_list = []
        for i in range(len(self.__books)):
            info_list.append(f"{self.__books[i].__str__()}")

        return info_list
    
    def top_by_price(self):
        list_top_seles = []
        for i in self.__books:
            list_top_seles.append([i.get_name(), i.price])
        
        return sorted(list_top_seles, key=lambda b: b[1], reverse=True)
    
    def top_by_sales(self):
        list_top_seles = []
        for i in self.__books:
            list_top_seles.append([i.get_name(), i.number_of_sales])

        return sorted(list_top_seles, key=lambda b: b[1], reverse=True)
    
    def remove_book(self, book):
        book.quantity -= 1

        if book.quantity == 0:
            for i in self.__books:
                if i.get_name().lower() == book.get_name().lower():
                    self.__books.remove(i)
                    break
            else:
                print("Такої книги немає")
        
advense = Book(name="Advense", genre="Adventure", author="Anton Dara", desciption=None, pages=364, year=200, price=749, quantity=50, number_of_sales=43)
cases = Book(name="Cases", genre="Adventure", author="Ben Karon", desciption=None, pages=256, year=2025, price=415, quantity=100, number_of_sales=89)
dark = Book(name="Dark", genre="Novel", author="Karl Shernu", desciption=None, pages=234, year=2000, price=299, quantity=30, number_of_sales=10)
zombie = Book(name="Zombie", genre="Adventure", author="Benor Mia", desciption=None, pages=126, year=2002, price=400, quantity=45, number_of_sales=18)
rosa = Book(name="Rosa", genre="Novel", author="Natalia Barna", desciption=None, pages=199, year=2016, price=100, quantity=2, number_of_sales=10)
books = [advense, cases, dark, zombie, rosa]

knigayea = BookShop()

for i in books:
    knigayea.add_book(i)

while True:
    os.system("cls")

    print("Меню:")
    print("1. Переглянути книги\n2. Пошук книг\n3. Переглянути топ книг\n(other). Вийти")
    action = input("Що бажаєте зробити? (Введіть одне з чисел зазначених вище): ")

    if action == "1":
        while True:
            os.system("cls")

            infa = knigayea.get_info()
            for i in infa:
                print(i)

            print("\n1. Купити книгу\n(something). Вийти")
            question = input("Що бажаєте зробити? (Введіть одне з чисел зазначених вище): ")

            if question == "1":
                knigayea.buy_book()

            else:
                break

    elif action == "2":
        os.system("cls")

        print("\n1. Пошук за назвою\n2. Пошук за роком\n3. Пошук за автором\n4. Пошук за жанром\n(other). Меню")
        type_search = input("Пошук за: ")

        if type_search in ("1", "2", "3", "4"):
            search, not_found = knigayea.search_book(type_search)
        else:
            continue

        if search:
            print(f"\nЗнайдено({len(search)}):")
            for i in search:
                print(" →", i)
            print("(something). Меню")
        else:
            print(not_found)

        input()
    
    elif action == "3":
        os.system("cls")
        
        print("Топ книг")
        print("1. Топ книг за ціною\n2. Топ книг за продажами\n(other). Вийти")
        type_search = input("Який топ ви хочете переглянути: ")

        if type_search in ("1", "2"):
            if type_search == "1":
                top = knigayea.top_by_price()
                for i, z in top:
                    print(f" → price: {z}\tName: {i}")
            else:
                top = knigayea.top_by_sales()
                for i, z in top:
                    print(f" → Number of sales: {z}\tName: {i}")


        else:
            continue
        
        input()

    else:
        break
