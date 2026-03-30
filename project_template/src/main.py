"""
1. read input
2. array of my friends age + various moves with them, like: 
 --finding yhe younges, 
 --the oldest
 --count of friends
 --sum of all ages
 --mean(average) and median of ages
3. finding my peer
4. report 

"""
from tools.file_utils import get_ages_array, finding_my_peer
from tools.report import print_results, print_peers
from tools.read_input import read_data

if __name__=='__main__':
    data=read_data()
    ages=get_ages_array(data)
    peers=finding_my_peer(data,2007)

    print_results(ages)
    print_peers(peers,2007)