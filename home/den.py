# # # # from elasticsearch import Elasticsearch
# # # # from django_elasticsearch_dsl import *
# # # #
# # # from elasticsearch import Elasticsearch
# # # #
# # # # es = Elasticsearch()
# # # #
# # # # es.indices.create(
# # # #     index='dictionary',
# # # #     body={
# # # #         "settings": {
# # # #             "index": {
# # # #                 "analysis": {
# # # #                     "analyzer": {
# # # #                         "my_analyzer": {
# # # #                             "type": "custom",
# # # #                             "tokenizer": "nori_tokenizer"
# # # #                         }
# # # #                     }
# # # #                 }
# # # #             }
# # # #         }
# # # #     }
# # # # )
# # # #
# # # #
# # # #
# # # #
# # # # def send_data_to_es(data):
# from django_elasticsearch import *
# # hes=django_elasticsearch.indices("dj")
#
#
# from elasticsearch import Elasticsearch
# es=Elasticsearch(HOST='http://127.0.0.1',PORT=9200)
# # es.Elasticsearch()
# data = {"Name": "john", "Age": 30, "address": "istanbul"}
# es.create(id=1,index="fix",doc_type="domain",body=data,timeout=300)
# # es.indices.create(index="first_index")
# #
# data = {"Name": "john", "Age": 30, "address": "istanbul"}
# res=es.index(index='first_index',doc_type='domains',body=data)
# # # #     # res=es.index(index='employee',doc_type="domains",  body=data, timeout="60s")
# # # #     res = es.indices.create(index='employee', body={
# # # #         "settings": {
# # # #             "index": {
# # # #                 "analysis": {
# # # #                     "analyzer": {
# # # #                         "my_analyzer": {
# # # #                             "type": "custom",
# # # #                             "tokenizer": "nori_tokenizer"
# # # #                         }
# # # #                     }
# # # #                 }
# # # #             }
# # # #         }
# # # #     })
# # # #     res=es.info()
# # # #     print(res)
# # # #
# # # #
# # # #
# # # # def get_data_from_es():
# # #     es = Elasticsearch(['localhost:9200'])
# # #     r=es.search(index='elastic_demo2',body={"query":{"match":{'title':' '}}})
# # #     print(r)
# # #     print(type(r))
# # # #     print(r["hits"]["hits"][0]["_source"])
# # # # data={"Name":"john","Age":30,"address":"istanbul"}
# # # # send_data_to_es(data)
# # # #
# # # # get_data_from_es()
# # # #
# # # #
# # # #
# # # client = Elasticsearch("http://localhost:9200")
# # from django_elasticsearch import *
# # client=Elasticsearch(HOST='http://127.0.0.1',PORT=9200)
# # resp = client.search(
# #     body={"query": {"bool": {"filter": {"term": {"status": "active"}}}}},
# # )
# # print(resp)
# # # resp = client.info()
# # # print(resp)