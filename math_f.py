
x = 0
y = 0
q = 0


def init(a, b, c):
    global x
    global y
    global q
    x = a
    y = b
    q = c


def write():
    with open('directory.txt', 'a') as data:
        data.write(x+' '+y+' '+q)
        data.write('\n')
      
# def read():
#      with open('directory.txt', 'r') as data:
#          new_fix = gui.get_value()
#          data.read(new_fix)
#     return

#     q='+'.join(map(str, mylist_all))
# with open('file20.total.txt', 'w') as data:
#     data.write(q)
