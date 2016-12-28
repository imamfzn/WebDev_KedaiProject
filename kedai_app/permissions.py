from rest_framework.permissions import BasePermission, SAFE_METHODS
from django.contrib.auth.models import User

class IsOwnerOrReadOnly(BasePermission):
	message = "You must logged in as customer"
	def has_permission(self,request,view):
		if request.method in SAFE_METHODS:
			return True
		return request.user.is_authenticated()

class IsReadOnly(BasePermission):
	my_safe_methods = ['GET']
	def has_permission(self,request,view):
		if request.method in self.my_safe_methods:
			return True
		return False

class OnlyCustomer(BasePermission):
	my_safe_methods = ['GET','POST']
	def has_permission(self,request,view):
		if request.user.is_authenticated():
			if request.method in SAFE_METHODS:
				return True
			else :
				return False
		else : #customer
			if request.method in self.my_safe_methods:
				return True
			else : return False

class OnlyCustomerService(BasePermission):
	message = "You must logged in as customer"
	def has_permission(self,request,view):
		if request.user.is_authenticated():
			return True
		return False


