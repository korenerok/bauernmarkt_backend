from rest_framework import permissions

class IsAdmin(permissions.IsAdminUser):
    #Permission to check if a user is Admin(level-object permission)
    def has_object_permission(self, request, view, obj):
        return request.user.is_staff

class IsOwner(permissions.BasePermission):
    #Permission to allow the owner to edit(mostly used to check users)    
    def has_object_permission(self, request, view, obj):
        return (obj == request.user)

class UserPermissions(permissions.BasePermission):
    #Permission for User Class: 
    # Users can only be created,listed and deleted by an admin
    # Users can be retrieved and updated by the own user or an admin
    def has_permission(self,request,view):
        if view.action in ['create','list']:
            return IsAdmin.has_permission(self,request,view)
        return True
    
    def has_object_permission(self,request,view,obj):
        if view.action in ['destroy']:
            return IsAdmin.has_object_permission(self,request,view,obj)
        elif view.action in ['update','retrieve']:
            return  IsOwner.has_object_permission(self,request,view,obj) or IsAdmin.has_object_permission(self,request,view,obj)

class ProductPermissions(permissions.BasePermission):
    #only Admins can create, update and delete products
    #everyone can list and retrieve
    def has_permission(self,request,view):
        if view.action in ['create']:
            return IsAdmin.has_permission(self,request,view)
        return True

    def has_object_permission(self,request,view,obj):
        if view.action in ['update','destroy']:
            return IsAdmin.has_object_permission(self,request,view,obj)
        else:
            return view.action in ['retrieve']

class MarketPermissions(permissions.BasePermission):
    #only Admins can create, and delete products
    #owner or admins can update
    #everyone can list and retrieve
    def has_permission(self,request,view):
        if view.action in ['create']:
            return IsAdmin.has_permission(self,request,view)
        return True

    def has_object_permission(self,request,view,obj):
        if view.action in ['destroy']:
            return IsAdmin.has_object_permission(self,request,view,obj)
        elif view.action in ['update']:
            return IsAdmin.has_object_permission(self,request,view,obj) or IsOwner.has_object_permission(self,request,view,obj)
        else:
            return view.action in ['retrieve']

class ItemPermissions(permissions.BasePermission):
    #Owners and Admins can create, update and delete item
    #everyone can list and retrieve
    def has_permission(self,request,view):
        if view.action in ['create']:
            return IsAdmin.has_permission(self,request,view) or IsOwner.has_permission(self,request,view)
        return True

    def has_object_permission(self,request,view,obj):
        if view.action in ['update','destroy']:
            return IsAdmin.has_object_permission(self,request,view,obj) or IsOwner.has_object_permission(self,request,view,obj)
        else:
            return view.action in ['retrieve']
