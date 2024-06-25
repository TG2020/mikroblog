from flask import render_template, request, session, flash, redirect, url_for, Blueprint
from app import app
from app.models import Book, Author, Loan, Return, db

#
# @app.route("/")
# def index():
#     all_books = Book.query.all()
#     return render_template("index.html", all_books=all_books)


@app.route('/add', methods=['GET'])
def add():
    return render_template("add.html")


@app.route("/add", methods=['POST'])
def add_post():
    title = request.form.get("title")
    authorName = request.form.get("authorName")
    authorSurname = request.form.get("authorSurname")
    authorName2 = request.form.get("authorName2")
    authorSurname2 = request.form.get("authorSurname2")
    b = Book(title=title)
    db.session.add(b)

    # check if author exist:
    if not Author.query.filter(Author.name == authorName, Author.surname == authorSurname).first():
        a = Author(name=authorName, surname=authorSurname)
    else:
        a = Author.query.filter(Author.name == authorName, Author.surname == authorSurname).first()
    b.authors.append(a)
    db.session.add(a)

    # check 2 author:
    if not authorName2 == "":
        if not Author.query.filter(Author.name == authorName2, Author.surname == authorSurname2).first():
            a2 = Author(name=authorName2, surname=authorSurname2)
        else:
            a2 = Author.query.filter(Author.name == authorName2, Author.surname == authorSurname2).first()
        b.authors.append(a2)
        db.session.add(a2)
    db.session.commit()
    return redirect('/')


@app.route('/delete', methods=['GET'])
def delete():
    return render_template("delete.html")


@app.route('/delete', methods=['POST'])
def delete_out():
    title = request.form.get("title")
    msg = None
    if Book.query.filter(Book.title == title).first():
        db.session.delete(Book.query.filter(Book.title == title).first())
        db.session.commit()
        msg = 'Book deleted'
    else:
        msg = 'Book not found'
    return render_template('delete.html', msg=msg)


@app.route('/find_book', methods=['GET'])
def update():
    return render_template("update.html")


@app.route("/update", methods=['POST'])
def update_post():
    id = request.form.get('id')
    title = request.form.get("title")
    authorName = request.form.get("authorName")
    authorSurname = request.form.get("authorSurname")
    authorName2 = request.form.get("authorName2")
    authorSurname2 = request.form.get("authorSurname2")
    available = request.form.get('available')
    if available:
        available = True
    else:
        available = False

    b = Book.query.filter(Book.id == id).first()
    b.title = title
    b.is_available = available
    db.session.add(b)
    b.authors = []
    if not Author.query.filter(Author.name == authorName, Author.surname == authorSurname).first():
        a = Author(name=authorName, surname=authorSurname)
    else:
        a = Author.query.filter(Author.name == authorName, Author.surname == authorSurname).first()
    b.authors.append(a)
    db.session.add(a)

    # check 2 author:
    if not authorName2 == "":
        if not Author.query.filter(Author.name == authorName2, Author.surname == authorSurname2).first():
            a2 = Author(name=authorName2, surname=authorSurname2)
        else:
            a2 = Author.query.filter(Author.name == authorName2, Author.surname == authorSurname2).first()
        b.authors.append(a2)
        db.session.add(a2)
    db.session.commit()
    return redirect('/')

@app.route('/')
def index():
    books = Book.query.all()
    authors = Author.query.all()
    loans = Loan.query.all()
    returns = Return.query.all()
    return render_template('index.html', books=books, authors=authors, loans=loans, returns=returns)

@app.route('/list_books')
def list_books():
    books = Book.query.all()
    return render_template('books.html', books=books)

@app.route('/list_authors')
def list_authors():
    authors = Author.query.all()
    return render_template('authors.html', authors=authors)

@app.route('/add_book', methods=['GET', 'POST'])
def add_book():
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        year = request.form['year']
        genre = request.form['genre']
        description = request.form['description']

        book = Book(title=title, author=author, year=year, genre=genre, description=description)
        db.session.add(book)
        db.session.commit()
        return redirect(url_for('list_books'))
    return render_template('add_book.html')

@app.route('/add_author', methods=['GET', 'POST'])
def add_author():
    if request.method == 'POST':
        name = request.form['name']
        birth_date = request.form['birth_date']
        nationality = request.form['nationality']

        author = Author(name=name, birth_date=birth_date, nationality=nationality)
        db.session.add(author)
        db.session.commit()
        return redirect(url_for('list_authors'))
    return render_template('add_author.html')

@app.route('/loans')
def list_loans():
    loans = Loan.query.all()
    return render_template('loans.html', loans=loans)

@app.route('/returns')
def list_returns():
    returns = Return.query.all()
    return render_template('returns.html', returns=returns)