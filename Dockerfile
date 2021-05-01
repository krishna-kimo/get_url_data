FROM python:3.7

COPY ./requirements.txt .
	
RUN pip install -r requirements.txt
	
EXPOSE 8080
	
COPY . .
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]
