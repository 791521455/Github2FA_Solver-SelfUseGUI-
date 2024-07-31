import pyotp #Time-based One-Time Password
import tkinter as tk  #GUI
#API:2fa.show/2fa/HQ6KBMKBJ3IOLTBW
def SecretKeyGet():
    secret_key = labelEntry.get()
    return secret_key

def ValGet(secret_key):
    # print('请输入你的 密钥字符串 :')# HQ6KBMKBJ3IOLTBW
    # secret_key = input('Enter your secret key: ')
    totp = pyotp.TOTP(secret_key)
    val = totp.now()
    return val

def HitBotton ():
    global on_hit
    if on_hit == False:
        on_hit = True
        var.set(ValGet(SecretKeyGet()))
    else:
        on_hit = False
        var.set('再点一次||Click once again')

def CreatWindow():
    # 创建一个主窗口
    window = tk.Tk()
    # 设置窗口标题
    window.title("Github2FA_Solver(SelfUseGUI-1.0.0)")
    # 设置窗口大小
    window.geometry("450x500")
    # 创建一个标签，并设置其文本内容为"Github2FA_Solver"
    labelMainText = tk.Label(window, text="Github2FA_Solver", bg="white", fg="black", font=("Arial", 35), width=35,
                             height=2, relief="flat")
    # 提示labelEntry
    labelTipEntry = tk.Label(window, text="输入你的密钥字符串||Enter your secret key", bg="white", fg="black",
                        font=("Arial", 15), width=45, height=2, relief="ridge")
    # 文本输入框
    global labelEntry
    labelEntry = tk.Entry(window,bd=4,font=("Arial", 15), width=50, relief="ridge")
    # 提示labelOutput
    labelTipOutput = tk.Label(window, text='输出||Output', bg="white", fg="black",
                             font=("Arial", 15), width=45, height=2, relief="ridge")
    # 文本输出框
    global labelOutput
    global var
    var = tk.StringVar()
    labelOutput = tk.Entry(window,textvariable=var,bd=4, font=("Arial", 15), width=50, relief="ridge",state=tk.NORMAL,exportselection=1)
    # 按钮
    global on_hit
    on_hit = False
    labelButton = tk.Button(window,text='解密||Decrypt',height=2,command=HitBotton)
    # 创建一个简介
    labelTailText1 = tk.Label(window, text="采用 CC BY-NC-SA 4.0 许可协议。转载请注明来自 CS青椒！", bg="white", fg="black", font=("Arial", 12), width=50,
                             height=2, relief="flat")
    # 创建一个小提示
    labelTailText2 = tk.Label(window, text="有效期30s||Use in 30s", bg="white",
                             fg="black", font=("Arial", 12), width=50,
                             height=2, relief="flat")
    # 将标签添加到窗口中
    labelMainText.pack()
    labelTipEntry.pack()
    labelEntry.pack()
    labelTipOutput.pack()
    labelOutput.pack()
    labelButton.pack()
    labelTailText2.pack()
    labelTailText1.pack()
    # 运行主循环，等待用户交互
    window.mainloop()
def main():
    CreatWindow()
main()


