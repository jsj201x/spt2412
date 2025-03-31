from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import requests
import json

app = Flask(__name__, template_folder='templates')

app.config.from_pyfile('settings.py')
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(50))
    password = db.Column(db.String(50))















@app.route('/')
def data():
    # new_user = User(name='John_Doe', email='johndoe@example.com', password='123456')
    # db.session.add(new_user)



    # new_user = User.query.all()
    # new_user = User.query.get(2)
    # new_user = User.query.filter_by(email='<EMAIL>').all()
    # db.session.delete(new_user)
    # print(new_user)
    # page = 1
    # per_page = 10
    # pagination = User.query.paginate(page=page, per_page=per_page)
    # users = pagination.items
    # return render_template('data.html', users=users, pagination=pagination)

    rol=User.query.get(1)
    print(rol.id)




    db.session.commit()
    return render_template('dataindex.html')


@app.route('/index/')
def index():

    return render_template('index.html')


@app.route('/inde_data/')
def index_data():
    ename = request.args.get('username')
    print(ename)

    jobName = 'python'
    # 构建请求头
    headers = {
        # 应用授权  Authorization
        "Authorization": 'Bearer pat_IDz0YvcRFAepH6SaHzZ75o5VTqYtDqWI5Hb4ZK9dlE63d2Ze8mh1NUcobRnbQFIS',  # 请替换为您的应用授权
        'Content-Type': 'application/json'  # 请求数据格式为json
    }
    payload = {
        "workflow_id": "7486396768991068200",  # 请替换为您的工作流ID
        "parameters": {'input': ename},  # 将input_text传递给input参数
        "app_id": "7486376923577729036"  # 请替换为您的应用ID
    }
    response = requests.post(
        'https://api.coze.cn/v1/workflow/run',  # 请求地址
        headers=headers,
        json=payload)
    if response.ok:
        print('请求数据成功')
        res = response.text
        dic = json.loads(res)
        dic1 = dic['data']
        # print(dic1)
        data = []
        jobdata = json.loads(dic1)['output']
        print(jobdata)
        for i in jobdata:
            print(i['address'])
            print(i['appUrl'])
            print(i['companyName'])
            print(i['name'])

    return render_template('index_data.html',jobdata=jobdata)


# 简历分析
@app.route('/inde_fx/')
def index_data_json():
    return render_template('index_fx.html')


# 建立分析结果
@app.route('/fx_jg/')
def index_data_json_jg():
    return render_template('index_fx_jg.html')


# 面试
@app.route('/index_ms/')
def index_ms():
    return render_template('index_ms.html')


# 面试问题
@app.route('/ms_wt/')
def index_ms_wt():
    return render_template('index_ms_wt.html')


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run()
