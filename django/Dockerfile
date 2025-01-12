FROM python:3.11-slim

# タイムゾーンと作業ディレクトリ設定
ENV TZ=Asia/Tokyo
WORKDIR /app

# 必要な依存パッケージをインストール
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        mariadb-client \
        libmariadb-dev \
        gcc \
        python3-dev \
        netcat-openbsd \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Pythonパッケージのインストール
COPY ./requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# アプリケーションコードのコピー
COPY . /app

# デフォルトコマンド
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]