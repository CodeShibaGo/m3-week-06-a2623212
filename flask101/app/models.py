from app import db, app
from sqlalchemy import text

sql = text('select * from users')

with app.app_context():
    result = db.session.execute(sql)
    print(result.fetchall())
