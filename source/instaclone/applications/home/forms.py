from flask_wtf import FlaskForm

from wtforms import StringField


class SearchForm(FlaskForm):
    search_item = StringField(
        label='Search Profiles',
    )
