import pymongo
import sys

def find_lowest_grade(scores):

	min_score = 101
	for score in scores:
		if score['score'] < min_score and score['type'] == 'homework':
			min_score = score['score']

	return min_score



def remove_lowest_score(lowest_score, _id):
	print "lowest score to be removed " + str(lowest_score) + " for student id " + str(_id)

	s = students_collection.find_one({"_id" : _id})

	for score in s['scores']:
		if score['score'] == lowest_score: 
			s['scores'].remove(score)
			continue

	print s['scores']

	students_collection.update({"_id" : _id},s)


from pymongo import Connection
connection = Connection('localhost', 27017)

db = connection.school
students_collection = db.students
students = students_collection.find()

#items = names.find({"type":"homework"}).sort([("student_id",pymongo.ASCENDING),("score",pymongo.ASCENDING)])

studentId = 0;
for student in students:
	print "\n\n\n\n **********"
	print student

	lowest_score = find_lowest_grade(student['scores'])
	print "the lowest score for " + student['name'] + " is " + str(lowest_score)
	remove_lowest_score(lowest_score,student['_id'])
	print "\n\n\n\n **********"
	#if doc['student_id'] != studentId:
#		print "Removed " + str(doc['_id']) + " and " + str(doc['student_id'])

#	student_id = doc['student_id']






