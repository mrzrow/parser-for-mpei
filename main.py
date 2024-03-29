import requests
from bs4 import BeautifulSoup

print('\n' + '_'*60 + '\n')


def find_pos(soup, snils):
    name = soup.find('div', class_='competitive-group').text
    vacancies = str(page.find('div', class_='title1')).split('<br/>')[2]
    print(f'{name}')
    print(f'{vacancies}\n')

    ind_add = 1
    count_agreed = 0
    all_abs = soup.find_all('tr', class_='accepted')
    for ind, ab in enumerate(all_abs):
        ab_inf = ab.find_all('td')

        ab_leaved = True if ab_inf[-1].text == 'Согласие в другой КГ' else False
        ab_agreed = True if ab_inf[-2].text == 'подано' else False
        ab_snils = ab_inf[-4].text

        if ab_leaved:
            ind_add -= 1
        if ab_agreed:
            count_agreed += 1
        if ab_snils == f'СНИЛС: {snils}':
            print(f'Place in the overall ranking: {ind + ind_add}')
            print(f'Place considering agreements: {count_agreed + 1}')
            break


snils = input('Enter  your SNILS (without hyphens): ')
sites = list(input('Enter links for each group with space:\n').split())
print()
for site in sites:
    src = requests.get(site)
    page = BeautifulSoup(src.text, 'lxml')
    find_pos(page, snils=snils)
    print('..' * 20 +'\n')
    
print('_' * 28 +'DONE' + '_' * 28 + '\n')
input('_Press eny key to close the programm_')
