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
    
    
# ====================================================================
# 0318_회원가입
# ====================================================================
    
@api_view(['POST'])
def Signup_api(request):
    if request.method == 'POST':
        # POST 요청에서 'login_info' 키를 통해 데이터를 받아옵니다.
        print(request.data)
        business_num = request.data.get('business_num','')
        file_pass= request.data.get('file_pass','')
        chkAll = request.data.get('chkAll','')              
        chk1= request.data.get('chk1','')
        chk2= request.data.get('chk2','')
        chk3= request.data.get('chk3','')
        chk4= request.data.get('chk4','')
        chk5= request.data.get('chk5','')         
        username = request.data.get('username','')              
        pw= request.data.get('pw','')
        name= request.data.get('name','')
        inst= request.data.get('inst','')
        phone= request.data.get('phone','')
        mail= request.data.get('mail','')
            
        print(business_num)
        print(chkAll)
        print(type(chk1))
        print(chk2)
        print(chk3)
        print("dtx04_api_signup 도착")
        

        if len(username) < 4 or len(username) > 20:
            print("아이디를 확인하세요")
            return Response({'message': 'fail1'})
        if len(pw) < 8 or len(pw) > 16:
            print("비밀번호를 확인하세요")
            return Response({'message': 'fail2'})
        if len(phone) != 11:
            print("휴대폰 번호를 확인하세요")
            return Response({'message': 'fail3'})
        if chk1 == None or chk2 == None or chk3 == None:
            print("약관 동의를 확인하세요")
            return Response({'message': 'fail4'})
        else:
            user = User_consultant(
                login_id = username,
                login_pw = pw,
                name = name,
                inst = inst,
                phone = phone,
                email = mail,
                # chk1 = chk1,
                # chk2 = chk2,
                # chk3 = chk3,
                # chk4 = chk4,
                # chk5 = chk5,
            )
            user.save()


            print("회원가입 성공, 로그인 화면으로 이동합니다.")
            return Response({'message': 'success'})
        
    else:
        print("두번째 else")
        return Response({'message': 'fail'})