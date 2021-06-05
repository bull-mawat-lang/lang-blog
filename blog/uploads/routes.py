import os
from flask import (render_template, current_app, url_for, flash,
                   redirect, request, abort, Blueprint)
from flask_login import current_user, login_required
from blog import db
from blog.models import Upload
from blog.uploads.forms import UploadForm

uploads = Blueprint('uploads', __name__)

@uploads.route("/upload/new", methods=["GET", "POST"])
@login_required
def new_upload():
    form = UploadForm()

    if request.method=="POST":
        file = request.files['data']
        if file.filename == '':
            flash('No file selected for upload')
            return redirect(request.url)
        else:

            path = os.path.join(current_app.root_path, 'static/documents', file.filename)
            file.save(path)
            if form.validate_on_submit():
                content=file.read(10240)
                upload = Upload(title=form.title.data, name=file.filename, data=content, author=current_user)
                db.session.add(upload)
                db.session.commit()

                flash("Your document has been uploaded successfully!", "success")
                return redirect(url_for("main.documents"))
    return render_template("create_upload.html",
    title='New Upload', form=form, legend="New Upload")

@uploads.route("/upload/<upload_id>", methods=["GET", "POST"])
def upload(upload_id):
    upload = Upload.query.get_or_404(upload_id)
    return render_template("upload.html", title=upload.title, upload=upload)

@uploads.route("/user/<string:username>")
def user_uploads(username):
    page = request.args.get('page', 1, type=int)
    user =  User.query.filter_by(username=username).first_or_404()
    uploads  = Upload.query.filter_by(author=user).order_by(Upload.date_posted.desc()).paginate(page=page, per_page=5)
    return render_template("user_uploads.html", uploads=uploads, user=user)


@uploads.route("/upload/<upload_id>/update", methods=["GET", "POST"])
@login_required
def update_upload(upload_id):
    upload = Upload.query.get_or_404(upload_id)

    if upload.author != current_user:
        abort(403)
    form = UploadForm()
    file = request.files['data']
    if form.validate_on_submit():
        upload.title = form.title.data
        upload.data = file.read(10240)
        upload.name = file.filename
        db.session.commit()
        flash("Your post has been updated", "success")
        return redirect(url_for("uploads.upload", upload_id=upload.id))
    elif request.method=="GET":
        form.title.data = upload.title
        form.data.data = upload.data

    return render_template("create_upload.html", title='Update Document', form=form, legend="Update Document")

@uploads.route("/upload/<upload_id>/delete", methods=["POST"])
@login_required
def delete_document(upload_id):
    upload = Upload.query.get_or_404(upload_id)

    if upload.author != current_user:
        abort(403)
    db.session.delete(upload)
    db.session.commit()
    flash("Your file was deleted", "success")
    return redirect(url_for("home"))
