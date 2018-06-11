# https://stackoverflow.com/a/33777090/1737957
import requests
import concurrent.futures

def get_urls():
    return ["url1","url2"]

def load_url(url, timeout):
    return requests.get(url, timeout = timeout)

with concurrent.futures.ThreadPoolExecutor(max_workers=20) as executor:

    future_to_url = {executor.submit(load_url, url, 10): url for url in     get_urls()}
    for future in concurrent.futures.as_completed(future_to_url):
        url = future_to_url[future]
        try:
            data = future.result()
        except Exception as exc:
            resp_err = resp_err + 1
        else:
            resp_ok = resp_ok + 1