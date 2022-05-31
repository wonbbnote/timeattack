from django.http import HttpResponse

class UserClass:
    def __init__(self):
        self.email = ''
        self.password = ''



def sign_up_view(request):
    if request.method == "POST":
        email = request.POST.get('email', None)
        # request.POST : POST로 온 데이터를 받는 방식
        # .get('username', None) : 그 중 username으로 되어있는 데이터 가져와
        # 데이터가 없다면 None(빈칸)으로 처리
        password = request.POST.get('password', None)

        new_user = UserClass()
        new_user.email = email
        new_user.password = password
        new_user.save()

    return HttpResponse("회원가입 성공")