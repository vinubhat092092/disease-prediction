from tkinter import *
import numpy as np
import pandas as pd
# from gui_stuff import *

l1=['itching','skin_rash','nodal_skin_eruptions','continuous_sneezing','shivering','chills',
'joint_pain','stomach_pain','acidity','ulcers_on_tongue','muscle_wasting','vomiting',
'burning_micturition','spotting_ urination','fatigue','weight_gain','anxiety','cold_hands_and_feets',
'mood_swings','weight_loss','restlessness','lethargy','patches_in_throat','irregular_sugar_level','cough',
'high_fever','sunken_eyes','breathlessness','sweating','dehydration','indigestion','headache',
'yellowish_skin','dark_urine','nausea','loss_of_appetite','pain_behind_the_eyes',
'back_pain','constipation','abdominal_pain','diarrhoea','mild_fever','yellow_urine',
'yellowing_of_eyes','acute_liver_failure','fluid_overload','swelling_of_stomach',
'swelled_lymph_nodes','malaise','blurred_and_distorted_vision','phlegm','throat_irritation',
'redness_of_eyes','sinus_pressure','runny_nose','congestion','chest_pain','weakness_in_limbs',
'fast_heart_rate','pain_during_bowel_movements','pain_in_anal_region','bloody_stool',
'irritation_in_anus','neck_pain','dizziness','cramps','bruising','obesity','swollen_legs',
'swollen_blood_vessels','puffy_face_and_eyes','enlarged_thyroid','brittle_nails',
'swollen_extremeties','excessive_hunger','extra_marital_contacts','drying_and_tingling_lips',
'slurred_speech','knee_pain','hip_joint_pain','muscle_weakness','stiff_neck','swelling_joints',
'movement_stiffness','spinning_movements','loss_of_balance','unsteadiness',
'weakness_of_one_body_side','loss_of_smell','bladder_discomfort','foul_smell_of urine',
'continuous_feel_of_urine','passage_of_gases','internal_itching','toxic_look_(typhos)',
'depression','irritability','muscle_pain','altered_sensorium','red_spots_over_body','belly_pain',
'abnormal_menstruation','dischromic _patches','watering_from_eyes','increased_appetite','polyuria','family_history','mucoid_sputum',
'rusty_sputum','lack_of_concentration','visual_disturbances','receiving_blood_transfusion',
'receiving_unsterile_injections','coma','stomach_bleeding','distention_of_abdomen',
'history_of_alcohol_consumption','fluid_overload','blood_in_sputum','prominent_veins_on_calf',
'palpitations','painful_walking','pus_filled_pimples','blackheads','scurring','skin_peeling',
'silver_like_dusting','small_dents_in_nails','inflammatory_nails','blister','red_sore_around_nose',
'yellow_crust_ooze']

disease=['Fungal infection','Fungal infection','Fungal infection','Fungal infection','Fungal infection',
         'Fungal infection','Fungal infection','Fungal infection','Fungal infection','Fungal infection',
         'Allergy','Allergy','Allergy','Allergy','Allergy',
         'Allergy','Allergy','Allergy','Allergy','Allergy',
         'SARS-CoV-2 (Covid-19)','SARS-CoV-2 (Covid-19)','SARS-CoV-2 (Covid-19)','SARS-CoV-2 (Covid-19)','SARS-CoV-2 (Covid-19)',
         'SARS-CoV-2 (Covid-19)','SARS-CoV-2 (Covid-19)','SARS-CoV-2 (Covid-19)','SARS-CoV-2 (Covid-19)','SARS-CoV-2 (Covid-19)',
         'Chronic cholestasis','Chronic cholestasis','Chronic cholestasis','Chronic cholestasis','Chronic cholestasis',
         'Chronic cholestasis','Chronic cholestasis','Chronic cholestasis','Chronic cholestasis','Chronic cholestasis',
         'Drug Reaction','Drug Reaction','Drug Reaction','Drug Reaction','Drug Reaction',
         'Drug Reaction','Drug Reaction','Drug Reaction','Drug Reaction','Drug Reaction',
         'Peptic ulcer diseae','Peptic ulcer diseae','Peptic ulcer diseae','Peptic ulcer diseae','Peptic ulcer diseae',
         'Peptic ulcer diseae','Peptic ulcer diseae','Peptic ulcer diseae','Peptic ulcer diseae','Peptic ulcer diseae',
         'AIDS','AIDS','AIDS','AIDS','AIDS',
         'AIDS','AIDS','AIDS','AIDS','AIDS',
         'Diabetes','Diabetes','Diabetes','Diabetes','Diabetes',
         'Diabetes','Diabetes','Diabetes','Diabetes','Diabetes',
         'Gastroenteritis','Gastroenteritis','Gastroenteritis','Gastroenteritis','Gastroenteritis',
         'Gastroenteritis','Gastroenteritis','Gastroenteritis','Gastroenteritis','Gastroenteritis',
         'Bronchial Asthma','Bronchial Asthma','Bronchial Asthma','Bronchial Asthma','Bronchial Asthma',
         'Bronchial Asthma','Bronchial Asthma','Bronchial Asthma','Bronchial Asthma','Bronchial Asthma',
         'Hypertension','Hypertension','Hypertension','Hypertension','Hypertension',
         'Hypertension','Hypertension','Hypertension','Hypertension','Hypertension',
         'Migraine','Migraine','Migraine','Migraine','Migraine',
         'Migraine','Migraine','Migraine','Migraine','Migraine',
         'Cervical spondylosis','Cervical spondylosis','Cervical spondylosis','Cervical spondylosis','Cervical spondylosis',
         'Cervical spondylosis','Cervical spondylosis','Cervical spondylosis','Cervical spondylosis','Cervical spondylosis',
         'Paralysis (brain hemorrhage)','Paralysis (brain hemorrhage)','Paralysis (brain hemorrhage)',
         'Paralysis (brain hemorrhage)','Paralysis (brain hemorrhage)','Paralysis (brain hemorrhage)',
         'Paralysis (brain hemorrhage)','Paralysis (brain hemorrhage)','Paralysis (brain hemorrhage)',
         'Paralysis (brain hemorrhage)',
         'Jaundice','Jaundice','Jaundice','Jaundice','Jaundice',
         'Jaundice','Jaundice','Jaundice','Jaundice','Jaundice',
         'Malaria','Malaria','Malaria','Malaria','Malaria',
         'Malaria','Malaria','Malaria','Malaria','Malaria',
         'Chicken pox','Chicken pox','Chicken pox','Chicken pox','Chicken pox',
         'Chicken pox','Chicken pox','Chicken pox','Chicken pox','Chicken pox',
         'Dengue','Dengue','Dengue','Dengue','Dengue',
         'Dengue','Dengue','Dengue','Dengue','Dengue',
         'Typhoid','Typhoid','Typhoid','Typhoid','Typhoid',
         'Typhoid','Typhoid','Typhoid','Typhoid','Typhoid',
         'hepatitis A','hepatitis A','hepatitis A','hepatitis A','hepatitis A',
         'hepatitis A','hepatitis A','hepatitis A','hepatitis A','hepatitis A',
         'Hepatitis B','Hepatitis B','Hepatitis B','Hepatitis B','Hepatitis B',
         'Hepatitis B','Hepatitis B','Hepatitis B','Hepatitis B','Hepatitis B',
         'Hepatitis C','Hepatitis C','Hepatitis C','Hepatitis C','Hepatitis C',
         'Hepatitis C','Hepatitis C','Hepatitis C','Hepatitis C','Hepatitis C',
         'Hepatitis D','Hepatitis D','Hepatitis D','Hepatitis D','Hepatitis D',
         'Hepatitis D','Hepatitis D','Hepatitis D','Hepatitis D','Hepatitis D',
         'Hepatitis E','Hepatitis E','Hepatitis E','Hepatitis E','Hepatitis E',
         'Hepatitis E','Hepatitis E','Hepatitis E','Hepatitis E','Hepatitis E',
         'Alcoholic hepatitis','Alcoholic hepatitis','Alcoholic hepatitis',
         'Alcoholic hepatitis','Alcoholic hepatitis','Alcoholic hepatitis',
         'Alcoholic hepatitis','Alcoholic hepatitis','Alcoholic hepatitis',
         'Alcoholic hepatitis',
         'Tuberculosis','Tuberculosis','Tuberculosis','Tuberculosis','Tuberculosis',
         'Tuberculosis','Tuberculosis','Tuberculosis','Tuberculosis','Tuberculosis',
         'Common Cold','Common Cold','Common Cold','Common Cold','Common Cold',
         'Common Cold','Common Cold','Common Cold','Common Cold','Common Cold',
         'Pneumonia','Pneumonia','Pneumonia','Pneumonia','Pneumonia',
         'Pneumonia','Pneumonia','Pneumonia','Pneumonia','Pneumonia',
         'Dimorphic hemmorhoids(piles)','Dimorphic hemmorhoids(piles)','Dimorphic hemmorhoids(piles)',
         'Dimorphic hemmorhoids(piles)','Dimorphic hemmorhoids(piles)','Dimorphic hemmorhoids(piles)',
         'Dimorphic hemmorhoids(piles)','Dimorphic hemmorhoids(piles)','Dimorphic hemmorhoids(piles)',
         'Dimorphic hemmorhoids(piles)',
         'Heart attack','Heart attack','Heart attack','Heart attack','Heart attack',
         'Heart attack','Heart attack','Heart attack','Heart attack','Heart attack',
         'Varicose veins','Varicose veins','Varicose veins','Varicose veins','Varicose veins',
         'Varicose veins','Varicose veins','Varicose veins','Varicose veins','Varicose veins',
         'Hypothyroidism','Hypothyroidism','Hypothyroidism','Hypothyroidism','Hypothyroidism',
         'Hypothyroidism','Hypothyroidism','Hypothyroidism','Hypothyroidism','Hypothyroidism',
         'Hyperthyroidism','Hyperthyroidism','Hyperthyroidism','Hyperthyroidism','Hyperthyroidism',
         'Hyperthyroidism','Hyperthyroidism','Hyperthyroidism','Hyperthyroidism','Hyperthyroidism',
         'Hypoglycemia','Hypoglycemia','Hypoglycemia','Hypoglycemia','Hypoglycemia',
         'Hypoglycemia','Hypoglycemia','Hypoglycemia','Hypoglycemia','Hypoglycemia',
         'Osteoarthristis','Osteoarthristis','Osteoarthristis','Osteoarthristis','Osteoarthristis',
         'Osteoarthristis','Osteoarthristis','Osteoarthristis','Osteoarthristis','Osteoarthristis',
         'Arthritis','Arthritis','Arthritis','Arthritis','Arthritis',
         'Arthritis','Arthritis','Arthritis','Arthritis','Arthritis',
         '(vertigo) Paroymsal  Positional Vertigo','(vertigo) Paroymsal  Positional Vertigo',
         '(vertigo) Paroymsal  Positional Vertigo','(vertigo) Paroymsal  Positional Vertigo',
         '(vertigo) Paroymsal  Positional Vertigo','(vertigo) Paroymsal  Positional Vertigo',
         '(vertigo) Paroymsal  Positional Vertigo','(vertigo) Paroymsal  Positional Vertigo',
         '(vertigo) Paroymsal  Positional Vertigo','(vertigo) Paroymsal  Positional Vertigo',
         'Acne', 'Acne', 'Acne', 'Acne', 'Acne',
         'Acne', 'Acne', 'Acne', 'Acne', 'Acne',
         'Urinary tract infection','Urinary tract infection','Urinary tract infection',
         'Urinary tract infection','Urinary tract infection','Urinary tract infection',
         'Urinary tract infection','Urinary tract infection','Urinary tract infection',
         'Urinary tract infection',
         'Psoriasis','Psoriasis','Psoriasis','Psoriasis','Psoriasis',
         'Psoriasis','Psoriasis','Psoriasis','Psoriasis','Psoriasis',
         'Impetigo','Impetigo','Impetigo','Impetigo','Impetigo',
         'Impetigo','Impetigo','Impetigo','Impetigo','Impetigo',
         'GERD','GERD','GERD','GERD','GERD',
         'GERD','GERD','GERD','GERD','GERD',
         'Polycystic ovary syndrome (PCOS)','Polycystic ovary syndrome (PCOS)','Polycystic ovary syndrome (PCOS)','Polycystic ovary syndrome (PCOS)',
         'Polycystic ovary syndrome (PCOS)','Polycystic ovary syndrome (PCOS)','Polycystic ovary syndrome (PCOS)','Polycystic ovary syndrome (PCOS)',
         'Polycystic ovary syndrome (PCOS)','Polycystic ovary syndrome (PCOS)',
         'Low Blood Pressure','Low Blood Pressure','Low Blood Pressure','Low Blood Pressure','Low Blood Pressure',
         'Low Blood Pressure','Low Blood Pressure','Low Blood Pressure','Low Blood Pressure','Low Blood Pressure',
         'High Blood Pressure','High Blood Pressure','High Blood Pressure','High Blood Pressure','High Blood Pressure',
         'High Blood Pressure','High Blood Pressure','High Blood Pressure','High Blood Pressure','High Blood Pressure',
         'Chronic lower respiratory system','Chronic lower respiratory system','Chronic lower respiratory system','Chronic lower respiratory system',
         'Chronic lower respiratory system','Chronic lower respiratory system','Chronic lower respiratory system','Chronic lower respiratory system',
         'Chronic lower respiratory system','Chronic lower respiratory system']
print(len(disease))


