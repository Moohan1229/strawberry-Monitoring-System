import tkinter.ttk as ttk
from tkinter import *

root = Tk()
root.title("Auto Moving Monitoring System")
root.geometry("720x600")

main_frame = None
info_label = None
auto_frame = None
Manual_frame = None


def clear_frames():
    global main_frame, info_label, auto_frame, Manual_frame

    if main_frame is not None:
        main_frame.destroy()
        main_frame = None
    if info_label is not None:
        info_label.destroy()
        info_label = None
    if auto_frame is not None:
        auto_frame.destroy()
        auto_frame = None
    if Manual_frame is not None:
        Manual_frame.destroy()
        Manual_frame = None


def Main():
    clear_frames()

    global main_frame
    main_frame = Frame(root)
    main_frame.pack(padx=5, pady=5, ipady=5)

    label = Label(main_frame, text="Main Screen", padx=10, pady=10)
    label.pack(pady=20)


def Auto():
    clear_frames()

    global auto_frame
    auto_frame = Frame(root)
    auto_frame.pack(padx=5, pady=5, ipady=5)

    for i in range(1, 7):
        create_setting_frame(auto_frame, i)


def create_setting_frame(parent, setting_number):
    frame = LabelFrame(parent, text=f"Setting {setting_number}")
    frame.pack(padx=5, pady=5, ipady=5)

    # Set Time (Hour)
    lbl_hour = Label(frame, text="Set Time(Hour)", width=15)
    lbl_hour.pack(side="left", padx=20, pady=5)

    opt_hour = [str(i) for i in range(24)]
    cmb_hour = ttk.Combobox(frame, state="readonly", values=opt_hour, width=10)
    cmb_hour.current(0)
    cmb_hour.pack(side="left", padx=5, pady=5)

    # Set Time (Min)
    lbl_min = Label(frame, text="Set Time(Min)", width=15)
    lbl_min.pack(side="left", padx=20, pady=5)

    opt_min = ["0", "10", "20", "30", "40", "50"]
    cmb_min = ttk.Combobox(frame, state="readonly", values=opt_min, width=10)
    cmb_min.current(0)
    cmb_min.pack(side="left", padx=5, pady=5)


def Manual():
    clear_frames()

    global Manual_frame
    Manual_frame = Frame(root)
    Manual_frame.pack(padx=5, pady=5, ipady=5)

    label = Label(Manual_frame, text="Manual_frame", padx=10, pady=10)
    label.pack(pady=20)


def Info():
    clear_frames()

    global info_label
    info_label = Frame(root)
    info_label.pack(padx=5, pady=5)

    Label(info_label, text="System Spec", padx=10, pady=10).pack(pady=5)
    Label(info_label, text="Axis Y Length : 8m  Z Length : 1m",
          padx=10, pady=10).pack(pady=5)
    Label(info_label, text="Camera IMX296 , GS camera x4",
          padx=10, pady=10).pack(pady=5)
    Label(info_label, text="Main: AC220v 60hz , System: DC24V",
          padx=10, pady=10).pack(pady=5)
    Label(info_label, text="Made by DongyangTechwin",
          padx=10, pady=10).pack(pady=150)


menu = Menu(root)


def create_menu_buttons():
    frame = Frame(root)
    frame.pack(side="top", padx=10)

    btn_main = Button(frame, text="Main", command=Main, width=17, height=1)
    btn_main.pack(side="left", padx=1)

    btn_auto = Button(frame, text="Auto", command=Auto, width=17, height=1)
    btn_auto.pack(side="left", padx=1)

    btn_manual = Button(frame, text="Manual",
                        command=Manual, width=17, height=1)
    btn_manual.pack(side="left", padx=1)

    btn_info = Button(frame, text="Info", command=Info, width=17, height=1)
    btn_info.pack(side="left", padx=1)

    btn_exit = Button(frame, text="Exit",
                      command=root.quit, width=17, height=1)
    btn_exit.pack(side="left", padx=1)


create_menu_buttons()

root.config(menu=menu)
root.mainloop()
