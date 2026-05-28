from core.permissions import IsOwner

class IsOwnerReview(IsOwner):
    
    owner_field = "user"