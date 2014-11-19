__author__ = 'anderson'

from ftplib import FTP_TLS

class FTPS:
    def __init__(self):
        self.ftps = FTP_TLS( )

    def connect(self):
        self.ftps.connect('192.168.0.102', 2121)
        print(self.ftps.getwelcome())

    def login(self):
        self.ftps.login('anderson', 'nosredna89')
        self.ftps.prot_p() #para fazer a conexação de dados segura

    def close(self):
        self.ftps.close()