medication=['radiation therapy and ultraviolet therapy','Terbinafine hydrochloride cream, ultraviolet therapy, ketoconazole cream',
            'Miconazole Nitrate Gel','Terbinafine hydrochloride, Miconazole Nitrate Gel','Clotrimazole, miconazole','Miconazole Nitrate Gel, ketoconazole',
            'amphotericin, radiation therapy','Terbinafine hydrochloride, Miconazole Nitrate Gel','econazole','radiation therapy and ultraviolet therapy',
            'Antihistamines, aspirin','Decongentants, antihistamines','Acetaminophen, polyethylene glycol & ophthalmic','Zyrtec, nasal spray','Antihistamines, Decongentants',
            'Antihistamines, Decongentants','Acetaminophen, polyethylene glycol & ophthalmic','Zyrtec, nasal spray','Antihistamines, Decongentants','Antihistamines, aspirin',
            'Paracetamol,Favipiravis, acebrophyltine & Acetyleystrne, ascorbic acid, zinc acetate','Favipiravis, acebrophyltine & Acetyleystrne, paracetamol, ascorbic acid, zinc acetate',
            'Paracetamol,Grilinctus, ivermectin, azithromycin, ascorbic acid, zinc acetate','Paracetamol,Methylprednisolone, Favipiravis, ascorbic acid, zinc acetate',
            'Grilinctus, ivermectin, azithromycin, ascorbic acid, zinc acetate','Grilinctus, ivermectin, azithromycin, ascorbic acid, zinc acetate','Azithromycin, ivermectin, ascorbic acid, zinc acetate',
            'Ivermectin, paracetamol, ascorbic acid, zinc acetate','Paracetamol,Grilinctus, Favipiravis, Methylprednisolone, ascorbic acid','Ivermectin, ascorbic acid, zinc acetate',
            'Not curable','Not curable','Not curable','Not curable','Not curable','Not curable','Not curable','Not curable','Not curable',
            'Not curable','Antihistamines, change medication','Corticosteroids, change medication','Bronchodilators, change medication','Bronchodilators, change medication',
            'Antihistamines','Corticosteroids, change medication','Antihistamines, change medication','Bronchodilators, change medication','Bronchodilators, change medication',
            'Antihistamines','panloprozole, penicillium','panloprozole, Omeprazole',
            'amoxicillin, tinidazole','tetracycline and levofloxacin','Lansoprazole','amoxicillin, tinidazole','tetracycline and levofloxacin','panloprozole, penicillium',
            'panloprozole, penicillium','panloprozole, penicillium, Lansoprazole','Not curable','Not curable','Not curable','Not curable','Not curable','Not curable',
            'Not curable','Not curable','Not curable','Not curable','Blood Diagnosis required','Blood Diagnosis required','Blood Diagnosis required','Blood Diagnosis required',
            'Blood Diagnosis required','Blood Diagnosis required','Blood Diagnosis required','Blood Diagnosis required','Blood Diagnosis required',
            'Blood Diagnosis required',' Loperamide, ondansetron',' Loperamide, ondansetron','plenty of water, Loperamide','Loperamide, ondansetron','plenty of water, ondansetron',
            'Self healing, plenty of fluids','Loperamide, ondansetron','plenty of water, Loperamide','Loperamide, ondansetron','plenty of water, ondansetron',
            'Predncrone, Bronchodilators, NSAID',' Bronchodilators, NSAID','NSAID, Bronchodilators','Bronchodilators','Bronchodilators','NSAID','Bronchodilators, NSAID',
            'Predncrone, Bronchodilators, NSAID','Bronchodilators, NSAID',' NSAID, Bronchodilators','Lisinopril, Acetaminophen',
            'Hydrochlorothiazide, Aspirin','Amlodipine besylate, Meclizine','Amlodipine besylate, Acetaminophen','Hydrochlorothiazide, Adderall',
            'Lisinopril, Dimenhydrinate','Amlodipine besylate,Ritalin','Lisinopril, Gentamicin','Acetaminophen,Hydrochlorothiazide (HCTZ)','Hydrochlorothiazide,Acetaminophen',
            'Ibuprofen, Dexlansoprazole, Acetaminophen','Ibuprofen, Acetaminophen',
            'Naproxen, Dexlansoprazole, Acetaminophen','Ibuprofen, Dexlansoprazole, Acetaminophen','Ibuprofen, Dexlansoprazole, Acetaminophen',
            'Naproxen, Dexlansoprazole, Acetaminophen','Ibuprofen, Dexlansoprazole, Acetaminophen','Ibuprofen, Dexlansoprazole, Naproxen',
            'Ibuprofen, Dexlansoprazole, Acetaminophen','Naproxen, Dexlansoprazole, Acetaminophen','Indomethacin, Dimenhydrinate, Gabapentin',
            'Oral Prednisone, Meclizine','Cyclobenzaprine, Dimenhydrinate, Gabapentin','Indomethacin, Meclizine, Gentamicin','Oral Prednisone, Pregabalin',
            'Oral Prednisone, Pregabalin, Gabapentin','Cyclobenzaprine, Meclizine','Indomethacin, Dimenhydrinate','Oral Prednisone, Meclizine, Gentamicin',
            'Indomethacin, Dimenhydrinate, Gabapentin','Consult a Doctor','Consult a Doctor','Consult a Doctor','Consult a Doctor','Consult a Doctor',
            'Consult a Doctor','Consult a Doctor','Consult a Doctor','Consult a Doctor','Consult a Doctor','Consult a Doctor','Consult a Doctor','Consult a Doctor','Acetaminophen, Eszopiclone',
            'Consult a Doctor','Acetaminophen, Eszopiclone','Acetaminophen, Meclizine Hydrochloride, Eszopiclone','Acetaminophen, Meclizine Hydrochloride, Eszopiclone',
            'Acetaminophen, Meclizine Hydrochloride, Eszopiclone','Consult a Doctor','Atovaquone-Proguanil, Aspirin, Loperamide','Primaquine Phosphate, Aspirin, Meclizine Hydrochloride',
            'Quinine sulfate with Doxycycline, Aspirin, Ibuprofen','Quinine sulfate with Doxycycline, Aspirin, Ibuprofen','Consult a Doctor',
            'Atovaquone-Proguanil, Aspirin, Loperamide','Consult a Doctor','Quinine sulfate with Doxycycline, Aspirin, Meclizine Hydrochloride','Consult a Doctor','Primaquine Phosphate, Aspirin',
            'Acyclovir, Hydroxyzine Pamoate, Acetaminophen','acyclovir,acetaminophen,Eszopiclone','Acyclovir, Hydroxyzine Pamoate, Acetaminophen','Acyclovir, Hydroxyzine Pamoate, Naproxen',
            'Acyclovir, Hydroxyzine Pamoate, Ibuprofen','Acyclovir, Hydroxyzine Pamoate, Ibuprofen','Acyclovir, Hydroxyzine Pamoate, Naproxen','Acyclovir, Hydroxyzine Pamoate, Acetaminophen',
            'Acyclovir, Hydroxyzine Pamoate, Acetaminophen','Acyclovir, Hydroxyzine Pamoate, Naproxen','Acetaminophen, Meclizine Hydrochloride, Hydrocortisone','Ibuprofen, Meclizine Hydrochloride',
            'Acetaminophen, Meclizine Hydrochloride, Eszopiclone','Ibuprofen, Meclizine hydrochloride, Hydrocortisone','Ibuprofen, Meclizine hydrochloride, Hydrocortisone',
            'Naproxen, Hydrocortisone, Aspirin','Acetaminophen, Hydrocortisone, Aspirin','Ibuprofen, Eszopiclone, Aspirin','Naproxen, Hydrocortisone, Eszopiclone','Acetaminophen, Hydrocortisone, Eszopiclone',
            'Ciprofloxacin, Linaclotide, Acetaminophen','Azithromycin, Linaclotide, Acetaminophen','Ceftriaxone, Meclizine hydrochloride, Ibuprofen','Ciprofloxacin, Ibuprofen, Eszopiclone',
            'Azithromycin, Linaclotide, Acetaminophen','Ciprofloxacin, Ibuprofen, Eszopiclone','Ceftriaxone, Linaclotide, Naproxen','Azithromycin, Linaclotide, Acetaminophen','Ciprofloxaci , Linaclotide, Naproxen',
            'Azithromycin, Linaclotide, Acetaminophen','acetaminophen,Meclizine hydrochloride','Ibuprofen, Promethazine','Ibuprofen, Meclizine Hydrochloride',
            'Naproxen, Pepto-Bismol','Naproxen, Meclizine hydrochloride','Acetaminophen, Pepto-Bismol',
            'acetaminophen,Pepto-Bismol','Ibuprofen, Meclizine Hydrochloride','Naproxen, Promethazine','Acetaminophen, Pepto-Bismol','Consult a Doctor',
            'Consult a Doctor','Consult a Doctor','Consult a Doctor','Consult a Doctor','Consult a Doctor','Consult a Doctor',
            'Consult a Doctor','Consult a Doctor','Consult a Doctor','Consult a Doctor','Consult a Doctor','Consult a Doctor',
            'Consult a Doctor','Consult a Doctor','Consult a Doctor','Consult a Doctor',
            'Consult a Doctor','Consult a Doctor','Consult a Doctor','Consult a Doctor','Consult a Doctor','Consult a Doctor','Consult a Doctor',
            'Consult a Doctor','Consult a Doctor','Consult a Doctor','Consult a Doctor','Consult a Doctor','Consult a Doctor','Consult a Doctor',
            'Consult a Doctor','Consult a Doctor','Consult a Doctor','Consult a Doctor','Consult a Doctor','Consult a Doctor','Consult a Doctor',
            'Consult a Doctor','Consult a Doctor','Corticosteroids, Atorvastatin, Simethicone','Atorvastatin, Oxandrolone, Simethicone','Atorvastatin, Oxandrolone, Simethicone',
            'Corticosteroids, Atorvastatin, Loperamide','Atorvastatin, Oxandrolone, Simethicone','Corticosteroids, Atorvastatin, Loperamide',
            'Atorvastatin, Oxandrolone, Simethicone','Corticosteroids, Atorvastatin, Loperamide','Corticosteroids, Atorvastatin, Loperamide',
            'Atorvastatin, Oxandrolone, Simethicone','Isoniazid, Oseltamivir, Salmeterol, Dextromethorphan, Acetaminophen','Rifampicin, Iced saline, Salbutamol, Dextromethorphan, Ibuprofen',
            'Isoniazid, Iced saline, Salmeterol, Dextromethorphan, Acetaminophen','Rifampicin, Oseltamivir, Salbutamol, Dextromethorphan, Ibuprofen',
            'Pyrazinamide, Iced saline, Salmeterol, Dextromethorphan, Ibuprofen','Pyrazinamide,oseltamivir,salmeterol,Dextromethorphan,acetaminophen,',
            'Isoniazid, Iced saline, Salbutamol, Acetaminophen','Pyrazinamide, Iced saline, Salmeterol, Dextromethorphan, Ibuprofen',
            'Rifampicin, Oseltamivir, Salbutamol, Dextromethorphan, Ibuprofen','Isoniazid, Iced saline, Salmeterol, Dextromethorphan, Acetaminophen,',
            'Oxymetazoline Nasal, Cetirizine','Phenylephrine Nasal, Cetirizine','Phenylephrine Oral','Oxymetazoline Nasal, Cetirizine',
            'Phenylephrine Nasal, Cetirizine','Phenylephrine Nasal, Cetirizine','Phenylephrine Oral, Cetirizine','Oxymetazoline Nasal, Cetirizine',
            'Phenylephrine Nasal, Cetirizine','Oxymetazoline Nasal, Cetirizine','Consult a Doctor','Oracea, Toprol, Acetaminophen, Salbutamol, Dextromethorphan',
            'Consult a Doctor','Levaquin, Toprol, Ibuprofen, Salmeterol, Dextromethorphan','Levaquin, Toprol, Acetaminophen, Salbutamol, Dextromethorphan','Oracea, Toprol, Ibuprofen, Salmeterol, Dextromethorphan',
            'Cipro, Toprol, Ibuprofen, Salmeterol, Dextromethorphan','Levaquin, Toprol, Ibuprofen, Salbutamol, Dextromethorphan','Consult a Doctor',
            'Cipro, Toprol, Acetaminophen, Salbutamol, Dextromethorphan','Hydrocortisone, Dulcolax','Consult a Doctor','Prednisolone, Docusate Sodium',
            'Hydrocortisone, Calcium Polycarbophil','Fluocortolone, Dulcolax',
            'Fluocortolone, Docusate Sodium','Hydrocortisone, Bisacodyl','Consult a Doctor','Consult a Doctor','Hydrocortisone, Calcium Polycarbophil',
            'Consult a Doctor','Consult a Doctor','Consult a Doctor','Consult a Doctor','Consult a Doctor','Consult a Doctor','Consult a Doctor',
            'Consult a Doctor','Consult a Doctor','Consult a Doctor','Ultrasound-guided Sclerotherapy, Asclera, Carisoprodol','Radiofrequency Ablation, Sodium Tetradecyl Sulfate, Diltiazem',
            'Ambulatory Phlebectomy, Asclera, Carisoprodol','Ultrasound-guided sclerotherapy,sodium tetradecyl sulfate','Ambulatory Phlebectomy, Asclera, Diltiazem',
            'Varicose vein laser surgery, Sodium Tetradecyl Sulfate, Orphenadrine',
            'Ambulatory Phlebectomy, Sodium Tetradecyl Sulfate, Carisoprodol','Ultrasound-guided Sclerotherapy, Sodium Tetradecyl Sulfate, Diltiazem',
            'Varicose vein laser surgery, Asclera, Diltiazem','Varicose vein laser surgery, Sodium Tetradecyl Sulfate, Orphenadrine','Levothyroxine','Levothyroxine, initially have regular blood tests until the correct dose of levothyroxine is reached',
            'Levothyroxine','Levothyroxine','Levothyroxine','Levothyroxine','Levothyroxine',
            'Levothyroxine, initially have regular blood tests until the correct dose of levothyroxine is reached',
            'Levothyroxine','Levothyroxine','propylthiouracil, Imodium','methimazole,  Lactobacillus rhamnosus GG',
            'methimazole , imodium','propylthiouracil, acetaminophen','propylthiouracil','propylthiouracil',
            'methimazole','methimazole','Tapazole, Lactobacillus rhamnosus GG','Tapazole',
            'Thiazolidinediones, glucose','Alpha-glucosidase inhibitors','Metformin','Sulfonylureas',
            'Metformin, glucose','Alpha-glucosidase inhibitors','Metformin, glucose','Metformin',
            'Sulfonylureas','Alpha-glucosidase inhibitors','arthroscopy, Acetaminophen','Joint replacement, Acetaminophen',
            'Acetaminophen','NSAID','arthroscopy, Acetaminophen','NSAID, Acetaminophen','Analgesic, NSAID',
            'arthroscopy, Acetaminophen','Joint replacement, Acetaminophen','Joint replacement, Acetaminophen, arthroscopy',
            'Cortisone Decadron, Aristocort Celestone, Acetaminophen (surgery needed)','Delta-cortef Deltasone, Cinalone Depo-medrol, Acetaminophen','Prednisone (sometimes surgery needed)','Methylprednisolone, Acetaminophen',
            'Aristocort Celestone, surgery needed','Delta-cortef Deltasone, Cinalone Depo-medrol, Acetaminophen','Methylprednisolone, Acetaminophen',
            'Aristocort Celestone, surgery needed','Prednisone (sometimes surgery needed)',
            'Cortisone Decadron, Aristocort Celestone, Acetaminophen (surgery needed)','Epley Maneuver','Epley Maneuver',
            'Epley Maneuver','Epley Maneuver','Epley Maneuver','Epley Maneuver','Epley Maneuver','Epley Maneuver',
            'Epley Maneuver','Epley Maneuver','glycolic Acid cream 6%','tretinoin cream','benzoyl peroxide cream',
            'clindamycin phosphate gel USP','clindamycin phosphate gel USP','clindamycin phosphate gel USP','salicylic acid',
            'adapalene-benzoyl peroxide','clindamycin-benzoyl peroxide','tazarotene','Trimethoprim, consuming plenty of fluids',
            'sulfamethoxazole, Lorabid','Cephalexin, Amoxicillin','Nitrofurantoin, Rocephin',
            'Ceftriaxone, Keflex','Fosfomycin, lorabid, consuming plenty of water','Nitrofurantoin, Rocephin','sulfamethoxazole, Lorabid',
            'Trimethoprim, consuming plenty of fluids','Trimethoprim, consuming plenty of fluids','photodynamic therapy, triamcinolone, NSAID',
            'photodynamic therapy, triamcinolone, NSAID','photodynamic therapy, triamcinolone','triamcinolone, aspirin','photodynamic therapy, ibuprofen',
            'photodynamic therapy, triamcinolone','photodynamic therapy, ibuprofen','triamcinolone, aspirin','photodynamic therapy, triamcinolone, NSAID',
            'photodynamic therapy, triamcinolone, NSAID','antistaphylococcal, Amoxicillin','antistaphylococcal, Amoxicillin','amoxicillin, clavulanate',
            'cephalosporins, Cephalexin','macrolides, Dicloxacillin','Dicloxacillin','amoxicillin, Dicloxacillin','Cephalexin','antistaphylococcal, Amoxicillin',
            'antistaphylococcal, Amoxicillin','Magnesium hydroxide, Esomeprazole, Axid AR','Gaviscon, Lansoprazole, Pepcid AC','Gaviscon, Esomeprazole, Axid AR',
            'Magnesium hydroxide, Lansoprazole, Prilosec OTC','Gaviscon, Lansoprazole, Tagamet HB','Pepto-Bismol, Esomeprazole, Axid AR','Magnesium hydroxide, Lansoprazole, Tagamet HB',
            'Pepto-Bismol, Lansoprazole, Prilosec OTC','Pepto-Bismol, Esomeprazole, Pepcid AC','Magnesium hydroxide, Lansoprazole, Tagamet HB',
            'Metformin, Medroxyprogesterone', 'Statins, Medroxyprogesterone, Citalopram','Clomiphene, Medroxyprogesterone, Citalopram',
            'Metformin, Medroxyprogesterone','Clomiphene,Medroxyprogesterone','Statins, Medroxyprogesterone, Citalopram','Clomiphene, Medroxyprogesterone, Citalopram',
            'Metformin, Medroxyprogesterone','Statins, Medroxyprogesterone, Citalopram','Metformin, Medroxyprogesterone, Citalopram',
            'Midodrine, Dimenhydrinate, Meclizine hydrochloride','Fludrocortisone, Dimenhydrinate, Hydralyte','Fludrocortisone, Dimenhydrinate, Meclizine hydrochloride',
            'Midodrine, Dimenhydrinate, Hydralyte', 'Fludrocortisone, Dimenhydrinate, Meclizine hydrochloride','Fludrocortisone, Dimenhydrinate, Pedialyte',
            'Fludrocortisone, Dimenhydrinate, Meclizine hydrochloride','Midodrine, Dimenhydrinate, Meclizine hydrochloride','Fludrocortisone, Dimenhydrinate, Pedialyte',
            'Midodrine, Dimenhydrinate, Meclizine hydrochloride',
            'Lisinopril, Acetaminophen','Acetaminophen,Hydrochlorothiazide (HCTZ)','Acetaminophen,Hydrochlorothiazide (HCTZ)',
            'Lisinopril, Acetaminophen','Acetaminophen,Hydrochlorothiazide (HCTZ)','Acetaminophen,Hydrochlorothiazide (HCTZ)',
            'Acetaminophen,Hydrochlorothiazide (HCTZ)',
            'Acetaminophen,Hydrochlorothiazide (HCTZ)',
            'Lisinopril, Acetaminophen','Lisinopril, Acetaminophen',
            'Nitroimidazole Antibiotics, Dextromethorphan, Salbutamol, Chlorpheniramine, Toprol',
            'Quinolone Antibiotics, Dextromethorphan, Salbutamol, Chlorpheniramine, Toprol','Tetracycline Antibiotics, Dextromethorphan, Salmeterol, Chlorpheniramine, Toprol',
            'Tetracycline Antibiotics, Dextromethorphan, Salmeterol, Toprol',
            'Nitroimidazole Antibiotics, Dextromethorphan, Salbutamol, Chlorpheniramine','Macrolide Antibiotics, Dextromethorphan, Salbutamol',
            'Quinolone Antibiotics, Dextromethorphan, Salmeterol, Toprol','Cephalosporin Antibiotics, Dextromethorphan, Salbutamol, Toprol',
            'Cephalosporin Antibiotics, Dextromethorphan, Chlorpheniramine, Toprol','Macrolide Antibiotics, Dextromethorphan, Salmeterol, Chlorpheniramine']
