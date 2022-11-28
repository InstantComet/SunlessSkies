
import json

def json_to_text():
    input_json_filename = "input.json" # Edit this
    output_text_filename = "output.txt" # Edit this

    f = open(input_json_filename, "r", encoding="utf-8")
    fout = open(output_text_filename, "w", encoding="utf-8")
    obj = json.load(f)
    fout.writelines([o["original"] + "=" + o["translation"] + "\n" for o in obj])
    fout.close()


def text_to_json():
    input_text_filename = "text.txt" # Edit this
    output_json_filename = "newpara.json" # Edit this

    f = open(input_text_filename, "r", encoding="utf-8")
    fout = open(output_json_filename, "w", encoding="utf-8")

    obj = []
    for i, l in enumerate(f):
        l = l.replace("\=", "____xxx____")
        l = l.strip().split("=")
        if len(l) == 2:
            obj.append({ "key": i+1, "original": l[0].replace("____xxx____", "\\="), "translation": l[1].replace("____xxx____", "\\=") })
    json.dump(obj, fout, ensure_ascii=False, indent = 2)
    fout.close()

# uncomment the required function

#json_to_text()
text_to_json()





