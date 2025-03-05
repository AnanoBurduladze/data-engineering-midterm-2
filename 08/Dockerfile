# Base image
FROM python:3.9

# სამუშაო დირექტორიის შექმნა
WORKDIR /app

# დამოკიდებულებების დამატება
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# მონაცემთა ბაზის ინიციალიზაცია
COPY init_db.py init_db.py
RUN python init_db.py

# აპლიკაციის კოპირება
COPY . .

# API-ს გაშვება
CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8000"]

