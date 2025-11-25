from django.shortcuts import render

# Create your views here.
from django.contrib import messages

import re
from urllib.request import Request
from django.shortcuts import render,redirect

from .forms import AccountForm, CardForm, CurrencyForm, CustomerRegistrationForm, LoanForm, NotificationsForm, ReceiptForm, RewardForm, ThirdPartyForm, TransactionForm, WalletForm
from .models import Account, Card, Currency, Customer, Loan, Notifications, Receipt, Reward, ThirdParty, Transaction, Wallet
# Create your views here.

# View to handle customer registration
def register_customer(request):
    # Check if the request is a POST (i.e., form submitted)
    if request.method == "POST":
        form = CustomerRegistrationForm(request.POST)  # Bind form with POST data
        if form.is_valid():  # Validate the form
            form.save()  # Save the valid form data to the database
            messages.success(request, "Customer registered successfully!")  # Display success message
            return redirect('register_customer')  # Redirect to the same page to prevent resubmission
        else:
            messages.error(request, "Please correct the errors below.")  # Display error message if form invalid
    else:
        # If GET request (initial page load), create an empty form
        form = CustomerRegistrationForm()
    
    # Render the registration template with the form (empty or filled with errors)
    return render(request, 'register_customer.html', {'form': form})


# View to list all customers
def list_customer(request):
    customers = Customer.objects.all()  # Fetch all customers from the database
    return render(request, "customer_list.html", {"customers": customers})  # Render template with customers


# View to show details of a single customer
def customer_profile(request, id):
    customer = Customer.objects.get(id=id)  # Get customer by ID
    return render(request, "customer_profile.html", {"customer": customer})  # Render template with customer details


def my_account(request):
    if request.method == "POST":
        form = AccountForm(request.POST)
        if form.is_valid():
            form.save()
            form = AccountForm()  # reset form after saving
    else:
        form = AccountForm()  # define form for GET requests
    return render(request, "account.html", {"form": form})
def list_account(request):
    accounts=Account.objects.all()
    return render(request,"account_list.html",{"accounts":accounts})
def account_profile (request,id):
    account=Account.objects.get(id=id)  
    return render(request,"account_profile.html",{"account":account})  




def wallet(request):
    if request.method=="POST":
        form=WalletForm(request.POST)
        if form.is_valid():
            form.save()
        else:
           form=WalletForm()  
        return render(request,"wallet.html",{"form":form})  

def list_wallet(request):
    wallets=Wallet.objects.all()
    return render(request,"wallet_list.html",{"wallets":wallets})        


def my_currency(request):
    if request.method=="POST":
        form=CurrencyForm(request.POST)
        if form.is_valid():
            form.save()
        else:    
            form=CurrencyForm()
    return render (request,"currency.html",{"form":form})


def list_currency(request):
    currencies=Currency.objects.all()
    return render(request,"currency_list.html",{"currencies":currencies})



def transaction(request):
    if request.method=="POST":
        form=TransactionForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            form=TransactionForm()
    return render (request,"transaction.html",{"form":form})    

def list_transaction(request):
    transactions=Transaction.objects.all()
    return render(request,"transaction_list.html",{"transactions":transactions})

def my_card(request):
    if request.method=="POST":
        form=CardForm(request.POST)
        if form.is_valid():
            form.save()
        else:
           form=CardForm()
    return render (request,"card.html",{"form":form})   

def list_card(request):
    cards=Card.objects.all() 
    return render(request,"card_list.html",{"cards":cards})    

def third_party(request):
    if request.method=="POST":
        form=ThirdPartyForm(request.POST)
        if form.is_valid():
            form.save()
        else:    
            form=ThirdPartyForm()
    return render (request,"thirdparty.html",{"form":form})  

def list_thirdparty(request):
    thirdparties=ThirdParty.objects.all()
    return render(request,"thirdparty_list.html",{"thirdparties":thirdparties})


def notifications(request): 
    if request.method=="POST":
        form=NotificationsForm(request.POST)
        if form.is_valid():
            form.save()
        else:
         form=NotificationsForm()
    return render (request,"notifications.html",{"form":form}) 