print(len(medication))
doctor=['Dermatologist','Dermatologist','Dermatologist','Dermatologist','Dermatologist',
        'Dermatologist','Dermatologist','Dermatologist','Dermatologist','Dermatologist',
        'Allergists','Allergists','Allergists','Allergists','Allergists',
        'Allergists','Allergists','Allergists','Allergists','Allergists',
        'General Physician', 'General Physician', 'General Physician', 'General Physician', 'General Physician',
        'General Physician', 'General Physician', 'General Physician', 'General Physician', 'General Physician',
        'Gastroenteroligist/Hepatoligist ','Gastroenteroligist/Hepatoligist ','Gastroenteroligist/Hepatoligist ','Gastroenteroligist/Hepatoligist ','Gastroenteroligist/Hepatoligist ',
        'Gastroenteroligist/Hepatoligist ','Gastroenteroligist/Hepatoligist ','Gastroenteroligist/Hepatoligist ','Gastroenteroligist/Hepatoligist ','Gastroenteroligist/Hepatoligist ',
        'Allergists' ,'Allergists' ,'Allergists' ,'Allergists' ,'Allergists' ,
        'Allergists' ,'Allergists' ,'Allergists' ,'Allergists' ,'Allergists' ,
        'Gastroenterologist','Gastroenterologist','Gastroenterologist','Gastroenterologist','Gastroenterologist',
        'Gastroenterologist','Gastroenterologist','Gastroenterologist','Gastroenterologist','Gastroenterologist',
        'HIV specialist','HIV specialist','HIV specialist','HIV specialist','HIV specialist',
        'HIV specialist','HIV specialist','HIV specialist','HIV specialist','HIV specialist',
        'Endocrinologist' ,'Endocrinologist' ,'Endocrinologist' ,'Endocrinologist' ,'Endocrinologist' ,
        'Endocrinologist' ,'Endocrinologist' ,'Endocrinologist' ,'Endocrinologist' ,'Endocrinologist' ,
        ' Gastroenterologist' ,' Gastroenterologist' ,' Gastroenterologist' ,' Gastroenterologist' ,' Gastroenterologist' ,
        ' Gastroenterologist' ,' Gastroenterologist' ,' Gastroenterologist' ,' Gastroenterologist' ,' Gastroenterologist' ,
        'Allergist ' ,'Allergist ' ,'Allergist ' ,'Allergist ' ,'Allergist ' ,
        'Allergist ' ,'Allergist ' ,'Allergist ' ,'Allergist ' ,'Allergist ' ,
        'Cardiologist' ,'Cardiologist' ,'Cardiologist' ,'Cardiologist' ,'Cardiologist' ,
        'Cardiologist' ,'Cardiologist' ,'Cardiologist' ,'Cardiologist' ,'Cardiologist' ,
        'Neurologists' ,'Neurologists' ,'Neurologists' ,'Neurologists' ,'Neurologists' ,
        'Neurologists' ,'Neurologists' ,'Neurologists' ,'Neurologists' ,'Neurologists' ,
        'Psychologist/Neurologist/Orthopedic spinal surgeon/Urologist' , 'Psychologist/Neurologist/Orthopedic spinal surgeon/Urologist' , 'Psychologist/Neurologist/Orthopedic spinal surgeon/Urologist' , 'Psychologist/Neurologist/Orthopedic spinal surgeon/Urologist' , 'Psychologist/Neurologist/Orthopedic spinal surgeon/Urologist' ,
        'Psychologist/Neurologist/Orthopedic spinal surgeon/Urologist' , 'Psychologist/Neurologist/Orthopedic spinal surgeon/Urologist' , 'Psychologist/Neurologist/Orthopedic spinal surgeon/Urologist' , 'Psychologist/Neurologist/Orthopedic spinal surgeon/Urologist' , 'Psychologist/Neurologist/Orthopedic spinal surgeon/Urologist' ,
        'Neurologist' ,'Neurologist' ,'Neurologist' ,'Neurologist' ,'Neurologist' ,
        'Neurologist' ,'Neurologist' ,'Neurologist' ,'Neurologist' ,'Neurologist' ,
        ' Gastroenterologist' ,' Gastroenterologist' ,' Gastroenterologist' ,' Gastroenterologist' ,' Gastroenterologist' ,
        ' Gastroenterologist' ,' Gastroenterologist' ,' Gastroenterologist' ,' Gastroenterologist' ,' Gastroenterologist' ,
        'General physician' ,'General physician' ,'General physician' ,'General physician' ,'General physician' ,
        'General physician' ,'General physician' ,'General physician' ,'General physician' ,'General physician' ,
        'General physician' ,'General physician' ,'General physician' ,'General physician' ,'General physician' ,
        'General physician' ,'General physician' ,'General physician' ,'General physician' ,'General physician' ,
        'General physician' ,'General physician' ,'General physician' ,'General physician' ,'General physician' ,
        'General physician' ,'General physician' ,'General physician' ,'General physician' ,'General physician' ,
        'General physician','General physician' ,'General physician' ,'General physician' ,'General physician' ,
        'General physician' ,'General physician' ,'General physician' ,'General physician' ,'General physician' ,
        'Hepatologist' ,'Hepatologist' ,'Hepatologist' ,'Hepatologist' ,'Hepatologist' ,
        'Hepatologist' ,'Hepatologist' ,'Hepatologist' ,'Hepatologist' ,'Hepatologist' ,
        'Hepatologist' ,'Hepatologist' ,'Hepatologist' ,'Hepatologist' ,'Hepatologist' ,
        'Hepatologist' ,'Hepatologist' ,'Hepatologist' ,'Hepatologist' ,'Hepatologist' ,
        'Hepatologist','Hepatologist' ,'Hepatologist' ,'Hepatologist' ,'Hepatologist' ,
        'Hepatologist' ,'Hepatologist' ,'Hepatologist' ,'Hepatologist' ,'Hepatologist' ,
        'Hepatologist' ,'Hepatologist' ,'Hepatologist' ,'Hepatologist' ,'Hepatologist' ,
        'Hepatologist' ,'Hepatologist' ,'Hepatologist' ,'Hepatologist' ,'Hepatologist' ,
        'Hepatologist' ,'Hepatologist' ,'Hepatologist' ,'Hepatologist' ,'Hepatologist' ,
        'Hepatologist' ,'Hepatologist' ,'Hepatologist' ,'Hepatologist' ,'Hepatologist' ,
        'Hepatologist' ,'Hepatologist' ,'Hepatologist' ,'Hepatologist' ,'Hepatologist' ,
        'Hepatologist' ,'Hepatologist' ,'Hepatologist' ,'Hepatologist' ,'Hepatologist' ,
        'Pulmonologist' ,'Pulmonologist' ,'Pulmonologist' ,'Pulmonologist' ,'Pulmonologist' ,
        'Pulmonologist' ,'Pulmonologist' ,'Pulmonologist' ,'Pulmonologist' ,'Pulmonologist' ,
        'General physician','General physician','General physician','General physician','General physician',
        'General physician','General physician','General physician','General physician','General physician',
        'Pulmonologist' ,'Pulmonologist' ,'Pulmonologist' ,'Pulmonologist' ,'Pulmonologist' ,
        'Pulmonologist' ,'Pulmonologist' ,'Pulmonologist' ,'Pulmonologist' ,'Pulmonologist' ,
        'Proctologist' ,'Proctologist' ,'Proctologist' ,'Proctologist' ,'Proctologist' ,
        'Proctologist' ,'Proctologist' ,'Proctologist' ,'Proctologist' ,'Proctologist' ,
        'Cardiologist' ,'Cardiologist' ,'Cardiologist' ,'Cardiologist' ,'Cardiologist' ,
        'Cardiologist' ,'Cardiologist' ,'Cardiologist' ,'Cardiologist' ,'Cardiologist' ,
        'Phlebologist/Dermatology surgeon' ,'Phlebologist/Dermatology surgeon' ,'Phlebologist/Dermatology surgeon' ,'Phlebologist/Dermatology surgeon' ,'Phlebologist/Dermatology surgeon' ,
        'Phlebologist/Dermatology surgeon' ,'Phlebologist/Dermatology surgeon' ,'Phlebologist/Dermatology surgeon' ,'Phlebologist/Dermatology surgeon' ,'Phlebologist/Dermatology surgeon' ,
        'Endocrinologist' ,'Endocrinologist' ,'Endocrinologist' ,'Endocrinologist' ,'Endocrinologist' ,
        'Endocrinologist' ,'Endocrinologist' ,'Endocrinologist' ,'Endocrinologist' ,'Endocrinologist' ,
        'Endocrinologist' ,'Endocrinologist' ,'Endocrinologist' ,'Endocrinologist' ,'Endocrinologist' ,
        'Endocrinologist' ,'Endocrinologist' ,'Endocrinologist' ,'Endocrinologist' ,'Endocrinologist' ,
        'Endocrinologist' ,'Endocrinologist' ,'Endocrinologist' ,'Endocrinologist' ,'Endocrinologist' ,
        'Endocrinologist' ,'Endocrinologist' ,'Endocrinologist' ,'Endocrinologist' ,'Endocrinologist' ,
        'Orthopedists' ,'Orthopedists' ,'Orthopedists' ,'Orthopedists' ,'Orthopedists' ,
        'Orthopedists' ,'Orthopedists' ,'Orthopedists' ,'Orthopedists' ,'Orthopedists' ,
        'Rheumatologists' ,'Rheumatologists' ,'Rheumatologists' ,'Rheumatologists' ,'Rheumatologists' ,
        'Rheumatologists' ,'Rheumatologists' ,'Rheumatologists' ,'Rheumatologists' ,'Rheumatologists' ,
        'neurologist' ,'neurologist' ,'neurologist' ,'neurologist' ,'neurologist' ,
        'neurologist' ,'neurologist' ,'neurologist' ,'neurologist' ,'neurologist' ,
        'Dermatologist' ,'Dermatologist' ,'Dermatologist' ,'Dermatologist' ,'Dermatologist' ,
        'Dermatologist' ,'Dermatologist' ,'Dermatologist' ,'Dermatologist' ,'Dermatologist' ,
        'Urologist/Nephrologist' ,'Urologist/Nephrologist' ,'Urologist/Nephrologist' ,'Urologist/Nephrologist' ,'Urologist/Nephrologist' ,
        'Urologist/Nephrologist' ,'Urologist/Nephrologist' ,'Urologist/Nephrologist' ,'Urologist/Nephrologist' ,'Urologist/Nephrologist' ,
        'Dermatologist' ,'Dermatologist' ,'Dermatologist' ,'Dermatologist' ,'Dermatologist' ,
        'Dermatologist' ,'Dermatologist' ,'Dermatologist' ,'Dermatologist' ,'Dermatologist' ,
        'Dermatologist' ,'Dermatologist' ,'Dermatologist' ,'Dermatologist' ,'Dermatologist' ,
        'Dermatologist' ,'Dermatologist' ,'Dermatologist' ,'Dermatologist' ,'Dermatologist' ,
        'Gastroenterologist/ENT' , 'Gastroenterologist/ENT' , 'Gastroenterologist/ENT' , 'Gastroenterologist/ENT' , 'Gastroenterologist/ENT' ,
        'Gastroenterologist/ENT' , 'Gastroenterologist/ENT' , 'Gastroenterologist/ENT' , 'Gastroenterologist/ENT' , 'Gastroenterologist/ENT' ,
        'Obstetrician/Gynecologists' , 'Obstetrician/Gynecologists' , 'Obstetrician/Gynecologists' , 'Obstetrician/Gynecologists' , 'Obstetrician/Gynecologists' ,
        'Obstetrician/Gynecologists' , 'Obstetrician/Gynecologists' , 'Obstetrician/Gynecologists' , 'Obstetrician/Gynecologists' , 'Obstetrician/Gynecologists' ,
        'General Physician' , 'General physician','General physician','General physician','General physician',
        'General physician','General physician','General physician','General physician','General physician',
        'General Physician' , 'General physician','General physician','General physician','General physician',
        'General physician','General physician','General physician','General physician','General physician',
        'Pulmonologist','Pulmonologist','Pulmonologist','Pulmonologist','Pulmonologist',
        'Pulmonologist','Pulmonologist','Pulmonologist','Pulmonologist','Pulmonologist']
