from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages


# ✅ เปลี่ยนชื่อฟังก์ชัน login เพื่อไม่ชนกับระบบของ Django
def login_view(request):
    return render(request, 'myapp/login.html')

def register(request):
    return render(request, 'myapp/register.html')

# ✅ บังคับล็อกอินก่อนเข้าหน้าเหล่านี้
@login_required(login_url='login')
def home(request):
    return render(request, 'myapp/home.html')

def menu(request):
    return render(request, 'myapp/menu.html')

def delivery(request):
    return render(request, 'myapp/delivery.html')

def trackorder(request):
    return render(request, 'myapp/trackorder.html')

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST, request.FILES)  # ถ้ามีไฟล์ (รูปโปรไฟล์) ให้ใส่ด้วย
        if form.is_valid():
            form.save()  # สร้าง user ใหม่
            # ไม่ล็อกอินให้อัตโนมัติ
            return redirect('login')  # ชื่อ url ของหน้าล็อคอิน
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def register(request):
    if request.method == "POST":
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            try:
                User.objects.create_user(username=username, password=password1)
                messages.success(request, "สมัครสมาชิกสำเร็จ! กรุณาเข้าสู่ระบบ")
                return redirect('login')  # ชื่อ URL สำหรับหน้าล็อกอิน
            except:
                messages.error(request, "ชื่อผู้ใช้นี้มีคนใช้แล้ว")
        else:
            messages.error(request, "รหัสผ่านไม่ตรงกัน")
    return render(request, 'register.html')



def order_status(request):
    customer_name = "คุณชมพู่"

    order_items = [
        {
            'name': 'มาการองรสสตรอว์เบอร์รี่',
            'quantity': 2,
            'price': 60,
            'image_url': 'https://i.imgur.com/1.png',
        },
        {
            'name': 'ชาเขียวมัทฉะเย็น',
            'quantity': 1,
            'price': 55,
            'image_url': 'https://i.imgur.com/2.png',
        },
        {
            'name': 'พุดดิ้งชานมไข่มุก',
            'quantity': 1,
            'price': 45,
            'image_url': 'https://i.imgur.com/3.png',
        },
    ]

    total_price = sum(item['quantity'] * item['price'] for item in order_items)

    return render(request, 'myapp/order_status.html', {
        'customer_name': customer_name,
        'order_items': order_items,
        'total_price': total_price,
    })
