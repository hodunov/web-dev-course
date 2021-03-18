from peewee import SqliteDatabase, Model, AutoField, CharField, TextField, ForeignKeyField, IntegerField

db = SqliteDatabase("new_db.sqlite3")


class Author(Model):
    id = AutoField(primary_key=True, unique=True)
    name = CharField(max_length=255)
    description = TextField(null=True)

    class Meta:
        database = db


class Genre(Model):
    id = AutoField(primary_key=True, unique=True)
    name = CharField(max_length=255)
    description = TextField(null=True)

    class Meta:
        database = db


class Book(Model):
    id = AutoField(primary_key=True, unique=True)
    author = ForeignKeyField(Author, backref='books')
    title = TextField(null=False)
    year = IntegerField(null=False)
    pages = IntegerField(null=True)
    genre = ForeignKeyField(Genre, backref='books')

    class Meta:
        database = db


if __name__ == '__main__':
    db.create_tables([Author, Genre, Book])
