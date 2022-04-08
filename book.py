class Book(object):

 #图书信息类

 def __init__(self, id, name, author, press, type, amount, available,score):

    self.id = id #索书号

    self.name = name #书名

    self.author = author #作者

    self.press = press #出版社

    self.type = type #图书类别

    self.amount = amount #库存总量

    self.available = available #可借本书

    self.score=score #图书评分