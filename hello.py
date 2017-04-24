
# def start_response(status, headers):
#     return 0


def app(env, start_response):
    query_string = env['QUERY_STRING']
    query_list = query_string[query_string.find("?")+1:].replace("&", "\n").encode()
    status = "200 OK"
    headers = [('Content-Type', 'text/plain'),
               ('Content-Length', str(len(query_list)))]
    start_response(status, headers)
    return [query_list]

# if __name__ == "__main__":
#     print(app({'QUERY_STRING': "/?a=1&a=2&b=3"}, start_response))
