import flask

from flask import url_for

from flask.views import MethodView

from instaclone.applications.views import FormViewMixin
from instaclone.applications.home import forms


class AboutView(MethodView, FormViewMixin):
    form_class = forms.SearchForm
    template_name = 'home/about.html'

    def post(self):
        form = self.get_form()

        return flask.redirect(url_for(endpoint='users.search_user', search_item=form.search_item.data))
