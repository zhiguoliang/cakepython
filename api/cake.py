# _*_ coding: utf-8 _*_
# @Time : 2019/4/11 18:29
# @Author : lorenzo
import logging
import logging.handlers


from werkzeug.exceptions import HTTPException

from app import create_app
from app.libs.error import APIException
from app.libs.error_code import ServerError

app = create_app()

#日记记录

if app.config['DEBUG'] == True:

    formatter = logging.Formatter("%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s", "%Y-%m-%d %H:%M:%S")
    log_file_handler = logging.handlers.TimedRotatingFileHandler(filename="cake.log", when="D", interval=1, backupCount=1)
    log_file_handler.setFormatter(formatter)
    logging.getLogger().addHandler(log_file_handler)


@app.errorhandler(Exception)
def framework_error(e):

    if isinstance(e, APIException):
       return e

    if isinstance(e,HTTPException):

       code = e.code
       msg = e.description
       error_code = 1007
       return  APIException(msg,code,error_code)

    else:
       #日记 log的记录
       if not app.config["DEBUG"]:
          return ServerError()
       else:
           pass
          #记录堆栈到日记里
        # logging.exception('Got exception on main handler')
          #app.logger.info(e)




if __name__=='__main__':   #判定当前文件是否是入口文件
 app.run(debug=True )