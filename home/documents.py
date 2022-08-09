# from django_elasticsearch_dsl import (
#     Document ,
#     fields,
#     Index,
# # )
# from django_elasticsearch_dsl.registries import registry
# # from .models import ElasticDemo
# from django_elasticsearch_dsl import documents
# from django_elasticsearch_dsl import fields
# from django_elasticsearch_dsl import indices
# from django_elasticsearch_dsl import Index
# from django_elasticsearch_dsl import Document
# from .models import ElasticDemo2
#
# # PUBLISHER_INDEX = Index('elastic_demo')
# #
# # PUBLISHER_INDEX.settings(
# #     number_of_shards=1,
# #     number_of_replicas=1
# # )
#
# PUBLISHER_INDEX = Index('elastic_demo2')
#
# PUBLISHER_INDEX.settings(
#     number_of_shards=1,
#     number_of_replicas=0
# )
#
#
# @PUBLISHER_INDEX.doc_type
# # @registry.register_document(Document)
# class NewsDocument(Document):
#     # class Index:
#     #     name='newsdocument'
#
#     id = fields.IntegerField(attr='id')
#     fielddata = True
#
#     # link = fields.TextField(
#     #     fields={
#     #         'raw': {
#     #             'type': 'keyword',
#     #         }
#     #
#     #     }
#     # )
#     # date = fields.TextField(
#     #     fields={
#     #         'raw': {
#     #             'type': 'keyword',
#     #         }
#     #
#     #     }
#     # )
#     #
#     # title = fields.TextField(
#     #     fields={
#     #         'raw':{
#     #             'type': 'keyword',
#     #         }
#     #
#     #     }
#     # )
#     # content = fields.TextField(
#     #     fields={
#     #         'raw': {
#     #             'type': 'keyword',
#     #
#     #         }
#     #     }
#     # )
#
#     class Django(object):
#         model = ElasticDemo2
#         fields = ['link', 'date', 'title', 'content']
#















# # from django_elasticsearch_dsl import (
# #     Document ,
# #     fields,
# #     Index,
# # )
from django_elasticsearch_dsl import documents
from django_elasticsearch_dsl import fields
from django_elasticsearch_dsl import indices
from django_elasticsearch_dsl import Index
from django_elasticsearch_dsl import Document
from .models import ElasticDemo
PUBLISHER_INDEX = Index('elastic_demo')

PUBLISHER_INDEX.settings(
    number_of_shards=1,
    number_of_replicas=0
)

#
#
#
@PUBLISHER_INDEX.doc_type
class NewsDocument(Document):
    id = fields.IntegerField(attr='id')
    fielddata=True
    # title = fields.TextField(
    #     fields={
    #         'raw':{
    #             'type': 'keyword',
    #         }
    #
    #     }
    # )
    # content = fields.TextField(
    #     fields={
    #         'raw': {
    #             'type': 'keyword',
    #
    #         }
    #     }
    # )
#     title = fields.TextField(
#         attr='title',
#         fields={
#             'raw': fields.CompletionField(),
#         }
#     )
#     content = fields.TextField(
#         attr='content',
#         fields={
#
#                  'raw': fields.CompletionField(),
#
#
#         }
#     )
#
#

    #
    # title = fields.TextField(
    #         attr='title',
    #         fields={
    #             'suggest': fields.CompletionField(),
    #         }
    #     )
    # content = fields.TextField(
    #         attr='content',
    #         fields={
    #             'suggest': fields.CompletionField(),
    #         }
    #     )


    class Django(object):
        model = ElasticDemo
        fields = ['title', 'content']