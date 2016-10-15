import json
import csv
from django.shortcuts import render, HttpResponse
def upload_csv(request):
	if request.method == 'POST':
		form = UploadCSVForm(request.POST, request.FILES)

		if form.is_valid():
			# get the posted file
			csv_file = request.FILES['CSV_FILE']

            data = [row for row in csv.reader(csv_file)]

            # do anythoing with the data 
            response_data = {}
            for value in data:
            	
            	response_data['value1'] = [1]
            	response_data['value2'] = [2]

             
            return HttpResponse(
            	json.dumps(response_data),
            	content_type='application/json',
            	)
    else:
    	form = UploadCSVForm()
    return render(request, 'index.html', {'form': form, })

