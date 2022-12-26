import os
from flask import Flask, request, send_from_directory, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_ckeditor import CKEditor
from flask_ckeditor import upload_success, upload_fail
from flask_wtf.csrf import CSRFProtect

db = SQLAlchemy()
ckeditor = CKEditor()
csrf = CSRFProtect()

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile("config/dev.py")

    db.init_app(app)
    ckeditor.init_app(app)
    csrf.init_app(app)

    from .routes import index, blog

    app.register_blueprint(index.bp, url_prefix="/")
    
    app.register_blueprint(blog.category_bp)
    app.register_blueprint(blog.post_bp)

    app.register_blueprint(blog.category_api)
    app.register_blueprint(blog.post_api)



    # Category va Post uchun
    @app.route('/uploads/<path:path>')
    def send_report(path):
        return send_from_directory('uploads', path)





    # CKEDITOR get file
    @app.route('/files/<filename>')
    def uploaded_files(filename):
        path = app.config['UPLOADED_PATH']
        return send_from_directory(path, filename)


    # CKEDITOR upload
    @app.route('/upload', methods=['POST'])
    def upload():
        f = request.files.get('upload')
        extension = f.filename.split('.')[-1].lower()
        if extension not in ['jpg', 'gif', 'png', 'jpeg']:
            return upload_fail(message='Image only!')
        f.save(os.path.join(app.config['UPLOADED_PATH'], f.filename))
        url = url_for('uploaded_files', filename=f.filename)
        return upload_success(url, filename=f.filename)

    with app.app_context():
        db.create_all()
  

    

    
    return app
