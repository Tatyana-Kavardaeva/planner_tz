from rest_framework.routers import SimpleRouter

from tasks.apps import TasksConfig
from tasks.views import TaskViewSet, TagViewSet

app_name = TasksConfig.name

router = SimpleRouter()
router.register('tasks', TaskViewSet)
router.register('tags', TagViewSet)

urlpatterns = [] + router.urls
