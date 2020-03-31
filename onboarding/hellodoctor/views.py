import csv

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render

from hellodoctor.doctor_data_manager import data_download
from hellodoctor.doctor_data_manager.upload_data import write_file


@login_required(login_url='/login/')
def download_doctors_data(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="doctor_data.csv"'

    writer = csv.writer(response)
    data_download.write_csv_file(writer, "ONBOARDED")

    return response


@login_required(login_url='/login/')
def upload_csv(request):
    if "GET" == request.method:
        return render(request, "upload_csv.html")

    write_file(request.FILES['csv_file'])
    return HttpResponse("<h1>Success</h1>")
