#!/usr/bin/env python3 
"""
This Module / Framework Just for the Owner (host1let)

this Framework is a Command line Program
"""

#----[ Modules ]----
import os 
import subprocess
import requests
import sys 
import platform
import pyfiglet
import getpass
import socket
import random
import hashlib

# For CMD to Show Colors
os.system('')

#----[ colors class ]----
class colors:
    red = '\033[91m'
    green = '\033[92m'
    blue = '\033[94m'
    yellow = '\033[93m'
    magenta = '\033[95m'
    cyan = '\033[96m'
    bold = '\033[1m'
    underline = '\033[4m'
    black='\033[30m'
    Backsilver='\033[100m'
    silver='\033[90m'
    Backwhite='\033[3m'
    Backgreen='\033[42m'
    Backyellow='\033[43m'
    BackBlue='\033[44m'
    Backpink='\033[45m'
    Backcyan='\033[46m'
    BackRed='\033[41m'
    green = '\033[32m' 
    red = '\033[31m' 
    blue = '\033[36m' 
    pink = '\033[35m' 
    yellow = '\033[93m' 
    darkblue = '\033[34m' 
    white = '\033[00m'
    bluo = '\033[34m'
    red_p = '\033[41m'
    green_p = '\033[42m'
    bluo_p = '\033[44m'
    pink_p = '\033[45m'
    blue_p = '\033[46m'
    white_p = '\033[47m'
    rd = '\033[91m'
    black='\033[30m'
    bold = '\033[1m'
    underline = '\033[4m'
    magenta = '\033[95m'
    
    MAIN = '\001\033[38;5;85m\002'
    GREEN = '\001\033[38;5;82m\002'
    GRAY = PLOAD = '\001\033[38;5;246m\002'
    NAME = '\001\033[38;5;228m\002'
    RED = '\001\033[1;31m\002'
    FAIL = '\001\033[1;91m\002'
    ORANGE = '\001\033[0;38;5;214m\002'
    LRED = '\001\033[0;38;5;196m\002'
    BOLD = '\001\033[1m\002'
    PURPLE = '\001\033[0;38;5;141m\002'
    BLUE = '\001\033[0;38;5;12m\002'
    UNDERLINE = '\001\033[4m\002'
    UNSTABLE = '\001\033[5m\002'
    END = '\001\033[0m\002'


    ''' MSG Prefixes '''
    INFO = f'{MAIN}Info{END}'
    WARN = f'{ORANGE}Warning{END}'
    IMPORTANT = f'{ORANGE}Important{END}'
    FAILED = f'{RED}Fail{END}'
    ERR = f'{LRED}Error{END}'
    DEBUG = f'{ORANGE}Debug{END}'
    CHAT =f'{BLUE}Chat{END}'
    GRN_BUL = f'[{GREEN}*{END}]'
    META_INFO = '\001\033[38;5;93m\002I\001\033[38;5;129m\002N\001\033[38;5;165m\002F\001\033[38;5;201m\002O\001\033[0m\002'

#----[ Connections ]----
class Connection:
    import psutil
    
    global connections
    # Get all network connections
    connections = psutil.net_connections()
    
    # Numbers to Check
    famNum = 0
    laddrNum = 0
    raddrNum = 0
    pidNum = 0
    statusNum = 0
    typeNum = 0
    fieldsNum = 0
    
    def connectionFamily():
        for connects in connections:
            Connection.famNum += 1
            print(f"""
family :: {colors.yellow}{connects.family} {colors.yellow}({Connection.famNum}""")
        
        Connection.famNum = 0
        
    def connectionLAddr():
        for connects in connections:
            Connection.laddrNum += 1
            print(f"""
laddr :: {colors.yellow}{connects.laddr} {colors.yellow}({Connection.laddrNum}""")        
    
        Connection.laddrNum = 0
    
    def connectionPID():
        for connects in connections:
            Connection.pidNum += 1
            print(f"""
pid :: {colors.yellow}{connects.pid} {colors.yellow}({Connection.pidNum}""")        
        
        Connection.pidNum = 0
        
    def connectionRAddr():
        for connects in connections:
            Connection.raddrNum += 1
            print(f"""
raddr :: {colors.yellow}{connects.raddr} {colors.yellow}({Connection.raddrNum}""")        
        
        Connection.raddrNum = 0
        
    def connectionStatus():
        for connects in connections:
            Connection.statusNum += 1
            print(f"""
status :: {colors.yellow}{connects.status} {colors.yellow}({Connection.statusNum}""")        
        
        Connection.statusNum = 0
        
    def connectionType():
        for connects in connections:
            Connection.typeNum += 1
            print(f"""
type :: {colors.yellow}{connects.type} {colors.yellow}({Connection.typeNum}""")        
        
        Connection.typeNum = 0
        
    def connectionFields():
        for connects in connections:
            Connection.fieldsNum += 1
            print(f"""
fields :: {colors.yellow}{connects._fields} {colors.yellow}({Connection.fieldsNum}""")        
            
        Connection.fieldsNum = 0
        
