# db.sqlite3をdumpdataして、review_test_db.sqlite3にloaddataするまでの流れ
**シェルスクリプトでコマンドをまとめました**

まずは必要なファイルを取得する

ec2に接続して別の場所にこのリポジトリをクローンする

クローンした後、oza_dev2にチェックアウト

```
git fetch
```
```
git branch oza_dev2 remotes/origin/oza_dev2
```
```
git checkout oza_dev2
```

<br>
このフォルダからcpコマンドを利用して、

- change_db_name.py
- webapp_bash.sh
- webapp_dumpdata.sh
- webapp_loaddata.sh

を自分のプロジェクトフォルダに持ってくる

<br>
自分のプロジェクトフォルダにて

mainブランチの.gitignoreにreview_test_db_sqlite3を追加したからプル忘れずに

```
git fetch
```
```
git pull
```

webappコンテナのbashを使う

```
./webapp_bash.sh
```

db.sqlite3をdumpdataする

```
./webapp_dumpdata.sh
```

review_test_db.sqlite3にloaddataする

```
./webapp_loaddata.sh
```