print (len(doctor))
l2=[]
for x in range(0,len(l1)):
    l2.append(0)
l3=[]
for x in range(0,len(l1)):
    l3.append(0)

# TESTING DATA df -------------------------------------------------------------------------------------
df=pd.read_csv("Training.csv")

df.replace({'prognosis':{'Fungal infection':0,'Allergy':1,'SARS-CoV-2 (Covid-19)':2,'Chronic cholestasis':3,'Drug Reaction':4,
'Peptic ulcer diseae':5,'AIDS':6,'Diabetes ':7,'Gastroenteritis':8,'Bronchial Asthma':9,'Hypertension ':10,
'Migraine':11,'Cervical spondylosis':12,
'Paralysis (brain hemorrhage)':13,'Jaundice':14,'Malaria':15,'Chicken pox':16,'Dengue':17,'Typhoid':18,'hepatitis A':19,
'Hepatitis B':20,'Hepatitis C':21,'Hepatitis D':22,'Hepatitis E':23,'Alcoholic hepatitis':24,'Tuberculosis':25,
'Common Cold':26,'Pneumonia':27,'Dimorphic hemmorhoids(piles)':28,'Heart attack':29,'Varicose veins':30,'Hypothyroidism':31,
'Hyperthyroidism':32,'Hypoglycemia':33,'Osteoarthristis':34,'Arthritis':35,
'(vertigo) Paroymsal  Positional Vertigo':36,'Acne':37,'Urinary tract infection':38,'Psoriasis':39,
'Impetigo':40,'GERD':41,'Polycystic ovary syndrome (PCOS)':42,'Low Blood Pressure':43,
'High Blood Pressure':44,'Chronic lower respiratory system':45}},inplace=True)

# print(df.head())

X= df[l1]

