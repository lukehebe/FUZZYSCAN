# FUZZYSCAN
FUZZYSCAN is an API endpoint fuzzer for CTF's and BugBounties. This simple tool helps discover hidden API paths by fuzzing with a supplied wordlist against a target domain or IP address. FUZZYSCAN supports both HTTP and HTTPS,filters noise like 404 responses and highlights important status codes for API fuzzing.



![FUZZYSCAN](./REALDEMO.gif)





FuzzyScan - Simple API Fuzzer
Usage:
cat <wordlist> | python3 fuzzy.py -t "<IP or domain name>" [--http | --https]

FuzzyScan is a lightweight tool for fuzzing web application APIs. You can use any wordlist of your choice. The included wordlist contains a variety of API endpoint names, many of which were discovered in real-world applications.
Note:
This tool was tested on the “Backend” machine from Hack The Box (HTB).