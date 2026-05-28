from core.permissions import IsOwner

class IsOwnerFavorite(IsOwner):
    
    owner_field = "user"