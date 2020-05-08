from flask import Blueprint

from instaclone.applications.home import views


blueprint = Blueprint(
    name='about',
    import_name=__name__,
    template_folder='templates'
)

blueprint.add_url_rule(
    rule='/',
    view_func=views.AboutView.as_view('about')
)
