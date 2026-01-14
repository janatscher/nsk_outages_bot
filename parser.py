from bs4 import BeautifulSoup
import requests

main_link = 'http://051.novo-sibirsk.ru/SitePages/off.aspx'
link_hw = 'http://051.novo-sibirsk.ru/SitePages/offfull.aspx?System=7&District=d_0JfQsNC10LvRjNGG0L7QstGB0LrQuNC5#0JfQsNC10LvRjNGG0L7QstGB0LrQuNC5'
link_cw = 'http://051.novo-sibirsk.ru/SitePages/offfull.aspx?System=8&District=d_0JvQtdC90LjQvdGB0LrQuNC5#0JvQtdC90LjQvdGB0LrQuNC5'
link_ht = 'http://051.novo-sibirsk.ru/SitePages/offfull.aspx?System=12&District=d_0JfQsNC10LvRjNGG0L7QstGB0LrQuNC5#0JfQsNC10LvRjNGG0L7QstGB0LrQuNC5'
link_el = 'http://051.novo-sibirsk.ru/SitePages/offfull.aspx?System=9&District=d_0JvQtdC90LjQvdGB0LrQuNC5#0JvQtdC90LjQvdGB0LrQuNC5'

def parse(utility):
    if utility == 'hw':
        response = requests.get(link_hw)
    elif utility == 'cw':
        response = requests.get(link_cw)
    elif utility == 'ht':
        response = requests.get(link_ht)
    elif utility == 'el':
        response = requests.get(link_el)
    page = BeautifulSoup(response.text, 'html.parser')
    page = page.prettify() #преттифай нужен обязательно чтобы форматирование работало
    soup = BeautifulSoup(page, 'html.parser')

    #список районов и информации
    f = ''.join([x.text.strip() for x in soup])
    f = f.replace('\xa0\xa0\xa0', '\n')
    f = f.split('\n')
    f = [x.strip() for x in f if x != '']
    f[:f.index('Отключения систем жизнеобеспечения')+1] = ''
    f[f.index('© Мэрия г. Новосибирска, 2013-2021. Сайт разработан компанией'):] = ''
    f = ' '.join(f)
    f = f.replace('району', 'бббб')
    f = f.split('район')
    for i in range(1, len(f)-1):
        if 'Железнодорожный' in f[i]:
            f[i] = ''.join(f[i][:-16] + 'pu' + f[i][-16:])
        elif 'Ленинский' not in f[i] and 'Советский' not in f[i] and 'Кировский' not in f[i]:
            f[i] = ''.join(f[i][:-13] + 'pu' + f[i][-13:])
        else:
            f[i] = ''.join(f[i][:-11] + 'pu' + f[i][-11:])
    for i in range(len(f)):
        f[i] = f[i].split('pu')
    nf = f[0]
    for i in range(1, len(f)):
        for j in range(len(f[i])):
            nf.append(f[i][j])

    #список районов
    dists = []
    for d in range(0, len(nf), 2):
        dists.append(nf[d])
    dists = [x.strip() for x in dists]

    #список информации
    info = []
    for i in range(1, len(nf), 2):
        info.append(nf[i])

    #список информации без лишнего
    for i in range(len(info)):
        info[i] = info[i].split('  ')
        for j in range(len(info[i])):
            if 'трассы' in info[i][j]: info[i][j] = ''
            elif 'снабжение' in info[i][j]: info[i][j] = ''
            elif 'Отключение ТП' in info[i][j]: info[i][j] = ''
            elif 'между' in info[i][j]: info[i][j] = ''
            elif 'Филиал' in info[i][j]: info[i][j] = ''
            elif 'параметр' in info[i][j]: info[i][j] = ''
            elif 'до ' in info[i][j]: info[i][j] = ''
            elif 'ЦТП' in info[i][j]: info[i][j] = ''
            elif '+' in info[i][j]: info[i][j] = ''
            elif 'дефект' in info[i][j]: info[i][j] = ''
            elif 'Кто отключил' in info[i][j]: info[i][j] = ''
            elif '"' in info[i][j]: info[i][j] = ''
            elif '«' in info[i][j]: info[i][j] = ''
            elif 'Горячее водоснабжение' in info[i][j]: info[i][j] = ''
            elif info[i][j] == 'Поставщик услуги': info[i][j] = ''
            elif info[i][j] == 'Поставщик услуги:': info[i][j] = ''
            elif info[i][j] == 'Телефон диспетчерской:': info[i][j] = ''
            elif info[i][j] == 'Дополнительная информация:': info[i][j] = ''
        info[i] = [x for x in info[i] if x != '']
    info = [x for x in info if x != '']

    all_info = dict(zip(dists, info))

    return all_info, dists, info
