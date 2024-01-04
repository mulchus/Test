# https://tproger.ru/translations/demystifying-decorators-in-python

# def benchmark(func):
#     import time
#
#     def wrapper():
#         start = time.time()
#         func()
#         end = time.time()
#         print('[*] Время выполнения: {} секунд.'.format(end-start))
#     return wrapper
#
# @benchmark
# def fetch_webpage():
#     import requests
#     print(requests.get('https://google.com').text[:200])
#
# # fetch_webpage = benchmark(fetch_webpage)
# fetch_webpage()

def benchmark(func):
    import time
    
    def wrapper(*args, **kwargs):
        start = time.time()
        return_value = func(*args, **kwargs)
        end = time.time()
        print('[*] Время выполнения: {} секунд.'.format(end - start))
        return return_value
    
    return wrapper

@benchmark
def fetch_webpage(url):
    import requests
    webpage = requests.get(url)
    return webpage.text[:200]

# fetch_webpage = benchmark(fetch_webpage)

webpage = fetch_webpage('https://google.com')
print(webpage)
