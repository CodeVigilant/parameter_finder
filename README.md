# parameter_finder
a script to find all parameters, GET,POST,REQUEST,COOKIE used in a php file and craft a request based on that.

## Commandline Usage 

```
$ python parameter_finder.py --help                          
usage: parameter_finder.py [-h] [--url TARGET] [--proxy PROXY] --folder FOLD

This program is used to identify various parameters in php files which can
then be fed to proxy services which can run automated scans

optional arguments:
  -h, --help     show this help message and exit
  --url TARGET   Provide Target URL
  --proxy PROXY  Provide HTTP Proxy in host:port format will be used for
                 http(s)
  --folder FOLD  Provide Local Directory

Credit (C) Anant Shrivastava http://anantshri.info
````

## Example

```
python parameter_finder.py --url https://SITE_NAME/ --proxy 127.0.0.1:8080 --folder "/SOURCE_LOCATION"
```
