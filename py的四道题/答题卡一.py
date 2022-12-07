import xlrd
import tkinter.messagebox

import pyautogui
import pyperclip
import time

if __name__=="__main__":
    #读取文档
    # workbook = xlrd.open_workbook("未做核酸学生名单2022.7.15.xlsx")
    #获取工作表

    #table = workbook.sheets()[0]
    #tmp=tkinter.messagebox.showwarning("Confirm your Wechat Client Hotkeys and Other Warnings","Open MainWindow: Crtl+Alt+V;\nSend Message: Ctrl+Enter.\nAll messages are to be sent via WeChat,\nbut students' accounts are found by searching their phone numbers, so tell them to enable relavant features.")
    #tmp=""
    
    i=1
    while(1):
        # try:
        #     row=table.row_values(i)
        # except:
        #     break
        
        # name=row[0]
        msg="庞开升"+"做核酸了没，三点前务必完成哈。"
        phoneNUM=13305401576
        pyautogui.hotkey("ctrl","alt","v")
        pyperclip.copy(str(int(phoneNUM)))
        pyautogui.hotkey("ctrl","f")
        pyautogui.hotkey("ctrl","v")
        pyautogui.hotkey("enter")
        time.sleep(0.2)
        pyautogui.hotkey("down")
        pyautogui.hotkey("up")
        pyautogui.hotkey("enter")
        time.sleep(0.5)
        pyperclip.copy(msg)
        time.sleep(0.5)
        pyautogui.hotkey("ctrl","v")
        time.sleep(0.5)
        pyautogui.hotkey("ctrl","enter")
        i+=1
        #停止一秒
    
        time.sleep(12)
    print("OK")
