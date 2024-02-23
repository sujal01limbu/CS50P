File = input("File name:")

if (File.endswith(".gif")):
    print("image/gif")

elif (File.endswith(".jpg")):
    print("image/jpeg")

elif (File.endswith(".jpeg")):
    print("image/jpeg")

elif (File.endswith(".png")):
    print("image/png")

elif (File.endswith(".pdf")):
    print("application/pdf")

elif (File.endswith(".txt")):
    print("text/plain")

elif (File.endswith(".zip")):
    print("application/zip")
