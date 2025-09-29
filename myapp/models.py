from django.db import models
from django.contrib.auth.models import User

class Dessert(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    image_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name

class Order(models.Model):
    STATUS_CHOICES = [
        ('pending', 'รอดำเนินการ'),
        ('delivering', 'กำลังจัดส่ง'),
        ('delivered', 'จัดส่งเรียบร้อยแล้ว'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')

    def __str__(self):
        return f"Order #{self.id} by {self.user.username}"

    def total_price(self):
        return sum(item.quantity * item.dessert.price for item in self.items.all())

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    dessert = models.ForeignKey(Dessert, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)


