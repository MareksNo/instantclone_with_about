import flask

from flask.views import MethodView

from instaclone.applications.views import FormViewMixin
from instaclone.applications.home import forms


class AboutView(MethodView, FormViewMixin):
    form_class = forms.SearchForm
    template_name = 'home/about.html'
