import json
from datetime import datetime
from Review import Review


def filename() -> str:
    return "reviews.json"


def get_reviews() -> list[Review]:
    try:
        with open(filename(), 'r') as f:
            reviews: list[Review] = json.load(f)
    except:
        print("init file " + filename())
        reviews = [Review("Admin", datetime.now(), "Welcome to our website!")]
        with open(filename(), 'w') as f:
            json.dump(reviews, f, ensure_ascii=False, indent=4)
    return reviews
