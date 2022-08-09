# from django.http import JsonResponse
# import requests
# import json
# from .models import *
# from .documents import NewsDocument
# from django.shortcuts import render,HttpResponse
#
# from .documents import *
# from .serializers import *
# from django_elasticsearch_dsl_drf.filter_backends import (
#     FilteringFilterBackend,
#     CompoundSearchFilterBackend
# )
# from django_elasticsearch_dsl_drf.viewsets import DocumentViewSet
# from django_elasticsearch_dsl_drf.filter_backends import (
#     FilteringFilterBackend,
#     OrderingFilterBackend,
# )
# from .documents import NewsDocument
#
#
# #
# # def generate_random_data():
# #     url = 'https://newsapi.org/v2/everything?q=apple&from=2021-04-23&to=2021-04-23&sortBy=popularity&apiKey=827705eea42e455cba8bf4afafc7da90'
# #     r = requests.get(url)
# #     payload = json.loads(r.text)
# #     count = 1
# #     for data in payload.get('articles'):
# #         print(count)
# #         ElasticDemo.objects.create(
# #             title = data.get('title'),
# #             content = data.get('description')
# #         )
#
#
# def generate_random_data2():
#     url = 'https://newsapi.org/v2/everything?q=apple&from=2021-04-23&to=2021-04-23&sortBy=popularity&apiKey=827705eea42e455cba8bf4afafc7da90'
#     r = requests.get(url)
#     payload = json.loads(r.text)
#     count = 1
#     for data in payload.get('articles'):
#         print(count)
#         ElasticDemo2.objects.create(
#             title=data.get('title'),
#             content=data.get('description')
#         )
#     # # the file to be converted
#     # filename = './home/ens.txt'
#     # # resultant dictionary
#     # dict1 = {}
#     # # fields in the sample file
#     # fields = ['link', 'date', 'title', 'content']
#     # with open(filename) as fh:
#     #     # count variable for employee id creation
#     #     l = 1
#     #     for line in fh:
#     #         print("aaaaaaaaaaaaaaaaaaaaaaa")
#     #         dizi = []
#     #         # new_line=line.split(';')
#     #         # ElasticDemo2.objects.create(
#     #         #     link={new_line[0]},
#     #         #     date={new_line[1]},
#     #         #     title={new_line[2]},
#     #         #     content={new_line[3]}
#     #         # )
#     #
#     #         #
#     #         # # reading line by line from the text file
#     #         description = list(line.split(';', 4))
#     #         print("aaaaaaaaaaabbbbbbbbbbbb")
#     #         # # for output see below
#     #         # # print(description)
#     #         # # for automatic creation of id for each employee
#     #         sno = 'news' + str(l)
#     #         # # loop variable
#     #         # i = 0
#     #         # # intermediate dictionary
#     #         dict2 = {}
#     #         while i < len(fields):
#     #             print("aaaaaaaaaaabbbbcccccccccccccc")
#     #             # creating dictionary for each employee
#     #             dict2[fields[i]] = description[i] #new_line[i]
#     #             i = i + 1
#     #         # # appending the record of each employee to
#     #         # # the main dictionary
#     #         # print("aaaaaadddddddddddd")
#     #         dict1[sno] = dict2
#     #         l = l + 1
#     #         dizi.append(dict2["link"])
#     #         dizi.append(dict2["date"])
#     #         dizi.append(dict2["title"])
#     #         dizi.append(dict2["content"])
#     #         # json_object = json.loads(dict1[sno], indent=4)
#     #         # # print(json_object)
#     #         # # for data in json_object:
#     #         # #     # print(count)
#     #         # #     print('}}}}}}}}}}==============')
#     #         # #     print(data)
#     #         # print("aaaaaaaeeeeeeeeeeeee")
#     #         # ElasticDemo2.objects.create(
#     #         #     # print("aaaafffffffffffffffffff")
#     #         #     link=dict2["link"],  # json_object["link"],
#     #         #     date=dict2["date"],  # json_object["date"],
#     #         #     title=dict2["title"],  # json_object["title"],
#     #         #     content=dict2["content"] # json_object["content"],
#     #         #     # link="a",#json_object["link"],
#     #         #     # date="a",#json_object["date"],
#     #         #     # title="a",#json_object["title"],
#     #         #     # content="a",#json_object["content"],
#     #         # )
#     #         print("aaaaaaagggggggggggggggggg")
#     #         # ElasticDemo2.objects.create(
#     #         #     link=dizi[0],  # json_object["link"],
#     #         #     date=dizi[1],  # json_object["date"],
#     #         #     title=dizi[2],  # json_object["title"],
#     #         #     content=dizi[3],  # json_object["content"],
#     #         #     # link="a",#json_object["link"],
#     #         #     # date="a",#json_object["date"],
#     #         #     # title="a",#json_object["title"],
#     #         #     # content="a",#json_object["content"],
#     #         # )
#     #
#     # # creating json file
#     # # out_file = open("testjs.json", "w")
#     # # json.dump(dict1, out_file)#, indent=4)
#     # #
#     # # payload = json.loads(out_file)
#     # count = 1
#     # # for data in payload:
#     # #     print(count)
#     # #     print('}}}}}}}}}}==============')
#     # #     print(data)
#     # #     ElasticDemo2.objects.create(
#     # #         link=data.get('link'),
#     # #         date=data.get('date'),
#     # #         title=data.get('title'),
#     # #         content=data.get('description')
#     # #     )
#     #
#     # # out_file.close()
#     #
#
# # generate_random_data2()
#
# def index(request):
#     generate_random_data2()
#     return JsonResponse({'status': 200})
#
# #
# # def arama(request):
# #     q = request.GET.get('q')
# #     if q:
# #         # posts=Document.search().query('match',title=q)
# #         posts = NewsDocument.search().query('match', title=q)
# #         # posts=Document.search().query('match',title=q)
# #     else:
# #         posts = ''
# #     return render(request, 'templates/arama.html', {'posts': posts})
#
#
# class PublisherDocumentView(DocumentViewSet):
#     document = NewsDocument
#     serializer_class = NewsDocumentSerializer
#     lookup_field = 'title'
#     fielddata = True
#     filter_backends = [
#         FilteringFilterBackend,
#         OrderingFilterBackend,
#         CompoundSearchFilterBackend,
#     ]
#
#     search_fields = (
#         'link',
#         'date',
#         'title',
#         'content',
#     )
#     multi_match_search_fields = (
#         'link',
#         'date',
#         'title',
#         'content',
#     )
#     filter_fields = {
#         'link': 'link',
#         'date': 'date',
#         'title': 'title',
#         'content': 'content',
#     }
#     ordering_fields = {
#         'id': None,
#     }
#     ordering = ('id',)
#
# #============================ end of  elastic search   }}}}}}}}}}}}}}}}}}}}}}}
#





