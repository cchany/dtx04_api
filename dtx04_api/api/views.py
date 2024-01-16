from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render
from .models import User_consultant, User_Medical

@api_view(['POST'])
def login_api(request):
    if request.method == 'POST':
        # POST 요청에서 'login_info' 키를 통해 데이터를 받아옵니다.
        print(request.data)
        login_info1 = request.data.get('id', '')
        login_info2 = request.data.get('pw', '')
        print(login_info1, login_info2)
        print("dtx04_api 도착")
        
        if User_consultant.objects.filter(login_id=login_info1, login_pw=login_info2).exists():
            print("로그인 성공")
            return Response({'message': 'success'})
        else:
            print("로그인 실패")
            return Response({'message': 'fail'})
        
    else:
        print("두번째 else")
        return Response({'message': 'fail'})


@api_view(['POST'])
def login_medi_api(request):
    if request.method == 'POST':
        # POST 요청에서 'login_info' 키를 통해 데이터를 받아옵니다.
        print(request.data)
        login_info1 = request.data.get('id', '')
        login_info2 = request.data.get('pw', '')
        print(login_info1, login_info2)
        print("dtx04_api 도착")
        
        if User_Medical.objects.filter(login_id=login_info1, login_pw=login_info2).exists():
            print("로그인 성공")
            return Response({'message': 'success'})
        else:
            print("로그인 실패")
            return Response({'message': 'fail'})
        
    else:
        print("두번째 else")
        return Response({'message': 'fail'})