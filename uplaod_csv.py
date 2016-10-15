import json
import csv
from django.shortcuts import render, HttpResponse
from myapp.forms import UploadCSVForm
def upload_csv(request):
	if request.method == 'POST':
		form = UploadCSVForm(request.POST, request.FILES)

		if form.is_valid():
			# get the posted file
			csv_file = request.FILES['CSV_FILE']

            data = [row for row in csv.reader(file.read().splitlines())]


            # do anything with the data 
            response_data = {}
            for value in data:
            	
            	response_data['value1'] = value[1]
            	response_data['value2'] = value[2]

             
            return HttpResponse(
            	json.dumps(response_data),
            	content_type='application/json',
            	)
    else:
    	form = UploadCSVForm()
    return render(request, 'index.html', {'form': form, })

