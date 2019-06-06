import requests, getpass
global loginUn, loginPass, success, failure

loginUn = [
"abc",
"root"
]
loginPass = getpass.getpass('Enter pass: ')
url = "https://google.com"




def ProxyAccess(user):
    try:
        proxies = {
            "http": "http://{}:{}@10.10.1.10:3128/".format(user, loginPass),
            "https": "https://{}:{}@10.10.1.10:3128/".format(user, loginPass)
        }

        r = requests.get(url, headers=headers, proxies=proxies)
        print("[+] Proxy Connection Successful! {}!\n".format(user))
        success.append(user)   
    except paramiko.AuthenticationException:
        print ("[-] Authentication Exception on {}!\n".format(user))
        failure[user] = "Auth Exception."
    except Exception as e:
        print("[-] SSH Failure on {}. {}\n".format(user,e))
        failure[user] = e


def linuxHosts(cmd):
    threads = []
    for user in loginUn:
        print("Trying {}...".format(user))
        t = threading.Thread(target=cmd, args=(user,)) #Create thread for each user
        t.daemon = True             #kill process if main thread ends
        t.start()
        threads.append(t)
        time.sleep(0.2)
    for t in threads:
        t.join()


if __name__ == "__main__":
    linuxHosts(ProxyAccess)
    print(success)
    print(failure)                      
