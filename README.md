# FUZZYSCAN
FUZZYSCAN is an API endpoint fuzzer for CTF's and BugBounties. This simple tool helps discover hidden API paths by fuzzing with a supplied wordlist against a target domain or IP address. FUZZYSCAN supports both HTTP and HTTPS,filters noise like 404 responses and highlights important status codes for API fuzzing.



![FUZZYSCAN](./REALDEMO.gif)







The instructions are simple:

usage: cat <whatever_wordlist> | python3 fuzzy.py -t "ip or domain name" --http(s)

FUZZYSCAN - Simple API Fuzzer


You may use whatever wordlist you like the one I have included contains various API names used for fuzzing web application APIs most of which were discovered out in the wild.

This was tested on the machine "Backend" from HTB

This is my first python project worth pushing to GitHub, enjoy!
