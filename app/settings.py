from pathlib import Path

# ベースディレクトリの設定
BASE_DIR = Path(__file__).resolve().parent.parent

# セキュリティキー
SECRET_KEY = 'django-insecure-%!j(5h+vru*9=gyyo)*w4#ftknk5(_9sxisaki(-*!x=9p+)ac'

# デバッグモード (開発時は True, 本番環境では False)
DEBUG = True

# 許可するホスト
ALLOWED_HOSTS = ['localhost', 'app.local', '0.0.0.0']

# インストール済みアプリケーション
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # 必要に応じて自作アプリを追加
    'app',  # Django アプリケーションを指定
]

# ミドルウェア設定
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# ルートURL設定
ROOT_URLCONF = 'app.urls'  # **この行を追加**

# テンプレート設定
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # 必要に応じて 'templates' フォルダを作成
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# WSGIアプリケーション
WSGI_APPLICATION = 'app.wsgi.application'

# データベース設定
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'lalatalk_db',
        'USER': 'lalatalk_user',
        'PASSWORD': 'Password@12345',
        'HOST': 'lalatalk-db',
        'PORT': '3306',
    }
}

# タイムゾーンとタイムスタンプ設定
TIME_ZONE = 'Asia/Tokyo'
USE_TZ = True

# 静的ファイルの設定
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'

# メディアファイルの設定
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# デフォルトのフィールド設定
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
