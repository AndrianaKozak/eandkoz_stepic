import urlparse
#from wsgiref.simple_server import make_server

def application (env, start_response):
    status = "200 OK"
    headers = [('content-Type', 'text/plain')]
        start_response(status, headers)
    parameters = environ['QUERY_STRING'].split('&')
    data = ''
    for param in parameters:
        data += param + '\n'

    return [data]


#a = wsgi_application('myid=333&tab=ioi')
#print(a)
