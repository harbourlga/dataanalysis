# -*- coding: utf-8 -*-
# # def yield_test(n):
# #     for i in range(n):
# #         yield call(i)
# #
# #     print("i=",i)
# #     print("do something.")
# #     print("end.")
# #
# # def call(i):
# #     return i*2
# #
# #
# # for i in yield_test(5):
# #     print(i,",")
#
#
#
# # def yield_example(n):
#
# #     for i in range(n):
# #         yield i+1
# #         print("you")
#
# #
# #
# # for i in yield_example(10):
# #     print(i)
# #
# #
# # def args_example(x, *args, **kwargs):
# #     print(x)
# #     print(args)
# #     print(kwargs)
# #
# # args_example(1, 2, 'b', a=2)
# print 1
# import PyV8
#
#
# ctxt = PyV8.JSContext()
# ctxt.enter()
# func = ctxt.eval("""
#     (function(){
#         function hello(){
#             return "Hello world.";
#         }
#         return hello();
#     })
# """)
# print func()
#

data = [{'a':4},{'b':5},{'c':5},{'d':5},{'e':5}]
for i in range(1,len(data)):
    print(i)

print(data[0])

