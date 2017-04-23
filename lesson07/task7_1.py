# l = [(i,j) for i in range(5) for j in range(5,10) if i + j == 10]
# print l
# print [(i,j) for i in range(5) for j in range(5,10) if i + j == 10]
# t = ((i,j) for i in range(5) for j in range(5,10) if i + j == 10)
# print t, dir(t)
# print t.next()
# print t.next()
# # t.close()
# print t.next()
#
# # def my_range(n):
# #     print "start"
# #     count = 0
# #     l = []
# #     while (count < n):
# #         l.append(count)
# #         count += 1
# #     return l
# # print my_range(8)
#
# def my_xrange(n):
#     print "start"
#     count = 0
#     while (count < n):
#         print "b_step: " + str(count)
#         yield count
#         print "a_step: " + str(count)
#         count += 1
#     print "end"
#
# g = my_xrange(8)
#
# print g
# print g.next()
# print "-"*33
# print g.next()
# for i in g:
#     print i
# # print g.next()
# print g1.next()
# print g1.next()
#
# # hw : make own generator
#
#  decorator

def my_f(func):
    def wraper():
        return func

    print "start"
    t = wraper()
    res = t()
    print "end", t
    return t

#     return func
# print my_f("hfggf")
# print "-"*33
# def foo():
#     return 1+1
#
# print foo()
# print "-"*33
#
@my_f
def foo2():
    print "foo2 - start"
    return 2+2
print foo2()