y = df[["prognosis"]]
np.ravel(y)
#print(y)
me=pd.read_csv("training1.csv")
me.replace({'medication':{'radiation therapy and ultraviolet therapy':0,'Terbinafine hydrochloride cream, ultraviolet therapy, ketoconazole cream':1,
                          'Miconazole Nitrate Gel':2,'Terbinafine hydrochloride, Miconazole Nitrate Gel':3,'Clotrimazole, miconazole':4,
                          'Miconazole Nitrate Gel, ketoconazole':5,
                          'amphotericin, radiation therapy':6,'Terbinafine hydrochloride, Miconazole Nitrate Gel':7,'econazole':8,
                          'radiation therapy and ultraviolet therapy':9,
                          'Antihistamines, aspirin':10,'Decongentants, antihistamines':11,'Acetaminophen, polyethylene glycol & ophthalmic':12,
                          'Zyrtec, nasal spray':13,'Antihistamines, Decongentants':14,
                          'Antihistamines, Decongentants':15,'Acetaminophen, polyethylene glycol & ophthalmic':16,'Zyrtec, nasal spray':17,
                          'Antihistamines, Decongentants':18,'Antihistamines, aspirin':19,
                          'Paracetamol,Favipiravis, acebrophyltine & Acetyleystrne, ascorbic acid, zinc acetate':20,'Favipiravis, acebrophyltine & Acetyleystrne, paracetamol, ascorbic acid, zinc acetate':21,
            'Paracetamol,Grilinctus, ivermectin, azithromycin, ascorbic acid, zinc acetate':22,'Paracetamol,Methylprednisolone, Favipiravis, ascorbic acid, zinc acetate':23,
            'Grilinctus, ivermectin, azithromycin, ascorbic acid, zinc acetate':24,'Grilinctus, ivermectin, azithromycin, ascorbic acid, zinc acetate':25,'Azithromycin, ivermectin, ascorbic acid, zinc acetate':26,
            'Ivermectin, paracetamol, ascorbic acid, zinc acetate':27,'Paracetamol,Grilinctus, Favipiravis, Methylprednisolone, ascorbic acid':28,'Ivermectin, ascorbic acid, zinc acetate':29,                          
                          'Not curable':30,'Not curable':31,'Not curable':32,'Not curable':33,'Not curable':34,'Not curable':35,'Not curable':36,
                          'Not curable':37,'Not curable':38,
                          'Not curable':39,'Antihistamines, change medication':40,'Corticosteroids, change medication':41,
                          'Bronchodilators, change medication':42,'Bronchodilators, change medication':43,
                          'Antihistamines':44,'Corticosteroids, change medication':45,'Antihistamines, change medication':46,
                          'Bronchodilators, change medication':47,'Bronchodilators, change medication':48,
                          'Antihistamines':49,'panloprozole, penicillium':50,'panloprozole, Omeprazole':51,
                          'amoxicillin, tinidazole':52,'tetracycline and levofloxacin':53,'Lansoprazole':54,
                          'amoxicillin, tinidazole':55,'tetracycline and levofloxacin':56,'panloprozole, penicillium':57,
                          'panloprozole, penicillium':58,'panloprozole, penicillium, Lansoprazole':59,'Not curable':60,
                          'Not curable':61,'Not curable':62,'Not curable':63,'Not curable':64,'Not curable':65,
                          'Not curable':66,'Not curable':67,'Not curable':68,'Not curable':69,'Blood Diagnosis required':70,
                          'Blood Diagnosis required':71,'Blood Diagnosis required':72,'Blood Diagnosis required':73,
                          'Blood Diagnosis required':74,'Blood Diagnosis required':75,'Blood Diagnosis required':76,'Blood Diagnosis required':77,
                          'Blood Diagnosis required':78,
                          'Blood Diagnosis required':79,'Loperamide, ondansetron':80,'Loperamide, ondansetron':81,'plenty of water, Loperamide':82,
                          'Loperamide, ondansetron':83,'plenty of water, ondansetron':84,
                          'Self healing, plenty of fluids':85,'Loperamide, ondansetron':86,'plenty of water, Loperamide':87,'Loperamide, ondansetron':88,
                          'plenty of water, ondansetron':89,
                          'Predncrone, Bronchodilators, NSAID':90,'Bronchodilators, NSAID':91,'NSAID, Bronchodilators':92,'Bronchodilators':93,
                          'Bronchodilators':94,'NSAID':95,'Bronchodilators, NSAID':96,
                          'Predncrone, Bronchodilators, NSAID':97,'Bronchodilators, NSAID':98,'NSAID, Bronchodilators':99,'Lisinopril, Acetaminophen':100,
                          'Hydrochlorothiazide, Aspirin':101,'Amlodipine besylate, Meclizine':102,'Amlodipine besylate, Acetaminophen':103,
                          'Hydrochlorothiazide, Adderall':104,
                          'Lisinopril, Dimenhydrinate':105,'Amlodipine besylate,Ritalin':106,'Lisinopril, Gentamicin':107,
                          'Acetaminophen,Hydrochlorothiazide (HCTZ)':108,'Hydrochlorothiazide,Acetaminophen':109,
                          'Ibuprofen, Dexlansoprazole, Acetaminophen':110,'Ibuprofen, Acetaminophen':111,
                          'Naproxen, Dexlansoprazole, Acetaminophen':112,'Ibuprofen, Dexlansoprazole, Acetaminophen':113,
                          'Ibuprofen, Dexlansoprazole, Acetaminophen':114,
                          'Naproxen, Dexlansoprazole, Acetaminophen':115,'Ibuprofen, Dexlansoprazole, Acetaminophen':116,
                          'Ibuprofen, Dexlansoprazole, Naproxen':117,
                          'Ibuprofen, Dexlansoprazole, Acetaminophen':118,'Naproxen, Dexlansoprazole, Acetaminophen':119,
                          'Indomethacin, Dimenhydrinate, Gabapentin':120,
                          'Oral Prednisone, Meclizine':121,'Cyclobenzaprine, Dimenhydrinate, Gabapentin':122,'Indomethacin, Meclizine, Gentamicin':123,
                          'Oral Prednisone, Pregabalin':124,
                          'Oral Prednisone, Pregabalin, Gabapentin':125,'Cyclobenzaprine, Meclizine':126,'Indomethacin, Dimenhydrinate':127,
                          'Oral Prednisone, Meclizine, Gentamicin':128,
                          'Indomethacin, Dimenhydrinate, Gabapentin':129,'Consult a Doctor':130,'Consult a Doctor':131,'Consult a Doctor':132,
                          'Consult a Doctor':133,'Consult a Doctor':134,
                          'Consult a Doctor':135,'Consult a Doctor':136,
                          'Consult a Doctor':137,'Consult a Doctor':138,'Consult a Doctor':139,'Consult a Doctor':140,'Consult a Doctor':141,
                          'Consult a Doctor':142,'Acetaminophen, Eszopiclone':143,
                          'Consult a Doctor':144,'Acetaminophen, Eszopiclone':145,'Acetaminophen, Meclizine Hydrochloride, Eszopiclone':146,
                          'Acetaminophen, Meclizine Hydrochloride, Eszopiclone':147,
                          'Acetaminophen, Meclizine Hydrochloride, Eszopiclone':148,'Consult a Doctor':149,'Atovaquone-Proguanil, Aspirin, Loperamide':150,
                          'Primaquine Phosphate, Aspirin, Meclizine Hydrochloride':151,
                          'Quinine sulfate with Doxycycline, Aspirin, Ibuprofen':152,'Quinine sulfate with Doxycycline, Aspirin, Ibuprofen':153,
                          'Consult a Doctor':154,
                          'Atovaquone-Proguanil, Aspirin, Loperamide':155,'Consult a Doctor':156,'Quinine sulfate with Doxycycline, Aspirin, Meclizine Hydrochloride':157,
                          'Consult a Doctor':158,'Primaquine Phosphate, Aspirin':159,
                          'Acyclovir, Hydroxyzine Pamoate, Acetaminophen':160,'acyclovir,acetaminophen,Eszopiclone':161,'Acyclovir, Hydroxyzine Pamoate, Acetaminophen':162,
                          'Acyclovir, Hydroxyzine Pamoate, Naproxen':163,
                          'Acyclovir, Hydroxyzine Pamoate, Ibuprofen':164,'Acyclovir, Hydroxyzine Pamoate, Ibuprofen':165,
                          'Acyclovir, Hydroxyzine Pamoate, Naproxen':166,'Acyclovir, Hydroxyzine Pamoate, Acetaminophen':167,
                          'Acyclovir, Hydroxyzine Pamoate, Acetaminophen':168,'Acyclovir, Hydroxyzine Pamoate, Naproxen':169,
                          'Acetaminophen, Meclizine Hydrochloride, Hydrocortisone':170,'Ibuprofen, Meclizine Hydrochloride':171,
                          'Acetaminophen, Meclizine Hydrochloride, Eszopiclone':172,'Ibuprofen, Meclizine hydrochloride, Hydrocortisone':173,
                          'Ibuprofen, Meclizine hydrochloride, Hydrocortisone':174,
                          'Naproxen, Hydrocortisone, Aspirin':175,'Acetaminophen, Hydrocortisone, Aspirin':176,'Ibuprofen, Eszopiclone, Aspirin':177,
                          'Naproxen, Hydrocortisone, Eszopiclone':178,'Acetaminophen, Hydrocortisone, Eszopiclone':179,
                          'Ciprofloxacin, Linaclotide, Acetaminophen':180,'Azithromycin, Linaclotide, Acetaminophen':181,
                          'Ceftriaxone, Meclizine hydrochloride, Ibuprofen':182,'Ciprofloxacin, Ibuprofen, Eszopiclone':183,
                          'Azithromycin, Linaclotide, Acetaminophen':184,'Ciprofloxacin, Ibuprofen, Eszopiclone':185,'Ceftriaxone, Linaclotide, Naproxen':186,
                          'Azithromycin, Linaclotide, Acetaminophen':187,'Ciprofloxaci , Linaclotide, Naproxen':188,
                          'Azithromycin, Linaclotide, Acetaminophen':189,'acetaminophen,Meclizine hydrochloride':190,'Ibuprofen, Promethazine':191,
                          'Ibuprofen, Meclizine Hydrochloride':192,
                          'Naproxen, Pepto-Bismol':193,'Naproxen, Meclizine hydrochloride':194,'Acetaminophen, Pepto-Bismol':195,
                          'acetaminophen,Pepto-Bismol':196,'Ibuprofen, Meclizine Hydrochloride':197,'Naproxen, Promethazine':198,
                          'Acetaminophen, Pepto-Bismol':199,'Consult a Doctor':200,
                          'Consult a Doctor':201,'Consult a Doctor':202,'Consult a Doctor':203,'Consult a Doctor':204,
                          'Consult a Doctor':205,'Consult a Doctor':206,
                          'Consult a Doctor':207,'Consult a Doctor':208,'Consult a Doctor':209,'Consult a Doctor':210,
                          'Consult a Doctor':211,'Consult a Doctor':212,
                          'Consult a Doctor':213,'Consult a Doctor':214,'Consult a Doctor':215,'Consult a Doctor':216,
                          'Consult a Doctor':217,'Consult a Doctor':218,'Consult a Doctor':219,'Consult a Doctor':220,'Consult a Doctor':221,

                          'Consult a Doctor':222,'Consult a Doctor':223,
                          'Consult a Doctor':224,'Consult a Doctor':225,'Consult a Doctor':226,'Consult a Doctor':227,'Consult a Doctor':228,
                          'Consult a Doctor':229,'Consult a Doctor':230,
                          'Consult a Doctor':231,'Consult a Doctor':232,'Consult a Doctor':233,'Consult a Doctor':234,'Consult a Doctor':235,
                          'Consult a Doctor':236,'Consult a Doctor':237,
                          'Consult a Doctor':238,
                          'Consult a Doctor':239,'Corticosteroids, Atorvastatin, Simethicone':240,'Atorvastatin, Oxandrolone, Simethicone':241,
                          'Atorvastatin, Oxandrolone, Simethicone':242,
                          'Corticosteroids, Atorvastatin, Loperamide':243,'Atorvastatin, Oxandrolone, Simethicone':244,
                          'Corticosteroids, Atorvastatin, Loperamide':245,
                          'Atorvastatin, Oxandrolone, Simethicone':246,'Corticosteroids, Atorvastatin, Loperamide':247,
                          'Corticosteroids, Atorvastatin, Loperamide':248,
                          'Atorvastatin, Oxandrolone, Simethicone':249,'Isoniazid, Oseltamivir, Salmeterol, Dextromethorphan, Acetaminophen':250,
                          'Rifampicin, Iced saline, Salbutamol, Dextromethorphan, Ibuprofen':251,
                          'Isoniazid, Iced saline, Salmeterol, Dextromethorphan, Acetaminophen':252,'Rifampicin, Oseltamivir, Salbutamol, Dextromethorphan, Ibuprofen':253,
                          'Pyrazinamide, Iced saline, Salmeterol, Dextromethorphan, Ibuprofen':254,
                          'Pyrazinamide,oseltamivir,salmeterol,Dextromethorphan,acetaminophen,':255,
                          'Isoniazid, Iced saline, Salbutamol, Acetaminophen':256,'Pyrazinamide, Iced saline, Salmeterol, Dextromethorphan, Ibuprofen':257,
                          'Rifampicin, Oseltamivir, Salbutamol, Dextromethorphan, Ibuprofen':258,'Isoniazid, Iced saline, Salmeterol, Dextromethorphan, Acetaminophen,':259,
                          'Oxymetazoline Nasal, Cetirizine':260,'Phenylephrine Nasal, Cetirizine':261,'Phenylephrine Oral':262,'Oxymetazoline Nasal, Cetirizine':263,
                          'Phenylephrine Nasal, Cetirizine':264,'Phenylephrine Nasal, Cetirizine':265,'Phenylephrine Oral, Cetirizine':266,
                          'Oxymetazoline Nasal, Cetirizine':267,
                          'Phenylephrine Nasal, Cetirizine':268,'Oxymetazoline Nasal, Cetirizine':269,'Consult a Doctor':270,'Oracea, Toprol, Acetaminophen, Salbutamol, Dextromethorphan':271,
                          'Consult a Doctor':272,'Levaquin, Toprol, Ibuprofen, Salmeterol, Dextromethorphan':273,'Levaquin, Toprol, Acetaminophen, Salbutamol, Dextromethorphan':274,'Oracea, Toprol, Ibuprofen, Salmeterol, Dextromethorphan':275,
                          'Cipro, Toprol, Ibuprofen, Salmeterol, Dextromethorphan':276,'Levaquin, Toprol, Ibuprofen, Salbutamol, Dextromethorphan':277,
                          'Consult a Doctor':278,
                          'Cipro, Toprol, Acetaminophen, Salbutamol, Dextromethorphan':279,'Hydrocortisone, Dulcolax':280,'Consult a Doctor':281,
                          'Prednisolone, Docusate Sodium':282,
                          'Hydrocortisone, Calcium Polycarbophil':283,'Fluocortolone, Dulcolax':286,
                          'Fluocortolone, Docusate Sodium':285,'Hydrocortisone, Bisacodyl':286,'Consult a Doctor':287,'Consult a Doctor':288,'Hydrocortisone, Calcium Polycarbophil':289,
                          'Consult a Doctor':290,'Consult a Doctor':291,'Consult a Doctor':292,'Consult a Doctor':293,'Consult a Doctor':294,'Consult a Doctor':295,'Consult a Doctor':296,
                          'Consult a Doctor':297,'Consult a Doctor':298,'Consult a Doctor':299,'Ultrasound-guided Sclerotherapy, Asclera, Carisoprodol':300,
                          'Radiofrequency Ablation, Sodium Tetradecyl Sulfate, Diltiazem':301,
                          'Ambulatory Phlebectomy, Asclera, Carisoprodol':302,'Ultrasound-guided sclerotherapy,sodium tetradecyl sulfate':303,
                          'Ambulatory Phlebectomy, Asclera, Diltiazem':304,
                          'Varicose vein laser surgery, Sodium Tetradecyl Sulfate, Orphenadrine':305,
                          'Ambulatory Phlebectomy, Sodium Tetradecyl Sulfate, Carisoprodol':306,'Ultrasound-guided Sclerotherapy, Sodium Tetradecyl Sulfate, Diltiazem':307,
                          'Varicose vein laser surgery, Asclera, Diltiazem':308,'Varicose vein laser surgery, Sodium Tetradecyl Sulfate, Orphenadrine':309,'Levothyroxine':310,'Levothyroxine, initially have regular blood tests until the correct dose of levothyroxine is reached':311,
                          'Levothyroxine':312,'Levothyroxine':313,'Levothyroxine':314,'Levothyroxine':315,'Levothyroxine':316,
                          'Levothyroxine, initially have regular blood tests until the correct dose of levothyroxine is reached':317,
                          'Levothyroxine':318,'Levothyroxine':319,'propylthiouracil, Imodium':320,'methimazole,  Lactobacillus rhamnosus GG':321,
                          'methimazole , imodium':322,'propylthiouracil, acetaminophen':323,'propylthiouracil':324,'propylthiouracil':325,
                          'methimazole':326,'methimazole':327,'Tapazole, Lactobacillus rhamnosus GG':328,'Tapazole':329,
                          'Thiazolidinediones, glucose':330,'Alpha-glucosidase inhibitors':331,'Metformin':332,'Sulfonylureas':333,
                          'Metformin, glucose':334,'Alpha-glucosidase inhibitors':335,'Metformin, glucose':336,'Metformin':337,
                          'Sulfonylureas':338,'Alpha-glucosidase inhibitors':339,'arthroscopy, Acetaminophen':340,'Joint replacement, Acetaminophen':341,
                          'Acetaminophen':342,'NSAID':343,'arthroscopy, Acetaminophen':344,'NSAID, Acetaminophen':345,'Analgesic, NSAID':346,
                          'arthroscopy, Acetaminophen':347,'Joint replacement, Acetaminophen':348,'Joint replacement, Acetaminophen, arthroscopy':349,
                          'Cortisone Decadron, Aristocort Celestone, Acetaminophen (surgery needed)':350,'Delta-cortef Deltasone, Cinalone Depo-medrol, Acetaminophen':351,'Prednisone (sometimes surgery needed)':352,'Methylprednisolone, Acetaminophen':353,
                          'Aristocort Celestone, surgery needed':354,'Delta-cortef Deltasone, Cinalone Depo-medrol, Acetaminophen':355,
                          'Methylprednisolone, Acetaminophen':356,
                          'Aristocort Celestone, surgery needed':357,'Prednisone (sometimes surgery needed)':358,
                          'Cortisone Decadron, Aristocort Celestone, Acetaminophen (surgery needed)':359,'Epley Maneuver':360,'Epley Maneuver':361,
                          'Epley Maneuver':362,'Epley Maneuver':363,'Epley Maneuver':364,'Epley Maneuver':365,'Epley Maneuver':366,'Epley Maneuver':367,
                          'Epley Maneuver':368,'Epley Maneuver':369,'glycolic Acid cream 6%':370,'tretinoin cream':371,'benzoyl peroxide cream':372,
                          'clindamycin phosphate gel USP':373,'clindamycin phosphate gel USP':374,'clindamycin phosphate gel USP':375,'salicylic acid':376,
                          'adapalene-benzoyl peroxide':377,'clindamycin-benzoyl peroxide':378,'tazarotene':379,'Trimethoprim, consuming plenty of fluids':380,
                          'sulfamethoxazole, Lorabid':381,'Cephalexin, Amoxicillin':382,'Nitrofurantoin, Rocephin':383,
                          'Ceftriaxone, Keflex':384,'Fosfomycin, lorabid, consuming plenty of water':385,'Nitrofurantoin, Rocephin':386,
                          'sulfamethoxazole, Lorabid':387,
                          'Trimethoprim, consuming plenty of fluids':388,'Trimethoprim, consuming plenty of fluids':389,
                          'photodynamic therapy, triamcinolone, NSAID':390,
                          'photodynamic therapy, triamcinolone, NSAID':391,'photodynamic therapy, triamcinolone':392,'triamcinolone, aspirin':393,
                          'photodynamic therapy, ibuprofen':394,
                          'photodynamic therapy, triamcinolone':395,'photodynamic therapy, ibuprofen':398,'triamcinolone, aspirin':397,
                          'photodynamic therapy, triamcinolone, NSAID':398,
                          'photodynamic therapy, triamcinolone, NSAID':399,'antistaphylococcal, Amoxicillin':400,'antistaphylococcal, Amoxicillin':401,
                          'amoxicillin, clavulanate':402,
                          'cephalosporins, Cephalexin':403,'macrolides, Dicloxacillin':404,'Dicloxacillin':405,'amoxicillin, Dicloxacillin':406,'Cephalexin':407,
                          'antistaphylococcal, Amoxicillin':408,
                          'antistaphylococcal, Amoxicillin':409,'Magnesium hydroxide, Esomeprazole, Axid AR':410,'Gaviscon, Lansoprazole, Pepcid AC':411,
                          'Gaviscon, Esomeprazole, Axid AR':412,
                          'Magnesium hydroxide, Lansoprazole, Prilosec OTC':413,'Gaviscon, Lansoprazole, Tagamet HB':414,'Pepto-Bismol, Esomeprazole, Axid AR':415,
                          'Magnesium hydroxide, Lansoprazole, Tagamet HB':416,
                          'Pepto-Bismol, Lansoprazole, Prilosec OTC':417,'Pepto-Bismol, Esomeprazole, Pepcid AC':418,
                          'Magnesium hydroxide, Lansoprazole, Tagamet HB':419,
                          'Metformin, Medroxyprogesterone':420, 'Statins, Medroxyprogesterone, Citalopram':421,'Clomiphene, Medroxyprogesterone, Citalopram':422,
                          'Metformin, Medroxyprogesterone':423,'Clomiphene,Medroxyprogesterone':424,'Statins, Medroxyprogesterone, Citalopram':425,
                          'Clomiphene, Medroxyprogesterone, Citalopram':426,
                          'Metformin, Medroxyprogesterone':427,'Statins, Medroxyprogesterone, Citalopram':428,'Metformin, Medroxyprogesterone, Citalopram':429,
                          'Midodrine, Dimenhydrinate, Meclizine hydrochloride':430,'Fludrocortisone, Dimenhydrinate, Hydralyte':431,
                          'Fludrocortisone, Dimenhydrinate, Meclizine hydrochloride':432,
                          'Midodrine, Dimenhydrinate, Hydralyte':433, 'Fludrocortisone, Dimenhydrinate, Meclizine hydrochloride':434,
                          'Fludrocortisone, Dimenhydrinate, Pedialyte':435,
                          'Fludrocortisone, Dimenhydrinate, Meclizine hydrochloride':436,'Midodrine, Dimenhydrinate, Meclizine hydrochloride':437,'Fludrocortisone, Dimenhydrinate, Pedialyte':438,
                          'Midodrine, Dimenhydrinate, Meclizine hydrochloride':439,
                          'Lisinopril, Acetaminophen':440,'Acetaminophen,Hydrochlorothiazide (HCTZ)':441,'Acetaminophen,Hydrochlorothiazide (HCTZ)':442,
                          'Lisinopril, Acetaminophen':443,'Acetaminophen,Hydrochlorothiazide (HCTZ)':444,'Acetaminophen,Hydrochlorothiazide (HCTZ)':445,
                          'Acetaminophen,Hydrochlorothiazide (HCTZ)':446,
                          'Acetaminophen,Hydrochlorothiazide (HCTZ)':447,
                          'Lisinopril, Acetaminophen':448,'Lisinopril, Acetaminophen':449,
                          'Nitroimidazole Antibiotics, Dextromethorphan, Salbutamol, Chlorpheniramine, Toprol':450,
                          'Quinolone Antibiotics, Dextromethorphan, Salbutamol, Chlorpheniramine, Toprol':451,
                          'Tetracycline Antibiotics, Dextromethorphan, Salmeterol, Chlorpheniramine, Toprol':452,
                          'Tetracycline Antibiotics, Dextromethorphan, Salmeterol, Toprol':453,
                          'Nitroimidazole Antibiotics, Dextromethorphan, Salbutamol, Chlorpheniramine':454,
                          'Macrolide Antibiotics, Dextromethorphan, Salbutamol':455,
                          'Quinolone Antibiotics, Dextromethorphan, Salmeterol, Toprol':456,
                          'Cephalosporin Antibiotics, Dextromethorphan, Salbutamol, Toprol':457,
                          'Cephalosporin Antibiotics, Dextromethorphan, Chlorpheniramine, Toprol':458,
                          'Macrolide Antibiotics, Dextromethorphan, Salmeterol, Chlorpheniramine':459}},inplace=True)
