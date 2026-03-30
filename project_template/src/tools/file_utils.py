import numpy as np

def get_ages_array(data):
    """Change list of data into massif array by numpy"""
    return np.array([item[2] for item in data]) if data else np.array([])

def finding_my_peer(data, target_year=2007):
    """By year of birstday finding my peer(im 2007)"""
    my_peer_list = []
    for surname, name, age, year in data:
        if year == target_year:
            my_peer_list.append(f"{surname} {name}")
    return my_peer_list