#
#
# from elasticsearch import Elasticsearch
# import json
# file=".ens.txt"
# payload = json.loads(file)
# count = 1
# for data in payload.get('articles'):
#     print(count)
#     ElasticDemo.objects.create(
#         title = data.get('title'),
#         content = data.get('description')
#     )
#
#
# def tojson():
#     # the file to be converted
#     filename = './home/ens.txt'
#
#     # resultant dictionary
#     dict1 = {}
#
#     # fields in the sample file
#     fields = ['link', 'date', 'title', 'content']
#
#     with open(filename) as fh:
#
#         # count variable for employee id creation
#         l = 1
#
#         for line in fh:
#
#             # reading line by line from the text file
#             description = list(line.strip().split(';', 4))
#
#             # for output see below
#             print(description)
#
#             # for automatic creation of id for each employee
#             sno = 'news' + str(l)
#
#             # loop variable
#             i = 0
#             # intermediate dictionary
#             dict2 = {}
#             while i < len(fields):
#                 # creating dictionary for each employee
#                 dict2[fields[i]] = description[i]
#                 i = i + 1
#
#             # appending the record of each employee to
#             # the main dictionary
#             dict1[sno] = dict2
#             l = l + 1
#
#     # creating json file
#     out_file = open("ens.json", "w")
#     json.dump(dict1, out_file, indent=4)
#     out_file.close()
# tojson()
#






