# 定义常量的py文件
# 这样的定义方式符合“命名全部为大写”和“值一旦绑定便不可再修改”这两个条件

class _const:
    class ConstError(TypeError): pass
    class ConstCaseError(ConstError): pass
    def __setattr__(self, name, value):
        if self.__dict__.has_key(name):
            raise self.ConstError, "Can't change const.%s" % name
        if not name.isupper():
            raise self.ConstCaseError, \
                  'const name "%s" is not all uppercase' % name
        self.__dict__[name] = value
import sys
sys.modules[__name__]=_const()
import const
const.MY_CONSTANT = 1
const.MY_SECOND_CONSTANT = 2
const.MY_THIRD_CONSTANT = 'a'
const.MY_FORTH_CONSTANT = 'b'
