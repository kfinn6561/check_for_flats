from config import *
import requests
from bs4 import BeautifulSoup
from flats import Flat
from general_tools import pload,remove_excess_whitespace

checks=[]

class Site_Checker():
    def __init__(self,name,url,class_name,method,placeholder='') -> None:
        self.name=name
        self.url=url
        self.method=method
        self.class_name=class_name
        self.placeholder=placeholder
    def __call__(self):
        print('Checking ' + self.name)
        try:
            response=requests.get(self.url)
        except:
            print('Error connecting to '+self.name)
            return []
        soup=BeautifulSoup(response.text,'lxml')
        properties=soup.select(self.class_name)
        out=[]
        for property in properties:
            if str(property)!=self.placeholder:
                try:
                    out.append(self.method(property))
                except:
                    print('error translating soup for ' +self.name)
                    pdump(str(property),'error_property.pkl')
        return out


rightmove_urls=[('Hoos Extended','https://www.rightmove.co.uk/property-to-rent/find.html?locationIdentifier=USERDEFINEDAREA%5E%7B%22id%22%3A6921602%7D&sortType=6&savedSearchId=38159337&maxPrice=1300&radius=0.0&propertyTypes=&mustHave=&dontShow=retirement%2ChouseShare&includeLetAgreed=false&furnishTypes=furnished'),
                ('Milngavie','https://www.rightmove.co.uk/property-to-rent/find.html?keywords=&sortType=6&includeLetAgreed=false&viewType=LIST&channel=RENT&index=0&maxPrice=1300&radius=0.0&locationIdentifier=REGION%5E17298'),
                ('Stirling','https://www.rightmove.co.uk/property-to-rent/find.html?locationIdentifier=REGION%5E1266&maxPrice=1300&propertyTypes=&includeLetAgreed=false&mustHave=&dontShow=houseShare%2Cretirement%2Cstudent&furnishTypes=&keywords='),
                ('Linlithgow','https://www.rightmove.co.uk/property-to-rent/find.html?locationIdentifier=REGION%5E806&maxPrice=1300&propertyTypes=&includeLetAgreed=false&mustHave=&dontShow=houseShare%2Cretirement%2Cstudent&furnishTypes=&keywords=')]


def rightmove_flat(soup):
    id='rightmove'+soup.find('a').get('id')
    link_soup=soup.select_one('.propertyCard-link')
    link='www.rightmove.co.uk'+link_soup.get('href').split('#')[0]
    description=link_soup.text
    return Flat(id,description,link)

for name, url in rightmove_urls:
    checks.append(Site_Checker('Rightmove: '+name,url,'.propertyCard',rightmove_flat,placeholder=pload(RIGHTMOVE_PLACEHOLDER_FNAME)))


def clyde_property_flat(soup):
    relative_link=soup.find('a').get('href')
    id='clyde'+relative_link.split('/')[-1]
    absolute_link='www.clydeproperty.co.uk'+relative_link
    description=soup.select_one('.property-item-info').text
    return Flat(id,description,absolute_link)

checks.append(Site_Checker('Clyde Property','https://www.clydeproperty.co.uk/search/West%20End%20Glasgow:55.8825861:-4.3019795:West%20End:place:West%20End/any/any/1300/any/any/any/any/any/2/1/price/',
                            '.property-avatar',clyde_property_flat))



dj_urls=[('G12','https://www.djalexander.co.uk/rent/map/location/g12/beds/0/from/any/to/1500/furnished/yes/hmo/no/order/DESC'),
        ('G3','https://www.djalexander.co.uk/rent/map/location/g3/beds/0/from/any/to/1500/furnished/yes/hmo/no/order/DESC'),]

def dj_alexander_flat(soup):
    relative_link=soup.get('data-purl')
    id='dj-alexander'+relative_link.split('/')[-1]
    absolute_link='www.djalexander.co.uk'+relative_link
    description=soup.select_one('.property-bedroom').text
    description+=' '+soup.select_one('.property-address').text
    description+=': '+soup.select_one('.property-price').text
    return Flat(id,description,absolute_link)

for name,url in dj_urls:
    checks.append(Site_Checker('DJ Alexander: '+name,url,'.property-box',dj_alexander_flat))


def tay_letting_flat(soup):
    relative_link=soup.get('href')
    id='tayletting'+relative_link.split('/')[-2]
    absolute_link='www.tayletting.co.uk'+relative_link
    description=soup.select_one('.title-desc').find('h4').text
    return Flat(id,description,absolute_link)

checks.append(Site_Checker('Tay Letting','https://www.tayletting.co.uk/property/?wppf_max_rent=1300&wppf_branch=smepro_1&wppf_soldlet=show&wppf_orderby=latest&wppf_view=grid&wppf_lat=0&wppf_lng=0&wppf_radius=10&wppf_records=12',
                            '.wppf_property_item',tay_letting_flat))


def slater_hogg_flat(soup):
    relative_link=soup.find('a').get('href')
    id='slaterhogg'+relative_link.split('/')[-2].split('-')[-1]
    description=soup.select_one('.card__text-title').text
    description+=' '+soup.select_one('.card__text-content').text
    absolute_link='www.slaterhogg.co.uk'+relative_link
    return Flat(id,description,absolute_link)

checks.append(Site_Checker('Slater Hogg and Howison','https://www.slaterhogg.co.uk/rent/search/west-end-glasgow/page-1/pricing-monthly/price-to-1300/',
                            '.card',slater_hogg_flat,placeholder=pload(SLATERHOGG_PLACEHOLDER_FNAME)))


def openrent_flat(soup):
    id='openrent'+soup.get('id')
    link='www.openrent.co.uk'+soup.get('href')
    description=soup.select_one('.listing-title').text
    return Flat(id,description,link)

checks.append(Site_Checker('OpenRent','https://www.openrent.co.uk/properties-to-rent/glasgow-west-end-scotland?term=Glasgow,%20West%20End,%20Scotland&prices_min=258&prices_max=1300&bedrooms_min=1&bedrooms_max=5&furnishedType=1&acceptNonStudents=true',
                            '.pli',openrent_flat))


def rettie_flat(soup):
    relative_link=soup.get('href')
    id='rettie'+relative_link.split('/')[-2]
    absolute_link='www.rettie.co.uk'+relative_link
    description=soup.select_one('.property-title').text
    return Flat(id,description,absolute_link)


checks.append(Site_Checker('Rettie','https://www.rettie.co.uk/property-for-rent/glasgow-city/glasgow-west-end/lettings/tag-furnished/up-to-1300',
                            '.property-block',rettie_flat))



def yates_hellier_flat(soup):
    description_html=soup.select_one('.details').find('a')
    link=description_html.get('href')
    id='yateshellier'+link.split('/')[-2]
    description=description_html.text
    return Flat(id, description,link)


checks.append(Site_Checker('Yates Hellier','https://yateshellier.com/properties/?address_keyword=&minimum_bedrooms=&maximum_bedrooms=&minimum_rent=0&maximum_rent=1300&minimum_price=&maximum_price=&department=residential-lettings',
                            '.type-property', yates_hellier_flat))


def check_sites():
    out=[]
    for check in checks:
        out+=check()
    return out
