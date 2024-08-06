import tkinter as tk
from tkinter import filedialog
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from webdav3.client import Client
import os
from threading import Thread

class FileUploaderApp(ttk.Window):
    def __init__(self):
        super().__init__(themename="darkly")
        self.title("WebDAV文件上传器")
        self.geometry("500x400")
        self.create_widgets()

    def create_widgets(self):
        self.file_path = tk.StringVar()

        frame = ttk.Frame(self)
        frame.pack(padx=20, pady=20, fill=BOTH, expand=YES)

        ttk.Label(frame, text="WebDAV服务器URL:").pack(fill=X, pady=5)
        self.server_entry = ttk.Entry(frame)
        self.server_entry.pack(fill=X, pady=5)
        self.server_entry.insert(0, "https://dav.caimaox.com/dav/ali/dataSync")


        ttk.Label(frame, text="选择文件:").pack(fill=X, pady=5)

        file_entry = ttk.Entry(frame, textvariable=self.file_path)
        file_entry.pack(side=LEFT, fill=X, expand=YES, pady=5)

        browse_btn = ttk.Button(frame, text="浏览", command=self.browse_file)
        browse_btn.pack(side=RIGHT, padx=5, pady=5)

        self.upload_btn = ttk.Button(self, text="上传", command=self.start_upload, style="success.TButton")
        self.upload_btn.pack(pady=10)

        self.progress = ttk.Progressbar(self, length=400, mode='determinate', style="success.Horizontal.TProgressbar")
        self.progress.pack(pady=10)

        self.status_label = ttk.Label(self, text="", font=("Helvetica", 10))
        self.status_label.pack(pady=10)

    def browse_file(self):
        filename = filedialog.askopenfilename()
        self.file_path.set(filename)

    def start_upload(self):
        Thread(target=self.upload_file).start()

    def upload_file(self):
        file_path = self.file_path.get()
        if not file_path:
            self.status_label.config(text="请先选择文件", foreground="red")
            return

        self.upload_btn.config(state=DISABLED)
        self.progress['value'] = 0
        self.status_label.config(text="正在上传...", foreground="white")

        try:
            options = {
                'webdav_hostname': self.server_entry.get(),
                'webdav_login': 'admin',
                'webdav_password': 'Yu9654321'
            }
            client = Client(options)

            file_name = os.path.basename(file_path)
            remote_path = f"/{file_name}"

            file_size = os.path.getsize(file_path)
            chunk_size = 1024 * 1024  # 1MB chunks

            with open(file_path, 'rb') as file:
                uploaded_size = 0
                while True:
                    chunk = file.read(chunk_size)
                    if not chunk:
                        break
                    client.upload_to(remote_path, chunk)
                    uploaded_size += len(chunk)
                    progress = int((uploaded_size / file_size) * 100)
                    self.progress['value'] = progress
                    self.update_idletasks()

            self.status_label.config(text="上传成功!", foreground="green")
        except Exception as e:
            self.status_label.config(text=f"错误: {str(e)}", foreground="red")
        finally:
            self.upload_btn.config(state=NORMAL)

if __name__ == "__main__":
    app = FileUploaderApp()
    app.mainloop()