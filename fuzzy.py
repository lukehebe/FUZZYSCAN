import requests
import sys
import argparse
import time

def arguments():
    parser = argparse.ArgumentParser(description="FUZZYSCAN - Simple API Fuzzer")
    parser.add_argument(
        "-t", "--target",
        required=True,
        help="Target domain or IP required (example.com or 10.10.0.1)"
    )
    parser.add_argument(
        "--https",
        action="store_true",
        help="Use HTTPS instead of HTTP"
    )
    parser.add_argument(
        "--http",
        action="store_true",
        help="Use HTTP instead of HTTPS"
    )
    return parser.parse_args()

def print_banner():
    BLUE1 = "\033[38;5;27m"
    BLUE2 = "\033[38;5;33m"
    BLUE3 = "\033[38;5;39m"
    RESET = "\033[0m"

    banner = rf"""
{BLUE1}                            __====-_  _-====___
                       _--^^^#####//      \\\\#####^^^--_
                    _-^##########// (    ) \\\\##########^-_
                   -############//  |\\^^/|  \\\\############-
                 _/############//   (@::@)   \\\\############\\_
                /#############((     \\\\//     ))#############\\
               -###############\\\\    (oo)    //###############-
              -#################\\\\  / UUU \\  //#################-
             -###################\\\\/  (v)  \\\/###################-
            _#/|##########/\\######(   /\\   )######/\\##########|\\#_
            |/ |#/\#/\#/\/  \\#/\##\\  ||||  //##/\#/  \\/\#/\#/\#| \\|
            `  |/  V  FUZZYSCAN V \\|  VVVV  |/  V  V  V \\|  ' 
                                `  API Fuzzer  `

{BLUE2}                         >> FUZZYSCAN INITIATED <<
{BLUE3}
"""

    print(banner + RESET)
    print(f"{BLUE2}[+] Starting Fuzzy Scan. FUZZING ACTIVATED.\n{RESET}")


if __name__ == "__main__":
    print_banner()
    time.sleep(2)
    args = arguments()

    if args.http:
        scheme = "http"
    elif args.https:
        scheme = "https"
    else:
        scheme = "http"

    status_codes_allowed = [200, 301, 302, 401, 403, 405, 500]
    url = f"{scheme}://{args.target}".rstrip("/")

    for word in sys.stdin:
        word = word.strip()
        fuzzy_url = f"{url}/{word.lstrip('/')}"

        try:
            response = requests.get(fuzzy_url, timeout=6)

            if response.status_code in status_codes_allowed:
                print(f"[{response.status_code}] {fuzzy_url}")
                if response.headers.get("Content-Type", "").startswith("application/json"):
                    try:
                        print(response.json())
                    except Exception:
                        print("[!!!] Failed to parse the JSON PLAYA!")

        except requests.RequestException as e:
            print(f"[!!!] Error with {fuzzy_url} ---> {e}")
