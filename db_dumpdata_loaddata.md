# db.sqlite3をdumpdataして、review_test_db.sqlite3にloaddataするまでの流れ
**シェルスクリプトでコマンドをまとめました**
## webappコンテナのbashを使う
```
./webapp_bash.sh
```
## db.sqlite3をdumpdataする
```
./webapp_dumpdata.sh
```
## review_test_db.sqlite3にloaddataする
```
./webapp_loaddata.sh
```