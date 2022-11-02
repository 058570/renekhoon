from .models import *
from .serializers import *

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework import status
from django.http import Http404, JsonResponse
from django.core.paginator import Paginator


class ManagerAccountListAPI(APIView):

    def get(self, request):
        request_data = request.GET
        request_page = request_data['page']
        request_offset = request_data['offset']
        ManagerAccount_list = Manager_Account.objects.all().order_by('-manager_account_number')
        page = request.GET.get('page', request_page)
        paginator = Paginator(ManagerAccount_list, request_offset)
        page_obj = paginator.page(page)
        page_serializer = ManagerAccountSerializer(page_obj, many=True)
        return Response(page_serializer.data)

    def post(self, request):
        serializer = ManagerAccountSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ManagerAccountList_DetailAPI(APIView):

    def get_object(self, pk):
        try:
            return Manager_Account.objects.get(pk=pk)
        except Manager_Account.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        manager_account = self.get_object(pk)
        serializer = ManagerAccountSerializer(manager_account)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        manager_account = self.get_object(pk)
        serializer = ManagerAccountSerializer(manager_account, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        manager_account = self.get_object(pk)
        manager_account.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




class LoginAPI(APIView):

    def post(self, request):
        succes = {
            "code": 200,
            "data": ""
        }
        request_data = JSONParser().parse(request)
        query_set = Manager_Account.objects.filter(manager_id=request_data['manager_id'],
                                                   manager_password=request_data['manager_pw'])
        if query_set.exists():
            serializer = ManagerAccountSerializer(query_set, many=True)
            succes['data'] = serializer.data
            return JsonResponse(succes)
        else:
            succes['code'] = 400
            succes['data'] = "로그인 실패"
            print("gohome")
            return JsonResponse(succes)



class InstitutionListAPI(APIView):

    def get(self, request):
        request_data = request.GET
        request_page = request_data['page']
        request_offset = request_data['offset']
        InstitutionList = Institution.objects.all().order_by('-institution_number')
        page = request.GET.get('page', request_page)
        paginator = Paginator(InstitutionList, request_offset)
        page_obj = paginator.page(page)
        page_serializer = InstitutionSerializer(page_obj, many=True)
        return Response(page_serializer.data)


class InstitutionList_detailAPI(APIView):

    def get_object(self, pk):
        try:
            return Institution.objects.get(pk=pk)
        except Institution.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        institution = self.get_object(pk)
        serializer = InstitutionSerializer(institution)
        return Response(serializer.data)

    def delete(self, request, pk, format=None):
        institution = self.get_object(pk)
        institution.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class NoticeAPI(APIView):
    def get(self, request):
        request_data = request.GET
        request_page = request_data['page']
        request_offset = request_data['offset']
        NoticeList = Notice.objects.all().order_by('-notice_number')
        page = request.GET.get('page', request_page)
        paginator = Paginator(NoticeList, request_offset)
        page_obj = paginator.page(page)
        page_serializer = NoticeSerializer(page_obj, many=True)
        return Response(page_serializer.data)

    def post(self, request):
        serializer = NoticeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class Notice_detailAPI(APIView):

    def get_object(self, pk):
        try:
            return Notice.objects.get(pk=pk)
        except Notice.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        notice = self.get_object(pk)
        serializer = NoticeSerializer(notice)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        notice = self.get_object(pk)
        serializer = NoticeSerializer(notice, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        notice = self.get_object(pk)
        notice.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class SoftwareUpdateListAPI(APIView):
    def get(self, request):
        request_data = request.GET
        request_page = request_data['page']
        request_offset = request_data['offset']
        SoftwareUpdateList = SoftwareUpdate.objects.all().order_by('-softwareupdate_number')
        page = request.GET.get('page', request_page)
        paginator = Paginator(SoftwareUpdateList, request_offset)
        page_obj = paginator.page(page)
        page_serializer = SoftwareUpdateSerializer(page_obj, many=True)
        return Response(page_serializer.data)

    def post(self, request):
        serializer = SoftwareUpdateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class SoftwareUpdateList_detailAPI(APIView):

    def get_object(self, pk):
        try:
            return SoftwareUpdate.objects.get(pk=pk)
        except SoftwareUpdate.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        software_update = self.get_object(pk)
        serializer = SoftwareUpdateSerializer(software_update)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        software_update = self.get_object(pk)
        serializer = SoftwareUpdateSerializer(software_update, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        software_update = self.get_object(pk)
        software_update.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
