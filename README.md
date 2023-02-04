## django-sekdilu139
Membangun aplikasi online Sekdilu 139
Github: https://github.com/gurnitha/django-sekdilu139


## 01. Setup

#### 01.1 Create django project and app

        modified:   README.md
        new file:   _docs/db-skema.py
        new file:   apps/sekdilu139/__init__.py
        new file:   apps/sekdilu139/admin.py
        new file:   apps/sekdilu139/apps.py
        new file:   apps/sekdilu139/migrations/__init__.py
        new file:   apps/sekdilu139/models.py
        new file:   apps/sekdilu139/tests.py
        new file:   apps/sekdilu139/views.py
        new file:   config/__init__.py
        new file:   config/asgi.py
        new file:   config/settings.py
        new file:   config/urls.py
        new file:   config/wsgi.py
        new file:   manage.py


## 02. Create Django Model

#### 02.1 Create Category model

        modified:   README.md
        modified:   apps/sekdilu139/admin.py
        new file:   apps/sekdilu139/migrations/0001_initial.py
        modified:   apps/sekdilu139/models.py

#### 02.2 Create SubCategory model

        modified:   README.md
        modified:   apps/sekdilu139/admin.py
        new file:   apps/sekdilu139/migrations/0002_alter_category_options_alter_category_slug_and_more.py
        modified:   apps/sekdilu139/models.py

#### 02.3 Create Rank model

        modified:   README.md
        modified:   apps/sekdilu139/admin.py
        new file:   apps/sekdilu139/migrations/0003_alter_category_slug_alter_subcategory_slug_rank.py
        new file:   apps/sekdilu139/migrations/0004_alter_category_options_alter_rank_options_and_more.py
        new file:   apps/sekdilu139/migrations/0005_alter_category_slug_alter_rank_slug_and_more.py
        modified:   apps/sekdilu139/models.py

#### 02.4 Create Person model

        modified:   README.md
        modified:   apps/sekdilu139/admin.py
        new file:   apps/sekdilu139/migrations/0006_person_person_sekdilu139__publish_7747e8_idx.py
        new file:   apps/sekdilu139/migrations/0007_person_image_alter_person_slug.py
        modified:   apps/sekdilu139/models.py
        new file:   media/person/cat-1.png


## 03. Create Pages

#### 03.1 Create home page

        modified:   README.md
        new file:   apps/sekdilu139/urls.py
        modified:   apps/sekdilu139/views.py
        modified:   config/settings.py
        modified:   config/urls.py
        new file:   templates/sekdilu139/index.html

#### 03.2 Add template and static files to home page

        modified:   .gitignore
        modified:   README.md
        modified:   config/settings.py
        modified:   templates/sekdilu139/index.html

#### 03.3 Template inheritance and mdify home page

        modified:   README.md
        new file:   templates/base.html
        modified:   templates/sekdilu139/index.html

#### 03.4 Rendering person and sosmed objects to home page

        modified:   README.md
        modified:   apps/sekdilu139/admin.py
        new file:   apps/sekdilu139/migrations/0008_remove_person_sosmed_person_is_facebook_and_more.py
        new file:   apps/sekdilu139/migrations/0009_sosmed_remove_person_is_facebook_and_more.py
        new file:   apps/sekdilu139/migrations/0010_sosmed_url.py
        new file:   apps/sekdilu139/migrations/0011_alter_sosmed_name.py
        modified:   apps/sekdilu139/models.py
        modified:   apps/sekdilu139/views.py
        modified:   config/settings.py
        modified:   config/urls.py
        modified:   templates/base.html
        modified:   templates/sekdilu139/index.html
        new file:   uploads/media/person/1.jpg

        NOTE:

        1. Removed sosmed status fields from Person model
        2. Created Sosmed model
        3. In Person field, add sosmed_id field with ManyToMany rel with Sosmed model

#### 03.5 Create detail page

        modified:   README.md
        new file:   apps/sekdilu139/migrations/0012_remove_person_pengalaman_alter_person_about_me_and_more.py
        new file:   apps/sekdilu139/migrations/0013_person_keluarga.py
        new file:   apps/sekdilu139/migrations/0014_person_pilosofi.py
        new file:   apps/sekdilu139/migrations/0015_rename_pilosofi_person_filosofi.py
        modified:   apps/sekdilu139/models.py
        modified:   apps/sekdilu139/urls.py
        modified:   apps/sekdilu139/views.py
        modified:   config/settings.py
        modified:   config/urls.py
        new file:   templates/sekdilu139/detail.html
        modified:   templates/sekdilu139/index.html
        new file:   uploads/media/person/berlian.PNG

#### 03.6 Modified footer

        modified:   README.md
        modified:   templates/base.html

#### 03.7 Create requirements.txt file

        modified:   README.md
        new file:   requirements.txt
        new file:   venv3941/Scripts/Activate.ps1
        new file:   venv3941/Scripts/activate
        new file:   venv3941/Scripts/activate.bat
        new file:   venv3941/Scripts/deactivate.bat
        new file:   venv3941/Scripts/django-admin.exe
        new file:   venv3941/Scripts/pip.exe
        new file:   venv3941/Scripts/pip3.10.exe
        new file:   venv3941/Scripts/pip3.9.exe
        new file:   venv3941/Scripts/pip3.exe
        new file:   venv3941/Scripts/python.exe
        new file:   venv3941/Scripts/pythonw.exe
        new file:   venv3941/Scripts/sqlformat.exe
        new file:   venv3941/pyvenv.cfg

#### 03.8 Removing (docs) from the project folder

        modified:   README.md
        1. Removing _docs
        deleted:    _docs/db-skema.py
        
        2. Modified url path
        modified:   apps/sekdilu139/urls.py

        from    :path('/<slug>/'
        to      :path('<slug>/'


## 04. DEPLOYMENT


#### 04.1 Setting up for deployment

        1. Modified
        modified:   README.md
        modified:   .gitignore
        
        2. Add static root
        modified:   config/settings.py

        STATIC_ROOT = os.path.join(BASE_DIR, 'static')
        
        3. Add static files
        new file:   config/static/assets/css/bootstrap.min.css
        ... 
        new file:   config/static/assets/php/form-process.php

        4. Configure static root path
        modified:   config/urls.py

        urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)