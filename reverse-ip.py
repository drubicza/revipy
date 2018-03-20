#!/usr/bin/python
import requests
from ast import literal_eval as d
from sys import exit

user_agent = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0"}
url        = "https://domains.yougetsignal.com/domains.php"
junk       = "=" * 70
err_key    = "\n\n[-] Error, Domain/IP Address is incorrect! or can reversed or check your connections\n" \
             "[-] Try using www. or remove http:// or try other domain format\n" \
             "[-] If you check many time in one day, you will get limit"
stat_ok    = [["[+] IP               :", "remoteIpAddress"],
              ["[+] Status           :", "status"],
              ["[+] Date and Time    :", "lastScrape"],
              ["[+] Results Method   :", "resultsMethod"],
              ["[+] Domain Count     :", "domainCount"]]
stat_no    = [["[-] Status           :", "status"],
              ["[-] Message          :", "message"]]

oops       = lambda msg: "\n".join("{} {}".format(stat_no[i][0], res[stat_no[i][1]]) for i in range(len(stat_no))) + "\n" + msg

print """{}
[+] Author    : Bayu Fedra
[+] Facebook  : Bayu Fedra
[+] Instagram : bayufedraa
[+] Github    : https://github.com/B3yeZ/\n{}""".format(junk, junk)

try:
    target = raw_input("[?] Target           : ")
    try:
        try:
            form = {"remoteAddress" : "{}".format(target), "key" : ""}
            res = d(requests.post(url, headers=user_agent, data=form, timeout=15).text)
        except:
            print "[-] Please check your internet connections..."
            exit(0)

        if res["status"] == "Success":
            print "\n".join("{} {}".format(stat_ok[i][0], res[stat_ok[i][1]]) for i in range(len(stat_ok)))
            print "\n".join("[+] Domain Reversed {}: {}".format(i + 1, res["domainArray"][i][0]) for i in range(len(res["domainArray"])))

        elif res["status"] == "Fail":
            if "Invalid remote address" in res["message"]:
                print oops("[i] Try using www. or remove http:// or try other domain format")

            elif "check limit reached for" in res["message"]:
                print oops("[i] Try to change your IP Address")

            else:
                print oops("")

        else:
            print "[+] Status           : {}".format(res["status"])

    except KeyError:
        print err_key

except KeyboardInterrupt:
    print "\n[i] Closing the program..."
