from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData
engine = create_engine('sqlite:///books.db', echo = True)
meta = MetaData()
books = Table(
    'Books', meta,
    Column('Id',Integer,primary_key = True),
    Column('Title', String),
    Column('Author', String),
    Column('Year', Integer),
    
    
)

# meta.create_all(engine)
# ins = books.insert()
# ins = books.insert().values(Id =1,Title ="Charlotte's Web" ,Author="E.B. White" ,Year=1952)
b = books.select()
b_list = []
conn = engine.connect()
result = conn.execute(b)

for title in result:
    b_list.append(title)
b_list.sort()
print(b_list)
# result = conn.execute(books.insert(), [
#     {"Id":2,"Title":"IT" ,"Author":"Stephen King" ,"Year":1986},
#     {"Id":3,"Title":"Of Mice and Men" ,"Author":"Johnm Steinbeck" ,"Year":1937},
#     {"Id":4,"Title":"To Kill a Mockingbird" ,"Author":"Harper lee" ,"Year":1960},
#     {"Id":5,"Title":"Catcher in the Rye" ,"Author":"J.D. Salinger" ,"Year":1951},
    
# ])

