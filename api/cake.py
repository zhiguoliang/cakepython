# _*_ coding: utf-8 _*_
# @Time : 2019/4/11 18:29
# @Author : lorenzo
from app.app import create_app
app = create_app()

if __name__=='__main__':   #判定当前文件是否是入口文件
 app.run(debug=True)