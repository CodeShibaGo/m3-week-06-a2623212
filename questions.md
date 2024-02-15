# Questions

## Q: 使用 `virtualenv` 建立虛擬環境 #116

虛擬環境就是一個獨立的開發環境，可以解決不同應用程式使用不同版本的套件的問題，即時在同一台機器上運行，也不會互相影響。而`virtualenv`是 Python 用來建立虛擬環境的套件。

建立的流程（適用 MacOS）：

1. 第一步先安裝 python
2. 利用 python 提供的套件管理工具`pip`安裝`virtualenv`:

```
pip install virtualenv
```

3. 看到成功安裝字樣後，進入專案資料夾，並用以下的指令自訂一個虛擬環境（自訂：venv01）

```
virtualenv venv01

# 如果有多個python的直譯器版本
virtualenv -p python[這裡可以指定python的版本] venv01

#也可以用這個指令
python -m venv venv01
```

4. 啟動虛擬環境，在 terminal 會發現路徑前面有（venv01）

```
$ source ./venv01/bin/activate
```

5. 離開虛擬環境

```
deactivate
```

## Q: python-dotenv 如何使用？ #119

`python-dotenv`可以讀取`.env`的內容，設定環境變數，這樣就不用每執行一次都要重新設定環境變數。
首先，必須先安裝 python-dotenv 套件：

```
(venv) $ pip install python-dotenv
```

接著在 root 目錄新增一個名為`.env`的檔案：

```
.
├── .env
└── app.py
```

接著在`app.py`檔案裡 import 套件：

```python=
from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.
```

最後，因為環境變數也可以儲存私密的資料，例如密碼或驗證資料，所以安全的作法並不適合推到 gitHub 上讓大家存取，所以要講`.env`加到`.gitignore`就不會被 git 追蹤。

