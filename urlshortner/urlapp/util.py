from urlapp.models import URLS
import random

def generateHash(counter):
    number_string = '0123456789'
    lower_string = 'abcdefghijklmnopqrstuvwxyz'
    upper_string = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    hash_string = ''
    while counter > 0:
        k = random.randint(1,62)
        ind = int(counter%k) + k
        #print(ind)
        hash_string += number_string[int(ind%random.randint(1,10))]
        hash_string += lower_string[int(ind%random.randint(1,26))]
        hash_string += upper_string[int(ind%random.randint(1,26))]
        counter /= k
    return hash_string


def hash(long_url_counter):
    short_url = ''
    hash_value = generateHash(long_url_counter)
    hash_value = hash_value[0:7]
    short_url += hash_value
    return hash_value,short_url

def checkHash(long_url):
    data = URLS.objects.filter(long_url=long_url).values()
    print(data)
    if not data:
        hash_value,short_url = hash(2)
        while URLS.objects.filter(id=hash_value).first() is not None:
            t = URLS.objects.filter(id=hash_value).first()
            counter = t['counter']
            t['counter'] += 1
            t.save()
            hash_value,short_url = hash(counter + 1)
        instance = URLS(id=hash_value,long_url=long_url,short_url=short_url,counter=2)
        instance.save()
        return short_url
    else:
        return data[0]['short_url']