#
# from django.shortcuts import render,HttpResponse
# from django.http.response import HttpResponse
# from django.shortcuts import redirect
# import os
# from io import StringIO
# import sys
import elasticsearch.exceptions
from django.shortcuts import render, HttpResponse, HttpResponseRedirect

# Create your views here.
from django.http import JsonResponse
import requests
import json
from home.models import *

from home.documents import *
from home.serializers import *

from django_elasticsearch_dsl_drf.filter_backends import (
    FilteringFilterBackend,
    CompoundSearchFilterBackend
)
from django_elasticsearch_dsl_drf.viewsets import DocumentViewSet
from django_elasticsearch_dsl_drf.filter_backends import (
    FilteringFilterBackend,
    OrderingFilterBackend,
)




def arama(request):
    q = request.GET.get('q')
    if q:
        # posts=Document.search().query('match',title=q)
        posts = NewsDocument.search().query('match', title=q)
        # posts=Document.search().query('match',title=q)
    else:
        posts = 'None'
    return render(request, 'arama.html', {'posts': posts})


# from elasticsearch import Elasticsearch
# from django_elasticsearch_dsl import *
# client = Elasticsearch("http://localhost:9200")
# resp = client.info()
# data={"Name":"john","Age":30,"address":"istanbul"}
# client.create(id=1,index='dene',  body=data, timeout="60s")
# # (index='employee',doc_type="text",  body=data, timeout="60s")
# print(resp)

from elasticsearch import Elasticsearch
def generate_random_data():
    filename = './home/karar_contain_kanser.txt'
    dict1 = {}
    fields = ['title', 'content']
    with open(filename) as fh:
        # l = 1
        for line in fh:
            if line.strip().startswith("http"):
                newline=line.strip().split(';')
                try:
                    ElasticDemo.objects.create(
                        # link={new_line[0]},
                        # date={new_line[1]},
                        title=newline[2],
                        content=newline[3]
                    )
                except Elasticsearch.exceptions.RequestError as ex:
                    if ex.error=='resource_already_exists_exception':
                        pass # Index already exists. Ignore.
                    else: # Other exception - raise it
                        raise ex
            else:
                pass


# generate_random_data()

            # # reading line by line from the text file
            # description = list(line.strip().split(';', 4))
            #
            # # for output see below
            # print(description)
            #
            # # for automatic creation of id for each employee
            # sno = 'news' + str(l)
            #
            # # loop variable
            # i = 0
            # # intermediate dictionary
            # dict2 = {}
            # while i < len(fields)+2:
            #     if i==0 or i==1:
            #         pass
            #     # creating dictionary for each employee
            #     else:
            #         dict2[fields[i]] = description[i]
            #         i = i + 1
            #
            # # appending the record of each employee to
            # # the main dictionary
            # dict1[sno] = dict2
            # print(dict2[0])
            # print(dict2[1])
            # l = l + 1


# generate_random_data()

# generate_random_data()
def index(request):
    generate_random_data()
    return JsonResponse({'status' : 200})




class PublisherDocumentView(DocumentViewSet):
    document = NewsDocument
    serializer_class = NewsDocumentSerializer
    lookup_field = 'elastic_demo'
    fielddata=True
    filter_backends = [
        FilteringFilterBackend,
        OrderingFilterBackend,
        CompoundSearchFilterBackend,
    ]

    search_fields = (
        'title',
        'content',
    )
    multi_match_search_fields = (
       'title',
        'content',
    )
    filter_fields = {
       'title' : 'title',
        'content' : 'content',
    }
    ordering_fields = {
        'id': None,
    }
    ordering = ( 'id'  ,)



