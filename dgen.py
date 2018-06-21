from faker import Faker
from faker.providers import BaseProvider
import random
import csv
gen = Faker()

class MedicalProvider(BaseProvider):
	def age(self):
		return random.randint(1,85)
	def gender(self):
		options = ['M', 'F']
		return options[random.randrange(len(options))]
	def race(self):
		options = ["White", "White","White","White","Black or African American","Black or African American","Black or African American","Asian","Asian","Native American or Alaska Native","Native Hawaiians or Other Pacific Islander","Two or more races","Some other race"]
		return options[random.randrange(len(options))]
	def blood(self):
		options = ["A+", "B+", "AB+", "O+", "A+", "B+", "AB+", "O+", "A+", "B+", "AB+", "O+", "A-", "B-", "AB-", "O-"]
		return options[random.randrange(len(options))]
	def diseases(self,age,gender):
		options20 = ["influenza", "influenza", "influenza", "influenza", "influenza", "influenza", "influenza", "influenza","gastritis", "gastritis", "gastritis", "gastritis","epilepsy","insufficiency renal","dehydration","hypothyroidism","hernia hiatal","fibroid tumor","deglutition disorder","osteoporosis","asthma","sepsis (invertebrate)","paranoia","ileus","neoplasm","obesity morbid","primary malignant neoplasm","tonic-clonic epilepsy","transient ischemic attack","malignant neoplasm of prostate","embolism pulmonary","tricuspid valve insufficiency","respiratory failure","degenerative polyarthritis","aphasia","neoplasm metastasis","malignant tumor of colon","lymphoma","anemia","chronic obstructive airway disease","sickle cell anemia","coronary arteriosclerosis","cholecystitis","psychotic disorder","thrombus","chronic kidney failure","depressive disorder","myocardial infarction","obesity","infection urinary tract","tachycardia sinus","gout","hyperglycemia","diverticulosis","failure kidney","schizophrenia","decubitus ulcer","encephalopathy","affect labile","carcinoma prostate","incontinence","hyperbilirubinemia","paroxysmal dyspnea","bipolar disorder","hepatitis","pericardial effusion body substance","adhesion","biliary calculus","endocarditis","acquired immuno-deficiency syndrome","pneumothorax","accident cerebrovascular","confusion","candidiasis","cirrhosis","pancytopenia","oral candidiasis","diverticulitis","spasm bronchial","ulcer peptic","depression mental","emphysema pulmonary","hypoglycemia","dependence","osteomyelitis","hemorrhoids","primary carcinoma of the liver cells","pyelonephritis","pancreatitis","cholelithiasis","cardiomyopathy","Pneumocystis carinii pneumonia","carcinoma colon","edema pulmonary","hemiparesis","mitral valve insufficiency","peripheral vascular disease","tonic-clonic seizures","effusion pericardial","thrombocytopaenia","adenocarcinoma","failure heart congestive","exanthema","ischemia","hypertension pulmonary","infection","cellulitis","lymphatic diseases","gastroenteritis","parkinson disease","hernia","kidney disease","colitis","deep vein thrombosis","personality disorder","hyperlipidemia","pneumonia","gastroesophageal reflux disease","pneumonia aspiration","stenosis aortic valve","hypertensive disease","glaucoma","septicemia","bronchitis","delusion","upper respiratory infection","dementia","ketoacidosis diabetic ","manic disorder","suicide attempt","hiv infections","benign prostatic hypertrophy","bacteremia","neutropenia","hepatitis B","hepatitis C","carcinoma of lung","arthritis","malignant neoplasm of lung","carcinoma","delirium","melanoma","kidney failure acute","diabetes","systemic infection","malignant neoplasms","neuropathy","overload fluid","migraine disorders"]
		options40 = options20 + ["chronic alcoholic intoxication", "chronic alcoholic intoxication", "chronic alcoholic intoxication","failure heart", "failure heart","degenerative polyarthritis","chronic kidney failure","Alzheimer's disease","acquired immuno-deficiency syndrome","HIV","coronary heart disease", "coronary heart disease","hypercholesterolemia", "hypercholesterolemia","anxiety state","anxiety state"]
		if gender == 'F':
			options40 += ["malignant neoplasm of breast","carcinoma breast","malignant neoplasm of breast","carcinoma breast"]
		diseases = []
		if age < 11:
			countDist = [0,0,1,1,1,1,1,1,1,2,2,2,2,2,2,2,3,3,3]
			count = countDist[random.randrange(len(countDist))]
			for _ in range(count):
				disease = options20[random.randrange(len(options20))]
				if disease in diseases:
					continue
				diseases.append(disease)
		elif age < 21:
			countDist = [0,1,1,1,1,2,2,2,2,3,3]
			count = countDist[random.randrange(len(countDist))]
			for _ in range(count):
				disease = options20[random.randrange(len(options20))]
				if disease in diseases:
					continue
				diseases.append(disease)
		elif age < 41:
			countDist = [0,1,1,1,1,1,2,2,2,2,2,2,3,3,3,3,3,4,4,5,6]
			count = countDist[random.randrange(len(countDist))]
			for _ in range(count):
				disease = options40[random.randrange(len(options40))]
				if disease in diseases:
					continue
				diseases.append(disease)
		elif age < 61:
			countDist = [0,1,1,1,1,2,2,2,2,3,3,3,4,4,5,6]
			count = countDist[random.randrange(len(countDist))]
			options60 = options40 + ["chronic alcoholic intoxication","failure heart","failure heart","failure heart","degenerative polyarthritis","chronic kidney failure","Alzheimer's disease","Alzheimer's disease","Alzheimer's disease","Alzheimer's disease","Alzheimer's disease","acquired immuno-deficiency syndrome","HIV","coronary heart disease","coronary heart disease","coronary heart disease","anxiety state","anxiety state"]
			for _ in range(count):
				disease = options60[random.randrange(len(options60))]
				if disease in diseases:
					continue
				diseases.append(disease)
		elif age > 60:
			countDist = [1,1,1,1,2,2,2,2,3,3,3,4,4,5,6]
			count = countDist[random.randrange(len(countDist))]
			options70 = options40 + ["chronic alcoholic intoxication","failure heart","failure heart","failure heart","degenerative polyarthritis","chronic kidney failure","Alzheimer's disease","Alzheimer's disease","Alzheimer's disease","Alzheimer's disease","Alzheimer's disease","acquired immuno-deficiency syndrome","HIV","coronary heart disease","coronary heart disease","coronary heart disease"]
			for _ in range(count):
				disease = options70[random.randrange(len(options70))]
				if disease in diseases:
					continue
				diseases.append(disease)
		return diseases
	def symptoms(self):
		symptoms = []
		# options = ["Pain", "Fatigue", "Weight Loss", "Headache", "Infection", "Swelling", "Nausea", "Vomiting", "Abdominal Pain", "Diarrhea", "Depression", "Stress", "Skin Rash", "Constipation", "Itch", "Dizziness", "Shortness of breath", "Cough", "Bleeding", "Back pain", "Chest pain", "Irritability", "Joint pain", "Inflammation", "Fever", "Fever", "Fever", "Fever", "Migraine", "Knee pain", "Muscle pain", "Hair loss"]
		countDist = [1,1,1,1,2,2,2,2,2,2,3,3,3,3,3,3,3,4,5]
		count = countDist[random.randrange(len(countDist))]
		diseases = ["influenza","gastritis","hypercholesterolemia","epilepsy","insufficiency renal","dehydration","hypothyroidism","hernia hiatal","fibroid tumor","deglutition disorder","osteoporosis","chronic alcoholic intoxication","asthma","sepsis (invertebrate)","paranoia","ileus","neoplasm","obesity morbid","primary malignant neoplasm","failure heart","malignant neoplasm of breast","tonic-clonic epilepsy","transient ischemic attack","malignant neoplasm of prostate","embolism pulmonary","tricuspid valve insufficiency","respiratory failure","degenerative polyarthritis","aphasia","neoplasm metastasis","malignant tumor of colon","lymphoma","anemia","chronic obstructive airway disease","sickle cell anemia","coronary arteriosclerosis","cholecystitis","psychotic disorder","thrombus","chronic kidney failure","depressive disorder","myocardial infarction","obesity","infection urinary tract","tachycardia sinus","gout","hyperglycemia","diverticulosis","failure kidney","schizophrenia","decubitus ulcer","encephalopathy","affect labile","carcinoma prostate","Alzheimer's disease","incontinence","hyperbilirubinemia","paroxysmal dyspnea","bipolar disorder","hepatitis","pericardial effusion body substance","adhesion","biliary calculus","endocarditis","acquired immuno-deficiency syndrome","pneumothorax","accident cerebrovascular","confusion","candidiasis","anxiety state","cirrhosis","pancytopenia","oral candidiasis","diverticulitis","spasm bronchial","ulcer peptic","depression mental","emphysema pulmonary","hypoglycemia","dependence","osteomyelitis","hemorrhoids","primary carcinoma of the liver cells","pyelonephritis","pancreatitis","cholelithiasis","cardiomyopathy","Pneumocystis carinii pneumonia","carcinoma colon","edema pulmonary","carcinoma breast","hemiparesis","mitral valve insufficiency","peripheral vascular disease","tonic-clonic seizures","effusion pericardial","thrombocytopaenia","adenocarcinoma","failure heart congestive","exanthema","ischemia","hypertension pulmonary","infection","cellulitis","lymphatic diseases","gastroenteritis","parkinson disease","hernia","kidney disease","colitis","deep vein thrombosis","personality disorder","hyperlipidemia","pneumonia","gastroesophageal reflux disease","pneumonia aspiration","stenosis aortic valve","hypertensive disease","glaucoma","septicemia","bronchitis","delusion","upper respiratory infection","dementia","ketoacidosis diabetic ","manic disorder","suicide attempt","hiv infections","benign prostatic hypertrophy","HIV","bacteremia","neutropenia","hepatitis B","hepatitis C","coronary heart disease","carcinoma of lung","arthritis","malignant neoplasm of lung","carcinoma","delirium","melanoma","kidney failure acute","diabetes","systemic infection","malignant neoplasms","neuropathy","overload fluid","migraine disorders"]
		disease = diseases[random.randrange(len(diseases))]
		possibilities = []

		with open('symptoms.csv', 'rt') as csvfile:
			reader = csv.reader(csvfile, delimiter=',')
			for row in reader:
				 if row[0] == disease:
				 	possibilities.append(row[1])

		for _ in range(count):
			# symptom = options[random.randrange(len(options))]
			symptom = possibilities[random.randrange(len(possibilities))]
			if symptom in symptoms:
				continue
			symptoms.append(symptom)
		return symptoms	

