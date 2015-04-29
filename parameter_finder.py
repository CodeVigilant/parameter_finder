import requests
import argparse
import sys
import os
import re

def request_url_show_error(url,proxy,cookies,post):
    try:
        if post != "":
            if proxy == "":
                r = requests.post(url,data=post,verify=False)
            else:
                r = requests.post(url,proxies=(proxy),data=post,verify=False)                
        else:
            if proxy == "":
                r = requests.get(url,verify=False)
            else:
                r = requests.get(url,proxies=(proxy),verify=False)
            #check if 200 OK then size of response more 0
            #check if 500 error
            #check if 200 with error or  error
    except Exception as e:
        print "Error in ; " + url + str(e)
        pass

def dequote(s):
    """
    If a string has single or double/single quotes around it, remove them.
    Make sure the pair of quotes match.
    If a matching pair of quotes is not found, return the string unchanged.
    """
    if (s[0] == s[-1]) and s.startswith(("'", '"')):
        return s[1:-1]
    return s

def recursive_list(folder,fld,target,proxy):
    print "CURRENT FOLDER : " + folder
    for x in os.listdir(folder):
        modi=""
        #print "A :" + folder + ": Seperator :" + os.path.sep + ": Folder :" + x
        if os.path.isdir(os.path.join(folder , x)):
            modi=os.path.sep
            #print "Dir Found : " + target + x + modi
            recursive_list(folder + modi + x,fld,target + x + modi,proxy)
            #uncomment to show Directory names
            #print target + x + modi
        #uncomment to show files names
        #print target + x
        fileName, fileExtension = os.path.splitext(folder + x)
        # add anyother php extension found.
        extension_list = {"php","php5","php4"}
        if fileExtension[1:] in extension_list:
            fname = folder + os.path.sep + x
            url=target  + os.path.sep + x
            regexp="\$_(GET|POST|REQUEST|COOKIE)\[(.*?)\]"
            textfile = open(fname, 'r')
            filetext = textfile.read()
            textfile.close()
            matches = re.findall(regexp, filetext)
            matches=sorted(set(matches))
            final_call=url + "?"
            #print matches
            cookies=""
            post=""
            for x in matches:
                if x[0] == "GET" or x[0] == "REQUEST":
                    final_call = final_call + dequote(x[1]) + "=1&"
                if x[0] == "COOKIE":
                    cookies=dequote(x[1]) + "=A;"
                if x[0] == "POST":
                    post=dequote(x[1]) + "=a&"

            # print final_call
            request_url_show_error(final_call,proxy,cookies,post[:-1])
    

def main(argv):
    desc="""This program is used to  identify various parameters in php files which can then be fed to proxy services which can run automated scans"""
    epilog="""Credit (C) Anant Shrivastava http://anantshri.info"""
    parser = argparse.ArgumentParser(description=desc,epilog=epilog)
    parser.add_argument("--url",help="Provide Target URL",dest='target',required=False)
    parser.add_argument("--proxy",help="Provide HTTP Proxy in host:port format will be used for http(s)", dest='proxy',required=False)
    parser.add_argument("--folder",help="Provide Local Directory", dest='fold',required=True)
    x=parser.parse_args()
    global fld
    target=x.target
    if target is None:
        target=""
    print "*" + target + "*"
    folder=x.fold
    fld=x.fold
    prox=x.proxy
    if prox is None:
        prox=""
    proxy_dict=""
    if prox != "":
        print "Proxy is Defined as " + prox
        print "Requests will be sent via Proxy"
        proxy_dict ={
            "http": prox,
            "https": prox
        }
        # proxy_dict = {"https":prox}
    else:
        print "Proxy not defined"
        proxy_dict = ""
    #print "Comment : URL : Status Code : Error Message"
    recursive_list(folder,fld,target,proxy_dict)
    #print os.listdir(folder)
    
    
        
if __name__ == "__main__":
    main(sys.argv[1:])