X1=me[l1]
z = me[["medication"]]
np.ravel(z)
#print(z)


# TRAINING DATA tr --------------------------------------------------------------------------------
tr=pd.read_csv("Testing.csv")
tr.replace({'prognosis':{'Fungal infection':0,'Allergy':1,'SARS-CoV-2 (Covid-19)':2,'Chronic cholestasis':3,'Drug Reaction':4,
'Peptic ulcer diseae':5,'AIDS':6,'Diabetes ':7,'Gastroenteritis':8,'Bronchial Asthma':9,'Hypertension ':10,
'Migraine':11,'Cervical spondylosis':12,
'Paralysis (brain hemorrhage)':13,'Jaundice':14,'Malaria':15,'Chicken pox':16,'Dengue':17,'Typhoid':18,'hepatitis A':19,
'Hepatitis B':20,'Hepatitis C':21,'Hepatitis D':22,'Hepatitis E':23,'Alcoholic hepatitis':24,'Tuberculosis':25,
'Common Cold':26,'Pneumonia':27,'Dimorphic hemmorhoids(piles)':28,'Heart attack':29,'Varicose veins':30,'Hypothyroidism':31,
'Hyperthyroidism':32,'Hypoglycemia':33,'Osteoarthristis':34,'Arthritis':35,
'(vertigo) Paroymsal  Positional Vertigo':36,'Acne':37,'Urinary tract infection':38,'Psoriasis':39,
'Impetigo':40,'GERD':41,'Polycystic ovary syndrome (PCOS)':42,'Low Blood Pressure':43,
'High Blood Pressure':44,'Chronic lower respiratory system':45}},inplace=True)

X_test= tr[l1]
y_test = tr[["prognosis"]]
np.ravel(y_test)

#print(y_test)
ne=pd.read_csv("testing1.csv")

