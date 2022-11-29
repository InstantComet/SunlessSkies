import tkinter as tk
from tkinter import filedialog
import ntpath
import json

'''打开选择文件夹对话框'''
root = tk.Tk()
root.withdraw()

Filepath = filedialog.askopenfilename() #获得选择好的文件
file_name = ntpath.basename(Filepath)
file_name_pure = file_name.split('.')[0]
file_type = file_name.split('.')[1]
jsonfile_name = file_name_pure + ".json"
txtfile_name = file_name_pure + ".txt"

def json_to_text():
    input_json_filename = Filepath # Edit this
    output_text_filename = "translated_text/" + txtfile_name # Edit this

    f = open(input_json_filename, "r", encoding="utf-8")
    fout = open(output_text_filename, "w", encoding="utf-8")
    obj = json.load(f)
    fout.writelines([o["original"] + "=" + o["translation"] + "\n" for o in obj])
    fout.close()


def text_to_json():
    input_text_filename = Filepath # Edit this
    output_json_filename = "jsons_to_upload/" + jsonfile_name # Edit this

    f = open(input_text_filename, "r", encoding="utf-8")
    fout = open(output_json_filename, "w", encoding="utf-8")

    obj = []
    for i, l in enumerate(f):
        l = l.replace("\=", "____xxx____")
        l = l.strip().split("=")
        keymum = str(i+1)
        if len(l) == 2:
            obj.append({ "key": file_name_pure + keymum, "original": l[0].replace("____xxx____", "\\="), "translation": l[1].replace("____xxx____", "\\=") })
    json.dump(obj, fout, ensure_ascii=False, indent = 2)
    fout.close()

# uncomment the required function

#json_to_text()
if file_type == "txt":
    text_to_json()
if file_type == "json":
    json_to_text()





