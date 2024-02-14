# Questions

## Q: 使用 `virtualenv` 建立虛擬環境 #116
虛擬環境就是一個獨立的開發環境，可以解決不同應用程式使用不同版本的套件的問題，即時在同一台機器上運行，也不會互相影響。而`virtualenv`是 Python 用來建立虛擬環境的套件。

建立的流程（適用MacOS）：
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
接著在root目錄新增一個名為`.env`的檔案：
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
- 先安裝`Flask-Migrate`套件(最新版本4.0.5):
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

## Q: 如何用土炮的方式建立 Table？ #126

## Q: 什麼是密碼雜湊？如何使用 Python 實現？ #129