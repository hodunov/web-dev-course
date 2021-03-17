from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)


# Additional methods
def execute_query(query):
    """
    Returns the query result to the database
    """
    with sqlite3.connect('db.db') as conn:
        cursor = conn.cursor()
        cursor.execute(query)
        return cursor.fetchall()


def get_column_names(table):
    """
    Get list of columns from the table
    """
    with sqlite3.connect('db.db') as connection:
        try:
            connection.row_factory = sqlite3.Row
            cursor = connection.execute(f'SELECT * FROM {table}')
            row = cursor.fetchone()
            names = row.keys()
            if 'id' in names:
                names.remove('id')
            return names
        except sqlite3.OperationalError:
            # avoid the error, in case the requested table is not found
            return ['Something went wrong. This table probably does not exist in database']


def select_all_by_id(table, record_id):
    """
    Make a query SELECT * FROM _ WHERE id=_ to the db
    """
    return execute_query(f"SELECT * FROM {table} WHERE id={record_id}")[0]


def select_id_by_name(table, record):
    """
    Make a request SELECT ID FROM 'tablename' WHERE name='record'
    """
    return execute_query(f"SELECT id FROM {table} WHERE name='{record}'")[0][0]


def insert_into_table(table, record):
    """
    Make a request INSERT OR IGNORE INTO 'tablename' VALUES ('record')
    """
    return execute_query(f"INSERT OR IGNORE INTO {table}(Name) VALUES ('{record}')")


# main urls
@app.route('/')
def main():
    """
    Display all books
    """
    books = execute_query("SELECT * FROM Books")
    return render_template('main.html',
                           books=books, get_by_id=select_all_by_id)


@app.route('/author/<int:author_pk>/')
def books_by_author(author_pk):
    """
    Display books by the author
    """
    books = execute_query(f"SELECT * FROM Books WHERE author={author_pk}")
    return render_template('main.html', books=books, get_by_id=select_all_by_id)


@app.route('/year/<int:year_pk>/')
def books_by_year(year_pk):
    """
    Display books by the year
    """
    books = execute_query(f"SELECT * FROM Books WHERE year={year_pk}")
    return render_template('main.html', books=books, get_by_id=select_all_by_id)


@app.route('/genre/<int:genre>/')
def books_by_genre(genre):
    """
    Display books by genre
    """
    books = execute_query(f"SELECT * FROM Books WHERE genre={genre}")
    return render_template('main.html', books=books, get_by_id=select_all_by_id)


# /create/
@app.route('/create/author/', methods=['GET', 'POST'])
def create_author():
    """
    Create author object in db
    """
    page_name = "New Author"
    columns = get_column_names('Authors')

    if request.method == 'POST':
        try:
            execute_query(f"INSERT OR IGNORE INTO Authors (name,description) "
                          f"VALUES ('{request.form.get('Name')}',"
                          f"'{request.form.get('Description')}')")
            return redirect(f'/')
        except Exception as e:
            return f"Catch error:\n {e}"
    return render_template('create.html', fields=columns, page_name=page_name)


@app.route('/create/genre/', methods=['GET', 'POST'])
def create_genre():
    """
    Create genre object in db
    """
    page_name = "New Genre"
    columns = get_column_names('genres')

    if request.method == 'POST':
        try:
            execute_query(f"INSERT OR IGNORE INTO Genres (name,description) "
                          f"VALUES ('{request.form.get('Name')}','{request.form.get('Description')}')"
                          )
            return redirect(f'/')
        except Exception as e:
            return f"Catch error:\n {e}"
    return render_template('create.html', fields=columns, page_name=page_name)


@app.route('/create/book/', methods=['GET', 'POST'])
def create_book():
    """
    Create book object in db
    """
    page_name = "New Book"
    columns = get_column_names('books')

    if request.method == 'POST':
        # add author into the Authors table
        insert_into_table('Authors', request.form.get('Author'))
        # add genre into the Genres table
        insert_into_table('Genres', request.form.get('Genre'))

        execute_query(
            f"INSERT INTO Books (Author, title, Year, Pages, Genre) "
            f"VALUES ("
            f"'{select_id_by_name('Authors', request.form.get('Author'))}', "
            f"'{request.form.get('Title')}', "
            f"'{request.form.get('Year')}', "
            f"'{request.form.get('Pages')}', "
            f"'{select_id_by_name('Genres', request.form.get('Genre'))}'"
            f")")
        return redirect('/')
    return render_template('create.html', fields=columns, page_name=page_name)


# /update/
@app.route('/update/book/<int:book_pk>/', methods=['GET', 'POST'])
def update_book(book_pk):
    """
    Update book object in db
    """
    current_book = execute_query(f"SELECT * FROM Books WHERE id={book_pk}")[0]

    if request.method == 'POST':
        # add author into the Authors table
        insert_into_table('Authors', request.form.get('Author'))
        # add genre into the Genres table
        insert_into_table('Genres', request.form.get('Genre'))

        execute_query(
            f"UPDATE Books SET "
            f"author='{select_id_by_name('Authors', request.form.get('author'))}', "
            f"title='{request.form.get('title')}', "
            f"year='{request.form.get('year')}', "
            f"pages='{request.form.get('pages')}', "
            f"genre='{select_id_by_name('Genres', request.form.get('genre'))}' "
            f"WHERE id = {book_pk}"
        )
        return redirect('/')
    return render_template('update.html', book=current_book, get_by_id=select_all_by_id)


# /delete/
@app.route('/delete/book/<int:book_pk>/', methods=['GET', 'POST'])
def delete_book(book_pk):
    """
    Delete book object in db
    """
    execute_query(f"DELETE FROM Books WHERE id = {book_pk}")
    return redirect('/')


if __name__ == '__main__':
    app.run(
        host='127.0.0.1',
        port=5000,
        debug=True
    )
