my_string = input("file: ").strip(" ").replace(".", " ").lower()
split_str = my_string.split()
a = split_str
for item in a[:] :
    if item == "txt.pdf":
        b = a.pop(2)
        print("application/pdf")
if item == "jpg" or item == "jpeg":
    print("image/jpeg")
elif item == "png" or item == "gif":
    print(f"image/{item}")
elif item == "PDF" or item == "pdf":
    print("application/pdf")
elif item == "txt":
    print("text/plain")
elif item == "zip":
    print("application/zip")
else:
    print("application/octet-stream")