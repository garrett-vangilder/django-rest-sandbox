# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import render

# Create your views here.
class HelloApiView(APIView):
    """Test API View"""

    def get(self, request):
        """Returns a list of APIView features."""

        an_apiview = [
            'Uses HTTP methods as functions (get, post, patch, put, delete)',
            'It is similar to a traditional Django view',
            'Gives you the most control over your logic',
            'Is mapped manually to URLs'
        ]
        return Response({'message': 'Hello', 'an_apiview': an_apiview})
