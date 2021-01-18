from rest_framework import pagination
from rest_framework.response import Response
from django.conf import settings


class PageNumberPagination(pagination.PageNumberPagination):
    def get_paginated_response(self, data):

        response = {
            "links": {
                "next": self.get_next_link(),
                "previous": self.get_previous_link(),
                "base": self.request.build_absolute_uri(),
            },
            "count": self.page.paginator.count,
            "current_page": self.page.number,
            "page_size": settings.PAGE_SIZE,
            "total_pages": self.page.paginator.num_pages,
        }

        if self.page.has_next():
            response.update({"next_page": self.page.next_page_number()})

        if self.page.has_previous():
            response.update({"previous_page": self.page.previous_page_number()})

        response.update({"results": data})
        return Response(response)
