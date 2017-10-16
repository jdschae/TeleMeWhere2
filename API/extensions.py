import pymysql
import pymysql.cursors
import config

url_secret = ''

def connect_to_database():
  options = {
    'host': config.env['host'],
    'user': config.env['user'],
    'passwd': config.env['password'],
    'db': config.env['db'],
    'cursorclass' : pymysql.cursors.DictCursor
  }
  db = pymysql.connect(**options)
  db.autocommit(True)
  return db

db = connect_to_database()