ne.replace({'medication':{'radiation therapy and ultraviolet therapy':0,'Terbinafine hydrochloride cream, ultraviolet therapy, ketoconazole cream':1,
                          'Miconazole Nitrate Gel':2,'Terbinafine hydrochloride, Miconazole Nitrate Gel':3,'Clotrimazole, miconazole':4,'Miconazole Nitrate Gel, ketoconazole':5,
                          'amphotericin, radiation therapy':6,'Terbinafine hydrochloride, Miconazole Nitrate Gel':7,'econazole':8,'radiation therapy and ultraviolet therapy':9,
                          'Antihistamines, aspirin':10,'Decongentants, antihistamines':11,'Acetaminophen, polyethylene glycol & ophthalmic':12,'Zyrtec, nasal spray':13,'Antihistamines, Decongentants':14,
                          'Antihistamines, Decongentants':15,'Acetaminophen, polyethylene glycol & ophthalmic':16,'Zyrtec, nasal spray':17,'Antihistamines, Decongentants':18,'Antihistamines, aspirin':19,
                          'Paracetamol,Favipiravis, acebrophyltine & Acetyleystrne, ascorbic acid, zinc acetate':20,'Favipiravis, acebrophyltine & Acetyleystrne, paracetamol, ascorbic acid, zinc acetate':21,
            'Paracetamol,Grilinctus, ivermectin, azithromycin, ascorbic acid, zinc acetate':22,'Paracetamol,Methylprednisolone, Favipiravis, ascorbic acid, zinc acetate':23,
            'Grilinctus, ivermectin, azithromycin, ascorbic acid, zinc acetate':24,'Grilinctus, ivermectin, azithromycin, ascorbic acid, zinc acetate':25,'Azithromycin, ivermectin, ascorbic acid, zinc acetate':26,
            'Ivermectin, paracetamol, ascorbic acid, zinc acetate':27,'Paracetamol,Grilinctus, Favipiravis, Methylprednisolone, ascorbic acid':28,'Ivermectin, ascorbic acid, zinc acetate':29,
                          'Not curable':30,'Not curable':31,'Not curable':32,'Not curable':33,'Not curable':34,'Not curable':35,'Not curable':36,'Not curable':37,'Not curable':38,
                          'Not curable':39,'Antihistamines, change medication':40,'Corticosteroids, change medication':41,'Bronchodilators, change medication':42,'Bronchodilators, change medication':43,
                          'Antihistamines':44,'Corticosteroids, change medication':45,'Antihistamines, change medication':46,'Bronchodilators, change medication':47,'Bronchodilators, change medication':48,
                          'Antihistamines':49,'panloprozole, penicillium':50,'panloprozole, Omeprazole':51,
                          'amoxicillin, tinidazole':52,'tetracycline and levofloxacin':53,'Lansoprazole':54,'amoxicillin, tinidazole':55,'tetracycline and levofloxacin':56,'panloprozole, penicillium':57,
                          'panloprozole, penicillium':58,'panloprozole, penicillium, Lansoprazole':59,'Not curable':60,'Not curable':61,'Not curable':62,'Not curable':63,'Not curable':64,'Not curable':65,
                          'Not curable':66,'Not curable':67,'Not curable':68,'Not curable':69,'Blood Diagnosis required':70,'Blood Diagnosis required':71,'Blood Diagnosis required':72,'Blood Diagnosis required':73,
                          'Blood Diagnosis required':74,'Blood Diagnosis required':75,'Blood Diagnosis required':76,'Blood Diagnosis required':77,'Blood Diagnosis required':78,
                          'Blood Diagnosis required':79,'Loperamide, ondansetron':80,'Loperamide, ondansetron':81,'plenty of water, Loperamide':82,'Loperamide, ondansetron':83,'plenty of water, ondansetron':84,
                          'Self healing, plenty of fluids':85,'Loperamide, ondansetron':86,'plenty of water, Loperamide':87,'Loperamide, ondansetron':88,'plenty of water, ondansetron':89,
                          'Predncrone, Bronchodilators, NSAID':90,'Bronchodilators, NSAID':91,'NSAID, Bronchodilators':92,'Bronchodilators':93,'Bronchodilators':94,'NSAID':95,'Bronchodilators, NSAID':96,
                          'Predncrone, Bronchodilators, NSAID':97,'Bronchodilators, NSAID':98,'NSAID, Bronchodilators':99,'Lisinopril, Acetaminophen':100,
                          'Hydrochlorothiazide, Aspirin':101,'Amlodipine besylate, Meclizine':102,'Amlodipine besylate, Acetaminophen':103,'Hydrochlorothiazide, Adderall':104,
                          'Lisinopril, Dimenhydrinate':105,'Amlodipine besylate,Ritalin':106,'Lisinopril, Gentamicin':107,'Acetaminophen,Hydrochlorothiazide (HCTZ)':108,'Hydrochlorothiazide,Acetaminophen':109,
                          'Ibuprofen, Dexlansoprazole, Acetaminophen':110,'Ibuprofen, Acetaminophen':111,
                          'Naproxen, Dexlansoprazole, Acetaminophen':112,'Ibuprofen, Dexlansoprazole, Acetaminophen':113,'Ibuprofen, Dexlansoprazole, Acetaminophen':114,
                          'Naproxen, Dexlansoprazole, Acetaminophen':115,'Ibuprofen, Dexlansoprazole, Acetaminophen':116,'Ibuprofen, Dexlansoprazole, Naproxen':117,
                          'Ibuprofen, Dexlansoprazole, Acetaminophen':118,'Naproxen, Dexlansoprazole, Acetaminophen':119,'Indomethacin, Dimenhydrinate, Gabapentin':120,
                          'Oral Prednisone, Meclizine':121,'Cyclobenzaprine, Dimenhydrinate, Gabapentin':122,'Indomethacin, Meclizine, Gentamicin':123,'Oral Prednisone, Pregabalin':124,
                          'Oral Prednisone, Pregabalin, Gabapentin':125,'Cyclobenzaprine, Meclizine':126,'Indomethacin, Dimenhydrinate':127,'Oral Prednisone, Meclizine, Gentamicin':128,
                          'Indomethacin, Dimenhydrinate, Gabapentin':129,'Consult a Doctor':130,'Consult a Doctor':131,'Consult a Doctor':132,'Consult a Doctor':133,'Consult a Doctor':134,
                          'Consult a Doctor':135,'Consult a Doctor':136,
                          'Consult a Doctor':137,'Consult a Doctor':138,'Consult a Doctor':139,'Consult a Doctor':140,'Consult a Doctor':141,'Consult a Doctor':142,'Acetaminophen, Eszopiclone':143,
                          'Consult a Doctor':144,'Acetaminophen, Eszopiclone':145,'Acetaminophen, Meclizine Hydrochloride, Eszopiclone':146,'Acetaminophen, Meclizine Hydrochloride, Eszopiclone':147,
                          'Acetaminophen, Meclizine Hydrochloride, Eszopiclone':148,'Consult a Doctor':149,'Atovaquone-Proguanil, Aspirin, Loperamide':150,'Primaquine Phosphate, Aspirin, Meclizine Hydrochloride':151,
                          'Quinine sulfate with Doxycycline, Aspirin, Ibuprofen':152,'Quinine sulfate with Doxycycline, Aspirin, Ibuprofen':153,'Consult a Doctor':154,
                          'Atovaquone-Proguanil, Aspirin, Loperamide':155,'Consult a Doctor':156,'Quinine sulfate with Doxycycline, Aspirin, Meclizine Hydrochloride':157,'Consult a Doctor':158,'Primaquine Phosphate, Aspirin':159,
                          'Acyclovir, Hydroxyzine Pamoate, Acetaminophen':160,'acyclovir,acetaminophen,Eszopiclone':161,'Acyclovir, Hydroxyzine Pamoate, Acetaminophen':162,'Acyclovir, Hydroxyzine Pamoate, Naproxen':163,
                          'Acyclovir, Hydroxyzine Pamoate, Ibuprofen':164,'Acyclovir, Hydroxyzine Pamoate, Ibuprofen':165,'Acyclovir, Hydroxyzine Pamoate, Naproxen':166,'Acyclovir, Hydroxyzine Pamoate, Acetaminophen':167,
                          'Acyclovir, Hydroxyzine Pamoate, Acetaminophen':168,'Acyclovir, Hydroxyzine Pamoate, Naproxen':169,'Acetaminophen, Meclizine Hydrochloride, Hydrocortisone':170,'Ibuprofen, Meclizine Hydrochloride':171,
                          'Acetaminophen, Meclizine Hydrochloride, Eszopiclone':172,'Ibuprofen, Meclizine hydrochloride, Hydrocortisone':173,'Ibuprofen, Meclizine hydrochloride, Hydrocortisone':174,
                          'Naproxen, Hydrocortisone, Aspirin':175,'Acetaminophen, Hydrocortisone, Aspirin':176,'Ibuprofen, Eszopiclone, Aspirin':177,'Naproxen, Hydrocortisone, Eszopiclone':178,'Acetaminophen, Hydrocortisone, Eszopiclone':179,
                          'Ciprofloxacin, Linaclotide, Acetaminophen':180,'Azithromycin, Linaclotide, Acetaminophen':181,'Ceftriaxone, Meclizine hydrochloride, Ibuprofen':182,'Ciprofloxacin, Ibuprofen, Eszopiclone':183,
                          'Azithromycin, Linaclotide, Acetaminophen':184,'Ciprofloxacin, Ibuprofen, Eszopiclone':185,'Ceftriaxone, Linaclotide, Naproxen':186,'Azithromycin, Linaclotide, Acetaminophen':187,'Ciprofloxaci , Linaclotide, Naproxen':188,
                          'Azithromycin, Linaclotide, Acetaminophen':189,'acetaminophen,Meclizine hydrochloride':190,'Ibuprofen, Promethazine':191,'Ibuprofen, Meclizine Hydrochloride':192,
                          'Naproxen, Pepto-Bismol':193,'Naproxen, Meclizine hydrochloride':194,'Acetaminophen, Pepto-Bismol':195,
                          'acetaminophen,Pepto-Bismol':196,'Ibuprofen, Meclizine Hydrochloride':197,'Naproxen, Promethazine':198,'Acetaminophen, Pepto-Bismol':199,'Consult a Doctor':200,
                          'Consult a Doctor':201,'Consult a Doctor':202,'Consult a Doctor':203,'Consult a Doctor':204,'Consult a Doctor':205,'Consult a Doctor':206,
                          'Consult a Doctor':207,'Consult a Doctor':208,'Consult a Doctor':209,'Consult a Doctor':210,'Consult a Doctor':211,'Consult a Doctor':212,
                          'Consult a Doctor':213,'Consult a Doctor':214,'Consult a Doctor':215,'Consult a Doctor':216,
                          'Consult a Doctor':217,'Consult a Doctor':218,'Consult a Doctor':219,'Consult a Doctor':220,'Consult a Doctor':221,'Consult a Doctor':222,'Consult a Doctor':223,
                          'Consult a Doctor':224,'Consult a Doctor':225,'Consult a Doctor':226,'Consult a Doctor':227,'Consult a Doctor':228,'Consult a Doctor':229,'Consult a Doctor':230,
                          'Consult a Doctor':231,'Consult a Doctor':232,'Consult a Doctor':233,'Consult a Doctor':234,'Consult a Doctor':235,'Consult a Doctor':236,'Consult a Doctor':237,
                          'Consult a Doctor':238,
                          'Consult a Doctor':239,'Corticosteroids, Atorvastatin, Simethicone':240,'Atorvastatin, Oxandrolone, Simethicone':241,'Atorvastatin, Oxandrolone, Simethicone':242,
                          'Corticosteroids, Atorvastatin, Loperamide':243,'Atorvastatin, Oxandrolone, Simethicone':244,'Corticosteroids, Atorvastatin, Loperamide':245,
                          'Atorvastatin, Oxandrolone, Simethicone':246,'Corticosteroids, Atorvastatin, Loperamide':247,'Corticosteroids, Atorvastatin, Loperamide':248,
                          'Atorvastatin, Oxandrolone, Simethicone':249,'Isoniazid, Oseltamivir, Salmeterol, Dextromethorphan, Acetaminophen':250,'Rifampicin, Iced saline, Salbutamol, Dextromethorphan, Ibuprofen':251,
                          'Isoniazid, Iced saline, Salmeterol, Dextromethorphan, Acetaminophen':252,'Rifampicin, Oseltamivir, Salbutamol, Dextromethorphan, Ibuprofen':253,
                          'Pyrazinamide, Iced saline, Salmeterol, Dextromethorphan, Ibuprofen':254,'Pyrazinamide,oseltamivir,salmeterol,Dextromethorphan,acetaminophen,':255,
                          'Isoniazid, Iced saline, Salbutamol, Acetaminophen':256,'Pyrazinamide, Iced saline, Salmeterol, Dextromethorphan, Ibuprofen':257,
                          'Rifampicin, Oseltamivir, Salbutamol, Dextromethorphan, Ibuprofen':258,'Isoniazid, Iced saline, Salmeterol, Dextromethorphan, Acetaminophen,':259,
                          'Oxymetazoline Nasal, Cetirizine':260,'Phenylephrine Nasal, Cetirizine':261,'Phenylephrine Oral':262,'Oxymetazoline Nasal, Cetirizine':263,
                          'Phenylephrine Nasal, Cetirizine':264,'Phenylephrine Nasal, Cetirizine':265,'Phenylephrine Oral, Cetirizine':266,'Oxymetazoline Nasal, Cetirizine':267,
                          'Phenylephrine Nasal, Cetirizine':268,'Oxymetazoline Nasal, Cetirizine':269,'Consult a Doctor':270,'Oracea, Toprol, Acetaminophen, Salbutamol, Dextromethorphan':271,
                          'Consult a Doctor':272,'Levaquin, Toprol, Ibuprofen, Salmeterol, Dextromethorphan':273,'Levaquin, Toprol, Acetaminophen, Salbutamol, Dextromethorphan':274,'Oracea, Toprol, Ibuprofen, Salmeterol, Dextromethorphan':275,
                          'Cipro, Toprol, Ibuprofen, Salmeterol, Dextromethorphan':276,'Levaquin, Toprol, Ibuprofen, Salbutamol, Dextromethorphan':277,'Consult a Doctor':278,
                          'Cipro, Toprol, Acetaminophen, Salbutamol, Dextromethorphan':279,'Hydrocortisone, Dulcolax':280,'Consult a Doctor':281,'Prednisolone, Docusate Sodium':282,
                          'Hydrocortisone, Calcium Polycarbophil':283,'Fluocortolone, Dulcolax':286,
                          'Fluocortolone, Docusate Sodium':285,'Hydrocortisone, Bisacodyl':286,'Consult a Doctor':287,'Consult a Doctor':288,'Hydrocortisone, Calcium Polycarbophil':289,
                          'Consult a Doctor':290,'Consult a Doctor':291,'Consult a Doctor':292,'Consult a Doctor':293,'Consult a Doctor':294,'Consult a Doctor':295,'Consult a Doctor':296,
                          'Consult a Doctor':297,'Consult a Doctor':298,'Consult a Doctor':299,'Ultrasound-guided Sclerotherapy, Asclera, Carisoprodol':300,'Radiofrequency Ablation, Sodium Tetradecyl Sulfate, Diltiazem':301,
                          'Ambulatory Phlebectomy, Asclera, Carisoprodol':302,'Ultrasound-guided sclerotherapy,sodium tetradecyl sulfate':303,'Ambulatory Phlebectomy, Asclera, Diltiazem':304,
                          'Varicose vein laser surgery, Sodium Tetradecyl Sulfate, Orphenadrine':305,
                          'Ambulatory Phlebectomy, Sodium Tetradecyl Sulfate, Carisoprodol':306,'Ultrasound-guided Sclerotherapy, Sodium Tetradecyl Sulfate, Diltiazem':307,
                          'Varicose vein laser surgery, Asclera, Diltiazem':308,'Varicose vein laser surgery, Sodium Tetradecyl Sulfate, Orphenadrine':309,'Levothyroxine':310,'Levothyroxine, initially have regular blood tests until the correct dose of levothyroxine is reached':311,
                          'Levothyroxine':312,'Levothyroxine':313,'Levothyroxine':314,'Levothyroxine':315,'Levothyroxine':316,
                          'Levothyroxine, initially have regular blood tests until the correct dose of levothyroxine is reached':317,
                          'Levothyroxine':318,'Levothyroxine':319,'propylthiouracil, Imodium':320,'methimazole,  Lactobacillus rhamnosus GG':321,
                          'methimazole , imodium':322,'propylthiouracil, acetaminophen':323,'propylthiouracil':324,'propylthiouracil':325,
                          'methimazole':326,'methimazole':327,'Tapazole, Lactobacillus rhamnosus GG':328,'Tapazole':329,
                          'Thiazolidinediones, glucose':330,'Alpha-glucosidase inhibitors':331,'Metformin':332,'Sulfonylureas':333,
                          'Metformin, glucose':334,'Alpha-glucosidase inhibitors':335,'Metformin, glucose':336,'Metformin':337,
                          'Sulfonylureas':338,'Alpha-glucosidase inhibitors':339,'arthroscopy, Acetaminophen':340,'Joint replacement, Acetaminophen':341,
                          'Acetaminophen':342,'NSAID':343,'arthroscopy, Acetaminophen':344,'NSAID, Acetaminophen':345,'Analgesic, NSAID':346,
                          'arthroscopy, Acetaminophen':347,'Joint replacement, Acetaminophen':348,'Joint replacement, Acetaminophen, arthroscopy':349,
                          'Cortisone Decadron, Aristocort Celestone, Acetaminophen (surgery needed)':350,'Delta-cortef Deltasone, Cinalone Depo-medrol, Acetaminophen':351,'Prednisone (sometimes surgery needed)':352,'Methylprednisolone, Acetaminophen':353,
                          'Aristocort Celestone, surgery needed':354,'Delta-cortef Deltasone, Cinalone Depo-medrol, Acetaminophen':355,'Methylprednisolone, Acetaminophen':356,
                          'Aristocort Celestone, surgery needed':357,'Prednisone (sometimes surgery needed)':358,
                          'Cortisone Decadron, Aristocort Celestone, Acetaminophen (surgery needed)':359,'Epley Maneuver':360,'Epley Maneuver':361,
                          'Epley Maneuver':362,'Epley Maneuver':363,'Epley Maneuver':364,'Epley Maneuver':365,'Epley Maneuver':366,'Epley Maneuver':367,
                          'Epley Maneuver':368,'Epley Maneuver':369,'glycolic Acid cream 6%':370,'tretinoin cream':371,'benzoyl peroxide cream':372,
                          'clindamycin phosphate gel USP':373,'clindamycin phosphate gel USP':374,'clindamycin phosphate gel USP':375,'salicylic acid':376,
                          'adapalene-benzoyl peroxide':377,'clindamycin-benzoyl peroxide':378,'tazarotene':379,'Trimethoprim, consuming plenty of fluids':380,
                          'sulfamethoxazole, Lorabid':381,'Cephalexin, Amoxicillin':382,'Nitrofurantoin, Rocephin':383,
                          'Ceftriaxone, Keflex':384,'Fosfomycin, lorabid, consuming plenty of water':385,'Nitrofurantoin, Rocephin':386,
                          'sulfamethoxazole, Lorabid':387,'Trimethoprim, consuming plenty of fluids':388,'Trimethoprim, consuming plenty of fluids':389,
                          'photodynamic therapy, triamcinolone, NSAID':390,'photodynamic therapy, triamcinolone, NSAID':391,'photodynamic therapy, triamcinolone':392,'triamcinolone, aspirin':393,'photodynamic therapy, ibuprofen':394,
                          'photodynamic therapy, triamcinolone':395,'photodynamic therapy, ibuprofen':396,'triamcinolone, aspirin':397,'photodynamic therapy, triamcinolone, NSAID':398,
                          'photodynamic therapy, triamcinolone, NSAID':399,'antistaphylococcal, Amoxicillin':400,'antistaphylococcal, Amoxicillin':401,'amoxicillin, clavulanate':402,
                          'cephalosporins, Cephalexin':403,'macrolides, Dicloxacillin':404,'Dicloxacillin':405,'amoxicillin, Dicloxacillin':406,'Cephalexin':407,'antistaphylococcal, Amoxicillin':408,
                          'antistaphylococcal, Amoxicillin':409,'Magnesium hydroxide, Esomeprazole, Axid AR':410,'Gaviscon, Lansoprazole, Pepcid AC':411,'Gaviscon, Esomeprazole, Axid AR':412,
                          'Magnesium hydroxide, Lansoprazole, Prilosec OTC':413,'Gaviscon, Lansoprazole, Tagamet HB':414,'Pepto-Bismol, Esomeprazole, Axid AR':415,'Magnesium hydroxide, Lansoprazole, Tagamet HB':416,
                          'Pepto-Bismol, Lansoprazole, Prilosec OTC':417,'Pepto-Bismol, Esomeprazole, Pepcid AC':418,'Magnesium hydroxide, Lansoprazole, Tagamet HB':419,
                          'Metformin, Medroxyprogesterone':420, 'Statins, Medroxyprogesterone, Citalopram':421,'Clomiphene, Medroxyprogesterone, Citalopram':422,
                          'Metformin, Medroxyprogesterone':423,'Clomiphene,Medroxyprogesterone':424,'Statins, Medroxyprogesterone, Citalopram':425,'Clomiphene, Medroxyprogesterone, Citalopram':426,
                          'Metformin, Medroxyprogesterone':427,'Statins, Medroxyprogesterone, Citalopram':428,'Metformin, Medroxyprogesterone, Citalopram':429,
                          'Midodrine, Dimenhydrinate, Meclizine hydrochloride':430,'Fludrocortisone, Dimenhydrinate, Hydralyte':431,'Fludrocortisone, Dimenhydrinate, Meclizine hydrochloride':432,
                          'Midodrine, Dimenhydrinate, Hydralyte':433, 'Fludrocortisone, Dimenhydrinate, Meclizine hydrochloride':434,'Fludrocortisone, Dimenhydrinate, Pedialyte':435,
                          'Fludrocortisone, Dimenhydrinate, Meclizine hydrochloride':436,'Midodrine, Dimenhydrinate, Meclizine hydrochloride':437,'Fludrocortisone, Dimenhydrinate, Pedialyte':438,
                          'Midodrine, Dimenhydrinate, Meclizine hydrochloride':439,
                          'Lisinopril, Acetaminophen':440,'Acetaminophen,Hydrochlorothiazide (HCTZ)':441,'Acetaminophen,Hydrochlorothiazide (HCTZ)':442,
                          'Lisinopril, Acetaminophen':443,'Acetaminophen,Hydrochlorothiazide (HCTZ)':444,'Acetaminophen,Hydrochlorothiazide (HCTZ)':445,
                          'Acetaminophen,Hydrochlorothiazide (HCTZ)':446,'Acetaminophen,Hydrochlorothiazide (HCTZ)':447,'Lisinopril, Acetaminophen':448,
                          'Lisinopril, Acetaminophen':449,
                          'Nitroimidazole Antibiotics, Dextromethorphan, Salbutamol, Chlorpheniramine, Toprol':450,
                          'Quinolone Antibiotics, Dextromethorphan, Salbutamol, Chlorpheniramine, Toprol':451,
                          'Tetracycline Antibiotics, Dextromethorphan, Salmeterol, Chlorpheniramine, Toprol':452,
                          'Tetracycline Antibiotics, Dextromethorphan, Salmeterol, Toprol':453,
                          'Nitroimidazole Antibiotics, Dextromethorphan, Salbutamol, Chlorpheniramine':454,
                          'Macrolide Antibiotics, Dextromethorphan, Salbutamol':455,
                          'Quinolone Antibiotics, Dextromethorphan, Salmeterol, Toprol':456,
                          'Cephalosporin Antibiotics, Dextromethorphan, Salbutamol, Toprol':457,
                          'Cephalosporin Antibiotics, Dextromethorphan, Chlorpheniramine, Toprol':458,
                          'Macrolide Antibiotics, Dextromethorphan, Salmeterol, Chlorpheniramine':459}},inplace=True)