def list_notifications(request):
    notifications=Notifications.objects.all()
    return render(request,"notifications_list.html",{"notifications":notifications})


def receipt(request)   :
     if request.method=="POST":
        form=ReceiptForm(request.POST)
        if form.is_valid():
            form.save()
        else:   
            form=ReceiptForm()  
     return render (request,"receipt.html",{"form":form})    
     
def list_receipt(request):
    receipts=Receipt.objects.all()  
    return render(request,"receipt_list.html",{"receipts":receipts})  

         


def loan(request)   :
    if request.method=="POST":
        form=LoanForm(request.POST)
        if form.is_valid():
            form.save()
        else:   
           form=LoanForm()
    return render (request,"loan.html",{"form":form}) 

def list_loan(request):
    loans=Loan.objects.all()  
    return render(request,"loan_list.html",{"loans":loans})  



def reward(request):
    if request.method=="POST":
        form=RewardForm(request.POST)
        if form.is_valid():
            form.save()
        else:   
         form=RewardForm()
    return render(request,"reward.html",{"form":form})    

def list_reward(request):
    rewards=Reward.objects.all()  
    return render(request,"reward_list.html",{"rewards":rewards})    




def edit_profile(request,id) :
    customer=Customer.objects.get(id=id)  
    if request.method=="POST":
        form=CustomerRegistrationForm(request.POST,instance=customer)
        if form.is_valid():
            form.save()
            return redirect("customer_profile",id=customer.id)
    else:
            form=CustomerRegistrationForm(instance=customer)
            return render(request,"edit_profile.html",{"form":form})

def wallet_profile(request,id)  :
    wallet=Wallet.objects.get(id=id) 
    return render(request,"wallet_profile.html",{"wallet":wallet})         

def edit_wallet(request,id)  :
    wallet=Wallet.objects.get(id=id)   
    if request.method=="POST":
        form=WalletForm(request.POST ,initial=wallet) 
        if form.is_valid():
           form.save()
        return redirect("wallet_profile",id=wallet.id)  
    else:
        form=WalletForm(instance=wallet)   
        return render(request,"wallet_profile.html",{"form":form})   



def edit_account(request,id) :
    account=Account.objects.get(id=id)  
    if request.method=="POST":
        form=AccountForm(request.POST,instance=account)
        if form.is_valid():
            form.save()
            return redirect("account_profile",id=account.id)
    else:
            form=AccountForm(instance=account)
            return render(request,"edit_account.html",{"form":form})


def card_profile(request,id):
    card=Card.objects.get(id=id)
    return render(request,"card_profile.html",{"card":card})

def edit_card(request,id)  :
    card=Card.objects.get(id=id)  
    if request.method=="POST":
        form=CardForm(request.POST,instance=card)
        if form.is_valid():
            form.save()
            return redirect("card_profile",id=card.id)
    else:
            form=CardForm(instance=card)
            return render(request,"edit_card.html",{"form":form})

def transaction_profile(request,id):
    transaction=Card.objects.get(id=id)
    return render(request,"transaction_profile.html",{"transaction":transaction})

def edit_transaction(request,id)  :
    transaction=TransactionForm.objects.get(id=id)  
    if request.method=="POST":
        form=TransactionForm(request.POST,instance=transaction)
        if form.is_valid():
            form.save()
            return redirect("transaction_profile",id=transaction.id)
    else:
            form=TransactionForm(instance=transaction)
            return render(request,"edit_transcation.html",{"form":form})


def receipt_profile(request,id):
    receipt=Receipt.objects.get(id=id)
    return render(request,"receipt_profile.html",{"receipt":receipt})

def edit_receipt(request,id)  :
    receipt=ReceiptForm.objects.get(id=id)  
    if request.method=="POST":
        form=ReceiptForm(request.POST,instance=receipt)
        if form.is_valid():
            form.save()
            return redirect("receipt_profile",id=receipt.id)
    else:
            form=ReceiptForm(instance=receipt)
            return render(request,"edit_receipt.html",{"form":form})

      
