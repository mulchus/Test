import time
import re
# или чтение архивов gzip
# import gzip
# gzip.open(...

src = "d:/Python/test.txt"
dst = "d:/Python/test_out.txt"

with open(src, "rt", encoding="utf-8", errors="ignore") as fin, open(dst, "wt", encoding="utf-8") as fout:
        for line in fin: # ленивое чтение строк
            print(line)
            time.sleep(0.5)
            if not re.match('\B', line): # игнорим пустые строки или любая другая фильтрация
                fout.write(line) # потоковая запись на диск

        fout.write("\n")                  # просто пример финальной записи
        fout.write("(done)")

print("(done)")
