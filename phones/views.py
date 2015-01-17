import urllib2
from django.template import Template, RequestContext
from django.shortcuts import render, render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.views.generic.detail import DetailView
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import json
import random
import math

from phones.models import Phone, Review
from forms import UpdatePhoneForm
from django.db import connection

from select import PhoneQuery

from pprint import pprint as pp

def dictfetchall(cursor):
    "Returns all rows from a cursor as a dict"
    desc = cursor.description
    return [
        dict(zip([col[0] for col in desc], row))
        for row in cursor.fetchall()
    ]

def savePhone(phone, old_model_number):
#    pq = PhoneQuery()
#    pq.insert(phone)
    cursor = connection.cursor()
    if old_model_number is not None and old_model_number != '':
        cursor.execute("UPDATE phones SET\
            model_number=%s,ram=%s,processor=%s,manufacturer=%s,system=%s,screen_size=%s, screen_resolution=%s, battery_capacity=%s, talk_time=%s, camera_megapixels=%s, price=%s, weight=%s, storage_options=%s, dimensions=%s\
    \
            WHERE model_number=%s;",
                [
                    phone.model_number,
                    phone.ram, 
                    phone.processor, 
                    phone.manufacturer, 
                    phone.system, 
                    phone.screen_size,
                    phone.screen_resolution,
                    phone.battery_capacity,
                    phone.talk_time,
                    phone.camera_megapixels,
                    phone.price,
                    phone.weight,
                    phone.storage_options,
                    phone.dimensions,
                    old_model_number, 
                ]
            )
    else:
        try:
            cursor.execute("INSERT INTO phones(\
                    model_number, ram, processor, manufacturer, system, screen_size, screen_resolution, battery_capacity, talk_time, camera_megapixels, price, weight, storage_options, dimensions) VALUES\
                    (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                    [
                        phone.model_number, 
                        phone.ram, 
                        phone.processor, 
                        phone.manufacturer, 
                        phone.system, 
                        phone.screen_size,
                        phone.screen_resolution,
                        phone.battery_capacity,
                        phone.talk_time,
                        phone.camera_megapixels,
                        phone.price,
                        phone.weight,
                        phone.storage_options,
                        phone.dimensions,
                    ]
                )
        except:
            pass

def deletePhone(request, model_number):
#    pq = PhoneQuery()
#    pq.delete_by_model_num(model_number)

    model_number = model_number.decode('utf-8')
    cursor = connection.cursor()
    try:
        cursor.execute("DELETE FROM phones\
                    WHERE model_number=\"%s\";" % model_number
                )
    except:
        # silently ignore
        print("except when deleting")
    return HttpResponseRedirect('/#phones')
#    return render(request, 'phones/delete.tpl', {'model_number':model_number})

class PhoneDetailView(DetailView):
    model = Phone
    template_name = 'phones/detail.tpl'

# Create your views here.
def allPhones(request):
    phone_raw_qry = Phone.objects.raw('SELECT * FROM phones')
    phone_all = []
    for p in phone_raw_qry:
        phone_all.append(p.toDict())
    return HttpResponse(json.dumps(phone_all), content_type='application/json') 

def getPhone(request):
    model_num = request.GET.get('model_number')
    phone_raw_qry = Phone.objects.raw('SELECT * FROM phones WHERE model_number = \"%s\"' % model_num)
    phone_all = []
    for p in phone_raw_qry:
        print p
        phone_all.append(p.toDict())
    ret = phone_all[0] if len(phone_all) > 0 else None
    print phone_raw_qry
    print phone_all
    return HttpResponse(json.dumps(ret), content_type='application/json')

def index(request):
#    pq = PhoneQuery()
#    phone_list = pq.select(None)
    PAGE_SIZE = 20
    MAX_PAGE_LINK = 10
    MID_PAGES = 5
    phone_raw_qry = Phone.objects.raw('SELECT * FROM phones')
    phone_all = []
    for p in phone_raw_qry:
        phone_all.append(p)

    paginator = Paginator(phone_all, PAGE_SIZE)
    page_str = request.GET.get('page')
    try:
        page = int(page_str)
        phone_list = paginator.page(page)
    except PageNotAnInteger:
        phone_list = paginator.page(1)
        page = 1
    except EmptyPage:
        phone_list = paginator.page(paginator.num_pages)
        page = paginator.num_pages
    except:
        page = 1
        phone_list = paginator.page(1)
    
    page_names = []
    
    if (paginator.num_pages > MID_PAGES*2 + 3):
        mid_left = page - MID_PAGES
        if mid_left < 1:
            mid_left = 1

        mid_right = page + MID_PAGES
        if mid_right > paginator.num_pages:
            mid_right = paginator.num_pages

        if mid_left > 1:
            page_names += ['...']

        for i in range(mid_left, mid_right+1):
            page_names += [i]

        if mid_right < paginator.num_pages:
            page_names += ['...']
    else:
        for i in range(1, paginator.num_pages+1):
            page_names += [i]

    page_prev = page - 1
    page_next = page + 1

    if page_next > paginator.num_pages:
        page_next = -1
    context = {
            'phone_list' : phone_list,
            'page_names' : page_names,
            'page_prev' : page_prev,
            'page_next' : page_next,
            'page' : page,
            }

    return render(request, 'phones/index.tpl', context)

