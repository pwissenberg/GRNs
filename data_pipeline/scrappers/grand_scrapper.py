import requests
'''
r = requests.get('https://grand.networkmedicine.org/api/v1/tissueapi/').json()
print(r.get('next'))
print(r.get('results'))

#Second side
r2 = requests.get('https://grand.networkmedicine.org/api/v1/tissueapi/?page=2').json()
print(r2)
'''

def get_next_subpage(url: str, file ):
    r = requests.get(url).json()
    #Get results
    results = r.get('results')
    for sample in results:
        f.write(sample.get('network')+'\n')
    if(r.get('next') != None):
        get_next_subpage(r.get('next'), file)
f = open('../../resources/grand_network_links.txt', 'a')

get_next_subpage('https://grand.networkmedicine.org/api/v1/tissueapi/', f)