import re
from tkinter import (END, Button, Entry, Label, LabelFrame, StringVar, Tk,
                     filedialog, scrolledtext)

from tqdm.tk import tqdm_tk, ttk


class MainTk:

    def __init__(self):
        tk = Tk()
        tk.title('看电影')
        self.tk = tk
        self.path_v = StringVar()

        # tk.geometry('700x500')

        # 输出路径
        lf1 = LabelFrame(tk, width=800, height=50)
        lf1.grid(row=0, column=0, padx=5, pady=5)

        lbl_path = Label(lf1, text='输出路径', font=('微软雅黑', 12), padx=4)

        lbl_path.place(x=4, y=10)
        txt_path = Entry(lf1, textvariable=self.path_v, width=80)
        txt_path.place(x=87, y=10)
        btn_path = Button(lf1, text='选择....', command=self.open_file)
        btn_path.place(x=700, y=8)

        # 下载地址
        lf2 = LabelFrame(tk, width=800, height=240)
        lf2.grid(row=1, column=0, padx=5, pady=5)

        lbl_url = Label(lf2, text='下载地址', font=('微软雅黑', 12), padx=4)
        lbl_url.place(x=4, y=8)
        self.txt_url = scrolledtext.ScrolledText(lf2, width=80)
        self.txt_url.place(x=87, y=10, height=200)
        btn_url = Button(lf2, text='开始下载', command=self.get_urls)
        btn_url.place(x=700, y=8)

        # 日志

        self.txt_res = scrolledtext.ScrolledText(tk, width=110)
        self.txt_res.grid(row=2, column=0, padx=5, pady=5)

        self.processbar = ttk.Progressbar(tk)
        self.processbar.grid(row=3, column=0, padx=5, pady=5)

        self.set_urls()

    def open_file(self):
        txt = filedialog.askdirectory()
        if not txt:
            return
        self.path_v.set(txt)

    def get_urls(self):
        url_raw = self.txt_url.get("0.0", "end")
        url_raw.split()
        urls = re.split(r'\s+', url_raw.strip())
        print(url_raw, urls)

        self.out(url_raw)

    def out(self, url_raw):
        for i in tqdm_tk(range(20), total=20, desc='1212', colour='yellow'):
            self.txt_res.config(state='normal')
            self.txt_res.insert(END, url_raw)
            self.tk.update_idletasks()
            self.txt_res.see(END)
            self.txt_res.config(state='disabled')
            # self.tk.after(1000, self.out, url_raw, t)

    def set_urls(self):
        self.txt_url.delete('0.0', END)
        self.txt_url.insert('0.0', '1\n2\n3\n4')


def main():

    app = MainTk()

    app.tk.mainloop()


if __name__ == '__main__':
    main()
