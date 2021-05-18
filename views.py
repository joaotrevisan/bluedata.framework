import json
import boto3

from botocore.config import Config
from decouple import config
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.views import View
from django.views.generic import ListView
from bluedata.helpers import remover_acentos


# Filtering and Pagination with Django
# https://www.caktusgroup.com/blog/2018/10/18/filtering-and-pagination-django/
#
class FilteredListView(ListView):
    filterset_class = None

    def get_queryset(self):
        # Get the queryset however you usually would.  For example:
        queryset = super().get_queryset()
        # Then use the query parameters and the queryset to
        # instantiate a filterset and save it as an attribute
        # on the view instance for later.
        self.filterset = self.filterset_class(self.request.GET, queryset=queryset)
        # Return the filtered queryset
        return self.filterset.qs.distinct()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Pass the filterset to the template - it provides the form.
        context['filterset'] = self.filterset
        return context


# Get signed url from Amazon S3
# use this url to upload files directly
#
class SignS3(LoginRequiredMixin, View):
    def get(self, *args, **kwargs):
        s3_key_id = config('AWS_ACCESS_KEY_ID')
        s3_secret_key = config('AWS_SECRET_ACCESS_KEY')
        s3_bucket = config('AWS_STORAGE_BUCKET_NAME')

        # local onde será enviado
        k_file_name = remover_acentos(kwargs['file_name'])
        file_name = 'media/arquivos/{}'.format(k_file_name)
        file_type = kwargs['file_type'].replace('__', '/')

        s3 = boto3.client(
            's3',
            aws_access_key_id=s3_key_id,
            aws_secret_access_key=s3_secret_key,
            config=Config(signature_version='s3v4'))

        presigned_post = s3.generate_presigned_post(
            Bucket=s3_bucket,
            Key=file_name,
            Fields={"acl": "public-read", "Content-Type": file_type},
            Conditions=[
                {"acl": "public-read"},
                {"Content-Type": file_type}
            ],
            ExpiresIn=3600
        )

        resp = json.dumps({
            'data': presigned_post,
            'url': 'https://s3.amazonaws.com/{}/{}'.format(s3_bucket, file_name)
        })

        return HttpResponse(resp)
