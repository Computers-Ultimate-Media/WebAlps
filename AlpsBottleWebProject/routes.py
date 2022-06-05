from bottle import route, view, error, post, request, redirect  # pip install bottle
from datetime import datetime

from AlpsBottleWebProject.modules.MountainConditions import get_mountain_conditions
from AlpsBottleWebProject.modules.Mountains import get_mountains
from AlpsBottleWebProject.modules.reviews import get_reviews, new_review
from modules.Humans import get_humans
from database_ import make_database_and_table, data_from_base, insert_data_in_base
import re

make_database_and_table() # создание базы и таблиц

# проверка email на валидность
def is_valid_email(email: str) -> bool:
    email_pattern = re.compile(r"([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+")
    arr = email.split('@')
    return bool(email_pattern.match(email)) and len(arr[0]) <= 64 and len(arr[1]) <= 255

# проверка login на валидность
def is_valid_login(login: str) -> bool:
    login_pattern = re.compile(r"^\w{3,16}$")
    return bool(login_pattern.match(login))

# проверка password на валидность
def is_valid_password(password: str) -> bool:
    password_pattern = re.compile(r"^\w{3,16}$")
    return bool(password_pattern.match(password))

# вывод ошибки, если что то не прошло валидацию
def validate_all(email, login, password):
    error = ""

    if not is_valid_email(email):
        error = "email не соответствует шаблону"
    elif not is_valid_login(login):
        error = "никнейм должен состоять только из латинских символов/цифр и быть от 3 до 16 символов"
    elif not is_valid_password(password):
        error = "некорректный заголовок, вы не можете использовать от 20 до 100 символов"
    elif is_insert_valid(email, login, password):
        error = "такой пользователь уже существует"

    if error != "":
        return f"Ошибка: {error}"

    return None

# страница проверки введённых данных
@route('/check_registration', method='post')
def check_registration():
    from json import dumps as json_dumps, loads as json_loads

    data = request.body.getvalue().decode('utf-8')
    data = json_loads(data)

    email = data['email']
    login = data['login']
    password = data['password']

    ret = validate_all(email, login, password)
    if ret is not None:
        return json_dumps({'error': ret})

    return json_dumps({'status': 'ok'})

# проверка на существующую запись пользователя, иначе вставить новую
def is_insert_valid(email_, login_, password_) -> bool:
    sql = "INSERT INTO stuff (login, email, password) VALUES (%s, %s, %s)"
    val = (login_, email_, password_)

    if len(data_from_base("select * from stuff where login = '{}'".format(login_), True)) > 0:
        return True
    else:
        insert_data_in_base(sql, val)
        return False

# редирект на страницу пользователей после регистрации
@post('/registration', method='post')
def my_form():
    return redirect('/users')

# страница ошибки 404
@error(404)
def error404(error):
    return '<pre> &lt;?php <br> echo \'Nothing here!\'; </pre>'

# главная страница
@route('/')
@route('/home')
@view('index')
def home():
    return add_users(dict(
        year=datetime.now().year,
        mountain_condition=get_mountain_conditions()
    ))

# страница о нас
@route('/about')
@view('about')
def about():
    return add_users(dict(
        title='About',
        message='Your application description page.',
        year=datetime.now().year
    ))

# страница регистрации
@route('/registration')
@view('registration')
def registration():
    return add_users(dict(
        title='Registration',
        year=datetime.now().year,
    ))

# страница пользователей
@route('/users')
@view('users')
def users():
    return add_users(dict(
        title='Users',
        message='Your application description page.',
        year=datetime.now().year,
        authors=data_from_base("select login, email from stuff", True)
    ))


@route('/mnt/<name>')
@view('mountain')
def preview(name):
    dicts = get_mountains()

    for x in dicts:
        if x["val"] == name:
            return add_users(x)


@route('/bio/<name>')
@view('human')
def humans(name):
    # gets
    dicts = get_humans()
    for x in dicts:
        if x["val"] == name:
            return add_users(x)


# displays all reviews to user
@route('/reviews')
@view('reviews')
def reviews():
    # gets reviews from model
    all_reviews = get_reviews()

    return add_users(dict(
        title='Mountain paradise',
        year=datetime.now().year,
        reviews=all_reviews
    ))


# displays user form where he creates new reviews
@route('/reviews/new')
@view('new_review')
def reviews():
    return add_users(dict(
        title='Mountain paradise',
        year=datetime.now().year
    ))


# method to get new review from user
@post('/reviews/new', method='post')
def new_review_form():
    # gets input from form
    author = request.forms.get('AUTHOR')
    text = request.forms.get('TEXT')

    # transfers params to model
    new_review(author, text)

    # sends user to list with all reviews, his including
    return redirect('/reviews')


def add_users(di: dict) -> dict:
    di["user_count"] = data_from_base("select count(*) from stuff", False)
    return di
