from flask import Flask, render_template, request, redirect, abort, flash
from models import Book, Author, Genre
from forms import BookForm, AuthorForm, GenreForm
from peewee import DoesNotExist

app = Flask(__name__)
app.secret_key = "something only you know"


# main urls
@app.route('/')
def main():
    """
    Display all books
    """
    books = Book.select().join_from(Book, Author).join_from(Book, Genre)
    return render_template('main.html', books=books, page_name='Book list 🕮')


@app.route('/author/<int:pk>/')
def books_by_author(pk):
    """
    Display books by the author
    """
    try:
        author = Author.select().where(Author.id == pk).get()
    except DoesNotExist:
        return abort(404)
    return render_template('details.html', table_name=author, page_name='Author ✍🏻')


@app.route('/year/<int:pk>/')
def books_by_year(pk):
    """
    Display books by the year
    """
    books = Book.select().where(Book.year == pk)
    return render_template('main.html', books=books, page_name=pk)


@app.route('/genre/<int:pk>/')
def books_by_genre(pk):
    """
    Display books by genre
    """
    try:
        genre = Genre.select().where(Genre.id == pk).get()
    except DoesNotExist:
        return abort(404)
    return render_template('details.html', table_name=genre, page_name='Genre 📚')


# /create/
@app.route('/create/author/', methods=['GET', 'POST'])
def create_author():
    """
    Create author object in db
    """
    form = AuthorForm(obj=Author.select())
    if request.method == "POST":
        form = AuthorForm(request.form)
        if form.validate():
            form.save()
            flash("You've added a new author! ✍️")
            return redirect('/')
    return render_template('create.html', form=form, page_name="Add Author ✍🏻")


@app.route('/create/genre/', methods=['GET', 'POST'])
def create_genre():
    """
    Create genre object in db
    """
    form = GenreForm()
    if request.method == 'POST':
        form = GenreForm(request.form)
        if form.validate():
            form.save()
            flash("You've added a new genre!📚")
            return redirect('/')

    return render_template('create.html', form=form, page_name="Add Genre 📚")


@app.route('/create/book/', methods=['GET', 'POST'])
def create_book():
    """
    Create book object in db
    """
    form = BookForm()

    # If you put these choices in forms.py, the new author or genre won't show up in the drop-down list.
    # This has to do with database queries.
    form.genre.choices = [(x.id, x.name) for x in Genre.select()]
    form.author.choices = [(x.id, x.name) for x in Author.select()]

    if request.method == 'POST':
        form = BookForm(request.form)
        # reassigned form, you must pass the choices again, otherwise there will be a validation error.
        form.genre.choices = [(x.id, x.name) for x in Genre.select()]
        form.author.choices = [(x.id, x.name) for x in Author.select()]
        if form.validate():
            form.save()
            flash("You've added a new book!📕")
            return redirect('/')

    return render_template('create.html', form=form, page_name='Add Book 📕')


# /update/
@app.route('/update/book/<int:pk>/', methods=['GET', 'POST'])
def update_book(pk):
    """
    Update book object in db
    """
    try:
        book = Book.get_by_id(pk)
    except DoesNotExist:
        return abort(404)
    form = BookForm(request.form, book)
    if request.method == 'POST' and form.validate():
        Book.update(request.form).where(Book.id == pk).execute()
        return redirect('/')

    return render_template('update.html', form=form, book=book)


# /delete/
@app.route('/delete/book/', methods=['POST'])
def delete_book():
    """
    Delete book object in db
    """
    Book.delete().where(Book.id == int(request.form['id'])).execute()
    return redirect('/')


if __name__ == '__main__':
    app.run(
        host='127.0.0.1',
        port=5000,
        debug=True
    )
