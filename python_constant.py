#python_constant.py

def constant(f):
    def setter(self, value):
        print("Error: Cannot reassign value to constant variable")
        raise TypeError()
    def getter(self):
        return f()
    return property(getter, setter)

class _Const(object):
    @constant
    def pi():
        return 3.14
    @constant
    def FOO():
        return 0xBAADFACE
    @constant
    def BAR():
        return 0xDEADBEEF

CONST = _Const()

print(hex(CONST.FOO))  # -> '0xbaadfaceL'

#CONST.FOO = 0

print(CONST.pi)
CONST.pi = "Pangam"