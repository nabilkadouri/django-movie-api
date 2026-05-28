from core.permissions import IsAdminOrOwner


class IsMovieAdminOrOwner(IsAdminOrOwner):
    
    owner_field = "created_by"


