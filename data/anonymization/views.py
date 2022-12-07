from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .models import bankUser, bankProfile, itProfile, User, sharedData, bankNames, ItName
from .forms import SignUpForm, LoginForm
from cryptography.fernet import Fernet
from django.contrib import messages

# key = Fernet.generate_key()
# print(key)
key = b'xqdMc9vb9bIbFzuWkSHAnjOjyFakZS8p5gh3XTuY6k8='


def encrypt(to_encrypt):
    fernet = Fernet(key)
    encrypted_amt = fernet.encrypt(to_encrypt.encode('utf-8'))
    return encrypted_amt


def register(request):
    msg = None
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            msg = 'user created'
            return redirect('login_view')
        else:
            msg = 'form is not valid'
    else:
        form = SignUpForm()
    return render(request, 'register.html', {'form': form, 'msg': msg})


def login_view(request):
    form = LoginForm(request.POST or None)
    msg = None
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            print('department :', user.department)
            if user is not None and user.department == "Bank":
                login(request, user)
                return redirect('bank_home')
            elif user is not None and user.department == "IT":
                login(request, user)
                return redirect('it_home')
            else:
                msg = 'invalid credentials'
        else:
            msg = 'error validating form'
    return render(request, 'login.html', {'form': form, 'msg': msg})


def logout(request):
    return redirect('login_view')


def it_home(request):
    pro = bankProfile.objects.all()
    list = []
    p = request.user.id
    s = sharedData.objects.all()
    for i in s:
        if p == i.it_user_id_id:
            list.append(i.bank_man_id)
    bank_man_profile = []
    for j in pro:
        if j.id in list:
            d = {
                'id': j.id,
                'name': j.name,
                'organization': j.organization,
                'address': j.address,
            }
            bank_man_profile.append(d)
            print(j.name)
    content = {'pro': bank_man_profile}
    return render(request, 'it_home.html', content)


def bank_home(request):
    bank_userlist = bankUser.objects.all()
    profiles_it = itProfile.objects.all()
    return render(request, 'bank_home.html', {'bank_userlist': bank_userlist, 'profiles_it': profiles_it})


def store_bank_profile(request):
    b = bankProfile()
    uid = request.user.id
    user_id = User.objects.get(id=uid)
    b.user = user_id
    b.name = request.POST.get('name')
    b.mail_id = request.POST.get('mail_id')
    b.mobile_no = request.POST.get('mobile_no')
    b.address = request.POST.get('address')
    b.organization = request.POST.get('organization')
    b.save()
    return redirect('bank_home')


def store_it_profile(request):
    i = itProfile()
    uid = request.user.id
    user_id = User.objects.get(id=uid)
    i.user = user_id
    i.name = request.POST.get('name')
    i.mail_id = request.POST.get('mail_id')
    i.mobile_no = request.POST.get('mobile_no')
    i.address = request.POST.get('address')
    i.organization = request.POST.get('organization')
    i.save()
    return redirect('it_home')


def bank_profile(request, pk):
    bank_names = bankNames.objects.all()
    profile = bankProfile.objects.all()
    for i in profile:
        print(i.user_id)
        if i.user_id == pk:
            profiles = bankProfile.objects.get(user_id=pk)
            return render(request, 'bank_profile.html', {'profiles': profiles, 'bank_names': bank_names})
    else:
        msg = "details are not available"
        return render(request, 'bank_profile.html', {'msg': msg, 'bank_names': bank_names})


def it_profile(request, pk):
    it_names = ItName.objects.all()
    profile = itProfile.objects.all()
    for i in profile:
        print('profile userid', i.user_id)
        if i.user_id == pk:
            profiles = itProfile.objects.get(user_id=pk)
            return render(request, 'it_profile.html', {'profiles': profiles,'bank_names': it_names})
    else:
        msg = "details are not available"
        return render(request, 'it_profile.html', {'msg': msg, 'bank_names': it_names})


def shared_data(request, pk):
    try:
        uid = request.user.id
        user_details = sharedData.objects.filter(it_user_id=uid, bank_man_id=pk)
        content = {'user_details': user_details}
    except:
        msg = "Complete Profile"
        content = {'msg': msg}
    return render(request, 'shareddata.html', content)


def data_to_share(some_var, check, value):
    if check in some_var:
        final_share = encrypt(value)
    else:
        final_share = value
    return final_share


def details_user(request, pk):
    b = bankUser.objects.get(id=pk)
    profiles_it = itProfile.objects.all()
    if request.method == "POST":
        sd = sharedData()
        some_var = request.POST.getlist('checks')

        pid = request.POST.get('bank_user_id')
        bank = bankUser.objects.get(id=pid)
        sd.bank_user = bank  # ID of bank user

        it_man = request.POST.get('it_man')  # Pk of IT profile models
        q = int(it_man)
        it = itProfile.objects.get(id=q)
        sd.it_man = it
        sd.name = it.name
        sd.organization = it.organization

        bank_man = request.user.id
        bank_man_id = bankProfile.objects.get(user_id=bank_man)
        sd.bank_man_user = bank_man_id.user_id
        sd.bank_man = bank_man_id

        it_user = it.user_id
        it = User.objects.get(id=it_user)
        sd.it_user_id = it

        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        fathers_name = request.POST.get('fathers_name')
        age = request.POST.get('age')
        dob = bank.dob
        mobile_no = request.POST.get('mobile_no')
        mail_id = request.POST.get('mail_id')
        address = request.POST.get('address')
        occupation = request.POST.get('occupation')
        account_no = request.POST.get('account_no')
        account_type = request.POST.get('account_type')
        pan_no = request.POST.get('pan_no')
        aadhar_no = request.POST.get('aadhar_no')
        balance = request.POST.get('balance')

        sd.first_name = data_to_share(some_var, '1', first_name)
        sd.fathers_name = data_to_share(some_var, '2', fathers_name)
        sd.last_name = data_to_share(some_var, '3', last_name)
        sd.mobile_no = data_to_share(some_var, '4', mobile_no)
        sd.age = data_to_share(some_var, '5', age)
        sd.dob = data_to_share(some_var, '6', dob)
        sd.mail_id = data_to_share(some_var, '7', mail_id)
        sd.account_no = data_to_share(some_var, '8', account_no)
        sd.account_type = data_to_share(some_var, '9', account_type)
        sd.pan_no = data_to_share(some_var, '10', pan_no)
        sd.aadhar_no = data_to_share(some_var, '11', aadhar_no)
        sd.occupation = data_to_share(some_var, '12', occupation)
        sd.address = data_to_share(some_var, '13', address)
        sd.balance = data_to_share(some_var, '14', balance)
        sd.save()

        messages.success(request, "Details sent Successfully")
        return redirect('bank_home')
    return render(request, 'details_user.html', {'b': b, 'profiles_it': profiles_it})