X_test1=ne[l1]
z_test = ne[["medication"]]
np.ravel(z_test)
#print(z_test)

# ------------------------------------------------------------------------------------------------------
def DecisionTree():

    from sklearn import tree

    clf3 = tree.DecisionTreeClassifier()   # empty model of the decision tree
    clf5 = clf3.fit(X,y)
    clf6 = clf3.fit(X1,z)

    # calculating accuracy-------------------------------------------------------------------
    from sklearn.metrics import accuracy_score
    y_pred=clf5.predict(X_test)
    z_pred=clf6.predict(X_test1)
    print(accuracy_score(y_test, y_pred))
    print(accuracy_score(y_test, y_pred,normalize=False))
    print(accuracy_score(z_test, z_pred))
    print(accuracy_score(z_test, z_pred,normalize=False))
    # -----------------------------------------------------

    psymptoms = [Symptom1.get(),Symptom2.get(),Symptom3.get(),Symptom4.get(),Symptom5.get()]

    for k in range(0,len(l1)):
        # print (k,)
        for f in psymptoms:
            if(f==l1[k]):
                l2[k]=1
                l3[k]=1

    inputtest = [l2]
    inputtest1 = [l3]
    predict = clf5.predict(inputtest)
    predict1 = clf6.predict(inputtest1)
    predicted=predict[0]
    predicted1=predict1[0]
    h='no'
    for a in range(0,len(disease)):
        if(predicted == a):
            h='yes'
            break
    if (h=='yes'):
        t1.delete("1.0", END)
        t1.insert(END, disease[a])
    else:
        t1.delete("1.0", END)
        t1.insert(END, "Not Found")

    for b in range(0,len(medication)):
        if(predicted1 == b):
            h='yes'
            break
    if (h=='yes'):
        t2.delete("1.0", END)
        t2.insert(END, medication[b])
    else:
        t2.delete("1.0", END)
        t2.insert(END, "Not Found")

    for s in range(0,len(disease)):
        if(predicted == s):
            h='yes'
            break
    if (h=='yes'):
        t3.delete("1.0", END)
        t3.insert(END, doctor[s])
    else:
        t3.delete("1.0", END)
        t3.insert(END, "Not Found")




def randomforest():
    from sklearn.ensemble import RandomForestClassifier
    clf4 = RandomForestClassifier()
    clf7 = clf4.fit(X,np.ravel(y))
    clf8 = clf4.fit(X1,np.ravel(z))

    # calculating accuracy-------------------------------------------------------------------
    from sklearn.metrics import accuracy_score
    y_pred=clf7.predict(X_test)
    z_pred=clf8.predict(X_test1)
    print(accuracy_score(y_test, y_pred))
    print(accuracy_score(y_test, y_pred,normalize=False))
    print(accuracy_score(z_test, z_pred))
    print(accuracy_score(z_test, z_pred,normalize=False))
    # -----------------------------------------------------

    psymptoms = [Symptom1.get(),Symptom2.get(),Symptom3.get(),Symptom4.get(),Symptom5.get()]

    for k in range(0,len(l1)):
        # print (k,)
        for f in psymptoms:
            if(f==l1[k]):
                l2[k]=1
                l3[k]=1

    inputtest = [l2]
    inputtest1 = [l3]
    predict = clf7.predict(inputtest)
    predict1 = clf8.predict(inputtest1)
    predicted=predict[0]
    predicted1=predict1[0]
    h='no'
    for a in range(0,len(disease)):
        if(predicted == a):
            h='yes'
            break
    if (h=='yes'):
        t4.delete("1.0", END)
        t4.insert(END, disease[a])
    else:
        t4.delete("1.0", END)
        t4.insert(END, "Not Found")

    for b in range(0,len(medication)):
        if(predicted1 == b):
            h='yes'
            break
    if (h=='yes'):
        t5.delete("1.0", END)
        t5.insert(END, medication[b])
    else:
        t5.delete("1.0", END)
        t5.insert(END, "Not Found")

    for s in range(0,len(doctor)):
        if(predicted==s):
            h='yes'
            break
    if (h=='yes'):
        t6.delete("1.0", END)
        t6.insert(END, doctor[s])
    else:
        t6.delete("1.0", END)
        t6.insert(END, "Not Found")




def NaiveBayes():
    from sklearn.naive_bayes import GaussianNB
    gnb = GaussianNB()
    gnb1=gnb.fit(X,np.ravel(y))
    gnb2=gnb.fit(X1,np.ravel(z))

    # calculating accuracy-------------------------------------------------------------------
    from sklearn.metrics import accuracy_score
    y_pred=gnb1.predict(X_test)
    z_pred=gnb2.predict(X_test1)
    print(accuracy_score(y_test, y_pred))
    print(accuracy_score(y_test, y_pred,normalize=False))
    print(accuracy_score(z_test, z_pred))
    print(accuracy_score(z_test, z_pred,normalize=False))
    # -----------------------------------------------------
    psymptoms = [Symptom1.get(),Symptom2.get(),Symptom3.get(),Symptom4.get(),Symptom5.get()]
    for k in range(0,len(l1)):
        # print (k,)
        for f in psymptoms:
            if(f==l1[k]):
                l2[k]=1
                l3[k]=1

    inputtest = [l2]
    inputtest1 = [l3]
    predict = gnb1.predict(inputtest)
    predict1 = gnb2.predict(inputtest1)
    predicted=predict[0]
    predicted1=predict1[0]
    h='no'
    for a in range(0,len(disease)):
        if(predicted == a):
            h='yes'
            break


    if (h=='yes'):
        t7.delete("1.0", END)
        t7.insert(END, disease[a])
    else:
        t7.delete("1.0", END)
        t7.insert(END, "Not Found")
    
    for b in range(0,len(medication)):
        if(predicted1 == b):
            h='yes'
            break
    if (h=='yes'):
        t8.delete("1.0", END)
        t8.insert(END, medication[b])
    else:
        t8.delete("1.0", END)
        t8.insert(END, "Not Found")

    for s in range(0,len(doctor)):
        if(predicted==s):
            h='yes'
            break
    if (h=='yes'):
        t9.delete("1.0", END)
        t9.insert(END, doctor[s])
    else:
        t9.delete("1.0", END)
        t9.insert(END, "Not Found")


# gui_stuff------------------------------------------------------------------------------------

root = Tk()
root.configure(background='tan')

# entry variables
Symptom1 = StringVar()
Symptom1.set(None)
Symptom2 = StringVar()
Symptom2.set(None)
Symptom3 = StringVar()
Symptom3.set(None)
Symptom4 = StringVar()
Symptom4.set(None)
Symptom5 = StringVar()
Symptom5.set(None)
Name = StringVar()

# Heading

w2 = Label(root, text="Human Disease Prediction using Machine Learning", fg="black", bg="tan")
w2.config(font=("Elephant", 25))
w2.grid(row=1, column=0, columnspan=2, padx=100,pady=3)

# labels

S1Lb = Label(root, text="Symptom 1", fg="white", bg="brown")
S1Lb.grid(row=6, column=0, pady=3, sticky=E,padx=50)
#S1Lb.config(anchor=CENTER)
#S1Lb.pack()

S2Lb = Label(root, text="Symptom 2", fg="white", bg="brown")
S2Lb.grid(row=8, column=0, pady=3, sticky=E,padx=50)
#S2Lb.config(anchor=CENTER)

S3Lb = Label(root, text="Symptom 3", fg="white", bg="brown")
S3Lb.grid(row=10, column=0, pady=3, sticky=E,padx=50)
#S3Lb.config(anchor=CENTER)

S4Lb = Label(root, text="Symptom 4", fg="white", bg="brown")
S4Lb.grid(row=12, column=0, pady=3, sticky=E,padx=50)
#S4Lb.config(anchor=CENTER)

S5Lb = Label(root, text="Symptom 5", fg="white", bg="brown")
S5Lb.grid(row=14, column=0, pady=3, sticky=E,padx=50)
#S5Lb.config(anchor=CENTER)

S6Lb = Label(root, text="DISEASE", fg="white", bg="gray")
S6Lb.grid(row=16, column=0, pady=3, sticky=E,padx=50)


S7Lb = Label(root, text="MEDICATION / TREATMENT", fg="white", bg="gray")
S7Lb.grid(row=18, column=0, pady=3, sticky=E,padx=50)


S8Lb = Label(root, text="RECOMMENDED SPECIALIST", fg="white", bg="gray")
S8Lb.grid(row=20, column=0, pady=3, sticky=E,padx=50)


S9Lb = Label(root, text="DISEASE", fg="white", bg="gray")
S9Lb.grid(row=22, column=0, pady=3, sticky=E,padx=50)


S11Lb = Label(root, text="MEDICATION / TREATMENT", fg="white", bg="gray")
S11Lb.grid(row=24, column=0, pady=3, sticky=E,padx=50)


S12Lb = Label(root, text="RECOMMENDED SPECIALIST", fg="white", bg="gray")
S12Lb.grid(row=26, column=0, pady=3, sticky=E,padx=50)


S13Lb = Label(root, text="DISEASE", fg="white", bg="gray")
S13Lb.grid(row=28, column=0, pady=3, sticky=E,padx=50)


S14Lb = Label(root, text="MEDICATION / TREATMENT", fg="white", bg="gray")
S14Lb.grid(row=30, column=0, pady=3, sticky=E,padx=50)

S15Lb = Label(root, text="RECOMMENDED SPECIALIST", fg="white", bg="gray")
S15Lb.grid(row=32, column=0, pady=3, sticky=E,padx=50)





# entries
OPTIONS = sorted(l1)

S1En = OptionMenu(root, Symptom1,*OPTIONS)
S1En.grid(row=6, column=1, sticky=W,padx=50)


S2En = OptionMenu(root, Symptom2,*OPTIONS)
S2En.grid(row=8, column=1, sticky=W,padx=50)


S3En = OptionMenu(root, Symptom3,*OPTIONS)
S3En.grid(row=10, column=1,sticky=W,padx=50)


S4En = OptionMenu(root, Symptom4,*OPTIONS)
S4En.grid(row=12, column=1, sticky=W,padx=50)


S5En = OptionMenu(root, Symptom5,*OPTIONS)
S5En.grid(row=14, column=1, sticky=W,padx=50)

dst = Button(root, text="DecisionTree", command=DecisionTree,bg="white",fg="green")
dst.grid(row=15, column=1, sticky=W, pady=3,padx=50)

rnf = Button(root, text="Randomforest", command=randomforest,bg="white",fg="green")
rnf.grid(row=21, column=1, sticky=W, pady=3,padx=50)

lr = Button(root, text="NaiveBayes", command=NaiveBayes,bg="white",fg="green")
lr.grid(row=27, column=1, sticky=W, pady=3,padx=50)

t1 = Text(root, height=1, width=40,bg="white",fg="black")
t1.grid(row=16, column=1, sticky=W,padx=50)

t2 = Text(root, height=2, width=40,bg="white",fg="black")
t2.grid(row=18, column=1 , sticky=W,padx=50)

t3 = Text(root, height=1, width=40,bg="white",fg="black")
t3.grid(row=20, column=1 , sticky=W,padx=50)

t4 = Text(root, height=1, width=40,bg="white",fg="black")
t4.grid(row=22, column=1 , sticky=W,padx=50)

t5 = Text(root, height=2, width=40,bg="white",fg="black")
t5.grid(row=24, column=1 , sticky=W,padx=50)

t6 = Text(root, height=1, width=40,bg="white",fg="black")
t6.grid(row=26, column=1 , sticky=W,padx=50)

t7 = Text(root, height=1, width=40,bg="white",fg="black")
t7.grid(row=28, column=1 , sticky=W,padx=50)

t8 = Text(root, height=2, width=40,bg="white",fg="black")
t8.grid(row=30, column=1 , sticky=W,padx=50)

t9 = Text(root, height=1, width=40,bg="white",fg="black")
t9.grid(row=32, column=1 , sticky=W,padx=50)




root.mainloop()
