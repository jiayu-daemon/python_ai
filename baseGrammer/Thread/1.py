'''
如果你打算编写多进程的服务程序，Unix/Linux无疑是正确的选择。由于Windows没有fork调用，
难道在Windows上无法用Python编写多进程的程序？由于Python是跨平台的，自然也应该提供一
个跨平台的多进程支持。multiprocessing模块就是跨平台版本的多进程模块。
'''
# import os
# print('Process (%s) start...' % os.getpid())
# pid = os.fork()
# if pid == 0:
# 	print('I am child (%s) and my parent is %s.' % (os.getpid(),os.getppid()))
# else:
# 	print('I (%s) just created a child proces (%s).' % (os.getpid(),pid))
from multiprocessing import Process
import os

# 子进程要执行的代码
def run_proc(name):
    print('Run child process %s (%s)...' % (name, os.getpid()))

if __name__=='__main__':
    print('Parent process %s.' % os.getpid())
    p = Process(target=run_proc, args=('test',))
    print('Child process will start.')
    p.start()
    p.join()
    print('Child process end.')