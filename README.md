# FUZZYSCAN
FUZZY scan is an API endpoint scanner for CTF's and BugBounties. This simple tool helps discover hidden API paths by fuzzing with a supplied wordlist against a target domain or IP address. FUZZYSCAN supports both HTTP and HTTPS,filters noise like 404 responses and highlights important status codes for API fuzzing.



![FUZZYSCAN](./FUZZYSCAN.gif)
















The instructions are simple:

usage: fuzzy.py [-h] -t TARGET [--https] [--http]

FUZZYSCAN - Simple API Fuzzer

options:
  -h, --help            show this help message and exit
  -t TARGET, --target TARGET
                        Target domain or IP required (example.com or 10.10.0.1)
  --https               Use HTTPS instead of HTTP
  --http                Use HTTP instead of HTTPS

You may use whatever wordlist you like the one I have included contains various API names used for fuzzing web application APIs most of which were discovered out in the wild.

This is my first python project worth pushing to GitHUb, enjoy!
