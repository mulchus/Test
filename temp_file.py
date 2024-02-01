import tempfile

temp = tempfile.NamedTemporaryFile()
print(temp.name)

try:
    temp.write(b"Hello World")
    temp.seek(0)    # Go to the beginning of the file
    print(temp.read())
finally:
    temp.close()
