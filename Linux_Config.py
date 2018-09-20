import threading, paramiko, time, datetime, getpass

global ips, loginUn, loginPass, enPass, run, success, failure

loginUn = input('Enter UN: ')
loginPass = getpass.getpass('Enter pass: ')
run = r"service lighttpd restart"
success = []
failure = {}
ips = [
    '10.11.1.30',
    '10.11.2.30',
    '10.11.3.30',
    '10.11.4.30',
    '10.11.5.30'
    ]


def SSHAccess(host):
    try:
        #Create SSH client object
        client = paramiko.SSHClient()
        #Automatically add ssh keys
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        #Attempt to establish SSH connection
        client.connect(host, username=loginUn, password=loginPass,timeout=1)
        print("[+] Connected to host {}!\n".format(host))
        #Call function to execute command
        runCMDS(client,host)
        #Close connection when finished
        client.close()
    except paramiko.AuthenticationException:
        print ("[-] Authentication Exception on {}!\n".format(host))
        failure[host] = "Auth Exception."
    except Exception as e:
        print("[-] SSH Failure on {}. {}\n".format(host,e))
        failure[host] = e


def runCMDS(client,host):
    try:
        global run
        cmd = run
        #Establish interactive shell
        conn = client.invoke_shell()
        #Read output from connection
        out = conn.recv(1000)
        #Print output to user
        print("Default OUTPUT from host {}\n{} \n".format(host,out))
        time.sleep(0.5)
        #Format output
        cmd += '\n'
        conn.send(cmd)
        time.sleep(10)
        out = conn.recv(10000)
        out = out.split(b'\r\n')
        success.append(host)   
        print("COMMAND{}HOST:{}\nOUTPUT{} \n".format(cmd, host,out[1]))
    except:
        print('[-] Error running command on host: {}'.format(host))
        failure[host] = e



def linuxHosts(cmd):
    threads = []
    hosts = ips  #Insert IPs of hosts to configure
    for address in hosts:
        print("Trying {}...".format(address))
        t = threading.Thread(target=cmd, args=(address,)) #Create thread for each host
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
