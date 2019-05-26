

#管理员可以访问的api
class AdminScope:
    allow_api = ['mobile.super_get_User']

#用户可以访问的api
class UserScope:
    allow_api = []

def is_in_scope(scope, endpoint):
    gl = globals()
    scope = globals()[scope]()

    if endpoint in scope.allow_api:
        return True
    else:
        return False