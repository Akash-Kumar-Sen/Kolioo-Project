from rest_framework.response import Response
from rest_framework import viewsets

from base.pagination import DefaultSetPagination
from base.json_renderer import ApiJSONRenderer


class ViewSetWrapper(viewsets.ViewSet):
    """Overriding the DRF viewset class with renderer and pagination"""
    renderer_classes = [ApiJSONRenderer]
    pagination_class = DefaultSetPagination

class ModelViewSetWrapper(viewsets.ModelViewSet):
    """Overriding the DRF model viewset class with renderer and pagination"""
    renderer_classes = [ApiJSONRenderer]
    pagination_class = DefaultSetPagination

    def generate_paginated_response(self, queryset):
        """Method to generate paginated queryset"""
        queryset = self.filter_queryset(queryset)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)