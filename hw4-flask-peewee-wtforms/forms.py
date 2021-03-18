import wtforms
from models import Author, Genre, Book


class GenreForm(wtforms.Form):
    name = wtforms.StringField(validators=[wtforms.validators.DataRequired()])
    description = wtforms.StringField(validators=[wtforms.validators.Optional()])

    def save(self):
        Genre.create(name=self.name.data,
                     description=self.description.data)


class AuthorForm(wtforms.Form):
    name = wtforms.StringField(validators=[wtforms.validators.DataRequired()])
    description = wtforms.StringField(validators=[wtforms.validators.Optional()])

    def save(self):
        Author.create(name=self.name.data,
                      description=self.description.data)


class BookForm(wtforms.Form):
    author = wtforms.SelectField(
        choices=[(x.id, x.name) for x in Author.select()]
    )
    title = wtforms.StringField(validators=[wtforms.validators.DataRequired()])
    year = wtforms.IntegerField(validators=[
        wtforms.validators.DataRequired(message='Enter the numbers'),
        wtforms.validators.NumberRange(0, 3030, message='The year is entered incorrectly')])
    pages = wtforms.IntegerField(validators=[wtforms.validators.DataRequired(),
                                             wtforms.validators.NumberRange(
                                                 min=1, max=9999,
                                                 message="Please enter the number of the book's pages")
])
    genre = wtforms.SelectField(
        choices=[(x.id, x.name) for x in Genre.select()]
    )

    def save(self):
        Book.create(author=self.author.data,
                    title=self.title.data,
                    year=self.year.data,
                    pages=self.pages.data,
                    genre=self.genre.data)
