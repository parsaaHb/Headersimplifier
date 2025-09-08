import requests

def get_request_headers(url):
    if not url.startswith("http://") and not url.startswith("https://"):
        url = "https://" + url
    r = requests.get(url)
    method = r.request.method
    requestHeaders = r.request.headers
    return method , requestHeaders