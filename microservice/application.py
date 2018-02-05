from flask import Flask
import getIOGPHiPoIncident
import getIOGPFatalIncident
import getClassification
import HSEClassifier


# EB looks for an 'application' callable by default.
application = Flask(__name__)

text_classifier = HSEClassifier.text_clf()

@application.route('/', methods=['GET'])
def hellWorld():
	return "<html><body><h1>This microservice is working!</h1><p>Congrats on launching!</p></body></html>"
	
@application.route('/classifyIOGPHiPoIncident/<int:post_id>', methods=['GET'])
def classifyIOGPHiPo(post_id):
	# takes the id and scrapes the incident from http://safetyzone.iogp.org/HighPotentialEvents/
	x = getIOGPHiPoIncident.get_post(post_id)
	if x == "invalid id":
		return getClassification.classifyIncident(x, text_classifier, 1)
	return getClassification.classifyIncident(x, text_classifier)

@application.route('/classifyIOGPFatalIncident/<int:post_id>', methods=['GET'])
def classifyIOGPFatal(post_id):
	# takes the id and scrapes the incident from http://safetyzone.iogp.org/FatalIncidents/
	x = getIOGPFatalIncident.get_post(post_id)
	if x == "invalid id":
		return getClassification.classifyIncident(x, text_classifier, 1)
	return getClassification.classifyIncident(x, text_classifier)

@application.route('/classifyTextInput/<string:incident>', methods=['GET'])
def classifyInput(incident):
	if len(incident) < 10:
		return getClassification.classifyIncident(incident, text_classifier, 2)
	return getClassification.classifyIncident(incident, text_classifier)

# run the app.
if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    application.debug = True
    application.run()
