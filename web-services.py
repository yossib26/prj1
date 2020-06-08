# --------------------  Check WWW Services  -----------------------
import os
import datetime
import requests


def check_srvice(srv):
    try:
        print("Checking " + srv + " ...")
        call_res = requests.get(srv)
        print("Response Code: " + str(call_res.status_code))
        srv_status = call_res.status_code
        # srv_status = "OK"
        return srv_status
    except ConnectionError as e:
        return -1


def log_url(url, srv_status):
    u = url.strip()
    u = strip_url(u)
    try:
        d = datetime.datetime.now()
        logFile_name = u + ".txt"
        logFile = open(logFile_name, "a")
        logFile.write(str(d) + "    " + u + "    " + srv_status + "\n")
        logFile.close()
    except IOError:
        print("Error writing to LOG file!")


def strip_url(url):
    try:
        u = url.replace("http://", "")
        u = u.replace("https://", "")
        u = u.replace("www.", "")
        u = u.replace("/", "")
        u = u.replace("\n", "")
        return u
    except:
        return ""


file_name = "urls.txt"
if os.path.exists(file_name):
    try:
        myFile = open(file_name)
        url = myFile.readline()
        url.strip()
        cnt = 0
        while url:
            url = url.replace("\n", "")
            # call check srv
            srv_status = check_srvice(url)
            # print(srv_status, end=' ')
            log_url(url, str(srv_status))
            cnt += 1
            url = myFile.readline()
        myFile.close()
    except IOError:
        print("Error Reading Url's File")
    finally:
        print("--------------------------------------------------------")
        print(str(cnt) + " services have been checked!")
else:
    print("File Not Exist!!!")

