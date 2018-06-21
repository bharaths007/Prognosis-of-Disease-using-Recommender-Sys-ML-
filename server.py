from flask import Flask, request, render_template
import html.parser
import csv
app = Flask(__name__)

@app.route("/")
def landing():
	parser = html.parser.HTMLParser()
	options = "<option value=\"volvo\">Volvo</option>"
	with open('symptomOptions.dat', 'r') as symptomOptions:
		options = parser.unescape(symptomOptions.read())
	print(options)
	return render_template('landing.html', options=options)

@app.route("/search", methods=['POST'])
def search(): 
	userSymptoms = []
	userSymptoms.append(request.form['symptom1'])
	userSymptoms.append(request.form['symptom2'])
	userSymptoms.append(request.form['symptom3'])
	userSymptoms.append(request.form['symptom4'])

	supersetD = 'influenza,gastritis,hypercholesterolemia,epilepsy,insufficiency renal,dehydration,hypothyroidism,hernia hiatal,fibroid tumor,deglutition disorder,osteoporosis,chronic alcoholic intoxication,asthma,sepsis (invertebrate),paranoia,ileus,neoplasm,obesity morbid,primary malignant neoplasm,failure heart,malignant neoplasm of breast,tonic-clonic epilepsy,transient ischemic attack,malignant neoplasm of prostate,embolism pulmonary,tricuspid valve insufficiency,respiratory failure,degenerative polyarthritis,aphasia,neoplasm metastasis,malignant tumor of colon,lymphoma,anemia,chronic obstructive airway disease,sickle cell anemia,coronary arteriosclerosis,cholecystitis,psychotic disorder,thrombus,chronic kidney failure,depressive disorder,myocardial infarction,obesity,infection urinary tract,tachycardia sinus,gout,hyperglycemia,diverticulosis,failure kidney,schizophrenia,decubitus ulcer,encephalopathy,affect labile,carcinoma prostate,Alzheimer\'s disease,incontinence,hyperbilirubinemia,paroxysmal dyspnea,bipolar disorder,hepatitis,pericardial effusion body substance,adhesion,biliary calculus,endocarditis,acquired immuno-deficiency syndrome,pneumothorax,accident cerebrovascular,confusion,candidiasis,anxiety state,cirrhosis,pancytopenia,oral candidiasis,diverticulitis,spasm bronchial,ulcer peptic,depression mental,emphysema pulmonary,hypoglycemia,dependence,osteomyelitis,hemorrhoids,primary carcinoma of the liver cells,pyelonephritis,pancreatitis,cholelithiasis,cardiomyopathy,Pneumocystis carinii pneumonia,carcinoma colon,edema pulmonary,carcinoma breast,hemiparesis,mitral valve insufficiency,peripheral vascular disease,tonic-clonic seizures,effusion pericardial,thrombocytopaenia,adenocarcinoma,failure heart congestive,exanthema,ischemia,hypertension pulmonary,infection,cellulitis,lymphatic diseases,gastroenteritis,parkinson disease,hernia,kidney disease,colitis,deep vein thrombosis,personality disorder,hyperlipidemia,pneumonia,gastroesophageal reflux disease,pneumonia aspiration,stenosis aortic valve,hypertensive disease,glaucoma,septicemia,bronchitis,delusion,upper respiratory infection,dementia,ketoacidosis diabetic ,manic disorder,suicide attempt,hiv infections,benign prostatic hypertrophy,HIV,bacteremia,neutropenia,hepatitis B,hepatitis C,coronary heart disease,carcinoma of lung,arthritis,malignant neoplasm of lung,carcinoma,delirium,melanoma,kidney failure acute,diabetes,systemic infection,malignant neoplasms,neuropathy,overload fluid,migraine disorders'
	symptomD = {}
	for disease in supersetD.split(','):
		symptomD[disease] = []

	with open('symptoms.csv', 'rt') as csvfile:
		reader = csv.reader(csvfile, delimiter=',')
		next(reader,None)
		for row in reader:
			symptomD[row[0]].append(row[1])

	results = {}

	for disease, symptoms in symptomD.items():
		for s in userSymptoms:
			if s in symptoms:
				if disease not in results:
					results[disease] = 0
				results[disease] += 1

	# with open('symptoms.csv', 'rt') as csvfile:
	# 		reader = csv.reader(csvfile, delimiter=',')
	# 		for row in reader:
	# 			 if text in row[1]:
	# 			 	if row[0] not in diseases:
	# 			 		diseases.append(row[0])
	return render_template('results.html', diseases=results)