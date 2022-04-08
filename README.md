# BookManagerSystem



# 程序设计题：图书借阅管理系统

## 1 系统的基本功能

本课题要求编写Python程序实现对图书信息录入、图书信息查询、图书借阅等方面的管理。一个综合的图书借阅管理系统，要求能够管理图书的基本信息（包含新图书入库、读者图书查询借阅等），需要实现以下功能：读取以数据文件形式存储的图书信息；管理员可以增加、修改、删除图书的信息；读者可以按照图书名、作者名、索书号等查询图书，并可通过该系统实现对图书的借阅、续借和归还；读者还可查询自己所借图书的信息（是否归还、归还日期等），并且能查询图书评分和图书受欢迎排行榜。

系统内的所有信息必须以文件的方式存储在硬盘中，图书信息文件，存放了图书的索书号、书名、作者、出版社、类别、库存总量、可借本数、图书评分。格式如下：

TN911.7/3-50:3 《信息、控制与系统》 张贤达 清华大学出版社 教材 10 6 3.7

I247.57/3-12808.1 《白色橄榄树》 玖月晞 百花洲文艺出版社 人文艺术 10 5 4.3

TN91/3-133 《现代通信概论》 张维玺 科学出版社 教材 20 16 4.7

...... 

## 2 要求及提示

### 2.1 基本要求

要能提供以下几个基本功能：

（1）系统内的相关信息文件由程序设计人员预先从键盘上录入，文件中的数据记录不得少于20条；

（2）设计并实现系统的相关界面，提供良好的交互界面；

（3）登录时输入帐号以区分读者和管理员；

（4）读者信息查询：

l 图书查询借阅功能：输入一个书名（或索书号、作者等其他信息），查出相关图书的基本信息并显示输出，同时提示是否需要借阅该图书；

l “我的”功能：显示个人图书借阅历史，显示所借图书的状态（是否归还、归还日期）、并选择是否归还或续借。

（5）管理端信息查询：

l 管理员可以增加、修改、删除图书的信息。

（6）读者可查询图书受欢迎榜；

2.2 选做要求

（1）仿照“豆瓣读书”，设计实现一个书评功能，提供读者对图书进行评分和评论的操作。

（2）使用Tkinter或其他GUI函数库，为本课题设计一个可视化的界面，要求界面美观、布局合理、功能正确以及对用户的错误操作能够进行友好提示。

### 2.3 提示

（1）程序的总体框图如下：程序的总体框图如下：

|     |
| --- | --- |
|     |     |

查询图书评分排名信息模块 图1 图书信息管理系统总体框图

（2）数据结构：

依据给定的图书信息，定义图书类，设计内容如下：

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

### 2.4 其他要求

（1）在上述功能要求的基础上，为了提高本课程的成绩，可以和任课教师沟通，为程序设计题添加一些额外的功能。

（2）变量、方法命名符合规范。

（3）注释详细：每个变量都要求有注释说明用途；方法有注释说明功能，对参数、返回值也要以注释的形式说明用途；关键的语句段要求有注释解释。

（4）程序的层次清晰，可读性强。

## 3 开发环境

开发环境使用Python3以上版本，开发工具可以选择IDLE或者PyCharm等集成开发工具。
