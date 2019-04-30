# _*_ coding: utf-8 _*_
# @Time : 2019/4/11 19:47
# @Author : lorenzo

class Redprint:
  def __init__(self, name):
     self.name = name
     self.mound = []

  def route(self, rule, **options):

      def decorator(f):
         self.mound.append((f, rule, options))
         return f
      return decorator

  def register(self, bp,url_prefix=None):
      print(self.name)
      if url_prefix is None:
          url_prefix = '/'+ self.name
      for f, rule, options in self.mound:
          endpoint = options.pop("endpoint", f.__name__)
          bp.add_url_rule(url_prefix+rule, endpoint,f, **options)