#----[ Hash ]----
# This Class Created By BrupRocket Framework => https://github.com/Zrexer/BrupRocket
class Hasher:
    def __init__(self) -> None:

            self.hashlib = hashlib
            self.argv = sys.argv
            self.pool = requests
            self.rand = random
            self.socket = socket
            self.hashlist = ['sha1', 'sha256', 'sha224', 'sha512', 'sha384', 'sha3_256', 'sha3_224', 'sha3_512', 'sha3_384']
        
    def createHasher(self, text : str, type_of_encrypt : str):
        """
        Hash Creator
        ~~~~~~~~~~~~~
        ```
        from BrupRocket import BrupRocket as br
        
        app = br()
        data = app.createHasher(text="Hello world", type_of_encrypt="md5")
        print(data)
        ```
        
        Available Type of hash: 
        
        `md5`
        `sha1`
        `sha256`
        `sha224`
        `sha512`
        `sha384`
        `sha3_256`
        
        or you can select a random type , just use "random" on parameter.
        
        """
        
        t = type_of_encrypt
        
        if t == "md5":
            md5 = self.hashlib.md5()
            md5.update(text.encode())
            return md5.hexdigest()
        
        elif (
            t == "sha1"
            ):
            sha1 = self.hashlib.sha1()
            sha1.update(
                text.encode()
                )
            return (
                sha1.hexdigest()
                )
        
        elif (
            t == "sha256"
            ):
            sha256 = self.hashlib.sha256()
            sha256.update(
                text.encode()
                )
            return (
                sha256.hexdigest()
                )
        
        elif (
            t == "sha224"
            ):
            sha224 = self.hashlib.sha224()
            sha224.update(
                text.encode()
                )
            return (
                sha224.hexdigest()
                )
        
        elif (
            t == "sha512"
            ):
            sha512 = self.hashlib.sha512()
            sha512.update(
                text.encode()
                )
            return (
                sha512.hexdigest()
                )
        
        elif (
            t == "sha384"
            ):
            sha384 = self.hashlib.sha384()
            sha384.update(
                text.encode()
                )
            return (
                sha384.hexdigest()
                )
        
        elif (
            t == "sha3_256"
            ):
            sha3_256 = self.hashlib.sha3_256()
            sha3_256.update(
                text.encode()
                )
            return (
                sha3_256.hexdigest()
                )
        
        elif (
            t == "sha3_224"
            ):
            sha3_224 = self.hashlib.sha3_224()
            sha3_224.update(
                text.encode()
                )
            return (
                sha3_224.hexdigest()
                )
        
        elif (
            t == "sha3_512"
            ):
            sha3_512 = self.hashlib.sha3_512()
            sha3_512.update(
                text.encode()
            )
            return (
                sha3_512.hexdigest()
            )
            
        elif (
            t == "sha3_384"
        ):
            sha3_384 = self.hashlib.sha3_384()
            sha3_384.update(
                text.encode()
            )
            return (
                sha3_384.hexdigest()
            )
            
        elif (
            t == "random"
        ):
            result = (
                random.choice(self.hashlist)
            )
            
            return Hasher().createHasher(text=text, type_of_encrypt=result)




#----[ commands ]----
argv = sys.argv

#----[ os type ]----
osType = platform.system()

