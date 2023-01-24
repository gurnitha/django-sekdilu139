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