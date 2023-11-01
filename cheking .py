import urllib.request, urllib.error, socket
socket.setdefaulttimeout(140)
proxyList = ['140.82.61.218:8080' , '141.101.113.121:80', '66.235.200.111:80']

def proxyHandler(proxy):    
    try:        
        proxy_handler = urllib.request.ProxyHandler({'http': proxy})        
        opener = urllib.request.build_opener(proxy_handler)
        opener.addheaders = [('User-agent', 'Mozilla/5.0')]
        urllib.request.install_opener(opener)        
        sock=urllib.request.urlopen('http://www.google.com')  
    except urllib.error.HTTPError as e:        
        print('Error code: ', e.code)
        return e.code
    except Exception as detail:

        print( "ERROR:", detail)
        return 1
    return 0