def suggest(request):
    print("TYPE", type(request.GET))
    dict = {
                'ram':(1500, 3000),
                'screen_size':(5, 10),
                'battery_capacity':(-2, 3000),
                'talk_time':(-2, 500),
                'camera_megapixels':(-2, 5),
                'price':(-2, 1500),
                'weight':(-2, 10),
           }
    qry = buildQuery(dict)
    phone_list = Phone.objects.raw(qry)
    return render_to_response('phones/index.tpl', 
                             {'phone_list': phone_list},context_instance=RequestContext(request))

def apiSuggest(request):
    print("TYPE", type(request.GET))
    data = json.loads(request.body)
    qry_param = {}
    for key in data:
        qry_param[key] = data[key]
    qry = buildQuery(qry_param, '')
    cursor = connection.cursor()
    cursor.execute(qry)
    suggest_phones = dictfetchall(cursor)
    cursor.close()
    return HttpResponse(json.dumps(suggest_phones), content_type="application/json")

def buildQuery(criteria, model_number):
    where_clause = ''
    video_criteria = ''
    text_criteria = ''

    try:
        phone_criteria = []
        phone_criteria += [" model_number <> \"{0}\"".format(model_number)]
        if 'ram' in criteria:
            phone_criteria += [" (ram>{0} AND ram<{1}) ".format(criteria['ram'][0], criteria['ram'][1])]

        if 'screen_size' in criteria:
            phone_criteria += [" (screen_size>{0} AND screen_size<{1}) ".format(criteria['screen_size'][0], criteria['screen_size'][1])]
        if 'battery_capacity' in criteria:
            phone_criteria += [" (battery_capacity<0 OR (battery_capacity>{0} AND battery_capacity<{1})) ".format(criteria['battery_capacity'][0], criteria['battery_capacity'][1])]
        if 'talk_time' in criteria:
            phone_criteria += [" (talk_time<0 OR (talk_time>{0} AND talk_time<{1})) ".format(criteria['talk_time'][0], criteria['talk_time'][1])]

        if 'camera_megapixels' in criteria:
            phone_criteria += [" (camera_megapixels<0 OR (camera_megapixels>{0} AND camera_megapixels<{1})) ".format(criteria['camera_megapixels'][0], criteria['camera_megapixels'][1])]

        if 'price' in criteria:
            phone_criteria += [" (price>{0} AND price<{1}) ".format(criteria['price'][0], criteria['price'][1])]

        if 'weight' in criteria:
            phone_criteria += [" (weight<0 OR (weight>{0} AND weight<{1})) ".format(criteria['weight'][0], criteria['weight'][1])]


        if len(phone_criteria) > 0:
            where_clause = ' WHERE '
            for r in range(len(phone_criteria)-1):
                where_clause += phone_criteria[r] + " AND "

            where_clause += phone_criteria[-1]

        if 'text_rating' in criteria:
            text_criteria = " WHERE rating>{0} AND rating>{1} ".format(criteria['text_rating'][0], criteria['text_rating'][1])

        if 'video_rating' in criteria:
            video_criteria = " WHERE rating>{0} AND rating>{1} ".format(criteria['video_rating'][0], criteria['video_rating'][1])
    except:
        pass

    qry = "SELECT s1.model_number, s1.image FROM (SELECT model_number, image FROM phones" + where_clause + ")as s1 JOIN (SELECT s2.model_number FROM (SELECT model_number FROM text_reviews " + text_criteria + ") as s2 JOIN (SELECT model_number FROM video_reviews" + video_criteria + ") AS s3 ON s2.model_number = s3.model_number) as s4 ON s1.model_number = s4.model_number"
    print('***************', qry)
    return qry


