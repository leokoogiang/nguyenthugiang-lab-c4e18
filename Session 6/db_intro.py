# Cơ sở dữ liệu
# Từ điên teencode, mình fix sẵn, cho ng dùng contribute, nhưng sau khi chạy lại từ điển đó ko đc cập nhật
# Làm thế nào giữ lại những thông tin này
# Nơi mình để dữ liệu
# 1 số loại phổ biến: SOL, no SQL (mongo dB), Graph SQL, postgre

# Sau khi đăng kí 1 tài khoản trên mlab. Cho mình 1 nhà kho
# Trong 1 nhà có nhiều phòng, 1 phòng là 1 database
# Mỗi database dùng cho 1 app riêng
# Trong 1 phòng có nhiều tủ
# Database, telcom, web, collection, document
# Nên có một user cho mỗi phòng

from pymongo import MongoClient

mongo_url = "mongodb://june2018:june2018@ds151840.mlab.com:51840/c4e18_lab"

# 1 connect to database 
client = MongoClient(mongo_url)


# 2 Get database
db = client.get_default_database()

# 3 Create collection
games = db['games']
milk_tea = db['milk_tea']


# 4 Create document
# new_game = {
#     "title": "PES",
#     "description": "pro evolution"

# }

# new_milk_tea = {
#     "title": "jasmine",
#     "description": "my favorite"
# }
# 5 Insert document into collection 
# games.insert_one(new_game)
# milk_tea.insert_one(new_milk_tea)

all_game = games.find()

for game in all_game:
    print(game)




