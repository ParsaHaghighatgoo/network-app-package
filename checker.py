import urllib.request
import socket
import urllib.error

def proxyHandler(proxy):
    try:
        proxy_handler = urllib.request.ProxyHandler({'http': proxy})
        opener = urllib.request.build_opener(proxy_handler)
        opener.addheaders = [('User-agent', 'Mozilla/5.0')]
        urllib.request.install_opener(opener)
        req=urllib.request.Request('http://www.google.com')  # change the URL to test here
        sock=urllib.request.urlopen(req)
    except urllib.error.HTTPError as e:
        print('Error code: ', e.code)
        return e.code
    except Exception as detail:
        print("ERROR:", detail)
        return True
    return False


def main():
    socket.setdefaulttimeout(120)

    # two sample proxy IPs
    proxyList = ['141.101.113.121:80', '66.235.200.111:80']

    for currentProxy in proxyList:
        if proxyHandler(currentProxy):
            print("Bad Proxy %s" % (currentProxy))
        else:
            print("%s is working" % (currentProxy))

if __name__ == '__main__':
    main()
# main()