#----[ Main Class ]----
class MainActivity:
    
    def banner():
        return f"""
{colors.green}|= = = = = = = = = = = =|========[{colors.red} ***      
{colors.green}|    {colors.yellow}EXPLOIT{colors.green}            \                   
{colors.green}|                        \                  
{colors.green}|------------------------------------       
{colors.green}|===[{colors.cyan}0x00 > {colors.green}]=========================\      
{colors.green}|                                     \     
{colors.green}|-------------------------------------      
{colors.green}\({colors.magenta}@{colors.green})({colors.magenta}@{colors.green})({colors.magenta}@{colors.green})({colors.magenta}@{colors.green})({colors.magenta}@{colors.green})({colors.magenta}@{colors.green})({colors.magenta}@{colors.green})({colors.magenta}@{colors.green})({colors.magenta}@{colors.green})({colors.magenta}@{colors.green})({colors.magenta}@{colors.green})({colors.magenta}@{colors.green})/      
{colors.green} ************************************       

"""

    def usage():
        return f"""{colors.red}
you lost Arguments

try: ' 0x00 --help '
"""

    def helpConsole(dictNumber):
        dictX = {
            'commands' : [
                {
                    'command' : '--help',
                    'info' : 'show this message',
                    'usage' : '0x00 --help'
                },
                {
                    'command' : '--pool',
                    'info' : 'start a Request session',
                    'usage' : '0x00 --pool https://www.example.com/ [--status: to see status code[--json: to see json data]]'
                },
                {
                    'command' : ''
                }
            ]
        }
        
        return dictX['commands'][dictNumber]
    
    def main():
        
        print(MainActivity.banner())
        
        if len(argv) == 1:
            pass
        
        if "--pool" in argv:
            try:
                url = argv[argv.index('--pool')+1]
                if '--status' in argv:
                    try:
                        reqStatus = requests.get(url).status_code
                        print(f'\n{colors.green}{reqStatus}\n')
                    
                    except Exception as ERS:
                        print(f'\n{colors.red}{ERS}\n')
                        
                elif '--json' in argv:
                    try:
                        reqJson = requests.get(url).json()
                        print(f'\n{colors.green}{reqJson}\n')
                    
                    except Exception as ERJ:
                        print(f'\n{colors.red}{ERJ}\n')
                        
                else:
                    try:
                        reqStatus = requests.get(url).status_code
                        print(f'\n{colors.green}{reqStatus}\n')
                    
                    except Exception as ERS:
                        print(f'\n{colors.red}{ERS}\n')
                    
            except Exception as EUP:
                print(f'\n{colors.red}{EUP}{colors.white}\n')
                pass
            
            

        if "--figlet" in argv:
            if "-f" in argv:
                fontForfig = argv[argv.index('-f')+1]
                textToFig = argv[argv.index('--figlet')+1]
                
                print()
                print(pyfiglet.figlet_format(textToFig, font=fontForfig))
                print()
                
            else:
                textToFix0 = argv[argv.index('--figlet')+1]
                
                print()
                print(pyfiglet.figlet_format(textToFix0))
                print()
                
        if "--sysinfo" in argv:
            host = socket.gethostname()

            dataSYS = platform.uname()
            sysOS = dataSYS[0]
            sysNODE = dataSYS[1]
            sysRELEASE = dataSYS[2]
            sysVERSION = dataSYS[3]
            sysMACHINE = dataSYS[4]
            sysIP = socket.gethostbyname(host)
            sysName = getpass.getuser()
            print(f"""
{colors.green}host:{colors.yellow} {host}
{colors.green}os:{colors.yellow} {sysOS}
{colors.green}node:{colors.yellow} {sysNODE}
{colors.green}release:{colors.yellow} {sysRELEASE}
{colors.green}version:{colors.yellow} {sysVERSION}
{colors.green}machine:{colors.yellow} {sysMACHINE}
{colors.green}ip:{colors.yellow} {sysIP}
{colors.green}sysname:{colors.yellow} {sysName}
""")
        
        if "--getoutput" in argv:
            command = argv[argv.index('--getoutput')+1]
            data = subprocess.getoutput(command)
            
            print()
            print(f"\n{colors.green}{data}\n")
            print()
            
        if "--net-scanner" in argv:
            if not osType == 'Windows':
                print()
                print(f'\n{colors.red}Your OS is not Windows !\n')
                print()
            
            else:
                print(f"\n{colors.green}family\n")
                Connection.connectionFamily()
                print(f"\n{colors.green}fields\n")
                Connection.connectionFields()
                print(f"\n{colors.green}laddr\n")
                Connection.connectionLAddr()
                print(f"\n{colors.green}raddr\n")
                Connection.connectionRAddr()
                print(f"\n{colors.green}pid\n")
                Connection.connectionPID()
                print(f"\n{colors.green}status\n")
                Connection.connectionStatus()
                print(f"\n{colors.green}type\n")
                Connection.connectionType()
                
        if "--json-hasher" in argv:
            url = argv[argv.index('--json-hasher')+1]
            typeENC = argv[argv.index('--json-hasher')+2]
            try:
                req = requests.get(url).json()
                enc = Hasher().createHasher(req, typeENC)
                print(f'\n{colors.green}{enc}\n')
            except Exception as E:
                print(f'\n{colors.red}{E}\n')
                pass
                

if __name__ == '__main__':
    try:
        MainActivity.main()
    except KeyboardInterrupt:
        exit()
