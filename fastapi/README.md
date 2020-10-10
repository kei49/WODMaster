# fastapi

## ローカルでCloud SQL Proxyのセットアップ
```
gcloud auth login
~/cloud_sql_proxy -instances=playground-292105:us-central1-f:wod-master=tcp:3306
```

## データベースの初期化
```
pipenv shell
pipenv install
cd app
python initial_data.py
```