"""
Database Class Design
"""
from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy

host = 'localhost'
user = 'devadmin'
passwd = 'dev_pwd'
database = 'devjobs_db'

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://{user}:{passwd}@{host}/{database}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Job(db.Model):
    """Job model
    """
    id = db.Column(db.Integer, primary_key=True)
    company = db.Column(db.String(100))
    logo = db.Column(db.String(100))
    logobackground = db.Column(db.String(100))
    position = db.Column(db.String(100))
    postedAt = db.Column(db.String(100))
    contract = db.Column(db.String(100))
    location = db.Column(db.String(100))
    apply = db.Column(db.String(100))
    website = db.Column(db.String(100))
    description = db.Column(db.String(1000))
    contents = db.Column(db.String(1000))
    items = db.Column(db.String(1000))

    def __init__(self, company, logo, logobackground, position, postedAt, contract, location, apply, website,
                 description, contents, items):
        self.company = company
        self.logo = logo
        self.logobackground = logobackground
        self.position = position
        self.postedAt = postedAt
        self.contract = contract
        self.location = location
        self.apply = apply
        self.website = website
        self.description = description
        self.contents = contents
        self.items = items


@app.route("/")
def home():
    #home route
    return render_template('index.html')


@app.route('/jobs', methods=['GET'])
def get_jobs():
    # Get all jobs
    try:
        jobs = Job.query.all()
        job_list = []
        for job in jobs:
            job_details = {
                'id': job.id,
                'company': job.company,
                'logo': job.logo,
                'logobackground': job.logobackground,
                'position': job.position,
                'postedAt': job.postedAt,
                'contract': job.contract,
                'location': job.location,
                'apply': job.apply,
                'website': job.website,
                'description': job.description,
                'contents': job.contents,
                'items': job.items,
            }
            job_list.append(job_details)

        return jsonify(job_list)
    except Exception as e:
        print('Error:', e)
        return jsonify(error='An error occurred'), 500


@app.route('/jobs', methods=['POST'])
def create_job():
    # create jobs
    try:
        data = request.json
        job = Job(
            company=data['company'],
            logo=data['logo'],
            logobackground=data['logobackground'],
            position=data['position'],
            postedAt=data['postedAt'],
            contract=data['contract'],
            location=data['location'],
            apply=data['apply'],
            website=data['website'],
            description=data['description'],
            contents=data['contents'],
            items=data['items']
        )
        db.session.add(job)
        db.session.commit()
        return jsonify({'message': 'Job created successfully'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/jobs/<int:jobId>', methods=['GET'])
def get_job_details(jobId):
    # Get job details
    try:
        job = Job.query.get(jobId)
        if job:
            job_details = {
                'id': job.id,
                'company': job.company,
                'logo': job.logo,
                'logobackground': job.logobackground,
                'position': job.position,
                'postedAt': job.postedAt,
                'contract': job.contract,
                'location': job.location,
                'apply': job.apply,
                'website': job.website,
                'description': job.description,
                'contents': job.contents,
                'items': job.items,
            }
            return jsonify(job_details)
        else:
            return jsonify({'error': 'Job not found'}), 404

    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/jobs/search', methods=['GET'])
def search_jobs():
    # Search jobs
    try:
        title = request.args.get('title')
        location = request.args.get('location')

        query = Job.query

        if title:
            query = query.filter(Job.title.like(f'%{title}%'))

        if location:
            query = query.filter(Job.location.like(f'%{location}%'))

        jobs = query.all()
        job_list = []
        for job in jobs:
            job_details = {
                'id': job.id,
                'company': job.company,
                'logo': job.logo,
                'logobackground': job.logobackground,
                'position': job.position,
                'postedAt': job.postedAt,
                'contract': job.contract,
                'location': job.location,
                'apply': job.apply,
                'website': job.website,
                'description': job.description,
                'contents': job.contents,
                'items': job.items,
            }
            job_list.append(job_details)

        return jsonify(job_list)

    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/create_tables')
def create_tables():
    with app.app_context():
        db.create_all()
    return 'Tables created'


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
