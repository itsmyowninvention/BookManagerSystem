import user
import book
import sys
import time

logged_in_user = None # 用户

def main(args):
    print("--------------------登录--------------------")
    global logged_in_user
    while(logged_in_user == None):
        id = input('ID:')
        password = input('密码:')
        logged_in_user = user.login(id, password)
        if logged_in_user == None:
            print('用户名或密码不正确')
    
    while(True):
        if(logged_in_user.identity == 'admin'):
            admin_menu()
        else:
            user_menu()
    
    print('-------------------------------------------------')  

def admin_menu():
    print('----------------------菜单------------------------')
    print('1.修改密码')
    print('2.添加图书')
    print('3.修改图书信息')
    print('4.查询图书信息')
    print('5.查询图书排名')
    print('6.删除图书')
    print('7.借阅图书')
    print('8.归还图书')
    print('9.图书借阅历史')
    print('10.退出')
    choice = input('选项:')
    admin_dispatch(choice)
    print('-------------------------------------------------')  

def user_menu():
    print('--------------------菜单------------------------')
    print('1.修改密码')
    print('2.查询图书信息')
    print('3.查询图书排名')
    print('4.借阅图书')
    print('5.归还图书')
    print('6.图书借阅历史')
    print('7.退出')
    user_dispatch(choice)
    print('-------------------------------------------------')  

def user_dispatch(choice):
    if(choice == '1'):
        changePassword()
    elif(choice == '2'):
        queryBook()
    elif(choice == '3'):
        sortBook()
    elif(choice == '4'):
        borrowBook()
    elif(choice == '5'):
        returnBook()
    elif(choice == '6'):
        queryBorrow()
    elif(choice == '7'):
        exit()
        
def admin_dispatch(choice):
    if(choice == '1'):
        changePassword()
    elif(choice == '2'):
        addBook()
    elif(choice == '3'):
        modifyBook()
    elif(choice == '4'):
        queryBook()
    elif(choice == '5'):
        sortBook()
    elif(choice == '6'):
        deleteBook()
    elif(choice == '7'):
        borrowBook()
    elif(choice == '8'):
        returnBook()
    elif(choice == '9'):
        queryBorrow()
    elif(choice == '10'):
        exit()
    
    
def changePassword():
    print('---------------修改密码-------------------------')
    password = input('新密码:')
    user.changePassword(password)
    print('-------------------------------------------------')

def addBook():
    print('------------------添加图书---------------------')
    id = input('索书号:')
    name = input('书名:')
    author = input('作者:')
    press = input('出版社:')
    type = input('类型:')
    amount = int(input('库存总量:'))
    available = int(input('可借书本数量:'))
    score = int(input('评分:'))
    _book = book.Book(id,name,author,press,type,amount,available,score)
    book.addBook(_book)
    print('-------------------------------------------------')

def modifyBook():
    print('------------------修改图书---------------------')
    id = input('索书号:')
    _book = book.selectBook(id)
    if _book == None:
        print('相关图书不存在')
        return
    name = input('书名:')
    author = input('作者:')
    press = input('出版社:')
    type = input('类型:')
    amount = input('库存总量:')
    available = input('可借书本数量:')
    score = input('评分:')
    _book = book.Book(id,name,author,press,type,amount,available,score)
    book.modifyBook(_book)
    print('-------------------------------------------------')
    
    
def queryBook():
    print('--------------------查询图书------------------')
    id = input('索书号:')
    _book = book.selectBook(id)
    if _book == None:
        print('相关图书不存在')
        return
    print('索书号:'+_book.id)
    print('书名:'+_book.name)
    print('作者:'+_book.author)
    print('出版社:'+_book.press)
    print('类型:'+ str(_book.type))
    print('库存总量:'+ str(_book.amount))
    print('可借书本数量:'+ str(_book.available))
    print('评分:'+ str(_book.score))
    print('-------------------------------------------------')
    
    
def sortBook():
    print('-------------------图书排名----------------------')
    books = book.sortBooks()
    for _book in books:
        print('索书号:'+_book.id)
        print('书名:'+_book.name)
        print('评分:'+str(_book.score))
    print('-------------------------------------------------')
    
def borrowBook():
    print('------------------借阅图书---------------------------')
    global logged_in_user
    id = input('索书号:')
    _book = book.selectBook(id)
    if _book == None:
        print('相关图书不存在')
        return
    book.borrowBook(logged_in_user, _book)
    
def returnBook():
    print('------------------归还图书---------------------------')
    global logged_in_user
    id = input('索书号:')
    _book = book.selectBook(id)
    if _book == None:
        print('相关图书不存在')
        return
    book.returnBook(logged_in_user, _book)
    
def queryBorrow():
    print('------------------个人借阅历史---------------------------')
    global logged_in_user
    borrow_book = book.queryBorrow(logged_in_user)
    for b in borrow_book.values():
        print("索书号:" + b['id'])
        if(b['isReturned']):
            print('图书状态:' + '已归还')
        else:
            print('图书状态:' + '未归还')
        print('借阅日期:' + time.strftime('%Y-%m-%d', time.localtime(b['borrowDate'])))
        if(b['isReturned']):
            print('归还日期:' + time.strftime('%Y-%m-%d', time.localtime(b['returnDate'])))
        print('------------------------------------------')
    
def deleteBook():
    print('------------------删除图书---------------------')
    id = input('索书号:')
    _book = book.selectBook(id)
    if _book == None:
        print('相关图书不存在')
        return
    book.deleteBook(_book)
    

if __name__ == "__main__":
    main(sys.argv)