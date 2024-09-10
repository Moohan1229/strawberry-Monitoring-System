import os
import tkinter.ttk as ttk
import tkinter.messagebox as msgbox
from tkinter import *  # __all__
from tkinter import filedialog

root = Tk()
root.title("Monitoring System")

# 옵션 프레임
frame_option = LabelFrame(root, text="설정 1")
frame_option.pack(padx=5, pady=5, ipady=5)

# 1. 가로 넓이 옵션
# 가로 넓이 레이블
lbl_width = Label(frame_option, text="시작 시간 (시)", width=15)
lbl_width.pack(side="left", padx=20, pady=5)

# 가로 넓이 콤보
opt_width = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12",
             "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23",]
cmb_width = ttk.Combobox(frame_option, state="readonly",
                         values=opt_width, width=10)
cmb_width.current(0)
cmb_width.pack(side="left", padx=5, pady=5)

# 2. 간격 옵션
# 간격 옵션 레이블
lbl_space = Label(frame_option, text="시작 시간 (분)", width=15)
lbl_space.pack(side="left", padx=20, pady=5)

# 간격 옵션 콤보
opt_space = ["0", "10", "20", "30", "40", "50",]
cmb_space = ttk.Combobox(frame_option, state="readonly",
                         values=opt_space, width=10)
cmb_space.current(0)
cmb_space.pack(side="left", padx=5, pady=5)  # 옵션 프레임

# ------------------------------------------------------------------------------------
frame_option = LabelFrame(root, text="설정 2")
frame_option.pack(padx=5, pady=5, ipady=5)

# 1. 가로 넓이 옵션
# 가로 넓이 레이블
lbl_width = Label(frame_option, text="시작 시간 (시)", width=15)
lbl_width.pack(side="left", padx=20, pady=5)

# 가로 넓이 콤보
opt_width = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12",
             "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23",]
cmb_width = ttk.Combobox(frame_option, state="readonly",
                         values=opt_width, width=10)
cmb_width.current(0)
cmb_width.pack(side="left", padx=5, pady=5)

# 2. 간격 옵션
# 간격 옵션 레이블
lbl_space = Label(frame_option, text="시작 시간 (분)", width=15)
lbl_space.pack(side="left", padx=20, pady=5)

# 간격 옵션 콤보
opt_space = ["0", "10", "20", "30", "40", "50",]
cmb_space = ttk.Combobox(frame_option, state="readonly",
                         values=opt_space, width=10)
cmb_space.current(0)
cmb_space.pack(side="left", padx=5, pady=5)

# ------------------------------------------------------------------------------------
frame_option = LabelFrame(root, text="설정 3")
frame_option.pack(padx=5, pady=5, ipady=5)

# 1. 가로 넓이 옵션
# 가로 넓이 레이블
lbl_width = Label(frame_option, text="시작 시간 (시)", width=15)
lbl_width.pack(side="left", padx=20, pady=5)

# 가로 넓이 콤보
opt_width = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12",
             "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23",]
cmb_width = ttk.Combobox(frame_option, state="readonly",
                         values=opt_width, width=10)
cmb_width.current(0)
cmb_width.pack(side="left", padx=5, pady=5)

# 2. 간격 옵션
# 간격 옵션 레이블
lbl_space = Label(frame_option, text="시작 시간 (분)", width=15)
lbl_space.pack(side="left", padx=20, pady=5)

# 간격 옵션 콤보
opt_space = ["0", "10", "20", "30", "40", "50",]
cmb_space = ttk.Combobox(frame_option, state="readonly",
                         values=opt_space, width=10)
cmb_space.current(0)
cmb_space.pack(side="left", padx=5, pady=5)

# ------------------------------------------------------------------------------------
frame_option = LabelFrame(root, text="설정 4")
frame_option.pack(padx=5, pady=5, ipady=5)

# 1. 가로 넓이 옵션
# 가로 넓이 레이블
lbl_width = Label(frame_option, text="시작 시간 (시)", width=15)
lbl_width.pack(side="left", padx=20, pady=5)

# 가로 넓이 콤보
opt_width = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12",
             "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23",]
cmb_width = ttk.Combobox(frame_option, state="readonly",
                         values=opt_width, width=10)
cmb_width.current(0)
cmb_width.pack(side="left", padx=5, pady=5)

# 2. 간격 옵션
# 간격 옵션 레이블
lbl_space = Label(frame_option, text="시작 시간 (분)", width=15)
lbl_space.pack(side="left", padx=20, pady=5)

# 간격 옵션 콤보
opt_space = ["0", "10", "20", "30", "40", "50",]
cmb_space = ttk.Combobox(frame_option, state="readonly",
                         values=opt_space, width=10)
cmb_space.current(0)
cmb_space.pack(side="left", padx=5, pady=5)

# ------------------------------------------------------------------------------------
frame_option = LabelFrame(root, text="설정 5")
frame_option.pack(padx=5, pady=5, ipady=5)

# 1. 가로 넓이 옵션
# 가로 넓이 레이블
lbl_width = Label(frame_option, text="시작 시간 (시)", width=15)
lbl_width.pack(side="left", padx=20, pady=5)

# 가로 넓이 콤보
opt_width = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12",
             "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23",]
cmb_width = ttk.Combobox(frame_option, state="readonly",
                         values=opt_width, width=10)
cmb_width.current(0)
cmb_width.pack(side="left", padx=5, pady=5)

# 2. 간격 옵션
# 간격 옵션 레이블
lbl_space = Label(frame_option, text="시작 시간 (분)", width=15)
lbl_space.pack(side="left", padx=20, pady=5)

# 간격 옵션 콤보
opt_space = ["0", "10", "20", "30", "40", "50",]
cmb_space = ttk.Combobox(frame_option, state="readonly",
                         values=opt_space, width=10)
cmb_space.current(0)
cmb_space.pack(side="left", padx=5, pady=5)

# ------------------------------------------------------------------------------------
frame_option = LabelFrame(root, text="설정 6")
frame_option.pack(padx=5, pady=5, ipady=5)

# 1. 가로 넓이 옵션
# 가로 넓이 레이블
lbl_width = Label(frame_option, text="시작 시간 (시)", width=15)
lbl_width.pack(side="left", padx=20, pady=5)

# 가로 넓이 콤보
opt_width = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12",
             "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23",]
cmb_width = ttk.Combobox(frame_option, state="readonly",
                         values=opt_width, width=10)
cmb_width.current(0)
cmb_width.pack(side="left", padx=5, pady=5)

# 2. 간격 옵션
# 간격 옵션 레이블
lbl_space = Label(frame_option, text="시작 시간 (분)", width=15)
lbl_space.pack(side="left", padx=20, pady=5)

# 간격 옵션 콤보
opt_space = ["0", "10", "20", "30", "40", "50",]
cmb_space = ttk.Combobox(frame_option, state="readonly",
                         values=opt_space, width=10)
cmb_space.current(0)
cmb_space.pack(side="left", padx=5, pady=5)
# ------------------------------------------------------------------------------------

path_frame = LabelFrame(root, text="Z 작동시간 추가")
path_frame.pack(fill="x", padx=5, pady=5, ipady=5)

txt_dest_path = Entry(path_frame)
txt_dest_path.pack(side="left", fill="x", expand=True,
                   padx=5, pady=5, ipady=5)  # 높이 변경

btn_dest_path = Button(path_frame, text="Z축 테스트",
                       width=20, )
btn_dest_path.pack(side="right", padx=5, pady=5)

cmb_space.current(0)
cmb_space.pack(side="left", padx=5, pady=5)
root.resizable(False, False)
root.mainloop()
root.mainloop()
