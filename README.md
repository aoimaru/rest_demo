# REST_DEMO
* Flaskで簡単なREST APIを実装しました。
* 取得、追加、更新、削除の基本的な機能を実装しました。

# URI設計
* GET /student : 全取得
* GET /student/{id} : 指定取得
* POST /student : 新規登録
* PUT /student/{id} : 更新
* DELETE /student/{id} : 削除

# Installation and Usage
```bash
git clone https://github.com/aoimaru/rest_demo
cd rest_demo
docker-compose up -d
docker inspect "databaseのコンテナID"
rest_demo_defaultネットワーク内でのdatabaseコンテナのIPアドレスをrun.pyでの
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{user}:{password}@{host}/{database}?charset=utf8'.format(
    **{
      'user': os.getenv('DB_USER', 'root'),
      'password': os.getenv('DB_PASSWORD', 'root'),
      'host': os.getenv('DB_HOST', '172.26.0.2'), <-ここに適用
      'database': os.getenv('DB_DATABASE', 'sample01'),
    })
```
# Author
* 中村碧海
* 立命館大学 情報理工学部
 
# License
# rest_demo
