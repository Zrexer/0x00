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
import psutil
import pyfiglet
import getpass
import socket

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
    
    def main():
        
        print(MainActivity.banner())
        
        if "--pool" in argv:
            url = argv[argv.index('--pool')+1]
            pov = argv[argv.index('--pool')+2]
            
            if pov == '--status':
                try:
                    reqStatus = requests.get(url).status_code
                    print(f'\n{colors.green}{reqStatus}\n')
                
                except Exception as ERS:
                    print(f'\n{colors.red}{ERS}\n')
                    
            elif pov == '--json':
                try:
                    reqJson = requests.get(url).json()
                    print(f'\n{colors.green}{reqJson}\n')
                
                except Exception as ERJ:
                    print(f'\n{colors.red}{ERJ}\n')
                    
            else:
                try:
                    reqStatusx = requests.get(url).status_code
                    print(f'\n{colors.green}{reqStatusx}\n')
                
                except Exception as ERSX:
                    print(f'\n{colors.red}{ERSX}\n')

        elif "--figlet" in argv:
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
                
        elif "--sysinfo" in argv:
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
        
        elif "--getoutput" in argv:
            command = argv[argv.index('--getoutput')+1]
            data = subprocess.getoutput(command)
            
            print()
            print(f"\n{colors.green}{data}\n")
            print()
            
        elif "--net-scanner" in argv:
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

MainActivity.main()