[參考資料](https://github.com/theskumar/python-dotenv)

`- 說出 .env 跟 .flaskenv 的差別是？`
相同點是`.flaskenv` 和`.env`這兩個檔案都是用來儲存環境變數，但是：

- `.flaskenv`作用於 Flask，而`.env`則是 Python 的通用套件，作用範圍比較廣。
- `.flaskenv`包含預設的環境變數，如`FLASK_APP`，而`.env`沒有預設的變數。
- `.flaskenv`可以直接被 Flask 讀取，而`.env`需要在檔案中寫入 import。
- 用 flask 開發 2 者可以共存，在 flask 的文件中，建議：
  > .flaskenv should be used for** public variables**, such as FLASK_APP, while .env should not be committed to your repository so that it can set **private variables**.

[參考資料](https://flask.palletsprojects.com/en/3.0.x/cli/#environment-variables-from-dotenv)

## Q: 如何使用 Flask-SQLAlchemy 連接上 MySQL？ #123

Flask 沒有內建資料庫，所以可以自己選擇適合的資料庫來連接，以下是連接上`MySQL`的方法：

- 首先，使用要使用`Flask-SQLAlchemy`套件。

```
(venv) $ pip install flask-sqlalchemy
```

- 接著，要在本機環境中安裝 MySQL 資料庫（已經完成）
- 下一步，安裝`PyMySQL`套件，讓 python 操作 MySQL 的套件。

```
$ pip install PyMySQL
```

- 完成套件安裝之後，要來設定「配置」 config。

```
app.config['SQLALCHEMY_DATABASE_URI'] = mysql://{username}:{username}@localhost:{port}/project
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
```

運作起來沒有噴錯， 應該就正確了。
[參考資料](https://medium.com/seaniap/python-web-flask-flask-sqlalchemy%E6%93%8D%E4%BD%9Cmysql%E8%B3%87%E6%96%99%E5%BA%AB-2a799acdec4c)

## Q: Flask-Migrate 如何使用？ #124

`Flask-Migrate`的用途是使用在 flask 和 SQLAlchemy 中，當有需要調整資料庫的時候，不需要全部刪掉、重新`db.create_all`，可以只將 Model 更動過的部分 migrate 到資料庫的 table 中。

- 先安裝`Flask-Migrate`套件(最新版本 4.0.5):

```
$ pip install Flask-Migrate
```

- 在 python 檔案中匯入套件：

```python
from flask_migrate import Migrate
migrate = Migrate(app, db)

```

- 接著初始化 migrations 創建更新資料夾

```
$ flask db init
flask db migrate -m "版本控制訊息"
```

- 完成資料庫的更新

```
flask db upgrade
```

成功在 flask 連接 MySQL 建立一個 Users Table!
[參考資料](https://github.com/miguelgrinberg/flask-migrate)

## Q: 如何使用 SQLAlchemy 下 Raw SQL？ #125

承接上面的內容，在安裝好`SQLAlchemy `的狀態下：

```python
from sqlalchemy import text
sql = text('select * from users')
with app.app_context():
    result = db.session.execute(sql)
    print(result.fetchall())
```

其中，`with app.app_context()`要確保在執行這資料庫操作時，flask app 是正在運行的，這是我在錯誤訊息中得到的。查看資料似乎是和 flask 的上下文有關。

`db.session.execute`是原生`SQLAlchemy`用來 Execute a SQL expression construct，會回傳執行結果的物件。可以用`text()`API 來建構一個 SQL 字串。

如果沒有加`fetchall()`結果是：

```
<sqlalchemy.engine.cursor.CursorResult object at 0x105084fa0>
```

有加`fetchall()`結果是：

```
[(1, 'Abby', 'abby@gmail.com', '0933929323'), (2, 'Benny', 'Benny@gmail.com', '0911929323'), (3, 'Cassy', 'cassy@gmail.com', '0911787434')]

```

> `fetchall()`Fetches all (remaining) cases from the active dataset, or if there are splits, the remaining cases in the current split. If there are no remaining rows, the result is an empty tuple. [Reference 1](https://www.ibm.com/docs/en/spss-statistics/29.0.0?topic=python-fetchall-method) || [Reference 2](https://magazine.techacademy.jp/magazine/47802#ta-toc-2)

[參考資料](https://juejin.cn/s/flask%20sqlalchemy%E6%89%A7%E8%A1%8C%E5%8E%9F%E7%94%9Fsql)

## Q: 如何用土炮的方式建立 Table？ #126

和前面的方式相同，也是使用`db.session.execute`語法：

```python
with app.app_context():
    sql = text("""\n  CREATE TABLE members (email VARCHAR(50),
    first_name VARCHAR(50),last_name VARCHAR(50),passwd VARCHAR(50) )""")
    db.session.execute(sql)
```

成功訊息：

```
-- 2024-02-15 18:26:27.5660
SELECT
  data_length AS `data_size`,
  index_length AS `index_size`,
  (data_length + index_length) AS `total_size`,
  table_comment AS `comment`
FROM
  information_schema.TABLES
WHERE
  table_schema = "MicroBlogData"
  AND table_name = "members";
```

## Q: 用 SQLAlchemy 下第一個 Raw SQL #127

依序回答下面的問題：

#### 了解什麼是 Raw SQL？

Raw SQL，也可以寫作 native SQL，我將它解釋為 SQL 的原始語法，用來操作資料庫，和資料庫互動，也就是前幾週學習的主要內容。相對`Raw SQL`，我們用的`SQLAlchemy`通過`ORM`技術結合物件導向的作法，可以更簡化的進行資料庫操作。

#### 了解如何用 SQLAlchemy 下 Raw SQL

參見`#125`的回答。

#### 試著比較其中的優缺點？

兩種都是第一次寫，所以體感上沒有什麼感覺，所以綜合找資料的時候看到其他人的文章，有一篇文章的觀點比較符合我的想像：「永遠記得同時使用 raw SQL queries 和 ORMs」。
`raw SQL queries`具有提供靈活性、效能最佳化以及使用進階資料庫存取的功能；而`ORM`簡化了常見的資料庫操作，提供物件 mapping 功能，還協助組織程式碼，而且他還可以透過自動處理 input 機制，為資料庫加一道安全層。

## Q: 什麼是密碼雜湊？如何使用 Python 實現？ #129

- 了解什麼是密碼雜湊:
它是用來將「不同」長度的輸入，轉換成「相同」長度的輸出，其輸出叫做「雜湊值（hash value）」，他的特性是單向而且不可逆。使用同一個雜湊函數算出來的結果會一樣。

- 如何使用 **Werkzeug 進行密碼雜湊**
    - **generate_password_hash 的功用是？**
    它的功用是對傳進來的資料進行雜湊運算，並且回傳一組雜湊密碼，和普通的密碼雜湊不同處是，它經過進一步的加鹽（即隨機產生、長度不固定、每次皆使用不同鹽），所以：**即使傳進去的是一樣的資料，也會產生不同的雜湊密碼**。
    ```
    hash = generate_password_hash(password)
    #回傳值：
    #第1次 scrypt:32768:8:1$cRKiHLD1wBEVidSf$4592ff6840e8a5e94ed564d6530651ab20b95ca1dd06f701e147cae8e449faa3ef0ee67b87f7be34d86de81573f77ee05c5939aecd2499a0bfe1e4d8e109d92b
    #第2次scrypt:32768:8:1$MM0uh4Z5RY1dSbgl$a9965dbce5fe224a47da551579b904bd79df3de8005a67ec6ae36ba4b623377015d4fa9d11b5fde5628cd14bfac88eaae62bfdb970378dc3480b8759c4257aa2
    ```
   - **check_password_hash 的功用是？**
    它的功用是接受之前生成的 hash 值以及原始數值，並進行運算匹配，根據匹配驗證結果，回傳布林值。
  ```
    print('answer1:',check_password_hash(hash, password))
    #回傳值：answer1: True
    print('answer2:',check_password_hash(hash,"Goodpassword"))
    #回傳值：answer1: False
   ```
