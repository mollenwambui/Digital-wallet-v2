from django.contrib import admin

# Register your models here.
from django.contrib import admin
# Register your models here.
from .models import Currency, Customer
from .models import Wallet
from .models import Account
from .models import Transaction
from .models import Card
from .models import ThirdParty
from .models import Notifications
from .models import Receipt
from .models import Reward
from .models import Loan

 
class CustomerAdmin(admin.ModelAdmin):
    list_display = ("first_name","last_name","address","email","phone_number","age","pin","gender","id_number","nationality","occupation",)
    search_fields = ("first_name","last_name","address",)
admin.site.register(Customer,CustomerAdmin)

class WalletAdmin(admin.ModelAdmin):
    list_display = ("balance","customer","date_created","pin",)
    search_fields = ("balance","customer",)
admin.site.register(Wallet,WalletAdmin)

class AccountAdmin(admin.ModelAdmin):
    list_display = ("account_type","balance","account_name","wallet",)
    search_fields = ("account_type","balance","account_name",)
admin.site.register(Account,AccountAdmin)

class TransactionAdmin(admin.ModelAdmin):
    list_display = ("wallet","transaction_amount","transaction_type","transaction_charge","transaction_date","receipt","origin_account","destination_account",)
    search_fields = ("transaction_type","receipt","transaction_date",)
admin.site.register(Transaction,TransactionAdmin)

class CardAdmin(admin.ModelAdmin):
    list_display = ("date_issued","card_name","card_number","card_type","expiry_date","card_status","security_code",)
    search_fields = ("date_issued","card_name","card_status",)
admin.site.register(Card,CardAdmin)

class ThirdPartyAdmin(admin.ModelAdmin):
    list_display = ("account","name","thirdparty_id","phone_number",)
    search_fields = ("name","phone_number",)
admin.site.register(ThirdParty,ThirdPartyAdmin)

class NotificationsAdmin(admin.ModelAdmin):
    list_display = ("notifications_id","name","status",)
    search_fields = ("name","status",)
admin.site.register(Notifications,NotificationsAdmin)

class ReceiptAdmin(admin.ModelAdmin):
    list_display = ("receipt_type","receipt_date","receipt_file","total_amount",)
    search_fields = ("receipt_type","total_amount",)
admin.site.register(Receipt,ReceiptAdmin)

class LoanAdmin(admin.ModelAdmin):
    list_display = ("loan_number","loan_type","amount","date_and_time","wallet","interest_rate","guarantor","pay_due_date","loan_balance",)
    search_fields = ("loan_number","loan_type","amount","wallet",)
admin.site.register(Loan,LoanAdmin)

class RewardAdmin(admin.ModelAdmin):
    list_display = ("transaction","date_and_time","customer_id","gender",)
    search_fields = ("transaction","gender","date_and_time",)
admin.site.register(Reward,RewardAdmin)

class CurrencyAdmin(admin.ModelAdmin):
    list_display = ("amount","origin_country",)
    search_fields = ("amount","origin_country",)
admin.site.register(Currency,CurrencyAdmin)