def search(request):
    key = request.POST['q']
    qry = "SELECT * FROM phones WHERE model_number LIKE '%%%%%s%%%%'" % key
    print qry
    phone_list = Phone.objects.raw(qry)
    print ("phonelist", connection.queries)
    return render_to_response('phones/index.tpl', 
                             {'phone_list': phone_list, 'scroll': True},context_instance=RequestContext(request))
    
def detail(request, model_number):
    #try:
    phone = Phone.objects.raw('SELECT * FROM phones WHERE model_number = \"%s\"' % model_number)
    phone = phone[0]

    #print phone
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM text_reviews WHERE model_number="%s";' % model_number) 
    text_reviews =dictfetchall(cursor)
    cursor.close()

    cursor = connection.cursor()
    cursor.execute('SELECT * FROM video_reviews WHERE model_number="%s";' % model_number) 
    video_reviews = dictfetchall(cursor)
    print(">>>VIDEO REVIEWS:")
    cursor.close()

    # suggest phones
    criteria = {}
    if phone.ram > 0:
        criteria['ram'] = (phone.ram * 0.5 + 1, phone.ram * 1.5)
    if phone.screen_size > 0:
        criteria['screen_size'] = (phone.screen_size - 0.5, phone.screen_size + 0.5)
    if phone.price > 0:
        criteria['price'] = (phone.price-300, phone.price+300)

    qry = buildQuery(criteria, model_number)
    cursor = connection.cursor()
    cursor.execute(qry)
    suggest_phones = dictfetchall(cursor)
    cursor.close()
    
    if len(suggest_phones) > 15:
        suggest_phones = random.sample(suggest_phones, 15)
    else:
        suggest_phones = random.shuffle(suggest_phones)
#    suggest_phones = suggest_phones[:15] if len(suggest_phones)>20 else suggest_phones

    context = {
            'phone': phone, 
            'text_reviews':text_reviews, 
            'video_reviews':video_reviews,
            'suggest_phones':suggest_phones,
        }

    return render(request, 'phones/detail.tpl', context)
    """
    except:
        return HttpResponseRedirect('/')
    """

def addPhone(request):
    return updatePhone(request, '')

# update phone
def updatePhone(request, model_number):
    print('update', model_number)
    model_number = model_number.decode('utf-8')
    # model_number = urllib2.unquote(model_number)
    print('update', model_number)
    """
    if not request.user.is_authenticated():
        # not auth, give error page
        raise Http404
        form = UpdatePhoneForm()
        return render(request, 'phones/updatePhone.tpl', {'form': form})
    """    
    if request.method=='POST':
        form = UpdatePhoneForm(request.POST)
        # pprint(request.POST)
        #Phone(model_number='update', ram=1, processor='arm', manufacturer='me', system='sys', screen_size='1x1')
        phone = Phone(
                model_number=request.POST['model_number'],
                ram=request.POST['ram'],
                processor=request.POST['processor'],
                manufacturer=request.POST['manufacturer'],
                system=request.POST['system'],
                screen_size=request.POST['screen_size'],
                screen_resolution=request.POST['screen_resolution'],
                battery_capacity=request.POST['battery_capacity'],
                talk_time=request.POST['talk_time'],
                camera_megapixels=request.POST['camera_megapixels'],
                price=request.POST['price'],
                weight=request.POST['weight'],
                storage_options=request.POST['storage_options'],
                dimensions=request.POST['dimensions'],
            )
        old_model_number = request.POST['old_model_number']
        # TODO: sanity check
        # phone.save()
        savePhone(phone, old_model_number)
        
        print ("save phone:", connection.queries)
        return HttpResponseRedirect('/{0}'.format(phone.model_number))
        
    elif str(model_number) != '':
        name_map = {
            'model_number':'model_number',
            'ram':'ram',
            'processor':'processor',
            'manufacturer':'manufacturer',
            'system':'system',
            'screen_size':'screen_size',
            'screen_resolution':'screen_resolution',
            'battery_capacity':'battery_capacity',
            'talk_time':'talk_time',
            'camera_megapixels':'camera_megapixels',
            'price':'price',
            'weight':'weight',
            'storage_options':'storage_options',
            'dimensions':'dimensions',
            }

        key = model_number
        phone = Phone.objects.raw('SELECT * FROM phones WHERE model_number=\"{0}\"'.format(model_number), translations=name_map)
        print(phone)
        phone = phone[0]
        print(phone)
            
        form = UpdatePhoneForm(phone.toDict())
    else:
        form = UpdatePhoneForm()
        
    return render(request, 'phones/updatePhone.tpl', {'form': form, 'model_number': model_number})

