from django.db import models
# from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.



class Article(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.title


# class Product(models.Model):
#     user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
#     name = models.CharField(max_length=200, null=True, blank=True)
#     image = models.ImageField(null=True, blank=True)
#     brand = models.CharField(max_length=200, null=True, blank=True)
#     category = models.CharField(max_length=200, null=True, blank=True)
#     description = models.TextField(null=True, blank=True)
#     rating = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
#     numReviews = models.IntegerField(null=True, blank=True, default=0)
#     price = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
#     countInStock = models.IntegerField(null=True, blank=True, default=0)
#     createdAt = models.DateTimeField(auto_now_add=True)
#     _id = models.AutoField(primary_key=True, editable=False)

#     def __str__(self):
#         return self.name
    

# class Review(models.Model):
#     product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
#     user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
#     name = models.CharField(max_length=200, null=True, blank=True)
#     rating = models.IntegerField(null=True, blank=True, default=0)
#     comment = models.TextField(null=True, blank=True)
#     _id = models.AutoField(primary_key=True, editable=False)

#     def __str__(self):
#         return str(self.rating)
    

# class Order(models.Model):
#     user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
#     paymentMethod = models.CharField(max_length=200, null=True, blank=True)
#     taxPrice = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
#     shippingPrice = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
#     totalPrice = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
#     isPaid = models.BooleanField(default=False)
#     paidAt = models.DateTimeField(auto_now_add=False, null=True, blank=True)
#     isDelivered = models.BooleanField(default=False)
#     deliveredAt = models.DateTimeField(auto_now_add=False, null=True, blank=True)
#     createdAt = models.DateTimeField(auto_now_add=True, null=True, blank=True)
#     _id = models.AutoField(primary_key=True, editable=False)

#     def __str__(self):
#         return str(self.createdAt)
    

# class OrderItem(models.Model):
#     product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
#     order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
#     name = models.CharField(max_length=200, null=True, blank=True)
#     qty = models.IntegerField(null=True, blank=True, default=0)
#     price = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
#     image = models.CharField(max_length=200, null=True, blank=True)
#     _id = models.AutoField(primary_key=True, editable=False)

#     def __str__(self):
#         return str(self.name)


# class ShippingAddress(models.Model):
#     order = models.OneToOneField(Order, on_delete=models.CASCADE, null=True, blank=True)
#     address = models.CharField(max_length=200, null=True, blank=True)
#     city = models.CharField(max_length=200, null=True, blank=True)
#     postalCode = models.CharField(max_length=200, null=True, blank=True)
#     country = models.CharField(max_length=200, null=True, blank=True)
#     shippingPrice = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
#     _id = models.AutoField(primary_key=True, editable=False)

#     def __str__(self):
#         return str(self.address)
    

# # ----------------------------------------------------
    


# class Department(models.Model):
#     Dept_ID = models.AutoField(primary_key=True)
#     Dept_Name = models.CharField(max_length=255)
#     Created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
#     date_created = models.DateField(auto_now_add=True)
#     # Updated_by = models.CharField(max_length=255)
#     # last_modified = models.DateField(auto_now=True)

#     def __str__(self):
#         return str(self.Dept_Name)
    

# class Designation(models.Model):
#     Designation_ID = models.AutoField(primary_key=True)
#     Designation_Name = models.CharField(max_length=255)
#     Created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
#     date_created = models.DateField(auto_now_add=True)
#     # Updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    
#     def __str__(self):
#         return str(self.Designation_Name)



# class EmployeeMaster(models.Model):
#     Emp_ID = models.AutoField(primary_key=True)
#     F_name = models.CharField(max_length=255)
#     L_name = models.CharField(max_length=255)
#     Designation_ID = models.ForeignKey(Designation, on_delete=models.CASCADE)
#     Dept_ID = models.ForeignKey(Department, on_delete=models.CASCADE)
#     Date_of_joining = models.DateTimeField()
#     Date_of_exit = models.DateTimeField(null=True, blank=True)
#     Email_ID = models.EmailField()
#     Emp_status = models.BooleanField()
#     Created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
#     date_created = models.DateField(auto_now_add=True)
#     # Updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
   
#     def __str__(self):
#         return f"{self.F_name} {self.L_name}"
    

# class VendorMaster(models.Model):
#     Vendor_ID = models.AutoField(primary_key=True)
#     Vendor_name = models.CharField(max_length=255)
#     Contact = models.BigIntegerField()
#     Email = models.CharField(max_length=255)
#     gst_no = models.IntegerField()
#     Created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
#     date_created = models.DateField(auto_now_add=True)
#     # Updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

#     def __str__(self):
#         return str(self.Vendor_name)


# class AssetCategory(models.Model):
#     asset_cat_ID = models.AutoField(primary_key=True)
#     asset_cat_name = models.CharField(max_length=255)
#     Created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
#     date_created = models.DateField(auto_now_add=True)
#     # Updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
   

#     def __str__(self):
#         return str(self.asset_cat_name)
    
#     class Meta:
#         verbose_name = "Asset Category"
#         verbose_name_plural = "Asset Categories"
    

# class AssetMaster(models.Model):
#     asset_serial_number = models.AutoField(primary_key=True)
#     model_number = models.IntegerField()
#     model_name = models.CharField(max_length=255)
#     asset_cat_ID = models.ForeignKey(AssetCategory, on_delete=models.SET_NULL, null=True)
#     erp_code = models.CharField(max_length=255)
#     invoice_number = models.IntegerField()
#     invoice_date = models.DateTimeField()
#     po_number = models.CharField(max_length=255)
#     po_date = models.DateTimeField()
#     cost_of_unit = models.IntegerField()
#     warranty_sdate = models.DateTimeField()
#     warranty_edate = models.DateTimeField()
#     grn_number = models.CharField(max_length=255)
#     grn_date = models.DateTimeField()
#     Vendor_ID = models.ForeignKey(VendorMaster, on_delete=models.SET_NULL, null=True)
#     Created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
#     date_created = models.DateField(auto_now_add=True)
#     # Updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    

#     def __str__(self):
#         return str(self.model_name)
    


# def default_assignment_date():
#     return timezone.now() + timezone.timedelta(hours=5, minutes=30)

# # class AssetAllocationTable(models.Model):
# #     assignment_ID = models.AutoField(primary_key=True)
# #     allocated_to = models.ForeignKey(EmployeeMaster, on_delete=models.CASCADE)
# #     asset_serial_number = models.OneToOneField(AssetMaster, on_delete=models.CASCADE)
# #     assignment_date = models.DateTimeField(default=default_assignment_date, editable=False)
# #     Employee_approval = 
# #     return_date = models.DateTimeField(blank=True, null=True)
# #     # Created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
# #     # update_by = models.CharField(max_length=255)


# #     def __str__(self):
# #         return str(self.asset_serial_number)
    

# class AssetAllocationTable(models.Model):
#     assignment_ID = models.AutoField(primary_key=True)
#     allocated_to = models.ForeignKey('EmployeeMaster', on_delete=models.CASCADE)
#     asset_serial_number = models.OneToOneField('AssetMaster', on_delete=models.CASCADE)
#     assignment_date = models.DateTimeField(default=default_assignment_date, editable=False)
#     Employee_approval = models.BooleanField(default=False)
#     return_date = models.DateTimeField(blank=True, null=True)
#     # Created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
#     # update_by = models.CharField(max_length=255)

#     def __str__(self):
#         return str(self.asset_serial_number)

#     def send_approval_email(self):
#         subject = 'Asset Allocation Approval'
#         message = f'Click the following link to approve asset allocation: {self.get_approval_link()}'
#         from_email = 'nileshkarkande10@gmail.com'  # Replace with your email
#         to_email = self.allocated_to.Email_ID  # Assuming EmployeeMaster has an Email_ID field
#         send_mail(subject, message, from_email, [to_email])

#     # def get_approval_link(self):
#         # Customize this link generation based on your application structure
#         # For example: return f'http://yourdomain.com/approve/{self.assignment_ID}/'



# class AssetHistory(models.Model):
#     asset_history_ID = models.AutoField(primary_key=True)
#     asset_serial_number = models.ForeignKey(AssetMaster, on_delete=models.CASCADE)
#     Emp_ID = models.ForeignKey(EmployeeMaster, on_delete=models.CASCADE)
#     assignment_date = models.DateTimeField()
#     return_date = models.DateTimeField(null=True, blank=True)

#     def __str__(self):
#         return str(self.asset_serial_number)
    
#     class Meta:
#         verbose_name = "Asset History"
#         verbose_name_plural = "Assets History"

# class AssetMaintenanceTable(models.Model):
#     maintainance_ID = models.AutoField(primary_key=True)
#     asset_serial_number = models.ForeignKey(AssetMaster, on_delete=models.CASCADE)
#     main_date = models.DateTimeField()
#     reassign_date = models.DateTimeField()
#     maintainance_type = models.CharField(max_length=255)
#     maintainance_date = models.DateTimeField()





