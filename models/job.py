import requests

url = 'http://127.0.0.1:5000/jobs'  # Replace with your actual URL

# JSON data for the job
data = {
    'company': 'Example Company',
    'logo': 'example_logo.png',
    'logobackground': 'example_logo_bg.png',
    'position': 'Software Engineer',
    'postedAt': '2023-06-05',
    'contract': 'Full-Time',
    'location': 'San Francisco, CA',
    'apply': 'http://example.com/apply',
    'website': 'http://example.com',
    'description': 'This is a job description',
    'contents': 'Job contents',
    'items': 'Job items'
}

response = requests.post(url, json=data)

if response.status_code == 200:
    print('Job created successfully')
else:
    print('Error:', response.json())
