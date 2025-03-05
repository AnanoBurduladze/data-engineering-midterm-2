# Base image
FROM python:3.9

# სამუშაო დირექტორიის შექმნა და დაყენება
WORKDIR /app

# დამოკიდებულებების დამატება
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# კოდის კოპირება კონტეინერში
COPY . .

# გაშვების ბრძანება
CMD ["python", "csv_processing.py"]

