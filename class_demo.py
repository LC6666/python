# -*- coding:utf-8 -*-
class DemoClass:
    def __init__(self):
        print("鍒濆鍖�")

    def output(self,text):
        #杈撳嚭text鍒癱onsole
        print(text)

    def output_none(self):
        #涓嶅甫鍙傛暟鐨勬柟娉�
        print("鎴戜笉鑳戒紶鍏ュ弬鏁�")

 # 缁ф壙DemoClass
class ChildDemoClass(DemoClass):
    def __init__(self):
        print("鎴戞槸瀛愮被")

    def output_none(self):
        print("鎴戞槸瀛愮被涓嶈兘浼犲弬鐨勬柟娉�")

if  __name__=="__main__":
    # 鍒涢�犱竴涓被瀵硅薄
    demo_obj = DemoClass()

    # 璋冪敤output
    demo_obj.output("鎴戞槸鍙傛暟")
    # 璋冪敤output_none
    demo_obj.output_none()
    print("---------------------------------------")

    # 鍒涘缓瀛愮被鐨勫璞�
    child_obj = ChildDemoClass()
    # 璋冪敤output, 璋冪敤鐨勬槸鐖剁被鐨勬柟娉�
    child_obj.output("鎴戞槸閫氳繃瀛愮被璋冪敤鐨勫弬鏁�")
    # 璋冪敤output_none, 璋冪敤鐨勬槸鑷繁鐨勬柟娉曪紝鍗抽噸鍐欏悗鐨勬柟娉�
    child_obj.output_none()