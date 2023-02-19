from rest_framework import routers
from .views import BookViewSet, AuthorViewSet

router = routers.SimpleRouter()

router.register('book', BookViewSet)
router.register('author', AuthorViewSet)