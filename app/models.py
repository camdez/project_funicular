from app import app, db
from datetime import datetime

class Request(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	request_time = db.Column(db.DateTime)
	gtfs_url = db.Column(db.String(240))
	gtfs_description = db.Column(db.String(360))
	agency_id = db.Column(db.String(120))
	email = db.Column(db.String(120))
	uuid = db.Column(db.String(36))
	status = db.Column(db.Integer)
	downloads = db.Column(db.Integer)

	def __init__(self, gtfs_url, gtfs_description, agency_id, email, uuid):
		self.request_time = datetime.utcnow()
		self.gtfs_url = gtfs_url
		self.gtfs_description = gtfs_description
		self.agency_id = agency_id
		self.email = email
		self.uuid = uuid
		self.status = 0
		self.downloads = 0

	# status indicators
	# 0: queued for processing
	# 1: currently being processed
	# 2: already processed

	def __repr__(self):
		return '<Request %r>' % (self.id)

	def begin_processing(self):
		self.status = 1
		db.session.commit()

	def finish_processing(self):
		self.status = 2
		db.session.commit()