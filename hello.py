
def application (environ, start_response):
    status = "200 OK"
    headers = [('Content-Type', 'text/plain')]
    start_response(status, headers)
    data = environ['QUERY_STRING'].replace('&','\n')
    print(data)
    #data = ''
    #for param in parameters:
        #data += param + '\n'

    return [data]


#a = wsgi_application('myid=333&tab=ioi')
#print(a)
