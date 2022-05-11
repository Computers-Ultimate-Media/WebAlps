from Review import Review
from database_ import insert_data_in_base, data_from_base


def new_review(author: str, text: str):
    sql = "insert into bottle_db.reviews (author, text) values (%s,%s);"
    val = (author, text)
    insert_data_in_base(sql, val)


def get_reviews() -> list[Review]:
    if (len(meme()) < 1):
        new_review("Admin", "Be free to write your reviews!")
    return meme()


def meme():
    return data_from_base("select * from reviews order by date asc",True)
