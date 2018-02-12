from ftplib import FTP
import ftplib
import os
import socket
HOST = 'ftp.mozilla.org'
DIRN = 'pub/mozilla.org/webtools'
FILE = 'bugzilla-LATEST.tar.gz'
def main():
    try:
        f = FTP(HOST)
    except (socket.error, socket.gaierror) as e:
        print('Error: cannot reach %s' %HOST)
        return
    print('***connect to host %s' %HOST)

    try:
        f.login()
    except ftplib.error_perm:
        print('Error: cannot login')
        f.quit()
        return
    print('logged in as annoymous')

    try:
        f.cwd(DIRN)
    except ftplib.error_perm:
        print('cannot to cd to %s' %DIRN)
        f.quit()
        return
    print('changed to %s' %DIRN)

    try:
        f.retrbinary('RETR %s' %FILE, open(FILE, 'wb').write)
    except ftplib.error_perm:
        print('conn')
        os.unlink(FILE)
if __name__ == '__main__':
    main()