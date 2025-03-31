host='0.0.0.0',
debug=True,
port=5000
SQLALCHEMY_DATABASE_URI='mysql://root:123456@127.0.0.1:3306/flask_data'
#每次请求结束后自动提交数据库
SQLALCHEMY_COMMIT_ON_TEARDOWN = True
#保证数据库和模型类同步
SQLALCHEMY_TRACK_MODIFICATIONS=True


