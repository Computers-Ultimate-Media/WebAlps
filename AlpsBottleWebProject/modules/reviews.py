from AlpsBottleWebProject.modules.Review import Review
from AlpsBottleWebProject.database_ import insert_data_in_base, data_from_base

# insert new review to databse
def new_review(author: str, text: str):
    sql = "insert into bottle_db.reviews (author, text) values (%s,%s);"
    val = (author, text)
    insert_data_in_base(sql, val)

# get all reviews from database and add first one if list is empty
def get_reviews() -> list[Review]:
    if (len(reviews()) < 1):
        new_review("Admin", "Be free to write your reviews!")
    return reviews()

# get all reviews from database
def reviews():
    return data_from_base("select * from reviews order by date desc",True)
