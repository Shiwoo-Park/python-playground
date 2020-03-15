from celery.result import AsyncResult
from django.views.generic import TemplateView
from rest_framework.response import Response
from rest_framework.views import APIView

from test_worker.celery import sleep


class CeleryProgressView(TemplateView):
    # template_name = "celery_progress.html"
    template_name = "celery_progress2.html"


class CeleryTriggerTaskAPIView(APIView):
    def get(self, request, *args, **kwargs):
        result = sleep.delay(30)
        return Response(data={"task_id": result.id, "message": "celery task started!!!"})


class CeleryTaskStatusAPIView(APIView):
    def get(self, request, *args, **kwargs):
        task_id = request.query_params["task_id"]
        result = AsyncResult(task_id)
        response_data = {
            'state': result.state,
            'details': result.info,  # meta 정보가 들어옴
            # {'current': i, 'total': seconds}
        }
        return Response(data=response_data)
