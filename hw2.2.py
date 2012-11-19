import pymongo
import sys
from pymongo import Connection
connection = Connection('localhost', 27017)

db = connection.students
names = db.grades
items = names.find({"type":"homework"}).sort([("student_id",pymongo.ASCENDING),("score",pymongo.ASCENDING)])

studentId = 0;
for doc in items:
	print doc
	if doc['student_id'] != studentId:
		print "Removed " + str(doc['_id']) + " and " + str(doc['student_id'])

	student_id = doc['student_id']


