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

## Q: Flask-Migrate 如何使用？ #124

## Q: 如何使用 SQLAlchemy 下 Raw SQL？ #125

## Q: 如何用土炮的方式建立 Table？ #126

## Q: 什麼是密碼雜湊？如何使用 Python 實現？ #129