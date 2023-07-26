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

#OR

media_type = {
        "gif": "image/gif",
        "jpg": "image/jpeg",
        "jpeg": "image/jpeg",
        "png": "image/png",
        "pdf": "application/pdf",
        "txt": "text/plain",
        "zip": "application/zip"
    }
file_suffix = input("enter: ").split('.')[-1]

if file_suffix in media_type:
    print(media_type[file_suffix])
else:
    print("application/octet-stream")
