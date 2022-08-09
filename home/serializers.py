# import json
# from .models import ElasticDemo2
#
# from django_elasticsearch_dsl_drf.serializers import DocumentSerializer
# from .documents import *
# from .documents import NewsDocument
#
#
# class NewsDocumentSerializer(DocumentSerializer):
#
#     class Meta(object):
#         """Meta options."""
#         model = ElasticDemo2
#         document = NewsDocument
#         fields = (
#             'link',
#             'date',
#             'title',
#             'content',
#         )
#         def get_location(self, obj):
#             """Represent location value."""
#             try:
#                 return obj.location.to_dict()
#             except:
#                 return {}







import json
from .models import ElasticDemo

from django_elasticsearch_dsl_drf.serializers import DocumentSerializer
from .documents import *


class NewsDocumentSerializer(DocumentSerializer):

    class Meta(object):
        """Meta options."""
        model = ElasticDemo
        document = NewsDocument
        fields = (
            'title',
            'content',
        )
        def get_location(self, obj):
            """Represent location value."""
            try:
                return obj.location.to_dict()
            except:
                return {}