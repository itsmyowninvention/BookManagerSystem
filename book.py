import json
import user
import time

class Book:

    #图书信息类
    def __init__(self, id, name, author, press, type, amount, available,score):

        self.id = id #索书号

        self.name = name #书名

        self.author = author #作者

        self.press = press #出版社

        self.type = type #图书类别

        self.amount = amount #库存总量

        self.available = available #可借书本数量

        self.score = score #图书评分

def load():
    result = {}
    with open('./data/book.json') as file:
        books = json.load(file)
    for book in books:
        result[book['id']] = Book(
                    id = book['id'], 
                    name = book['name'], 
                    author = book['author'], 
                    press = book['press'], 
                    type = book['type'], 
                    amount = book['amount'], 
                    available = book['available'], 
                    score = book['score'])
    return result

def load_borrow():
    with open('./data/borrow.json') as file:
        borrows = json.load(file)
    return borrows

def dump_borrow(borrows):
    with open('./data/borrow.json', 'w') as file:
        borrows = json.dump(borrows, file)
        

def dump(books):
    result = [
        {
            'id': _book.id,
            'name': _book.name,
            'author': _book.author,
            'press': _book.press,
            'type': _book.type,
            'amount': _book.amount,
            'available': _book.available,
            'score': _book.score
        } 
        for _book in books.values()
    ]
    with open('./data/book.json', 'w') as file:
        json.dump(result, file)
        
def addBook(book) -> bool:
    books = load()
    if book.id in books:
        return False
    books[book.id] = book
    dump(books)
    return True

def modifyBook(book):
    books = load()
    if not book.id in books:
        return False
    books[book.id] = book
    dump(books)

def deleteBook(book):
    books = load()
    del books[book.id]
    dump(books)
    
def selectBook(id):
    books = load()
    return books[id]

# 借书
def borrowBook(user, book) -> bool:
    result = False
    books = load() # 图书目录
    borrows = load_borrow() # 借阅记录
    
    borrow_books = borrows[user.id]['book'] # 该用户借阅的图书
    books[book.id].available = books[book.id].available - 1 # 可借书本数量减一
    if not book.id in borrow_books: # 该用户没有借阅该图书
        borrow_books[book.id] = { # 添加借阅记录
                'id': book.id,
                'isReturned': False,
                'borrowDate': time.time()
            }
        result = True    
    
    dump_borrow(borrows)
    dump(books)
    
    return result

# 还书  
def returnBook(user, book) -> bool:
    result = False
    books = load() # 图书目录
    borrows = load_borrow() # 借阅记录
    
    borrow_books = borrows[user.id]['book'] # 该用户借阅的图书
    
    if book.id in borrow_books: # 归还图书
        borrow_books[book.id]['isReturned'] = True
        borrow_books[book.id]['returnDate'] = time.time()
    
    dump_borrow(borrows)
    dump(books)
    
    return result

def queryBorrow(user):
    result = []
    books = load() # 图书目录
    borrows = load_borrow() # 借阅记录
    
    if user.id in borrows: 
        return borrows[user.id]['book'] # 该用户借阅的图书
    else:
        return None
    

# 获取图书评分
def takeScore(book):
    return book.score

def sortBooks():
    books = load()
    books_list = [_book for _book in books.values()]
    books_list.sort(key=takeScore, reverse=True)
    return books_list
