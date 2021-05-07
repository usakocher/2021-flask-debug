from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user
from may_blog.models import Post, db
from may_blog.forms import BlogPostForm

site = Blueprint('site', __name__, template_folder='site_templates')

"""
IN the above code, some arguments are specified when creating the Blueprint object
This first argument 'site', is the Blueprint's name,
this will be used by flasks routing mechanism.
The second parameter __name__, is the BP's import name,
which flask uses to locate resources
"""

@site.route('/')
def home():
    posts = Post.query.all
    returnrender_template('indexes.html', posts=posts)

@site.route('/profile')
def profile():
    return render_template('profile.html')

@site.route('/createposts', methods=['GET','POST'])
@login_required
def createposts():
    form = BlogPostForm
    if request.method == 'POST' and form.validate():
        title = form.title.data
        content = form.content.data
        user_id = current_user
        print('\n', title, content)
        post = Post(title, content, user_id)
        db.session.add(,post)
        db.session.commit()
        return redirect(url_for('site.createposts'))
    return render_template("createposts.html", form=form)