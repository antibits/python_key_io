#-*- coding:utf-8 -*-

import os,win32api,win32con,win32process,time,win32gui,win32event

def callback(hwnd, procid):
    if procid in  win32process.GetWindowThreadProcessId(hwnd):
        win32gui.SetForegroundWindow(hwnd)

def show_window_by_process(procid):
    win32gui.EnumWindows(callback, procid)
    
def input_password(passwd):
    for k in passwd:
        release_shift = False
        if k >= 'a' and k <= 'z':
            k = k.capitalize()
        elif k >='A' and k <= 'Z':
            win32api.keybd_event(win32con.VK_SHIFT,0,0,0)
            release_shift = True
        win32api.keybd_event(ord(k),0,0,0)
        win32api.keybd_event(ord(k),0,win32con.KEYEVENTF_KEYUP,0)
        if release_shift:
            win32api.keybd_event(win32con.VK_SHIFT,0,win32con.KEYEVENTF_KEYUP,0)
    win32api.keybd_event(win32con.VK_RETURN,0,0,0)
    win32api.keybd_event(win32con.VK_RETURN,0,win32con.KEYEVENTF_KEYUP,0)

proc_start_info = win32process.STARTUPINFO()
# proc_start_info.hStdOutput = win32api.GetStdHandle(win32api.STD_OUTPUT_HANDLE)
phandle, pid, thandle, tid = win32process.CreateProcess("""C:\Windows\System32\cmd.exe""", '', None, None, 0, win32process.CREATE_NEW_CONSOLE, None, None, proc_start_info)
print phandle, pid, thandle, tid

ret_code = win32event.WaitForSingleObject(phandle, 1000)
print "waite for single proc, ret code:",ret_code
try:
    show_window_by_process(pid)
except Exception, err:
    print err
else:
    input_password('PassWord')
    