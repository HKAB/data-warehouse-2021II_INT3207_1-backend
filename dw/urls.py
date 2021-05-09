from django.urls import include, path

from dw.views.job import JobGetView, JobListView

job_patterns = [
    path('get', JobGetView.as_view()),
    path('list', JobListView.as_view())
]

urlpatterns = [
    path('job/', include((job_patterns, 'job')))
]