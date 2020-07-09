


import threading

import os,subprocess


def fun():

    cur_dir = os.path.dirname(os.path.abspath(__file__))
    print('**********',cur_dir)
    case_dir = cur_dir + "\\" + 'case'
    goal = ['test1.py','test2.py']

    def run_py(name):
        print('run py start')
        subprocess.run(r"python C:\Users\Administrator\PycharmProjects\practice\work\case\%s" % name)
        print('run py end')

    tlist = []
    for i in goal:
        t = threading.Thread(target=run_py,args=(i,))
        t.setDaemon(True)
        tlist.append(t)


    for i in tlist:

        i.start()

    for i in tlist:

        i.join()





    print('主线程结束')


if __name__ == '__main__':
    fun()