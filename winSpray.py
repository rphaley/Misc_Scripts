import threading, paramiko, time, datetime, getpass

global ips, loginUn, loginPass, enPass, run, success, failure

loginUn = [
"abc",
"root"
]

loginPass = getpass.getpass('Enter pass: ')
run = r'whoami'
success = []
failure = {}
ip = '10.12.1.25'


def SSHAccess(user):
    try:
        #Create SSH client object
        client = paramiko.SSHClient()
        #Automatically add ssh keys
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        #Attempt to establish SSH connection
        client.connect(ip, username=user, password=loginPass,timeout=10)
        print("[+] Connected with user {}!\n".format(user))
        #Call function to execute command.

        runCMDS(client,ip)
        #Close connection when finished
        client.close()
    except paramiko.AuthenticationException:
        print ("[-] Authentication Exception on {}!\n".format(user))
        failure[user] = "Auth Exception."
    except Exception as e:
        print("[-] SSH Failure on {}. {}\n".format(user,e))
        failure[user] = e


def runCMDS(client,user):
    try:
        global run
        cmd = run
        #Establish interactive shell
        conn = client.invoke_shell()
        #Read output from connection
        out = conn.recv(1000)
        #Print output to user
        print("Default OUTPUT from user {}\n{} \n".format(user,out))
        time.sleep(0.5)
        #Format output
        cmd += '\n'
        conn.send(cmd)
        time.sleep(10)
        out = conn.recv(10000)
        out = out.split(b'\r\n')
        success.append(user)   
        print("COMMAND{}HOST:{}\nOUTPUT{} \n".format(cmd, user,out[1]))
    except:
        print('[-] Error running command on user: {}'.format(user))
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
    linuxHosts(SSHAccess)
    print(success)
    print(failure)                      
