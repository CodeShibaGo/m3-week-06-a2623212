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

## Q: 如何使用 Flask-SQLAlchemy 連接上 MySQL？ #123

## Q: Flask-Migrate 如何使用？ #124

## Q: 如何使用 SQLAlchemy 下 Raw SQL？ #125

## Q: 如何用土炮的方式建立 Table？ #126

## Q: 什麼是密碼雜湊？如何使用 Python 實現？ #129