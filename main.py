
"""
1. read auth.log
2. filter lines
3. parsing 
4. report 

"""
from tools.read_log import read_auth_log
from tools.counting_problems import count_errors
from tools.report import print_report

if __name__=='__main__':
    data=read_auth_log()
    x=count_errors(data)
    print_report(x)


