# типа скачивание нескольких файлов параллельно с помощью ThreadPoolExecutor
# разве потоки не блокируются GIL ?
# как пример аналогии асинхронности

import os
import urllib.request
import time

from concurrent.futures import ThreadPoolExecutor, as_completed

def downloader(url):
    """Скачивает указанный URL и сохраняет его на диск"""
    req = urllib.request.urlopen(url)
    filename = os.path.basename(url)
    ext = os.path.splitext(url)[1]
    if not ext:
        raise RuntimeError('URL не содержит расширения')

    with open(filename, 'wb') as file_handle:
        while True:
            chunk = req.read(1024)
            if not chunk:
                break
            file_handle.write(chunk)

    time.sleep(1)
    return f'Загрузка завершена: {filename}'

def main(urls):
    """Создаёт пул потоков и скачивает указанные файлы"""
    with ThreadPoolExecutor(max_workers=2) as executor:     # max_workers - количество потоков, при = 5 идет квазипараллельно
        futures = [executor.submit(downloader, url) for url in urls]
        for future in as_completed(futures):
            print(future.result())

if __name__ == '__main__':
    urls = [
        "http://www.irs.gov/pub/irs-pdf/f1040.pdf",
        "http://www.irs.gov/pub/irs-pdf/f1040a.pdf",
        "http://www.irs.gov/pub/irs-pdf/f1040ez.pdf",
        "http://www.irs.gov/pub/irs-pdf/f1040es.pdf",
        "http://www.irs.gov/pub/irs-pdf/f1040sb.pdf"
    ]
    main(urls)