gen.add_provider(MedicalProvider)

f = open('csvfile.csv','w')
f.write('ID,Age,Gender,Race,Blood Group,Disease Group A (0-5),Disease Group B (6-10),Disease Group C (11-20),Disease Group D (21-30),Disease Group E (31-40),Disease Group F (41-50),Disease Group G (51-60),Disease Group H (61-70),Disease Group I (70+),Current Symptoms\n')
for i in range(2999):
	age = gen.age()
	gender = gen.gender()
	race = gen.race()
	blood = gen.blood()
	diseases = [gen.diseases(5, gender), gen.diseases(10, gender), gen.diseases(20, gender), gen.diseases(30, gender), gen.diseases(40, gender), gen.diseases(50, gender), gen.diseases(60, gender), gen.diseases(70, gender), gen.diseases(80, gender)]
	symptoms = gen.symptoms()
	if age < 71:
		diseases[8] = []
	if age < 61:
		diseases[7] = []
	if age < 51:
		diseases[6] = []
	if age < 41:
		diseases[5] = []
	if age < 31:
		diseases[4] = []
	if age < 21:
		diseases[3] = []
	if age < 11:
		diseases[2] = []
	if age < 6:
		diseases[1] = []
	csvString = "{0}, {1}, {2}, {3}, {4}, \"{5}\", \"{6}\", \"{7}\", \"{8}\", \"{9}\", \"{10}\", \"{11}\", \"{12}\", \"{13}\", \"{14}\"\n".format(i, age, gender, race, blood, ", ".join(diseases[0]), ", ".join(diseases[1]), ", ".join(diseases[2]), ", ".join(diseases[3]), ", ".join(diseases[4]), ", ".join(diseases[5]), ", ".join(diseases[6]), ", ".join(diseases[7]), ", ".join(diseases[8]), ", ".join(symptoms))
	f.write(csvString)
f.close()
