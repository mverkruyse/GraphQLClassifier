import HSEClassifier
import json

def classifyIncident(incident, text_classifier, version=0):

	if version==0:
		#Classifier is expecting a list of documents
		incident = [incident]
	
		#np objects are not json serializable, need to convert them to list
		predicted = text_classifier.text_clf1.predict(incident)
		predicted = predicted.tolist()
		predicted = predicted[0]
	
		predicted_confidence = text_classifier.text_clf1.predict_proba(incident)
		predicted_confidence = predicted_confidence.tolist()
		predicted_confidence = predicted_confidence[0]
		predicted_score = max(predicted_confidence)
	
		categories = text_classifier.text_clf1.classes_
		categories = categories.tolist()

		predicted_grid = text_classifier.gs_clf.predict(incident)
		predicted_grid = predicted_grid.tolist()
	
		predicted_grid_confidence = text_classifier.gs_clf.predict_proba(incident)
		predicted_grid_confidence = predicted_grid_confidence.tolist()
		predicted_grid_confidence = predicted_grid_confidence[0]
		predicted_grid_score = max(predicted_grid_confidence)
	
	
		#put results in a JSON format for returning to the flask server
		predicted_results = json.dumps({
		"incident_description": incident[0],
		"prediction_flag": "Success",
		"prediction_categories": categories,
		"NB_prediction":{
			"prediction": predicted,  
			"prediction_confidence": predicted_score,
			"all_scores": predicted_confidence,
			},
		"NB_optimized_prediction":{
			"prediction": predicted_grid,
			"prediction_confidence": predicted_grid_score,
			"all_scores": predicted_grid_confidence,
		}})

		return predicted_results
	elif version==1:
		null_results = json.dumps({
		"incident_description": incident,
		"prediction_flag": "No prediction (invalid incident ID)",
		"prediction_categories": "none",
		"NB_prediction":{
			"prediction": "none",  
			"prediction_confidence": "1",
			},
		"NB_optimized_prediction":{
			"grid_prediction": "none",
			"grid_prediction_confidence": "0"
		}})
		return null_results
	else:
		null_results = json.dumps({
		"incident_description": incident,
		"prediction_flag": "No prediction (Too short of a description)",
		"prediction_categories": "none",
		"NB_prediction":{
			"prediction": "none",  
			"prediction_confidence": "1",
			},
		"NB_optimized_prediction":{
			"grid_prediction": "none",
			"grid_prediction_confidence": "0"
		}})
		return null_results