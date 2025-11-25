# Codebook Matches

## rec_id (column)

```
Field Note Choices, Calculations, etc.)
Instrument: Data Abstraction Form (data_abstraction_form)
1 [rec_id] Record ID text, Identifier
2 [date_data_collect] 1. Date of data collection text (date_dmy), Required
3 [name_of_rrh] 2. Name of Regional Referral Hospital (RRH) radio, Required
```

## date_data_collect (column)

```
Instrument: Data Abstraction Form (data_abstraction_form)
1 [rec_id] Record ID text, Identifier
2 [date_data_collect] 1. Date of data collection text (date_dmy), Required
3 [name_of_rrh] 2. Name of Regional Referral Hospital (RRH) radio, Required
1 Arua
```

## name_of_rrh (column)

```
1 [rec_id] Record ID text, Identifier
2 [date_data_collect] 1. Date of data collection text (date_dmy), Required
3 [name_of_rrh] 2. Name of Regional Referral Hospital (RRH) radio, Required
1 Arua
2 Kabale
```

## patient_id (column)

```
8 Masaka
9 Mbarara
4 [patient_id] Section Header: Section 2: Patient data for abstraction text, Required
3. Patient Unique Identification Number
5 [re_admit] 4. Was the patient a re-admission at the same yesno, Required
```

## re_admit (column)

```
4 [patient_id] Section Header: Section 2: Patient data for abstraction text, Required
3. Patient Unique Identification Number
5 [re_admit] 4. Was the patient a re-admission at the same yesno, Required
hospital?
1 Yes
```

## age (column)

```
1 Yes
0 No
6 [age] 5. Age in completed years text (integer), Required
7 [sex] 6. Sex radio, Required
1 Female
```

## sex (column)

```
0 No
6 [age] 5. Age in completed years text (integer), Required
7 [sex] 6. Sex radio, Required
1 Female
2 Male
```

## res_district (column)

```
1 Female
2 Male
8 [res_district] 7. Residence District text
9 [res_subcounty] 8a. Residence Sub-county text
10 [village] 8b. Residence Village text (alpha_only)
```

## res_subcounty (column)

```
2 Male
8 [res_district] 7. Residence District text
9 [res_subcounty] 8a. Residence Sub-county text
10 [village] 8b. Residence Village text (alpha_only)
11 [occupation] Occupation text
```

## village (column)

```
8 [res_district] 7. Residence District text
9 [res_subcounty] 8a. Residence Sub-county text
10 [village] 8b. Residence Village text (alpha_only)
11 [occupation] Occupation text
If more than one occupation separate with comma e.g.,
```

## occupation (column)

```
9 [res_subcounty] 8a. Residence Sub-county text
10 [village] 8b. Residence Village text (alpha_only)
11 [occupation] Occupation text
If more than one occupation separate with comma e.g.,
job1, job2
```

## allergies (column)

```
If more than one occupation separate with comma e.g.,
job1, job2
12 [allergies] 9. History of allergies and antibiotic side effects yesno
.
1 Yes
```

## infect_site___1 (column)

```
13 [infect_site] 10. Site of Infection (Suspected based on checkbox
symptoms)
1 infect_site___1 Central Nervous
Suspected based on symptoms
System
```

## infect_site___2 (column)

```
Suspected based on symptoms
System
2 infect_site___2 Gastrointestinal
system
3 infect_site___3 Respiratory system
```

## infect_site___3 (column)

```
2 infect_site___2 Gastrointestinal
system
3 infect_site___3 Respiratory system
https://idiredcap.idi.co.ug/redcap_v14.7.4/Design/data_dictionary_codebook.php?pid=147 1/48
9/17/25, 11:25 AM GHS-CAMO-Net Project 3 Additional Data Collection | REDCap
```

## infect_site___4 (column)

```
https://idiredcap.idi.co.ug/redcap_v14.7.4/Design/data_dictionary_codebook.php?pid=147 1/48
9/17/25, 11:25 AM GHS-CAMO-Net Project 3 Additional Data Collection | REDCap
4 infect_site___4 Genital Urinary
System
5 infect_site___5 Musculoskeletal
```

## infect_site___5 (column)

```
4 infect_site___4 Genital Urinary
System
5 infect_site___5 Musculoskeletal
system
6 infect_site___6 Cardiovascular system
```

## infect_site___6 (column)

```
5 infect_site___5 Musculoskeletal
system
6 infect_site___6 Cardiovascular system
7 infect_site___7 Integumentary
8 infect_site___8 Reproductive system
```

## infect_site___7 (column)

```
system
6 infect_site___6 Cardiovascular system
7 infect_site___7 Integumentary
8 infect_site___8 Reproductive system
14 [site_based_sample] Site of infection (Based on sample collection) checkbox
```

## infect_site___8 (column)

```
6 infect_site___6 Cardiovascular system
7 infect_site___7 Integumentary
8 infect_site___8 Reproductive system
14 [site_based_sample] Site of infection (Based on sample collection) checkbox
Based on sample collection
```

## site_based_sample___1 (column)

```
14 [site_based_sample] Site of infection (Based on sample collection) checkbox
Based on sample collection
1 site_based_sample___1 Central
Nervous
System
```

## site_based_sample___2 (column)

```
Nervous
System
2 site_based_sample___2 Gastrointestinal
system
3 site_based_sample___3 Respiratory
```

## site_based_sample___3 (column)

```
2 site_based_sample___2 Gastrointestinal
system
3 site_based_sample___3 Respiratory
system
4 site_based_sample___4 Genital urinary
```

## site_based_sample___4 (column)

```
3 site_based_sample___3 Respiratory
system
4 site_based_sample___4 Genital urinary
system
5 site_based_sample___5 Musculoskeletal
```

## site_based_sample___5 (column)

```
4 site_based_sample___4 Genital urinary
system
5 site_based_sample___5 Musculoskeletal
system
6 site_based_sample___6 Cardiovascular
```

## site_based_sample___6 (column)

```
5 site_based_sample___5 Musculoskeletal
system
6 site_based_sample___6 Cardiovascular
system
7 site_based_sample___7 Integumentary
```

## site_based_sample___7 (column)

```
6 site_based_sample___6 Cardiovascular
system
7 site_based_sample___7 Integumentary
8 site_based_sample___8 Reproductive
system
```

## site_based_sample___8 (column)

```
system
7 site_based_sample___7 Integumentary
8 site_based_sample___8 Reproductive
system
9 site_based_sample___9 None
```

## site_based_sample___9 (column)

```
8 site_based_sample___8 Reproductive
system
9 site_based_sample___9 None
15 [sec_site_infection] 11. Site of infection (Confirmed by a positive checkbox
culture)
```

## sec_site_infection___1 (column)

```
15 [sec_site_infection] 11. Site of infection (Confirmed by a positive checkbox
culture)
1 sec_site_infection___1 Central
Confirmed by positive culture result
Nervous
```

## sec_site_infection___2 (column)

```
Nervous
System
2 sec_site_infection___2 Gastrointestinal
system
3 sec_site_infection___3 Respiratory
```

## sec_site_infection___3 (column)

```
2 sec_site_infection___2 Gastrointestinal
system
3 sec_site_infection___3 Respiratory
system
4 sec_site_infection___4 Genital Urinary
```

## sec_site_infection___4 (column)

```
3 sec_site_infection___3 Respiratory
system
4 sec_site_infection___4 Genital Urinary
System
5 sec_site_infection___5 Musculoskeletal
```

## sec_site_infection___5 (column)

```
4 sec_site_infection___4 Genital Urinary
System
5 sec_site_infection___5 Musculoskeletal
system
6 sec_site_infection___6 Cardiovascular
```

## sec_site_infection___6 (column)

```
5 sec_site_infection___5 Musculoskeletal
system
6 sec_site_infection___6 Cardiovascular
system
7 sec_site_infection___7 Integumentary
```

## sec_site_infection___7 (column)

```
6 sec_site_infection___6 Cardiovascular
system
7 sec_site_infection___7 Integumentary
8 sec_site_infection___8 Reproductive
system
```

## sec_site_infection___8 (column)

```
system
7 sec_site_infection___7 Integumentary
8 sec_site_infection___8 Reproductive
system
9 sec_site_infection___9 None
```

## sec_site_infection___9 (column)

```
8 sec_site_infection___8 Reproductive
system
9 sec_site_infection___9 None
16 [referral] 12a. Was the patient referred from another yesno, Required
health service delivery point?
```

## referral (column)

```
1 [rec_id] Record ID text, Identifier
2 [date_data_collect] 1. Date of data collection text (date_dmy), Required
3 [name_of_rrh] 2. Name of Regional Referral Hospital (RRH) radio, Required
1 Arua
2 Kabale
```

## facility_category (column)

```
1 Yes
0 No
17 [facility_category] 12b. If referred from another health service radio
delivery point, indicate the category.
1 Lower-level public health facility
```

## admission_date (column)

```
9/17/25, 11:25 AM GHS-CAMO-Net Project 3 Additional Data Collection | REDCap
4 Not specified
18 [admission_date] 13. Date patient was admitted(DD/MM/YYYY) text (date_dmy), Required
19 [ward] 14. Admission ward radio
1 Maternity/ Post-Natal ward
```

## ward (column)

```
4 Not specified
18 [admission_date] 13. Date patient was admitted(DD/MM/YYYY) text (date_dmy), Required
19 [ward] 14. Admission ward radio
1 Maternity/ Post-Natal ward
2 Surgical
```

## antib_prior_admi (column)

```
Show the field ONLY if:
[ward]='10'
21 [antib_prior_admi] 15a. Was the patient on antibiotics prior to radio, Required
admission?
1 Yes
```

## prio_antib_name___1 (column)

```
3 Unknown
22 [prio_antib_name] 15b. If yes, indicate the antibiotics received. checkbox
1 prio_antib_name___1 Amikacin
Show the field ONLY if:
[antib_prior_admi]='1' 2 prio_antib_name___2 Amoxicillin
```

## prio_antib_name___2 (column)

```
1 prio_antib_name___1 Amikacin
Show the field ONLY if:
[antib_prior_admi]='1' 2 prio_antib_name___2 Amoxicillin
3 prio_antib_name___3 Amoxicillin/C
acid
```

## prio_antib_name___3 (column)

```
Show the field ONLY if:
[antib_prior_admi]='1' 2 prio_antib_name___2 Amoxicillin
3 prio_antib_name___3 Amoxicillin/C
acid
4 prio_antib_name___4 Ampicillin
```

## prio_antib_name___4 (column)

```
3 prio_antib_name___3 Amoxicillin/C
acid
4 prio_antib_name___4 Ampicillin
5 prio_antib_name___5 Ampicillin/Su
6 prio_antib_name___6 Azithromycin
```

## prio_antib_name___5 (column)

```
acid
4 prio_antib_name___4 Ampicillin
5 prio_antib_name___5 Ampicillin/Su
6 prio_antib_name___6 Azithromycin
7 prio_antib_name___7 Aztreonam
```

## prio_antib_name___6 (column)

```
4 prio_antib_name___4 Ampicillin
5 prio_antib_name___5 Ampicillin/Su
6 prio_antib_name___6 Azithromycin
7 prio_antib_name___7 Aztreonam
8 prio_antib_name___8 Cefepime
```

## prio_antib_name___7 (column)

```
5 prio_antib_name___5 Ampicillin/Su
6 prio_antib_name___6 Azithromycin
7 prio_antib_name___7 Aztreonam
8 prio_antib_name___8 Cefepime
9 prio_antib_name___9 Cefixime
```

## prio_antib_name___8 (column)

```
6 prio_antib_name___6 Azithromycin
7 prio_antib_name___7 Aztreonam
8 prio_antib_name___8 Cefepime
9 prio_antib_name___9 Cefixime
10 prio_antib_name___10 Cefotaxime
```

## prio_antib_name___9 (column)

```
7 prio_antib_name___7 Aztreonam
8 prio_antib_name___8 Cefepime
9 prio_antib_name___9 Cefixime
10 prio_antib_name___10 Cefotaxime
11 prio_antib_name___11 Cefoxitin
```

## prio_antib_name___10 (column)

```
8 prio_antib_name___8 Cefepime
9 prio_antib_name___9 Cefixime
10 prio_antib_name___10 Cefotaxime
11 prio_antib_name___11 Cefoxitin
12 prio_antib_name___12 Ceftazidime
```

## prio_antib_name___11 (column)

```
9 prio_antib_name___9 Cefixime
10 prio_antib_name___10 Cefotaxime
11 prio_antib_name___11 Cefoxitin
12 prio_antib_name___12 Ceftazidime
13 prio_antib_name___13 Ceftriaxone
```

## prio_antib_name___12 (column)

```
10 prio_antib_name___10 Cefotaxime
11 prio_antib_name___11 Cefoxitin
12 prio_antib_name___12 Ceftazidime
13 prio_antib_name___13 Ceftriaxone
14 prio_antib_name___14 Ceftriaxone-
```

## prio_antib_name___13 (column)

```
11 prio_antib_name___11 Cefoxitin
12 prio_antib_name___12 Ceftazidime
13 prio_antib_name___13 Ceftriaxone
14 prio_antib_name___14 Ceftriaxone-
salbactam
```

## prio_antib_name___14 (column)

```
12 prio_antib_name___12 Ceftazidime
13 prio_antib_name___13 Ceftriaxone
14 prio_antib_name___14 Ceftriaxone-
salbactam
15 prio_antib_name___15 Cefuroxime
```

## prio_antib_name___15 (column)

```
14 prio_antib_name___14 Ceftriaxone-
salbactam
15 prio_antib_name___15 Cefuroxime
1617 prio_antib_name___1617 Ciprofloxacin
18 prio_antib_name___18 Clindamycin
```

## prio_antib_name___1617 (column)

```
salbactam
15 prio_antib_name___15 Cefuroxime
1617 prio_antib_name___1617 Ciprofloxacin
18 prio_antib_name___18 Clindamycin
19 prio_antib_name___19 Cofotaxime
```

## prio_antib_name___18 (column)

```
15 prio_antib_name___15 Cefuroxime
1617 prio_antib_name___1617 Ciprofloxacin
18 prio_antib_name___18 Clindamycin
19 prio_antib_name___19 Cofotaxime
20 prio_antib_name___20 Doripenem
```

## prio_antib_name___19 (column)

```
1617 prio_antib_name___1617 Ciprofloxacin
18 prio_antib_name___18 Clindamycin
19 prio_antib_name___19 Cofotaxime
20 prio_antib_name___20 Doripenem
21 prio_antib_name___21 Doxycycline
```

## prio_antib_name___20 (column)

```
18 prio_antib_name___18 Clindamycin
19 prio_antib_name___19 Cofotaxime
20 prio_antib_name___20 Doripenem
21 prio_antib_name___21 Doxycycline
22 prio_antib_name___22 Ertapenem
```

## prio_antib_name___21 (column)

```
19 prio_antib_name___19 Cofotaxime
20 prio_antib_name___20 Doripenem
21 prio_antib_name___21 Doxycycline
22 prio_antib_name___22 Ertapenem
23 prio_antib_name___23 Erythromyci
```

## prio_antib_name___22 (column)

```
20 prio_antib_name___20 Doripenem
21 prio_antib_name___21 Doxycycline
22 prio_antib_name___22 Ertapenem
23 prio_antib_name___23 Erythromyci
https://idiredcap.idi.co.ug/redcap_v14.7.4/Design/data_dictionary_codebook.php?pid=147 3/48
```

## prio_antib_name___23 (column)

```
21 prio_antib_name___21 Doxycycline
22 prio_antib_name___22 Ertapenem
23 prio_antib_name___23 Erythromyci
https://idiredcap.idi.co.ug/redcap_v14.7.4/Design/data_dictionary_codebook.php?pid=147 3/48
9/17/25, 11:25 AM GHS-CAMO-Net Project 3 Additional Data Collection | REDCap
```

## prio_antib_name___24 (column)

```
https://idiredcap.idi.co.ug/redcap_v14.7.4/Design/data_dictionary_codebook.php?pid=147 3/48
9/17/25, 11:25 AM GHS-CAMO-Net Project 3 Additional Data Collection | REDCap
24 prio_antib_name___24 Gentamicin
25 prio_antib_name___25 Imipenem
26 prio_antib_name___26 Levofloxacin
```

## prio_antib_name___25 (column)

```
9/17/25, 11:25 AM GHS-CAMO-Net Project 3 Additional Data Collection | REDCap
24 prio_antib_name___24 Gentamicin
25 prio_antib_name___25 Imipenem
26 prio_antib_name___26 Levofloxacin
27 prio_antib_name___27 Linezolid
```

## prio_antib_name___26 (column)

```
24 prio_antib_name___24 Gentamicin
25 prio_antib_name___25 Imipenem
26 prio_antib_name___26 Levofloxacin
27 prio_antib_name___27 Linezolid
28 prio_antib_name___28 Meropenem
```

## prio_antib_name___27 (column)

```
25 prio_antib_name___25 Imipenem
26 prio_antib_name___26 Levofloxacin
27 prio_antib_name___27 Linezolid
28 prio_antib_name___28 Meropenem
29 prio_antib_name___29 Nalidixic acid
```

## prio_antib_name___28 (column)

```
26 prio_antib_name___26 Levofloxacin
27 prio_antib_name___27 Linezolid
28 prio_antib_name___28 Meropenem
29 prio_antib_name___29 Nalidixic acid
30 prio_antib_name___30 Nitrofuranto
```

## prio_antib_name___29 (column)

```
27 prio_antib_name___27 Linezolid
28 prio_antib_name___28 Meropenem
29 prio_antib_name___29 Nalidixic acid
30 prio_antib_name___30 Nitrofuranto
31 prio_antib_name___31 Oxacillin
```

## prio_antib_name___30 (column)

```
28 prio_antib_name___28 Meropenem
29 prio_antib_name___29 Nalidixic acid
30 prio_antib_name___30 Nitrofuranto
31 prio_antib_name___31 Oxacillin
32 prio_antib_name___32 Penicillin G
```

## prio_antib_name___31 (column)

```
29 prio_antib_name___29 Nalidixic acid
30 prio_antib_name___30 Nitrofuranto
31 prio_antib_name___31 Oxacillin
32 prio_antib_name___32 Penicillin G
33 prio_antib_name___33 Piperacillin
```

## prio_antib_name___32 (column)

```
30 prio_antib_name___30 Nitrofuranto
31 prio_antib_name___31 Oxacillin
32 prio_antib_name___32 Penicillin G
33 prio_antib_name___33 Piperacillin
34 prio_antib_name___34 Piperacillin
```

## prio_antib_name___33 (column)

```
31 prio_antib_name___31 Oxacillin
32 prio_antib_name___32 Penicillin G
33 prio_antib_name___33 Piperacillin
34 prio_antib_name___34 Piperacillin
tazobactam
```

## prio_antib_name___34 (column)

```
32 prio_antib_name___32 Penicillin G
33 prio_antib_name___33 Piperacillin
34 prio_antib_name___34 Piperacillin
tazobactam
35 prio_antib_name___35 Rifampin
```

## prio_antib_name___35 (column)

```
34 prio_antib_name___34 Piperacillin
tazobactam
35 prio_antib_name___35 Rifampin
36 prio_antib_name___36 Streptomyci
37 prio_antib_name___37 Tetracycline
```

## prio_antib_name___36 (column)

```
tazobactam
35 prio_antib_name___35 Rifampin
36 prio_antib_name___36 Streptomyci
37 prio_antib_name___37 Tetracycline
38 prio_antib_name___38 Tigecycline
```

## prio_antib_name___37 (column)

```
35 prio_antib_name___35 Rifampin
36 prio_antib_name___36 Streptomyci
37 prio_antib_name___37 Tetracycline
38 prio_antib_name___38 Tigecycline
39 prio_antib_name___39 Trimethopri
```

## prio_antib_name___38 (column)

```
36 prio_antib_name___36 Streptomyci
37 prio_antib_name___37 Tetracycline
38 prio_antib_name___38 Tigecycline
39 prio_antib_name___39 Trimethopri
Sulfamethox
```

## prio_antib_name___39 (column)

```
37 prio_antib_name___37 Tetracycline
38 prio_antib_name___38 Tigecycline
39 prio_antib_name___39 Trimethopri
Sulfamethox
40 prio_antib_name___40 Vancomycin
```

## prio_antib_name___40 (column)

```
39 prio_antib_name___39 Trimethopri
Sulfamethox
40 prio_antib_name___40 Vancomycin
41 prio_antib_name___41 Others
23 [ref_other] Other, please specify text
```

## prio_antib_name___41 (column)

```
Sulfamethox
40 prio_antib_name___40 Vancomycin
41 prio_antib_name___41 Others
23 [ref_other] Other, please specify text
Show the field ONLY if:
```

## ref_other (column)

```
40 prio_antib_name___40 Vancomycin
41 prio_antib_name___41 Others
23 [ref_other] Other, please specify text
Show the field ONLY if:
[prio_antib_name(41)]
```

## sympt_dura (column)

```
[prio_antib_name(41)]
='1'
24 [sympt_dura] 16. Duration of symptoms before admission in text (integer)
days.
25 [date_diagn] 17. Date of diagnosis of infection text (date_dmy)
```

## date_diagn (column)

```
24 [sympt_dura] 16. Duration of symptoms before admission in text (integer)
days.
25 [date_diagn] 17. Date of diagnosis of infection text (date_dmy)
26 [diag_system] 18a. Affected body system (based on the checkbox
diagnosis)
```

## diag_system___1 (column)

```
26 [diag_system] 18a. Affected body system (based on the checkbox
diagnosis)
1 diag_system___1 Central Nervous
Based on the diagnosis
System
```

## diag_system___2 (column)

```
Based on the diagnosis
System
2 diag_system___2 Gastrointestinal
system
3 diag_system___3 Respiratory system
```

## diag_system___3 (column)

```
2 diag_system___2 Gastrointestinal
system
3 diag_system___3 Respiratory system
4 diag_system___4 Genital Urinary
System
```

## diag_system___4 (column)

```
system
3 diag_system___3 Respiratory system
4 diag_system___4 Genital Urinary
System
5 diag_system___5 Musculoskeletal
```

## diag_system___5 (column)

```
4 diag_system___4 Genital Urinary
System
5 diag_system___5 Musculoskeletal
system
6 diag_system___6 Cardiovascular
```

## diag_system___6 (column)

```
5 diag_system___5 Musculoskeletal
system
6 diag_system___6 Cardiovascular
system
7 diag_system___7 Integumentary
```

## diag_system___7 (column)

```
6 diag_system___6 Cardiovascular
system
7 diag_system___7 Integumentary
8 diag_system___8 Reproductive
system
```

## diag_system___8 (column)

```
system
7 diag_system___7 Integumentary
8 diag_system___8 Reproductive
system
27 [diag_cns] State diagnosis on patient file (Central Nervous text
```

## diag_cns (column)

```
8 diag_system___8 Reproductive
system
27 [diag_cns] State diagnosis on patient file (Central Nervous text
System)
Show the field ONLY if:
```

## diag_git (column)

```
Show the field ONLY if:
[diag_system(1)]='1'
28 [diag_git] State diagnosis on patient file (Gastrointestinal text
system)
Show the field ONLY if:
```

## diag_resp (column)

```
https://idiredcap.idi.co.ug/redcap_v14.7.4/Design/data_dictionary_codebook.php?pid=147 4/48
9/17/25, 11:25 AM GHS-CAMO-Net Project 3 Additional Data Collection | REDCap
29 [diag_resp] State diagnosis on patient file (Respiratory text
system)
Show the field ONLY if:
```

## diag_genit (column)

```
Show the field ONLY if:
[diag_system(3)]='1'
30 [diag_genit] State diagnosis on patient file (Genital Urinary text
System)
Show the field ONLY if:
```

## diag_musculo (column)

```
Show the field ONLY if:
[diag_system(4)]='1'
31 [diag_musculo] State diagnosis on patient file (Musculoskeletal text
system)
Show the field ONLY if:
```

## diad_cardio (column)

```
Show the field ONLY if:
[diag_system(5)]='1'
32 [diad_cardio] State diagnosis on patient file (Cardiovascular text
system)
Show the field ONLY if:
```

## diag_integu (column)

```
Show the field ONLY if:
[diag_system(6)]='1'
33 [diag_integu] State diagnosis on patient file (Integumentary) text
Show the field ONLY if:
[diag_system(7)]='1'
```

## diag_reprod (column)

```
Show the field ONLY if:
[diag_system(7)]='1'
34 [diag_reprod] State diagnosis on patient file (Reproductive text
system)
Show the field ONLY if:
```

## hiv_status (column)

```
Show the field ONLY if:
[diag_system(8)]='1'
35 [hiv_status] 19. HIV Status radio
1 Negative
2 Positive
```

## indwel_inst___1 (column)

```
36 [indwel_inst] 20a. Did the patient have any indwelling checkbox
instrument during this admission?
1 indwel_inst___1 Urinary catheter
2 indwel_inst___2 IV cannula
3 indwel_inst___3 Central catheters
```

## indwel_inst___2 (column)

```
instrument during this admission?
1 indwel_inst___1 Urinary catheter
2 indwel_inst___2 IV cannula
3 indwel_inst___3 Central catheters
4 indwel_inst___4 Chest tubes
```

## indwel_inst___3 (column)

```
1 indwel_inst___1 Urinary catheter
2 indwel_inst___2 IV cannula
3 indwel_inst___3 Central catheters
4 indwel_inst___4 Chest tubes
5 indwel_inst___5 Abdominal drain
```

## indwel_inst___4 (column)

```
2 indwel_inst___2 IV cannula
3 indwel_inst___3 Central catheters
4 indwel_inst___4 Chest tubes
5 indwel_inst___5 Abdominal drain
6 indwel_inst___6 Cranial drain
```

## indwel_inst___5 (column)

```
3 indwel_inst___3 Central catheters
4 indwel_inst___4 Chest tubes
5 indwel_inst___5 Abdominal drain
6 indwel_inst___6 Cranial drain
7 indwel_inst___7 Intubation tubes
```

## indwel_inst___6 (column)

```
4 indwel_inst___4 Chest tubes
5 indwel_inst___5 Abdominal drain
6 indwel_inst___6 Cranial drain
7 indwel_inst___7 Intubation tubes
8 indwel_inst___8 Others
```

## indwel_inst___7 (column)

```
5 indwel_inst___5 Abdominal drain
6 indwel_inst___6 Cranial drain
7 indwel_inst___7 Intubation tubes
8 indwel_inst___8 Others
9 indwel_inst___9 None
```

## indwel_inst___8 (column)

```
6 indwel_inst___6 Cranial drain
7 indwel_inst___7 Intubation tubes
8 indwel_inst___8 Others
9 indwel_inst___9 None
37 [oth_indwel] Others, specify text
```

## indwel_inst___9 (column)

```
7 indwel_inst___7 Intubation tubes
8 indwel_inst___8 Others
9 indwel_inst___9 None
37 [oth_indwel] Others, specify text
Show the field ONLY if:
```

## oth_indwel (column)

```
8 indwel_inst___8 Others
9 indwel_inst___9 None
37 [oth_indwel] Others, specify text
Show the field ONLY if:
[indwel_inst(8)]='1'
```

## cormobid_condition (column)

```
Show the field ONLY if:
[indwel_inst(8)]='1'
38 [cormobid_condition] 20b. Does the patient have any underlying yesno
chronic co-morbid conditions?
1 Yes
```

## cormobidities___1 (column)

```
39 [cormobidities] 20c. If yes indicate the underlying chronic co- checkbox
morbid conditions (Select Multiple)
1 cormobidities___1 Diabetes
Show the field ONLY if:
[cormobid_condition] 2 cormobidities___2 HIV & AIDS
```

## cormobidities___2 (column)

```
1 cormobidities___1 Diabetes
Show the field ONLY if:
[cormobid_condition] 2 cormobidities___2 HIV & AIDS
='1'
3 cormobidities___3 Hypertension
```

## cormobidities___3 (column)

```
[cormobid_condition] 2 cormobidities___2 HIV & AIDS
='1'
3 cormobidities___3 Hypertension
4 cormobidities___4 Sickle Cell Disease
5 cormobidities___5 Cancer
```

## cormobidities___4 (column)

```
='1'
3 cormobidities___3 Hypertension
4 cormobidities___4 Sickle Cell Disease
5 cormobidities___5 Cancer
6 cormobidities___6 Chronic Kidney
```

## cormobidities___5 (column)

```
3 cormobidities___3 Hypertension
4 cormobidities___4 Sickle Cell Disease
5 cormobidities___5 Cancer
6 cormobidities___6 Chronic Kidney
Disease
```

## cormobidities___6 (column)

```
4 cormobidities___4 Sickle Cell Disease
5 cormobidities___5 Cancer
6 cormobidities___6 Chronic Kidney
Disease
https://idiredcap.idi.co.ug/redcap_v14.7.4/Design/data_dictionary_codebook.php?pid=147 5/48
```

## cormobidities___7 (column)

```
https://idiredcap.idi.co.ug/redcap_v14.7.4/Design/data_dictionary_codebook.php?pid=147 5/48
9/17/25, 11:25 AM GHS-CAMO-Net Project 3 Additional Data Collection | REDCap
7 cormobidities___7 Chronic Liver
Disease
8 cormobidities___8 Other
```

## cormobidities___8 (column)

```
7 cormobidities___7 Chronic Liver
Disease
8 cormobidities___8 Other
40 [other_comorbidities] Others specify text
Show the field ONLY if:
```

## other_comorbidities (column)

```
Disease
8 cormobidities___8 Other
40 [other_comorbidities] Others specify text
Show the field ONLY if:
[cormobidities(8)]='1'
```

## antibiotics (column)

```
Show the field ONLY if:
[ward]='10'
21 [antib_prior_admi] 15a. Was the patient on antibiotics prior to radio, Required
admission?
1 Yes
```

## antibiotics_prescribed___1 (column)

```
42 [antibiotics_prescribe 21b. If yes, list antibiotics prescribed. (Select checkbox
d] Multiple)
1 antibiotics_prescribed___1 Amikacin
Show the field ONLY if: 2 antibiotics_prescribed___2 Amoxicillin
[antibiotics]='1'
```

## antibiotics_prescribed___2 (column)

```
d] Multiple)
1 antibiotics_prescribed___1 Amikacin
Show the field ONLY if: 2 antibiotics_prescribed___2 Amoxicillin
[antibiotics]='1'
3 antibiotics_prescribed___3 Amoxicillin/C
```

## antibiotics_prescribed___3 (column)

```
Show the field ONLY if: 2 antibiotics_prescribed___2 Amoxicillin
[antibiotics]='1'
3 antibiotics_prescribed___3 Amoxicillin/C
acid
4 antibiotics_prescribed___4 Ampicillin
```

## antibiotics_prescribed___4 (column)

```
3 antibiotics_prescribed___3 Amoxicillin/C
acid
4 antibiotics_prescribed___4 Ampicillin
5 antibiotics_prescribed___5 Ampicillin/S
6 antibiotics_prescribed___6 Azithromyci
```

## antibiotics_prescribed___5 (column)

```
acid
4 antibiotics_prescribed___4 Ampicillin
5 antibiotics_prescribed___5 Ampicillin/S
6 antibiotics_prescribed___6 Azithromyci
7 antibiotics_prescribed___7 Aztreonam
```

## antibiotics_prescribed___6 (column)

```
4 antibiotics_prescribed___4 Ampicillin
5 antibiotics_prescribed___5 Ampicillin/S
6 antibiotics_prescribed___6 Azithromyci
7 antibiotics_prescribed___7 Aztreonam
8 antibiotics_prescribed___8 Cefepime
```

## antibiotics_prescribed___7 (column)

```
5 antibiotics_prescribed___5 Ampicillin/S
6 antibiotics_prescribed___6 Azithromyci
7 antibiotics_prescribed___7 Aztreonam
8 antibiotics_prescribed___8 Cefepime
9 antibiotics_prescribed___9 Cefixime
```

## antibiotics_prescribed___8 (column)

```
6 antibiotics_prescribed___6 Azithromyci
7 antibiotics_prescribed___7 Aztreonam
8 antibiotics_prescribed___8 Cefepime
9 antibiotics_prescribed___9 Cefixime
10 antibiotics_prescribed___10 Cefotaxime
```

## antibiotics_prescribed___9 (column)

```
7 antibiotics_prescribed___7 Aztreonam
8 antibiotics_prescribed___8 Cefepime
9 antibiotics_prescribed___9 Cefixime
10 antibiotics_prescribed___10 Cefotaxime
11 antibiotics_prescribed___11 Cefoxitin
```

## antibiotics_prescribed___10 (column)

```
8 antibiotics_prescribed___8 Cefepime
9 antibiotics_prescribed___9 Cefixime
10 antibiotics_prescribed___10 Cefotaxime
11 antibiotics_prescribed___11 Cefoxitin
12 antibiotics_prescribed___12 Ceftazidime
```

## antibiotics_prescribed___11 (column)

```
9 antibiotics_prescribed___9 Cefixime
10 antibiotics_prescribed___10 Cefotaxime
11 antibiotics_prescribed___11 Cefoxitin
12 antibiotics_prescribed___12 Ceftazidime
13 antibiotics_prescribed___13 Ceftriaxone
```

## antibiotics_prescribed___12 (column)

```
10 antibiotics_prescribed___10 Cefotaxime
11 antibiotics_prescribed___11 Cefoxitin
12 antibiotics_prescribed___12 Ceftazidime
13 antibiotics_prescribed___13 Ceftriaxone
14 antibiotics_prescribed___14 Ceftriaxone-
```

## antibiotics_prescribed___13 (column)

```
11 antibiotics_prescribed___11 Cefoxitin
12 antibiotics_prescribed___12 Ceftazidime
13 antibiotics_prescribed___13 Ceftriaxone
14 antibiotics_prescribed___14 Ceftriaxone-
salbactam
```

## antibiotics_prescribed___14 (column)

```
12 antibiotics_prescribed___12 Ceftazidime
13 antibiotics_prescribed___13 Ceftriaxone
14 antibiotics_prescribed___14 Ceftriaxone-
salbactam
15 antibiotics_prescribed___15 Cefuroxime
```

## antibiotics_prescribed___15 (column)

```
14 antibiotics_prescribed___14 Ceftriaxone-
salbactam
15 antibiotics_prescribed___15 Cefuroxime
16 antibiotics_prescribed___16 Chloramphe
17 antibiotics_prescribed___17 Ciprofloxaci
```

## antibiotics_prescribed___16 (column)

```
salbactam
15 antibiotics_prescribed___15 Cefuroxime
16 antibiotics_prescribed___16 Chloramphe
17 antibiotics_prescribed___17 Ciprofloxaci
18 antibiotics_prescribed___18 Clindamycin
```

## antibiotics_prescribed___17 (column)

```
15 antibiotics_prescribed___15 Cefuroxime
16 antibiotics_prescribed___16 Chloramphe
17 antibiotics_prescribed___17 Ciprofloxaci
18 antibiotics_prescribed___18 Clindamycin
19 antibiotics_prescribed___19 Cofotaxime
```

## antibiotics_prescribed___18 (column)

```
16 antibiotics_prescribed___16 Chloramphe
17 antibiotics_prescribed___17 Ciprofloxaci
18 antibiotics_prescribed___18 Clindamycin
19 antibiotics_prescribed___19 Cofotaxime
20 antibiotics_prescribed___20 Doripenem
```

## antibiotics_prescribed___19 (column)

```
17 antibiotics_prescribed___17 Ciprofloxaci
18 antibiotics_prescribed___18 Clindamycin
19 antibiotics_prescribed___19 Cofotaxime
20 antibiotics_prescribed___20 Doripenem
21 antibiotics_prescribed___21 Doxycycline
```

## antibiotics_prescribed___20 (column)

```
18 antibiotics_prescribed___18 Clindamycin
19 antibiotics_prescribed___19 Cofotaxime
20 antibiotics_prescribed___20 Doripenem
21 antibiotics_prescribed___21 Doxycycline
22 antibiotics_prescribed___22 Ertapenem
```

## antibiotics_prescribed___21 (column)

```
19 antibiotics_prescribed___19 Cofotaxime
20 antibiotics_prescribed___20 Doripenem
21 antibiotics_prescribed___21 Doxycycline
22 antibiotics_prescribed___22 Ertapenem
23 antibiotics_prescribed___23 Erythromyci
```

## antibiotics_prescribed___22 (column)

```
20 antibiotics_prescribed___20 Doripenem
21 antibiotics_prescribed___21 Doxycycline
22 antibiotics_prescribed___22 Ertapenem
23 antibiotics_prescribed___23 Erythromyci
24 antibiotics_prescribed___24 Gentamicin
```

## antibiotics_prescribed___23 (column)

```
21 antibiotics_prescribed___21 Doxycycline
22 antibiotics_prescribed___22 Ertapenem
23 antibiotics_prescribed___23 Erythromyci
24 antibiotics_prescribed___24 Gentamicin
25 antibiotics_prescribed___25 Imipenem
```

## antibiotics_prescribed___24 (column)

```
22 antibiotics_prescribed___22 Ertapenem
23 antibiotics_prescribed___23 Erythromyci
24 antibiotics_prescribed___24 Gentamicin
25 antibiotics_prescribed___25 Imipenem
26 antibiotics_prescribed___26 Levofloxacin
```

## antibiotics_prescribed___25 (column)

```
23 antibiotics_prescribed___23 Erythromyci
24 antibiotics_prescribed___24 Gentamicin
25 antibiotics_prescribed___25 Imipenem
26 antibiotics_prescribed___26 Levofloxacin
27 antibiotics_prescribed___27 Linezolid
```

## antibiotics_prescribed___26 (column)

```
24 antibiotics_prescribed___24 Gentamicin
25 antibiotics_prescribed___25 Imipenem
26 antibiotics_prescribed___26 Levofloxacin
27 antibiotics_prescribed___27 Linezolid
28 antibiotics_prescribed___28 Meropenem
```

## antibiotics_prescribed___27 (column)

```
25 antibiotics_prescribed___25 Imipenem
26 antibiotics_prescribed___26 Levofloxacin
27 antibiotics_prescribed___27 Linezolid
28 antibiotics_prescribed___28 Meropenem
29 antibiotics_prescribed___29 Nalidixic aci
```

## antibiotics_prescribed___28 (column)

```
26 antibiotics_prescribed___26 Levofloxacin
27 antibiotics_prescribed___27 Linezolid
28 antibiotics_prescribed___28 Meropenem
29 antibiotics_prescribed___29 Nalidixic aci
30 antibiotics_prescribed___30 Nitrofuranto
```

## antibiotics_prescribed___29 (column)

```
27 antibiotics_prescribed___27 Linezolid
28 antibiotics_prescribed___28 Meropenem
29 antibiotics_prescribed___29 Nalidixic aci
30 antibiotics_prescribed___30 Nitrofuranto
31 antibiotics_prescribed___31 Oxacillin
```

## antibiotics_prescribed___30 (column)

```
28 antibiotics_prescribed___28 Meropenem
29 antibiotics_prescribed___29 Nalidixic aci
30 antibiotics_prescribed___30 Nitrofuranto
31 antibiotics_prescribed___31 Oxacillin
32 antibiotics_prescribed___32 Penicillin G
```

## antibiotics_prescribed___31 (column)

```
29 antibiotics_prescribed___29 Nalidixic aci
30 antibiotics_prescribed___30 Nitrofuranto
31 antibiotics_prescribed___31 Oxacillin
32 antibiotics_prescribed___32 Penicillin G
33 antibiotics_prescribed___33 Piperacillin
```

## antibiotics_prescribed___32 (column)

```
30 antibiotics_prescribed___30 Nitrofuranto
31 antibiotics_prescribed___31 Oxacillin
32 antibiotics_prescribed___32 Penicillin G
33 antibiotics_prescribed___33 Piperacillin
https://idiredcap.idi.co.ug/redcap_v14.7.4/Design/data_dictionary_codebook.php?pid=147 6/48
```

## antibiotics_prescribed___33 (column)

```
31 antibiotics_prescribed___31 Oxacillin
32 antibiotics_prescribed___32 Penicillin G
33 antibiotics_prescribed___33 Piperacillin
https://idiredcap.idi.co.ug/redcap_v14.7.4/Design/data_dictionary_codebook.php?pid=147 6/48
9/17/25, 11:25 AM GHS-CAMO-Net Project 3 Additional Data Collection | REDCap
```

## antibiotics_prescribed___34 (column)

```
https://idiredcap.idi.co.ug/redcap_v14.7.4/Design/data_dictionary_codebook.php?pid=147 6/48
9/17/25, 11:25 AM GHS-CAMO-Net Project 3 Additional Data Collection | REDCap
34 antibiotics_prescribed___34 Piperacillin
tazobactam
35 antibiotics_prescribed___35 Rifampin
```

## antibiotics_prescribed___35 (column)

```
34 antibiotics_prescribed___34 Piperacillin
tazobactam
35 antibiotics_prescribed___35 Rifampin
36 antibiotics_prescribed___36 Streptomyci
37 antibiotics_prescribed___37 Tetracycline
```

## antibiotics_prescribed___36 (column)

```
tazobactam
35 antibiotics_prescribed___35 Rifampin
36 antibiotics_prescribed___36 Streptomyci
37 antibiotics_prescribed___37 Tetracycline
38 antibiotics_prescribed___38 Tigecycline
```

## antibiotics_prescribed___37 (column)

```
35 antibiotics_prescribed___35 Rifampin
36 antibiotics_prescribed___36 Streptomyci
37 antibiotics_prescribed___37 Tetracycline
38 antibiotics_prescribed___38 Tigecycline
39 antibiotics_prescribed___39 Trimethopri
```

## antibiotics_prescribed___38 (column)

```
36 antibiotics_prescribed___36 Streptomyci
37 antibiotics_prescribed___37 Tetracycline
38 antibiotics_prescribed___38 Tigecycline
39 antibiotics_prescribed___39 Trimethopri
Sulfamethox
```

## antibiotics_prescribed___39 (column)

```
37 antibiotics_prescribed___37 Tetracycline
38 antibiotics_prescribed___38 Tigecycline
39 antibiotics_prescribed___39 Trimethopri
Sulfamethox
40 antibiotics_prescribed___40 Vancomycin
```

## antibiotics_prescribed___40 (column)

```
39 antibiotics_prescribed___39 Trimethopri
Sulfamethox
40 antibiotics_prescribed___40 Vancomycin
41 antibiotics_prescribed___41 Others
43 [other_antibiotic] Other antibiotic text
```

## antibiotics_prescribed___41 (column)

```
Sulfamethox
40 antibiotics_prescribed___40 Vancomycin
41 antibiotics_prescribed___41 Others
43 [other_antibiotic] Other antibiotic text
Show the field ONLY if:
```

## other_antibiotic (column)

```
40 antibiotics_prescribed___40 Vancomycin
41 antibiotics_prescribed___41 Others
43 [other_antibiotic] Other antibiotic text
Show the field ONLY if:
[antibiotics_prescribed
```

## start_date_antib (column)

```
[antibiotics_prescribed
(41)]='1'
44 [start_date_antib] 21c. If antibiotics were not prescribed on the text (date_dmy)
date of admission, state the start date for
Show the field ONLY if:
```

## clin_param___1 (column)

```
[antibiotics]='0'
45 [clin_param] 22. Which clinical parameters were monitored? checkbox
1 clin_param___1 Blood pressure (BP)
2 clin_param___2 Pulse
3 clin_param___3 Temperature
```

## clin_param___2 (column)

```
45 [clin_param] 22. Which clinical parameters were monitored? checkbox
1 clin_param___1 Blood pressure (BP)
2 clin_param___2 Pulse
3 clin_param___3 Temperature
4 clin_param___4 Respiratory Rate (RR)
```

## clin_param___3 (column)

```
1 clin_param___1 Blood pressure (BP)
2 clin_param___2 Pulse
3 clin_param___3 Temperature
4 clin_param___4 Respiratory Rate (RR)
5 clin_param___5 Oxygen saturation
```

## clin_param___4 (column)

```
2 clin_param___2 Pulse
3 clin_param___3 Temperature
4 clin_param___4 Respiratory Rate (RR)
5 clin_param___5 Oxygen saturation
(Spo2)
```

## clin_param___5 (column)

```
3 clin_param___3 Temperature
4 clin_param___4 Respiratory Rate (RR)
5 clin_param___5 Oxygen saturation
(Spo2)
6 clin_param___6 Glasgow Coma Scale
```

## clin_param___6 (column)

```
5 clin_param___5 Oxygen saturation
(Spo2)
6 clin_param___6 Glasgow Coma Scale
(GCS)
7 clin_param___7 Other
```

## clin_param___7 (column)

```
6 clin_param___6 Glasgow Coma Scale
(GCS)
7 clin_param___7 Other
46 [bp_type] Specify the BP checkbox
1 bp_type___1 Systolic BP
```

## bp_type___1 (column)

```
7 clin_param___7 Other
46 [bp_type] Specify the BP checkbox
1 bp_type___1 Systolic BP
Show the field ONLY if:
[clin_param(1)]='1' 2 bp_type___2 Diastolic BP
```

## bp_type___2 (column)

```
1 bp_type___1 Systolic BP
Show the field ONLY if:
[clin_param(1)]='1' 2 bp_type___2 Diastolic BP
47 [systolic_bp_baseline] Systolic BP reading on admission text
Show the field ONLY if:
```

## systolic_bp_baseline (column)

```
Show the field ONLY if:
[clin_param(1)]='1' 2 bp_type___2 Diastolic BP
47 [systolic_bp_baseline] Systolic BP reading on admission text
Show the field ONLY if:
[bp_type(1)]='1'
```

## sysbp_samplecoll (column)

```
Show the field ONLY if:
[bp_type(1)]='1'
48 [sysbp_samplecoll] Systolic BP reading at time of sample collection text (number)
Show the field ONLY if:
[bp_type(1)]='1'
```

## disatbp_admit (column)

```
Show the field ONLY if:
[bp_type(1)]='1'
49 [disatbp_admit] Diastolic BP on admission text (number)
Show the field ONLY if:
[bp_type(2)]='1'
```

## pulse_baseline (column)

```
Show the field ONLY if:
[bp_type(2)]='1'
51 [pulse_baseline] Pulse reading on admission text
Show the field ONLY if:
[clin_param(2)]='1'
```

## pulse_discharge (column)

```
Show the field ONLY if:
[clin_param(2)]='1'
52 [pulse_discharge] Pulse reading at time of sample collection text
Show the field ONLY if:
https://idiredcap.idi.co.ug/redcap_v14.7.4/Design/data_dictionary_codebook.php?pid=147 7/48
```

## temp_baseline (column)

```
9/17/25, 11:25 AM GHS-CAMO-Net Project 3 Additional Data Collection | REDCap
[clin_param(2)]='1'
53 [temp_baseline] Temperature reading on admission text
Show the field ONLY if:
[clin_param(3)]='1'
```

## temp_discharge (column)

```
Show the field ONLY if:
[clin_param(3)]='1'
54 [temp_discharge] Temp reading at time of sample collection text
Show the field ONLY if:
[clin_param(3)]='1'
```

## rr_baseline (column)

```
Show the field ONLY if:
[clin_param(3)]='1'
55 [rr_baseline] RR reading on admission text
Show the field ONLY if:
[clin_param(4)]='1'
```

## rr_discharge (column)

```
Show the field ONLY if:
[clin_param(4)]='1'
56 [rr_discharge] RR reading at time of sample collection text
Show the field ONLY if:
[clin_param(4)]='1'
```

## spo2_baseline (column)

```
Show the field ONLY if:
[clin_param(4)]='1'
57 [spo2_baseline] Spo2 reading on admission text
Show the field ONLY if:
[clin_param(5)]='1'
```

## spo2_discharge (column)

```
Show the field ONLY if:
[clin_param(5)]='1'
58 [spo2_discharge] Spo2 reading at time of sample collection text
Show the field ONLY if:
[clin_param(5)]='1'
```

## gcs_baseline (column)

```
Show the field ONLY if:
[clin_param(5)]='1'
59 [gcs_baseline] GCS reading on admission text
Show the field ONLY if:
[clin_param(6)]='1'
```

## gcs_discharge (column)

```
Show the field ONLY if:
[clin_param(6)]='1'
60 [gcs_discharge] GCS reading at time of sample collection text
Show the field ONLY if:
[clin_param(6)]='1'
```

## other_param (column)

```
Show the field ONLY if:
[clin_param(6)]='1'
61 [other_param] Other clinical parameter monitored. text
Show the field ONLY if:
[clin_param(7)]='1'
```

## other_baseline (column)

```
Show the field ONLY if:
[clin_param(7)]='1'
62 [other_baseline] Other reading on admission text
Show the field ONLY if:
[clin_param(7)]='1'
```

## other_discharge (column)

```
Show the field ONLY if:
[clin_param(7)]='1'
63 [other_discharge] Other reading at time of sample collection text
Show the field ONLY if:
[clin_param(7)]='1'
```

## culture_and_sensitivity (column)

```
1 Blood
Show the field ONLY if:
[culture_and_sensitivity] 2 Urine
='1'
3 Stool
```

## specimen_type (column)

```
1 Yes
0 No
65 [specimen_type] 24. Specimen/sample type radio, Required
1 Blood
Show the field ONLY if:
```

## oth_spectype (column)

```
https://idiredcap.idi.co.ug/redcap_v14.7.4/Design/data_dictionary_codebook.php?pid=147 8/48
9/17/25, 11:25 AM GHS-CAMO-Net Project 3 Additional Data Collection | REDCap
66 [oth_spectype] Others, please specify text
Show the field ONLY if:
[specimen_type]='8'
```

## collection_date (column)

```
Show the field ONLY if:
[specimen_type]='8'
67 [collection_date] 25. Date of sample collection text (date_dmy)
Show the field ONLY if:
[culture_and_sensitivity]
```

## growth1 (column)

```
[culture_and_sensitivity]
='1'
68 [growth1] 26a. If culture was done, was there growth? yesno
1 Yes
Show the field ONLY if:
```

## organism_isolated (column)

```
[culture_and_sensitivity] 0 No
='1'
69 [organism_isolated] 26b. If yes, how many organisms were radio
isolated?
1 1
```

## first_organism (column)

```
[growth1]='1' 2 2
3 3
70 [first_organism] 27a. First organism isolated text
Show the field ONLY if:
[organism_isolated]>=1
```

## ast_anti1___1 (column)

```
[organism_isolated]>=1
71 [ast_anti1] 27b. Antibiotics set for AST checkbox
1 ast_anti1___1 Amikacin
Show the field ONLY if:
[organism_isolated]>=1 2 ast_anti1___2 Amoxicillin
```

## ast_anti1___2 (column)

```
1 ast_anti1___1 Amikacin
Show the field ONLY if:
[organism_isolated]>=1 2 ast_anti1___2 Amoxicillin
3 ast_anti1___3 Amoxicillin/Clavulanic
acid
```

## ast_anti1___3 (column)

```
Show the field ONLY if:
[organism_isolated]>=1 2 ast_anti1___2 Amoxicillin
3 ast_anti1___3 Amoxicillin/Clavulanic
acid
4 ast_anti1___4 Ampicillin
```

## ast_anti1___4 (column)

```
3 ast_anti1___3 Amoxicillin/Clavulanic
acid
4 ast_anti1___4 Ampicillin
5 ast_anti1___5 Ampicillin/Sulbactam
6 ast_anti1___6 Azithromycin
```

## ast_anti1___5 (column)

```
acid
4 ast_anti1___4 Ampicillin
5 ast_anti1___5 Ampicillin/Sulbactam
6 ast_anti1___6 Azithromycin
7 ast_anti1___7 Aztreonam
```

## ast_anti1___6 (column)

```
4 ast_anti1___4 Ampicillin
5 ast_anti1___5 Ampicillin/Sulbactam
6 ast_anti1___6 Azithromycin
7 ast_anti1___7 Aztreonam
8 ast_anti1___8 Cefepime
```

## ast_anti1___7 (column)

```
5 ast_anti1___5 Ampicillin/Sulbactam
6 ast_anti1___6 Azithromycin
7 ast_anti1___7 Aztreonam
8 ast_anti1___8 Cefepime
9 ast_anti1___9 Cefixime
```

## ast_anti1___8 (column)

```
6 ast_anti1___6 Azithromycin
7 ast_anti1___7 Aztreonam
8 ast_anti1___8 Cefepime
9 ast_anti1___9 Cefixime
10 ast_anti1___10 Cefotaxime
```

## ast_anti1___9 (column)

```
7 ast_anti1___7 Aztreonam
8 ast_anti1___8 Cefepime
9 ast_anti1___9 Cefixime
10 ast_anti1___10 Cefotaxime
11 ast_anti1___11 Cefoxitin
```

## ast_anti1___10 (column)

```
8 ast_anti1___8 Cefepime
9 ast_anti1___9 Cefixime
10 ast_anti1___10 Cefotaxime
11 ast_anti1___11 Cefoxitin
12 ast_anti1___12 Ceftazidime
```

## ast_anti1___11 (column)

```
9 ast_anti1___9 Cefixime
10 ast_anti1___10 Cefotaxime
11 ast_anti1___11 Cefoxitin
12 ast_anti1___12 Ceftazidime
13 ast_anti1___13 Ceftriaxone
```

## ast_anti1___12 (column)

```
10 ast_anti1___10 Cefotaxime
11 ast_anti1___11 Cefoxitin
12 ast_anti1___12 Ceftazidime
13 ast_anti1___13 Ceftriaxone
14 ast_anti1___14 Ceftriaxone-
```

## ast_anti1___13 (column)

```
11 ast_anti1___11 Cefoxitin
12 ast_anti1___12 Ceftazidime
13 ast_anti1___13 Ceftriaxone
14 ast_anti1___14 Ceftriaxone-
salbactam
```

## ast_anti1___14 (column)

```
12 ast_anti1___12 Ceftazidime
13 ast_anti1___13 Ceftriaxone
14 ast_anti1___14 Ceftriaxone-
salbactam
15 ast_anti1___15 Cefuroxime
```

## ast_anti1___15 (column)

```
14 ast_anti1___14 Ceftriaxone-
salbactam
15 ast_anti1___15 Cefuroxime
16 ast_anti1___16 Chlorampenicol
17 ast_anti1___17 Ciprofloxacin
```

## ast_anti1___16 (column)

```
salbactam
15 ast_anti1___15 Cefuroxime
16 ast_anti1___16 Chlorampenicol
17 ast_anti1___17 Ciprofloxacin
18 ast_anti1___18 Clindamycin
```

## ast_anti1___17 (column)

```
15 ast_anti1___15 Cefuroxime
16 ast_anti1___16 Chlorampenicol
17 ast_anti1___17 Ciprofloxacin
18 ast_anti1___18 Clindamycin
19 ast_anti1___19 Cofotaxime
```

## ast_anti1___18 (column)

```
16 ast_anti1___16 Chlorampenicol
17 ast_anti1___17 Ciprofloxacin
18 ast_anti1___18 Clindamycin
19 ast_anti1___19 Cofotaxime
20 ast_anti1___20 Doripenem
```

## ast_anti1___19 (column)

```
17 ast_anti1___17 Ciprofloxacin
18 ast_anti1___18 Clindamycin
19 ast_anti1___19 Cofotaxime
20 ast_anti1___20 Doripenem
21 ast_anti1___21 Doxycycline
```

## ast_anti1___20 (column)

```
18 ast_anti1___18 Clindamycin
19 ast_anti1___19 Cofotaxime
20 ast_anti1___20 Doripenem
21 ast_anti1___21 Doxycycline
22 ast_anti1___22 Ertapenem
```

## ast_anti1___21 (column)

```
19 ast_anti1___19 Cofotaxime
20 ast_anti1___20 Doripenem
21 ast_anti1___21 Doxycycline
22 ast_anti1___22 Ertapenem
23 ast_anti1___23 Erythromycin
```

## ast_anti1___22 (column)

```
20 ast_anti1___20 Doripenem
21 ast_anti1___21 Doxycycline
22 ast_anti1___22 Ertapenem
23 ast_anti1___23 Erythromycin
24 ast_anti1___24 Gentamicin
```

## ast_anti1___23 (column)

```
21 ast_anti1___21 Doxycycline
22 ast_anti1___22 Ertapenem
23 ast_anti1___23 Erythromycin
24 ast_anti1___24 Gentamicin
25 ast_anti1___25 Imipenem
```

## ast_anti1___24 (column)

```
22 ast_anti1___22 Ertapenem
23 ast_anti1___23 Erythromycin
24 ast_anti1___24 Gentamicin
25 ast_anti1___25 Imipenem
https://idiredcap.idi.co.ug/redcap_v14.7.4/Design/data_dictionary_codebook.php?pid=147 9/48
```

## ast_anti1___25 (column)

```
23 ast_anti1___23 Erythromycin
24 ast_anti1___24 Gentamicin
25 ast_anti1___25 Imipenem
https://idiredcap.idi.co.ug/redcap_v14.7.4/Design/data_dictionary_codebook.php?pid=147 9/48
9/17/25, 11:25 AM GHS-CAMO-Net Project 3 Additional Data Collection | REDCap
```

## ast_anti1___26 (column)

```
https://idiredcap.idi.co.ug/redcap_v14.7.4/Design/data_dictionary_codebook.php?pid=147 9/48
9/17/25, 11:25 AM GHS-CAMO-Net Project 3 Additional Data Collection | REDCap
26 ast_anti1___26 Levofloxacin
27 ast_anti1___27 Linezolid
28 ast_anti1___28 Meropenem
```

## ast_anti1___27 (column)

```
9/17/25, 11:25 AM GHS-CAMO-Net Project 3 Additional Data Collection | REDCap
26 ast_anti1___26 Levofloxacin
27 ast_anti1___27 Linezolid
28 ast_anti1___28 Meropenem
29 ast_anti1___29 Nalidixic acid
```

## ast_anti1___28 (column)

```
26 ast_anti1___26 Levofloxacin
27 ast_anti1___27 Linezolid
28 ast_anti1___28 Meropenem
29 ast_anti1___29 Nalidixic acid
30 ast_anti1___30 Nitrofurantoin
```

## ast_anti1___29 (column)

```
27 ast_anti1___27 Linezolid
28 ast_anti1___28 Meropenem
29 ast_anti1___29 Nalidixic acid
30 ast_anti1___30 Nitrofurantoin
31 ast_anti1___31 Oxacillin
```

## ast_anti1___30 (column)

```
28 ast_anti1___28 Meropenem
29 ast_anti1___29 Nalidixic acid
30 ast_anti1___30 Nitrofurantoin
31 ast_anti1___31 Oxacillin
32 ast_anti1___32 Penicillin G
```

## ast_anti1___31 (column)

```
29 ast_anti1___29 Nalidixic acid
30 ast_anti1___30 Nitrofurantoin
31 ast_anti1___31 Oxacillin
32 ast_anti1___32 Penicillin G
33 ast_anti1___33 Piperacillin
```

## ast_anti1___32 (column)

```
30 ast_anti1___30 Nitrofurantoin
31 ast_anti1___31 Oxacillin
32 ast_anti1___32 Penicillin G
33 ast_anti1___33 Piperacillin
34 ast_anti1___34 Piperacillin
```

## ast_anti1___33 (column)

```
31 ast_anti1___31 Oxacillin
32 ast_anti1___32 Penicillin G
33 ast_anti1___33 Piperacillin
34 ast_anti1___34 Piperacillin
tazobactam
```

## ast_anti1___34 (column)

```
32 ast_anti1___32 Penicillin G
33 ast_anti1___33 Piperacillin
34 ast_anti1___34 Piperacillin
tazobactam
35 ast_anti1___35 Rifampin
```

## ast_anti1___35 (column)

```
34 ast_anti1___34 Piperacillin
tazobactam
35 ast_anti1___35 Rifampin
36 ast_anti1___36 Streptomycin
37 ast_anti1___37 Tetracycline
```

## ast_anti1___36 (column)

```
tazobactam
35 ast_anti1___35 Rifampin
36 ast_anti1___36 Streptomycin
37 ast_anti1___37 Tetracycline
38 ast_anti1___38 Tigecycline
```

## ast_anti1___37 (column)

```
35 ast_anti1___35 Rifampin
36 ast_anti1___36 Streptomycin
37 ast_anti1___37 Tetracycline
38 ast_anti1___38 Tigecycline
39 ast_anti1___39 Trimethoprim/
```

## ast_anti1___38 (column)

```
36 ast_anti1___36 Streptomycin
37 ast_anti1___37 Tetracycline
38 ast_anti1___38 Tigecycline
39 ast_anti1___39 Trimethoprim/
Sulfamethoxazole
```

## ast_anti1___39 (column)

```
37 ast_anti1___37 Tetracycline
38 ast_anti1___38 Tigecycline
39 ast_anti1___39 Trimethoprim/
Sulfamethoxazole
40 ast_anti1___40 Vancomycin
```

## ast_anti1___40 (column)

```
39 ast_anti1___39 Trimethoprim/
Sulfamethoxazole
40 ast_anti1___40 Vancomycin
41 ast_anti1___41 Others1
42 ast_anti1___42 Others2
```

## ast_anti1___41 (column)

```
Sulfamethoxazole
40 ast_anti1___40 Vancomycin
41 ast_anti1___41 Others1
42 ast_anti1___42 Others2
72 [first_amikacin] Amikacin radio (Matrix)
```

## ast_anti1___42 (column)

```
40 ast_anti1___40 Vancomycin
41 ast_anti1___41 Others1
42 ast_anti1___42 Others2
72 [first_amikacin] Amikacin radio (Matrix)
1 Resistant
```

## first_amikacin (column)

```
41 ast_anti1___41 Others1
42 ast_anti1___42 Others2
72 [first_amikacin] Amikacin radio (Matrix)
1 Resistant
Show the field ONLY if:
```

## first_amoxicillin (column)

```
[ast_anti1(1)]='1' 2 Intermediate
3 Susceptible
73 [first_amoxicillin] Amoxicillin radio (Matrix)
1 Resistant
Show the field ONLY if:
```

## first_amoxiclav (column)

```
[ast_anti1(2)]='1' 2 Intermediate
3 Susceptible
74 [first_amoxiclav] Amoxicillin/Clavulanic acid radio (Matrix)
1 Resistant
Show the field ONLY if:
```

## first_ampicillin (column)

```
[ast_anti1(3)]='1' 2 Intermediate
3 Susceptible
75 [first_ampicillin] Ampicillin radio (Matrix)
1 Resistant
Show the field ONLY if:
```

## first_amp_sulbactam (column)

```
[ast_anti1(4)]='1' 2 Intermediate
3 Susceptible
76 [first_amp_sulbactam] Ampicillin/Sulbactam radio (Matrix)
1 Resistant
Show the field ONLY if:
```

## first_azithromycin (column)

```
[ast_anti1(5)]='1' 2 Intermediate
3 Susceptible
77 [first_azithromycin] Azithromycin radio (Matrix)
1 Resistant
Show the field ONLY if:
```

## first_aztreonam (column)

```
[ast_anti1(6)]='1' 2 Intermediate
3 Susceptible
78 [first_aztreonam] Aztreonam radio (Matrix)
https://idiredcap.idi.co.ug/redcap_v14.7.4/Design/data_dictionary_codebook.php?pid=147 10/48
9/17/25, 11:25 AM GHS-CAMO-Net Project 3 Additional Data Collection | REDCap
```

## first_cefepime (column)

```
2 Intermediate
3 Susceptible
79 [first_cefepime] Cefepime radio (Matrix)
1 Resistant
Show the field ONLY if:
```

## first_cefixime (column)

```
[ast_anti1(8)]='1' 2 Intermediate
3 Susceptible
80 [first_cefixime] Cefixime radio (Matrix)
1 Resistant
Show the field ONLY if:
```

## first_cefotaxime (column)

```
[ast_anti1(9)]='1' 2 Intermediate
3 Susceptible
81 [first_cefotaxime] Cefotaxime radio (Matrix)
1 Resistant
Show the field ONLY if:
```

## first_cefoxitin (column)

```
[ast_anti1(10)]='1' 2 Intermediate
3 Susceptible
82 [first_cefoxitin] Cefoxitin radio (Matrix)
1 Resistant
Show the field ONLY if:
```

## first_ceftazidime (column)

```
[ast_anti1(11)]='1' 2 Intermediate
3 Susceptible
83 [first_ceftazidime] Ceftazidime radio (Matrix)
1 Resistant
Show the field ONLY if:
```

## first_ceftriaxone (column)

```
[ast_anti1(12)]='1' 2 Intermediate
3 Susceptible
84 [first_ceftriaxone] Ceftriaxone radio (Matrix)
1 Resistant
Show the field ONLY if:
```

## first_cefsalbactam (column)

```
[ast_anti1(13)]='1' 2 Intermediate
3 Susceptible
85 [first_cefsalbactam] Ceftriaxone-salbactam radio (Matrix)
1 Resistant
Show the field ONLY if:
```

## first_cefuroxime (column)

```
[ast_anti1(14)]='1' 2 Intermediate
3 Susceptible
86 [first_cefuroxime] Cefuroxime radio (Matrix)
1 Resistant
Show the field ONLY if:
```

## first_ciprofloxacin (column)

```
[ast_anti1(16)]='1'
3 Susceptible
88 [first_ciprofloxacin] Ciprofloxacin radio (Matrix)
1 Resistant
Show the field ONLY if:
```

## first_clindamycin (column)

```
https://idiredcap.idi.co.ug/redcap_v14.7.4/Design/data_dictionary_codebook.php?pid=147 11/48
9/17/25, 11:25 AM GHS-CAMO-Net Project 3 Additional Data Collection | REDCap
89 [first_clindamycin] Clindamycin radio (Matrix)
1 Resistant
Show the field ONLY if:
```

## first_cofotaxime (column)

```
[ast_anti1(18)]='1' 2 Intermediate
3 Susceptible
90 [first_cofotaxime] Cofotaxime radio (Matrix)
1 Resistant
Show the field ONLY if:
```

## first_doripenem (column)

```
[ast_anti1(19)]='1' 2 Intermediate
3 Susceptible
91 [first_doripenem] Doripenem radio (Matrix)
1 Resistant
Show the field ONLY if:
```

## first_doxycycline (column)

```
[ast_anti1(20)]='1' 2 Intermediate
3 Susceptible
92 [first_doxycycline] Doxycycline radio (Matrix)
1 Resistant
Show the field ONLY if:
```

## first_ertapenem (column)

```
[ast_anti1(21)]='1' 2 Intermediate
3 Susceptible
93 [first_ertapenem] Ertapenem radio (Matrix)
1 Resistant
Show the field ONLY if:
```

## first_erythromycin (column)

```
[ast_anti1(22)]='1' 2 Intermediate
3 Susceptible
94 [first_erythromycin] Erythromycin radio (Matrix)
1 Resistant
Show the field ONLY if:
```

## first_gentamicin (column)

```
[ast_anti1(23)]='1' 2 Intermediate
3 Susceptible
95 [first_gentamicin] Gentamicin radio (Matrix)
1 Resistant
Show the field ONLY if:
```

## first_imipenem (column)

```
[ast_anti1(24)]='1' 2 Intermediate
3 Susceptible
96 [first_imipenem] Imipenem radio (Matrix)
1 Resistant
Show the field ONLY if:
```

## first_levofloxacin (column)

```
[ast_anti1(25)]='1' 2 Intermediate
3 Susceptible
97 [first_levofloxacin] Levofloxacin radio (Matrix)
1 Resistant
Show the field ONLY if:
```

## first_linezolid (column)

```
[ast_anti1(26)]='1' 2 Intermediate
3 Susceptible
98 [first_linezolid] Linezolid radio (Matrix)
1 Resistant
Show the field ONLY if:
```

## first_meropenem (column)

```
https://idiredcap.idi.co.ug/redcap_v14.7.4/Design/data_dictionary_codebook.php?pid=147 12/48
9/17/25, 11:25 AM GHS-CAMO-Net Project 3 Additional Data Collection | REDCap
99 [first_meropenem] Meropenem radio (Matrix)
1 Resistant
Show the field ONLY if:
```

## first_nalidixicacid (column)

```
[ast_anti1(28)]='1' 2 Intermediate
3 Susceptible
100 [first_nalidixicacid] Nalidixic acid radio (Matrix)
1 Resistant
Show the field ONLY if:
```

## first_nitrofurantoin (column)

```
[ast_anti1(29)]='1' 2 Intermediate
3 Susceptible
101 [first_nitrofurantoin] Nitrofurantoin radio (Matrix)
1 Resistant
Show the field ONLY if:
```

## first_oxacillin (column)

```
[ast_anti1(30)]='1' 2 Intermediate
3 Susceptible
102 [first_oxacillin] Oxacillin radio (Matrix)
1 Resistant
Show the field ONLY if:
```

## first_pen_g (column)

```
[ast_anti1(31)]='1' 2 Intermediate
3 Susceptible
103 [first_pen_g] Penicillin G radio (Matrix)
1 Resistant
Show the field ONLY if:
```

## first_piperacillin (column)

```
[ast_anti1(32)]='1' 2 Intermediate
3 Susceptible
104 [first_piperacillin] Piperacillin radio (Matrix)
1 Resistant
Show the field ONLY if:
```

## first_pip_tazobactam (column)

```
[ast_anti1(33)]='1' 2 Intermediate
3 Susceptible
105 [first_pip_tazobactam] Piperacillin tazobactam radio (Matrix)
1 Resistant
Show the field ONLY if:
```

## first_rifampin (column)

```
[ast_anti1(34)]='1' 2 Intermediate
3 Susceptible
106 [first_rifampin] Rifampin radio (Matrix)
1 Resistant
Show the field ONLY if:
```

## first_streptomycin (column)

```
[ast_anti1(35)]='1' 2 Intermediate
3 Susceptible
107 [first_streptomycin] Streptomycin radio (Matrix)
1 Resistant
Show the field ONLY if:
```

## first_tetracycline (column)

```
[ast_anti1(36)]='1' 2 Intermediate
3 Susceptible
108 [first_tetracycline] Tetracycline radio (Matrix)
1 Resistant
Show the field ONLY if:
```

## first_tigecycline (column)

```
https://idiredcap.idi.co.ug/redcap_v14.7.4/Design/data_dictionary_codebook.php?pid=147 13/48
9/17/25, 11:25 AM GHS-CAMO-Net Project 3 Additional Data Collection | REDCap
109 [first_tigecycline] Tigecycline radio (Matrix)
1 Resistant
Show the field ONLY if:
```

## first_sxt (column)

```
[ast_anti1(38)]='1' 2 Intermediate
3 Susceptible
110 [first_sxt] Trimethoprim/ Sulfamethoxazole radio (Matrix)
1 Resistant
Show the field ONLY if:
```

## first_vancomycin (column)

```
[ast_anti1(39)]='1' 2 Intermediate
3 Susceptible
111 [first_vancomycin] Vancomycin radio (Matrix)
1 Resistant
Show the field ONLY if:
```

## firs_othe (column)

```
[ast_anti1(40)]='1' 2 Intermediate
3 Susceptible
112 [firs_othe] Other antibiotic, please specify text
1 Resistant
Show the field ONLY if:
```

## firs_oth_ast (column)

```
[ast_anti1(41)]='1' 2 Intermediate
3 Susceptible
113 [firs_oth_ast] Other antibiotic AST results radio
1 Resistant
Show the field ONLY if:
```

## firs_oth2_name (column)

```
[ast_anti1(41)]='1' 2 Intermediate
3 Susceptible
114 [firs_oth2_name] Other antibiotic, please specify text
1 Resistant
Show the field ONLY if:
```

## firs_oth2_ast (column)

```
[ast_anti1(42)]='1' 2 Intermediate
3 Susceptible
115 [firs_oth2_ast] Other antibiotic AST results radio
1 Resistant
Show the field ONLY if:
```

## sec_organism (column)

```
[ast_anti1(42)]='1' 2 Intermediate
3 Susceptible
116 [sec_organism] 27c. Second organism isolated text
Show the field ONLY if:
[organism_isolated]>=2
```

## ast_anti2___1 (column)

```
[organism_isolated]>=2
117 [ast_anti2] 27d. Antibiotics set for AST checkbox
1 ast_anti2___1 Amikacin
Show the field ONLY if:
[organism_isolated]>=2 2 ast_anti2___2 Amoxicillin
```

## ast_anti2___2 (column)

```
1 ast_anti2___1 Amikacin
Show the field ONLY if:
[organism_isolated]>=2 2 ast_anti2___2 Amoxicillin
3 ast_anti2___3 Amoxicillin/Clavulanic
acid
```

## ast_anti2___3 (column)

```
Show the field ONLY if:
[organism_isolated]>=2 2 ast_anti2___2 Amoxicillin
3 ast_anti2___3 Amoxicillin/Clavulanic
acid
4 ast_anti2___4 Ampicillin
```

## ast_anti2___4 (column)

```
3 ast_anti2___3 Amoxicillin/Clavulanic
acid
4 ast_anti2___4 Ampicillin
5 ast_anti2___5 Ampicillin/Sulbactam
6 ast_anti2___6 Azithromycin
```

## ast_anti2___5 (column)

```
acid
4 ast_anti2___4 Ampicillin
5 ast_anti2___5 Ampicillin/Sulbactam
6 ast_anti2___6 Azithromycin
7 ast_anti2___7 Aztreonam
```

## ast_anti2___6 (column)

```
4 ast_anti2___4 Ampicillin
5 ast_anti2___5 Ampicillin/Sulbactam
6 ast_anti2___6 Azithromycin
7 ast_anti2___7 Aztreonam
8 ast_anti2___8 Cefepime
```

## ast_anti2___7 (column)

```
5 ast_anti2___5 Ampicillin/Sulbactam
6 ast_anti2___6 Azithromycin
7 ast_anti2___7 Aztreonam
8 ast_anti2___8 Cefepime
9 ast_anti2___9 Cefixime
```

## ast_anti2___8 (column)

```
6 ast_anti2___6 Azithromycin
7 ast_anti2___7 Aztreonam
8 ast_anti2___8 Cefepime
9 ast_anti2___9 Cefixime
10 ast_anti2___10 Cefotaxime
```

## ast_anti2___9 (column)

```
7 ast_anti2___7 Aztreonam
8 ast_anti2___8 Cefepime
9 ast_anti2___9 Cefixime
10 ast_anti2___10 Cefotaxime
11 ast_anti2___11 Cefoxitin
```

## ast_anti2___10 (column)

```
8 ast_anti2___8 Cefepime
9 ast_anti2___9 Cefixime
10 ast_anti2___10 Cefotaxime
11 ast_anti2___11 Cefoxitin
https://idiredcap.idi.co.ug/redcap_v14.7.4/Design/data_dictionary_codebook.php?pid=147 14/48
```

## ast_anti2___11 (column)

```
9 ast_anti2___9 Cefixime
10 ast_anti2___10 Cefotaxime
11 ast_anti2___11 Cefoxitin
https://idiredcap.idi.co.ug/redcap_v14.7.4/Design/data_dictionary_codebook.php?pid=147 14/48
9/17/25, 11:25 AM GHS-CAMO-Net Project 3 Additional Data Collection | REDCap
```

## ast_anti2___12 (column)

```
https://idiredcap.idi.co.ug/redcap_v14.7.4/Design/data_dictionary_codebook.php?pid=147 14/48
9/17/25, 11:25 AM GHS-CAMO-Net Project 3 Additional Data Collection | REDCap
12 ast_anti2___12 Ceftazidime
13 ast_anti2___13 Ceftriaxone
14 ast_anti2___14 Ceftriaxone-
```

## ast_anti2___13 (column)

```
9/17/25, 11:25 AM GHS-CAMO-Net Project 3 Additional Data Collection | REDCap
12 ast_anti2___12 Ceftazidime
13 ast_anti2___13 Ceftriaxone
14 ast_anti2___14 Ceftriaxone-
salbactam
```

## ast_anti2___14 (column)

```
12 ast_anti2___12 Ceftazidime
13 ast_anti2___13 Ceftriaxone
14 ast_anti2___14 Ceftriaxone-
salbactam
15 ast_anti2___15 Cefuroxime
```

## ast_anti2___15 (column)

```
14 ast_anti2___14 Ceftriaxone-
salbactam
15 ast_anti2___15 Cefuroxime
16 ast_anti2___16 Chlorampenicol
17 ast_anti2___17 Ciprofloxacin
```

## ast_anti2___16 (column)

```
salbactam
15 ast_anti2___15 Cefuroxime
16 ast_anti2___16 Chlorampenicol
17 ast_anti2___17 Ciprofloxacin
18 ast_anti2___18 Clindamycin
```

## ast_anti2___17 (column)

```
15 ast_anti2___15 Cefuroxime
16 ast_anti2___16 Chlorampenicol
17 ast_anti2___17 Ciprofloxacin
18 ast_anti2___18 Clindamycin
19 ast_anti2___19 Cofotaxime
```

## ast_anti2___18 (column)

```
16 ast_anti2___16 Chlorampenicol
17 ast_anti2___17 Ciprofloxacin
18 ast_anti2___18 Clindamycin
19 ast_anti2___19 Cofotaxime
20 ast_anti2___20 Doripenem
```

## ast_anti2___19 (column)

```
17 ast_anti2___17 Ciprofloxacin
18 ast_anti2___18 Clindamycin
19 ast_anti2___19 Cofotaxime
20 ast_anti2___20 Doripenem
21 ast_anti2___21 Doxycycline
```

## ast_anti2___20 (column)

```
18 ast_anti2___18 Clindamycin
19 ast_anti2___19 Cofotaxime
20 ast_anti2___20 Doripenem
21 ast_anti2___21 Doxycycline
22 ast_anti2___22 Ertapenem
```

## ast_anti2___21 (column)

```
19 ast_anti2___19 Cofotaxime
20 ast_anti2___20 Doripenem
21 ast_anti2___21 Doxycycline
22 ast_anti2___22 Ertapenem
23 ast_anti2___23 Erythromycin
```

## ast_anti2___22 (column)

```
20 ast_anti2___20 Doripenem
21 ast_anti2___21 Doxycycline
22 ast_anti2___22 Ertapenem
23 ast_anti2___23 Erythromycin
24 ast_anti2___24 Gentamicin
```

## ast_anti2___23 (column)

```
21 ast_anti2___21 Doxycycline
22 ast_anti2___22 Ertapenem
23 ast_anti2___23 Erythromycin
24 ast_anti2___24 Gentamicin
25 ast_anti2___25 Imipenem
```

## ast_anti2___24 (column)

```
22 ast_anti2___22 Ertapenem
23 ast_anti2___23 Erythromycin
24 ast_anti2___24 Gentamicin
25 ast_anti2___25 Imipenem
26 ast_anti2___26 Levofloxacin
```

## ast_anti2___25 (column)

```
23 ast_anti2___23 Erythromycin
24 ast_anti2___24 Gentamicin
25 ast_anti2___25 Imipenem
26 ast_anti2___26 Levofloxacin
27 ast_anti2___27 Linezolid
```

## ast_anti2___26 (column)

```
24 ast_anti2___24 Gentamicin
25 ast_anti2___25 Imipenem
26 ast_anti2___26 Levofloxacin
27 ast_anti2___27 Linezolid
28 ast_anti2___28 Meropenem
```

## ast_anti2___27 (column)

```
25 ast_anti2___25 Imipenem
26 ast_anti2___26 Levofloxacin
27 ast_anti2___27 Linezolid
28 ast_anti2___28 Meropenem
29 ast_anti2___29 Nalidixic acid
```

## ast_anti2___28 (column)

```
26 ast_anti2___26 Levofloxacin
27 ast_anti2___27 Linezolid
28 ast_anti2___28 Meropenem
29 ast_anti2___29 Nalidixic acid
30 ast_anti2___30 Nitrofurantoin
```

## ast_anti2___29 (column)

```
27 ast_anti2___27 Linezolid
28 ast_anti2___28 Meropenem
29 ast_anti2___29 Nalidixic acid
30 ast_anti2___30 Nitrofurantoin
31 ast_anti2___31 Oxacillin
```

## ast_anti2___30 (column)

```
28 ast_anti2___28 Meropenem
29 ast_anti2___29 Nalidixic acid
30 ast_anti2___30 Nitrofurantoin
31 ast_anti2___31 Oxacillin
32 ast_anti2___32 Penicillin G
```

## ast_anti2___31 (column)

```
29 ast_anti2___29 Nalidixic acid
30 ast_anti2___30 Nitrofurantoin
31 ast_anti2___31 Oxacillin
32 ast_anti2___32 Penicillin G
33 ast_anti2___33 Piperacillin
```

## ast_anti2___32 (column)

```
30 ast_anti2___30 Nitrofurantoin
31 ast_anti2___31 Oxacillin
32 ast_anti2___32 Penicillin G
33 ast_anti2___33 Piperacillin
34 ast_anti2___34 Piperacillin
```

## ast_anti2___33 (column)

```
31 ast_anti2___31 Oxacillin
32 ast_anti2___32 Penicillin G
33 ast_anti2___33 Piperacillin
34 ast_anti2___34 Piperacillin
tazobactam
```

## ast_anti2___34 (column)

```
32 ast_anti2___32 Penicillin G
33 ast_anti2___33 Piperacillin
34 ast_anti2___34 Piperacillin
tazobactam
35 ast_anti2___35 Rifampin
```

## ast_anti2___35 (column)

```
34 ast_anti2___34 Piperacillin
tazobactam
35 ast_anti2___35 Rifampin
36 ast_anti2___36 Streptomycin
37 ast_anti2___37 Tetracycline
```

## ast_anti2___36 (column)

```
tazobactam
35 ast_anti2___35 Rifampin
36 ast_anti2___36 Streptomycin
37 ast_anti2___37 Tetracycline
38 ast_anti2___38 Tigecycline
```

## ast_anti2___37 (column)

```
35 ast_anti2___35 Rifampin
36 ast_anti2___36 Streptomycin
37 ast_anti2___37 Tetracycline
38 ast_anti2___38 Tigecycline
39 ast_anti2___39 Trimethoprim/
```

## ast_anti2___38 (column)

```
36 ast_anti2___36 Streptomycin
37 ast_anti2___37 Tetracycline
38 ast_anti2___38 Tigecycline
39 ast_anti2___39 Trimethoprim/
Sulfamethoxazole
```

## ast_anti2___39 (column)

```
37 ast_anti2___37 Tetracycline
38 ast_anti2___38 Tigecycline
39 ast_anti2___39 Trimethoprim/
Sulfamethoxazole
40 ast_anti2___40 Vancomycin
```

## ast_anti2___40 (column)

```
39 ast_anti2___39 Trimethoprim/
Sulfamethoxazole
40 ast_anti2___40 Vancomycin
41 ast_anti2___41 Others1
42 ast_anti2___42 Others2
```

## ast_anti2___41 (column)

```
Sulfamethoxazole
40 ast_anti2___40 Vancomycin
41 ast_anti2___41 Others1
42 ast_anti2___42 Others2
118 [sec_amikacin] Amikacin radio (Matrix)
```

## ast_anti2___42 (column)

```
40 ast_anti2___40 Vancomycin
41 ast_anti2___41 Others1
42 ast_anti2___42 Others2
118 [sec_amikacin] Amikacin radio (Matrix)
1 Resistant
```

## sec_amikacin (column)

```
41 ast_anti2___41 Others1
42 ast_anti2___42 Others2
118 [sec_amikacin] Amikacin radio (Matrix)
1 Resistant
Show the field ONLY if:
```

## sec_amoxicillin (column)

```
[ast_anti2(1)]='1' 2 Intermediate
3 Susceptible
119 [sec_amoxicillin] Amoxicillin radio (Matrix)
1 Resistant
Show the field ONLY if:
```

## sec_amoxiclav (column)

```
[ast_anti2(2)]='1' 2 Intermediate
3 Susceptible
120 [sec_amoxiclav] Amoxicillin/Clavulanic acid radio (Matrix)
1 Resistant
Show the field ONLY if:
```

## sec_ampicillin (column)

```
9/17/25, 11:25 AM GHS-CAMO-Net Project 3 Additional Data Collection | REDCap
3 Susceptible
121 [sec_ampicillin] Ampicillin radio (Matrix)
1 Resistant
Show the field ONLY if:
```

## sec_amp_sulbactam (column)

```
[ast_anti2(4)]='1' 2 Intermediate
3 Susceptible
122 [sec_amp_sulbactam] Ampicillin/Sulbactam radio (Matrix)
1 Resistant
Show the field ONLY if:
```

## sec_azithromycin (column)

```
[ast_anti2(5)]='1' 2 Intermediate
3 Susceptible
123 [sec_azithromycin] Azithromycin radio (Matrix)
1 Resistant
Show the field ONLY if:
```

## sec_aztreonam (column)

```
[ast_anti2(6)]='1' 2 Intermediate
3 Susceptible
124 [sec_aztreonam] Aztreonam radio (Matrix)
1 Resistant
Show the field ONLY if:
```

## sec_cefepime (column)

```
[ast_anti2(7)]='1' 2 Intermediate
3 Susceptible
125 [sec_cefepime] Cefepime radio (Matrix)
1 Resistant
Show the field ONLY if:
```

## sec_cefixime (column)

```
[ast_anti2(8)]='1' 2 Intermediate
3 Susceptible
126 [sec_cefixime] Cefixime radio (Matrix)
1 Resistant
Show the field ONLY if:
```

## sec_cefotaxime (column)

```
[ast_anti2(9)]='1' 2 Intermediate
3 Susceptible
127 [sec_cefotaxime] Cefotaxime radio (Matrix)
1 Resistant
Show the field ONLY if:
```

## sec_cefoxitin (column)

```
[ast_anti2(10)]='1' 2 Intermediate
3 Susceptible
128 [sec_cefoxitin] Cefoxitin radio (Matrix)
1 Resistant
Show the field ONLY if:
```

## sec_ceftazidime (column)

```
[ast_anti2(11)]='1' 2 Intermediate
3 Susceptible
129 [sec_ceftazidime] Ceftazidime radio (Matrix)
1 Resistant
Show the field ONLY if:
```

## sec_ceftriaxone (column)

```
[ast_anti2(12)]='1' 2 Intermediate
3 Susceptible
130 [sec_ceftriaxone] Ceftriaxone radio (Matrix)
1 Resistant
Show the field ONLY if:
```

## sec_cefsalbactam (column)

```
[ast_anti2(13)]='1' 2 Intermediate
3 Susceptible
131 [sec_cefsalbactam] Ceftriaxone-salbactam radio (Matrix)
1 Resistant
Show the field ONLY if:
```

## sec_cefuroxime (column)

```
2 Intermediate
3 Susceptible
132 [sec_cefuroxime] Cefuroxime radio (Matrix)
1 Resistant
Show the field ONLY if:
```

## sec_chloramphenicol (column)

```
[ast_anti2(15)]='1' 2 Intermediate
3 Susceptible
133 [sec_chloramphenicol] Chloramphenicol radio (Matrix)
1 Resistant
Show the field ONLY if:
```

## sec_ciprofloxacin (column)

```
[ast_anti2(16)]='1' 2 Intermediate
3 Susceptible
134 [sec_ciprofloxacin] Ciprofloxacin radio (Matrix)
1 Resistant
Show the field ONLY if:
```

## sec_clindamycin (column)

```
[ast_anti2(17)]='1' 2 Intermediate
3 Susceptible
135 [sec_clindamycin] Clindamycin radio (Matrix)
1 Resistant
Show the field ONLY if:
```

## sec_cofotaxime (column)

```
[ast_anti2(18)]='1' 2 Intermediate
3 Susceptible
136 [sec_cofotaxime] Cofotaxime radio (Matrix)
1 Resistant
Show the field ONLY if:
```

## sec_doripenem (column)

```
[ast_anti2(19)]='1' 2 Intermediate
3 Susceptible
137 [sec_doripenem] Doripenem radio (Matrix)
1 Resistant
Show the field ONLY if:
```

## sec_doxycycline (column)

```
[ast_anti2(20)]='1' 2 Intermediate
3 Susceptible
138 [sec_doxycycline] Doxycycline radio (Matrix)
1 Resistant
Show the field ONLY if:
```

## sec_ertapenem (column)

```
[ast_anti2(21)]='1' 2 Intermediate
3 Susceptible
139 [sec_ertapenem] Ertapenem radio (Matrix)
1 Resistant
Show the field ONLY if:
```

## sec_erythromycin (column)

```
[ast_anti2(22)]='1' 2 Intermediate
3 Susceptible
140 [sec_erythromycin] Erythromycin radio (Matrix)
1 Resistant
Show the field ONLY if:
```

## sec_gentamicin (column)

```
[ast_anti2(23)]='1' 2 Intermediate
3 Susceptible
141 [sec_gentamicin] Gentamicin radio (Matrix)
1 Resistant
Show the field ONLY if:
```

## sec_imipenem (column)

```
[ast_anti2(24)]='1' 2 Intermediate
3 Susceptible
142 [sec_imipenem] Imipenem radio (Matrix)
https://idiredcap.idi.co.ug/redcap_v14.7.4/Design/data_dictionary_codebook.php?pid=147 17/48
9/17/25, 11:25 AM GHS-CAMO-Net Project 3 Additional Data Collection | REDCap
```

## sec_levofloxacin (column)

```
2 Intermediate
3 Susceptible
143 [sec_levofloxacin] Levofloxacin radio (Matrix)
1 Resistant
Show the field ONLY if:
```

## sec_linezolid (column)

```
[ast_anti2(26)]='1' 2 Intermediate
3 Susceptible
144 [sec_linezolid] Linezolid radio (Matrix)
1 Resistant
Show the field ONLY if:
```

## sec_meropenem (column)

```
[ast_anti2(27)]='1' 2 Intermediate
3 Susceptible
145 [sec_meropenem] Meropenem radio (Matrix)
1 Resistant
Show the field ONLY if:
```

## sec_nalidixicacid (column)

```
[ast_anti2(28)]='1' 2 Intermediate
3 Susceptible
146 [sec_nalidixicacid] Nalidixic acid radio (Matrix)
1 Resistant
Show the field ONLY if:
```

## sec_nitrofurantoin (column)

```
[ast_anti2(29)]='1' 2 Intermediate
3 Susceptible
147 [sec_nitrofurantoin] Nitrofurantoin radio (Matrix)
1 Resistant
Show the field ONLY if:
```

## sec_oxacillin (column)

```
[ast_anti2(30)]='1' 2 Intermediate
3 Susceptible
148 [sec_oxacillin] Oxacillin radio (Matrix)
1 Resistant
Show the field ONLY if:
```

## sec_pen_g (column)

```
[ast_anti2(31)]='1' 2 Intermediate
3 Susceptible
149 [sec_pen_g] Penicillin G radio (Matrix)
1 Resistant
Show the field ONLY if:
```

## sec_piperacillin (column)

```
[ast_anti2(32)]='1' 2 Intermediate
3 Susceptible
150 [sec_piperacillin] Piperacillin radio (Matrix)
1 Resistant
Show the field ONLY if:
```

## sec_pip_tazobactam (column)

```
[ast_anti2(33)]='1' 2 Intermediate
3 Susceptible
151 [sec_pip_tazobactam] Piperacillin tazobactam radio (Matrix)
1 Resistant
Show the field ONLY if:
```

## sec_rifampin (column)

```
[ast_anti2(34)]='1' 2 Intermediate
3 Susceptible
152 [sec_rifampin] Rifampin radio (Matrix)
1 Resistant
Show the field ONLY if:
```

## sec_streptomycin (column)

```
https://idiredcap.idi.co.ug/redcap_v14.7.4/Design/data_dictionary_codebook.php?pid=147 18/48
9/17/25, 11:25 AM GHS-CAMO-Net Project 3 Additional Data Collection | REDCap
153 [sec_streptomycin] Streptomycin radio (Matrix)
1 Resistant
Show the field ONLY if:
```

## sec_tetracycline (column)

```
[ast_anti2(36)]='1' 2 Intermediate
3 Susceptible
154 [sec_tetracycline] Tetracycline radio (Matrix)
1 Resistant
Show the field ONLY if:
```

## sec_tigecycline (column)

```
[ast_anti2(37)]='1' 2 Intermediate
3 Susceptible
155 [sec_tigecycline] Tigecycline radio (Matrix)
1 Resistant
Show the field ONLY if:
```

## sec_sxt (column)

```
[ast_anti2(38)]='1' 2 Intermediate
3 Susceptible
156 [sec_sxt] Trimethoprim/ Sulfamethoxazole radio (Matrix)
1 Resistant
Show the field ONLY if:
```

## sec_vancomycin (column)

```
[ast_anti2(39)]='1' 2 Intermediate
3 Susceptible
157 [sec_vancomycin] Vancomycin radio (Matrix)
1 Resistant
Show the field ONLY if:
```

## sec_othe (column)

```
[ast_anti2(40)]='1' 2 Intermediate
3 Susceptible
158 [sec_othe] Other antibiotic, please specify text
1 Resistant
Show the field ONLY if:
```

## sec_oth_ast (column)

```
[ast_anti2(41)]='1' 2 Intermediate
3 Susceptible
159 [sec_oth_ast] Other antibiotic AST results radio
1 Resistant
Show the field ONLY if:
```

## sec_oth2_name (column)

```
[ast_anti2(41)]='1' 2 Intermediate
3 Susceptible
160 [sec_oth2_name] Other antibiotic, please specify text
1 Resistant
Show the field ONLY if:
```

## sec_oth2_ast (column)

```
[ast_anti2(42)]='1' 2 Intermediate
3 Susceptible
161 [sec_oth2_ast] Other antibiotic AST results radio
1 Resistant
Show the field ONLY if:
```

## third_organism (column)

```
[ast_anti2(42)]='1' 2 Intermediate
3 Susceptible
162 [third_organism] 27e. Third organism isolated text
Show the field ONLY if:
[organism_isolated]>=3
```

## ast_anti3___1 (column)

```
[organism_isolated]>=3
163 [ast_anti3] 27f. Antibiotics set for AST checkbox
1 ast_anti3___1 Amikacin
Show the field ONLY if:
[organism_isolated]>=3 2 ast_anti3___2 Amoxicillin
```

## ast_anti3___2 (column)

```
1 ast_anti3___1 Amikacin
Show the field ONLY if:
[organism_isolated]>=3 2 ast_anti3___2 Amoxicillin
3 ast_anti3___3 Amoxicillin/Clavulanic
acid
```

## ast_anti3___3 (column)

```
Show the field ONLY if:
[organism_isolated]>=3 2 ast_anti3___2 Amoxicillin
3 ast_anti3___3 Amoxicillin/Clavulanic
acid
https://idiredcap.idi.co.ug/redcap_v14.7.4/Design/data_dictionary_codebook.php?pid=147 19/48
```

## ast_anti3___4 (column)

```
https://idiredcap.idi.co.ug/redcap_v14.7.4/Design/data_dictionary_codebook.php?pid=147 19/48
9/17/25, 11:25 AM GHS-CAMO-Net Project 3 Additional Data Collection | REDCap
4 ast_anti3___4 Ampicillin
5 ast_anti3___5 Ampicillin/Sulbactam
6 ast_anti3___6 Azithromycin
```

## ast_anti3___5 (column)

```
9/17/25, 11:25 AM GHS-CAMO-Net Project 3 Additional Data Collection | REDCap
4 ast_anti3___4 Ampicillin
5 ast_anti3___5 Ampicillin/Sulbactam
6 ast_anti3___6 Azithromycin
7 ast_anti3___7 Aztreonam
```

## ast_anti3___6 (column)

```
4 ast_anti3___4 Ampicillin
5 ast_anti3___5 Ampicillin/Sulbactam
6 ast_anti3___6 Azithromycin
7 ast_anti3___7 Aztreonam
8 ast_anti3___8 Cefepime
```

## ast_anti3___7 (column)

```
5 ast_anti3___5 Ampicillin/Sulbactam
6 ast_anti3___6 Azithromycin
7 ast_anti3___7 Aztreonam
8 ast_anti3___8 Cefepime
9 ast_anti3___9 Cefixime
```

## ast_anti3___8 (column)

```
6 ast_anti3___6 Azithromycin
7 ast_anti3___7 Aztreonam
8 ast_anti3___8 Cefepime
9 ast_anti3___9 Cefixime
10 ast_anti3___10 Cefotaxime
```

## ast_anti3___9 (column)

```
7 ast_anti3___7 Aztreonam
8 ast_anti3___8 Cefepime
9 ast_anti3___9 Cefixime
10 ast_anti3___10 Cefotaxime
11 ast_anti3___11 Cefoxitin
```

## ast_anti3___10 (column)

```
8 ast_anti3___8 Cefepime
9 ast_anti3___9 Cefixime
10 ast_anti3___10 Cefotaxime
11 ast_anti3___11 Cefoxitin
12 ast_anti3___12 Ceftazidime
```

## ast_anti3___11 (column)

```
9 ast_anti3___9 Cefixime
10 ast_anti3___10 Cefotaxime
11 ast_anti3___11 Cefoxitin
12 ast_anti3___12 Ceftazidime
13 ast_anti3___13 Ceftriaxone
```

## ast_anti3___12 (column)

```
10 ast_anti3___10 Cefotaxime
11 ast_anti3___11 Cefoxitin
12 ast_anti3___12 Ceftazidime
13 ast_anti3___13 Ceftriaxone
14 ast_anti3___14 Ceftriaxone-
```

## ast_anti3___13 (column)

```
11 ast_anti3___11 Cefoxitin
12 ast_anti3___12 Ceftazidime
13 ast_anti3___13 Ceftriaxone
14 ast_anti3___14 Ceftriaxone-
salbactam
```

## ast_anti3___14 (column)

```
12 ast_anti3___12 Ceftazidime
13 ast_anti3___13 Ceftriaxone
14 ast_anti3___14 Ceftriaxone-
salbactam
15 ast_anti3___15 Cefuroxime
```

## ast_anti3___15 (column)

```
14 ast_anti3___14 Ceftriaxone-
salbactam
15 ast_anti3___15 Cefuroxime
16 ast_anti3___16 Chlorampenicol
17 ast_anti3___17 Ciprofloxacin
```

## ast_anti3___16 (column)

```
salbactam
15 ast_anti3___15 Cefuroxime
16 ast_anti3___16 Chlorampenicol
17 ast_anti3___17 Ciprofloxacin
18 ast_anti3___18 Clindamycin
```

## ast_anti3___17 (column)

```
15 ast_anti3___15 Cefuroxime
16 ast_anti3___16 Chlorampenicol
17 ast_anti3___17 Ciprofloxacin
18 ast_anti3___18 Clindamycin
19 ast_anti3___19 Cofotaxime
```

## ast_anti3___18 (column)

```
16 ast_anti3___16 Chlorampenicol
17 ast_anti3___17 Ciprofloxacin
18 ast_anti3___18 Clindamycin
19 ast_anti3___19 Cofotaxime
20 ast_anti3___20 Doripenem
```

## ast_anti3___19 (column)

```
17 ast_anti3___17 Ciprofloxacin
18 ast_anti3___18 Clindamycin
19 ast_anti3___19 Cofotaxime
20 ast_anti3___20 Doripenem
21 ast_anti3___21 Doxycycline
```

## ast_anti3___20 (column)

```
18 ast_anti3___18 Clindamycin
19 ast_anti3___19 Cofotaxime
20 ast_anti3___20 Doripenem
21 ast_anti3___21 Doxycycline
22 ast_anti3___22 Ertapenem
```

## ast_anti3___21 (column)

```
19 ast_anti3___19 Cofotaxime
20 ast_anti3___20 Doripenem
21 ast_anti3___21 Doxycycline
22 ast_anti3___22 Ertapenem
23 ast_anti3___23 Erythromycin
```

## ast_anti3___22 (column)

```
20 ast_anti3___20 Doripenem
21 ast_anti3___21 Doxycycline
22 ast_anti3___22 Ertapenem
23 ast_anti3___23 Erythromycin
24 ast_anti3___24 Gentamicin
```

## ast_anti3___23 (column)

```
21 ast_anti3___21 Doxycycline
22 ast_anti3___22 Ertapenem
23 ast_anti3___23 Erythromycin
24 ast_anti3___24 Gentamicin
25 ast_anti3___25 Imipenem
```

## ast_anti3___24 (column)

```
22 ast_anti3___22 Ertapenem
23 ast_anti3___23 Erythromycin
24 ast_anti3___24 Gentamicin
25 ast_anti3___25 Imipenem
26 ast_anti3___26 Levofloxacin
```

## ast_anti3___25 (column)

```
23 ast_anti3___23 Erythromycin
24 ast_anti3___24 Gentamicin
25 ast_anti3___25 Imipenem
26 ast_anti3___26 Levofloxacin
27 ast_anti3___27 Linezolid
```

## ast_anti3___26 (column)

```
24 ast_anti3___24 Gentamicin
25 ast_anti3___25 Imipenem
26 ast_anti3___26 Levofloxacin
27 ast_anti3___27 Linezolid
28 ast_anti3___28 Meropenem
```

## ast_anti3___27 (column)

```
25 ast_anti3___25 Imipenem
26 ast_anti3___26 Levofloxacin
27 ast_anti3___27 Linezolid
28 ast_anti3___28 Meropenem
29 ast_anti3___29 Nalidixic acid
```

## ast_anti3___28 (column)

```
26 ast_anti3___26 Levofloxacin
27 ast_anti3___27 Linezolid
28 ast_anti3___28 Meropenem
29 ast_anti3___29 Nalidixic acid
30 ast_anti3___30 Nitrofurantoin
```

## ast_anti3___29 (column)

```
27 ast_anti3___27 Linezolid
28 ast_anti3___28 Meropenem
29 ast_anti3___29 Nalidixic acid
30 ast_anti3___30 Nitrofurantoin
31 ast_anti3___31 Oxacillin
```

## ast_anti3___30 (column)

```
28 ast_anti3___28 Meropenem
29 ast_anti3___29 Nalidixic acid
30 ast_anti3___30 Nitrofurantoin
31 ast_anti3___31 Oxacillin
32 ast_anti3___32 Penicillin G
```

## ast_anti3___31 (column)

```
29 ast_anti3___29 Nalidixic acid
30 ast_anti3___30 Nitrofurantoin
31 ast_anti3___31 Oxacillin
32 ast_anti3___32 Penicillin G
33 ast_anti3___33 Piperacillin
```

## ast_anti3___32 (column)

```
30 ast_anti3___30 Nitrofurantoin
31 ast_anti3___31 Oxacillin
32 ast_anti3___32 Penicillin G
33 ast_anti3___33 Piperacillin
34 ast_anti3___34 Piperacillin
```

## ast_anti3___33 (column)

```
31 ast_anti3___31 Oxacillin
32 ast_anti3___32 Penicillin G
33 ast_anti3___33 Piperacillin
34 ast_anti3___34 Piperacillin
tazobactam
```

## ast_anti3___34 (column)

```
32 ast_anti3___32 Penicillin G
33 ast_anti3___33 Piperacillin
34 ast_anti3___34 Piperacillin
tazobactam
35 ast_anti3___35 Rifampin
```

## ast_anti3___35 (column)

```
34 ast_anti3___34 Piperacillin
tazobactam
35 ast_anti3___35 Rifampin
36 ast_anti3___36 Streptomycin
37 ast_anti3___37 Tetracycline
```

## ast_anti3___36 (column)

```
tazobactam
35 ast_anti3___35 Rifampin
36 ast_anti3___36 Streptomycin
37 ast_anti3___37 Tetracycline
38 ast_anti3___38 Tigecycline
```

## ast_anti3___37 (column)

```
35 ast_anti3___35 Rifampin
36 ast_anti3___36 Streptomycin
37 ast_anti3___37 Tetracycline
38 ast_anti3___38 Tigecycline
39 ast_anti3___39 Trimethoprim/
```

## ast_anti3___38 (column)

```
36 ast_anti3___36 Streptomycin
37 ast_anti3___37 Tetracycline
38 ast_anti3___38 Tigecycline
39 ast_anti3___39 Trimethoprim/
Sulfamethoxazole
```

## ast_anti3___39 (column)

```
37 ast_anti3___37 Tetracycline
38 ast_anti3___38 Tigecycline
39 ast_anti3___39 Trimethoprim/
Sulfamethoxazole
40 ast_anti3___40 Vancomycin
```

## ast_anti3___40 (column)

```
39 ast_anti3___39 Trimethoprim/
Sulfamethoxazole
40 ast_anti3___40 Vancomycin
41 ast_anti3___41 Others1
42 ast_anti3___42 Others2
```

## ast_anti3___41 (column)

```
Sulfamethoxazole
40 ast_anti3___40 Vancomycin
41 ast_anti3___41 Others1
42 ast_anti3___42 Others2
164 [third_amikacin] Amikacin radio (Matrix)
```

## ast_anti3___42 (column)

```
40 ast_anti3___40 Vancomycin
41 ast_anti3___41 Others1
42 ast_anti3___42 Others2
164 [third_amikacin] Amikacin radio (Matrix)
1 Resistant
```

## third_amikacin (column)

```
41 ast_anti3___41 Others1
42 ast_anti3___42 Others2
164 [third_amikacin] Amikacin radio (Matrix)
1 Resistant
Show the field ONLY if:
```

## third_amoxicillin (column)

```
9/17/25, 11:25 AM GHS-CAMO-Net Project 3 Additional Data Collection | REDCap
3 Susceptible
165 [third_amoxicillin] Amoxicillin radio (Matrix)
1 Resistant
Show the field ONLY if:
```

## third_amoxiclav (column)

```
[ast_anti3(2)]='1' 2 Intermediate
3 Susceptible
166 [third_amoxiclav] Amoxicillin/Clavulanic acid radio (Matrix)
1 Resistant
Show the field ONLY if:
```

## third_ampicillin (column)

```
[ast_anti3(3)]='1' 2 Intermediate
3 Susceptible
167 [third_ampicillin] Ampicillin radio (Matrix)
1 Resistant
Show the field ONLY if:
```

## third_amp_sulbactam (column)

```
[ast_anti3(4)]='1' 2 Intermediate
3 Susceptible
168 [third_amp_sulbactam] Ampicillin/Sulbactam radio (Matrix)
1 Resistant
Show the field ONLY if:
```

## third_azithromycin (column)

```
[ast_anti3(5)]='1' 2 Intermediate
3 Susceptible
169 [third_azithromycin] Azithromycin radio (Matrix)
1 Resistant
Show the field ONLY if:
```

## third_aztreonam (column)

```
[ast_anti3(6)]='1' 2 Intermediate
3 Susceptible
170 [third_aztreonam] Aztreonam radio (Matrix)
1 Resistant
Show the field ONLY if:
```

## third_cefepime (column)

```
[ast_anti3(7)]='1' 2 Intermediate
3 Susceptible
171 [third_cefepime] Cefepime radio (Matrix)
1 Resistant
Show the field ONLY if:
```

## third_cefixime (column)

```
[ast_anti3(8)]='1' 2 Intermediate
3 Susceptible
172 [third_cefixime] Cefixime radio (Matrix)
1 Resistant
Show the field ONLY if:
```

## third_cefotaxime (column)

```
[ast_anti3(9)]='1' 2 Intermediate
3 Susceptible
173 [third_cefotaxime] Cefotaxime radio (Matrix)
1 Resistant
Show the field ONLY if:
```

## third_cefoxitin (column)

```
[ast_anti3(10)]='1' 2 Intermediate
3 Susceptible
174 [third_cefoxitin] Cefoxitin radio (Matrix)
1 Resistant
Show the field ONLY if:
```

## third_ceftazidime (column)

```
[ast_anti3(11)]='1' 2 Intermediate
3 Susceptible
175 [third_ceftazidime] Ceftazidime radio (Matrix)
1 Resistant
Show the field ONLY if:
```

## third_ceftriaxone (column)

```
2 Intermediate
3 Susceptible
176 [third_ceftriaxone] Ceftriaxone radio (Matrix)
1 Resistant
Show the field ONLY if:
```

## third_cefsalbactam (column)

```
[ast_anti3(13)]='1' 2 Intermediate
3 Susceptible
177 [third_cefsalbactam] Ceftriaxone-salbactam radio (Matrix)
1 Resistant
Show the field ONLY if:
```

## third_cefuroxime (column)

```
[ast_anti3(14)]='1' 2 Intermediate
3 Susceptible
178 [third_cefuroxime] Cefuroxime radio (Matrix)
1 Resistant
Show the field ONLY if:
```

## third_ciprofloxacin (column)

```
[ast_anti3(16)]='1'
3 Susceptible
180 [third_ciprofloxacin] Ciprofloxacin radio (Matrix)
1 Resistant
Show the field ONLY if:
```

## third_clindamycin (column)

```
[ast_anti3(17)]='1' 2 Intermediate
3 Susceptible
181 [third_clindamycin] Clindamycin radio (Matrix)
1 Resistant
Show the field ONLY if:
```

## third_cofotaxime (column)

```
[ast_anti3(18)]='1' 2 Intermediate
3 Susceptible
182 [third_cofotaxime] Cofotaxime radio (Matrix)
1 Resistant
Show the field ONLY if:
```

## third_doripenem (column)

```
[ast_anti3(19)]='1' 2 Intermediate
3 Susceptible
183 [third_doripenem] Doripenem radio (Matrix)
1 Resistant
Show the field ONLY if:
```

## third_doxycycline (column)

```
[ast_anti3(20)]='1' 2 Intermediate
3 Susceptible
184 [third_doxycycline] Doxycycline radio (Matrix)
1 Resistant
Show the field ONLY if:
```

## third_ertapenem (column)

```
[ast_anti3(21)]='1' 2 Intermediate
3 Susceptible
185 [third_ertapenem] Ertapenem radio (Matrix)
1 Resistant
Show the field ONLY if:
```

## third_erythromycin (column)

```
[ast_anti3(22)]='1' 2 Intermediate
3 Susceptible
186 [third_erythromycin] Erythromycin radio (Matrix)
https://idiredcap.idi.co.ug/redcap_v14.7.4/Design/data_dictionary_codebook.php?pid=147 22/48
9/17/25, 11:25 AM GHS-CAMO-Net Project 3 Additional Data Collection | REDCap
```

## third_gentamicin (column)

```
2 Intermediate
3 Susceptible
187 [third_gentamicin] Gentamicin radio (Matrix)
1 Resistant
Show the field ONLY if:
```

## third_imipenem (column)

```
[ast_anti3(24)]='1' 2 Intermediate
3 Susceptible
188 [third_imipenem] Imipenem radio (Matrix)
1 Resistant
Show the field ONLY if:
```

## third_levofloxacin (column)

```
[ast_anti3(25)]='1' 2 Intermediate
3 Susceptible
189 [third_levofloxacin] Levofloxacin radio (Matrix)
1 Resistant
Show the field ONLY if:
```

## third_linezolid (column)

```
[ast_anti3(26)]='1' 2 Intermediate
3 Susceptible
190 [third_linezolid] Linezolid radio (Matrix)
1 Resistant
Show the field ONLY if:
```

## third_meropenem (column)

```
[ast_anti3(27)]='1' 2 Intermediate
3 Susceptible
191 [third_meropenem] Meropenem radio (Matrix)
1 Resistant
Show the field ONLY if:
```

## third_nalidixicacid (column)

```
[ast_anti3(28)]='1' 2 Intermediate
3 Susceptible
192 [third_nalidixicacid] Nalidixic acid radio (Matrix)
1 Resistant
Show the field ONLY if:
```

## third_nitrofurantoin (column)

```
[ast_anti3(29)]='1' 2 Intermediate
3 Susceptible
193 [third_nitrofurantoin] Nitrofurantoin radio (Matrix)
1 Resistant
Show the field ONLY if:
```

## third_oxacillin (column)

```
[ast_anti3(30)]='1' 2 Intermediate
3 Susceptible
194 [third_oxacillin] Oxacillin radio (Matrix)
1 Resistant
Show the field ONLY if:
```

## third_pen_g (column)

```
[ast_anti3(31)]='1' 2 Intermediate
3 Susceptible
195 [third_pen_g] Penicillin G radio (Matrix)
1 Resistant
Show the field ONLY if:
```

## third_piperacillin (column)

```
[ast_anti3(32)]='1' 2 Intermediate
3 Susceptible
196 [third_piperacillin] Piperacillin radio (Matrix)
1 Resistant
Show the field ONLY if:
```

## third_pip_tazobactam (column)

```
https://idiredcap.idi.co.ug/redcap_v14.7.4/Design/data_dictionary_codebook.php?pid=147 23/48
9/17/25, 11:25 AM GHS-CAMO-Net Project 3 Additional Data Collection | REDCap
197 [third_pip_tazobactam] Piperacillin tazobactam radio (Matrix)
1 Resistant
Show the field ONLY if:
```

## third_rifampin (column)

```
[ast_anti3(34)]='1' 2 Intermediate
3 Susceptible
198 [third_rifampin] Rifampin radio (Matrix)
1 Resistant
Show the field ONLY if:
```

## third_streptomycin (column)

```
[ast_anti3(35)]='1' 2 Intermediate
3 Susceptible
199 [third_streptomycin] Streptomycin radio (Matrix)
1 Resistant
Show the field ONLY if:
```

## third_tetracycline (column)

```
[ast_anti3(36)]='1' 2 Intermediate
3 Susceptible
200 [third_tetracycline] Tetracycline radio (Matrix)
1 Resistant
Show the field ONLY if:
```

## third_tigecycline (column)

```
[ast_anti3(37)]='1' 2 Intermediate
3 Susceptible
201 [third_tigecycline] Tigecycline radio (Matrix)
1 Resistant
Show the field ONLY if:
```

## third_sxt (column)

```
[ast_anti3(38)]='1' 2 Intermediate
3 Susceptible
202 [third_sxt] Trimethoprim/ Sulfamethoxazole radio (Matrix)
1 Resistant
Show the field ONLY if:
```

## third_vancomycin (column)

```
[ast_anti3(39)]='1' 2 Intermediate
3 Susceptible
203 [third_vancomycin] Vancomycin radio (Matrix)
1 Resistant
Show the field ONLY if:
```

## third_othe (column)

```
[ast_anti3(40)]='1' 2 Intermediate
3 Susceptible
204 [third_othe] Other antibiotic, please specify text
Show the field ONLY if:
[ast_anti3(41)]='1'
```

## third_oth_ast (column)

```
Show the field ONLY if:
[ast_anti3(41)]='1'
205 [third_oth_ast] Other antibiotic AST results radio
1 Resistant
Show the field ONLY if:
```

## third_oth2_name (column)

```
[ast_anti3(41)]='1' 2 Intermediate
3 Susceptible
206 [third_oth2_name] Other antibiotic, please specify text
Show the field ONLY if:
[ast_anti3(42)]='1'
```

## third_oth2_ast (column)

```
Show the field ONLY if:
[ast_anti3(42)]='1'
207 [third_oth2_ast] Other antibiotic AST results radio
1 Resistant
Show the field ONLY if:
```

## antib_aft_culture (column)

```
[ast_anti3(42)]='1' 2 Intermediate
3 Susceptible
208 [antib_aft_culture] 28. Were antibiotics prescribed directed (based yesno
on culture and sensitivity results) following
1 Yes
```

## date_antib_admin (column)

```
[growth1]='1'
0 No
209 [date_antib_admin] 29. If yes, indicate date antibiotics were text (date_dmy)
prescribed.
Show the field ONLY if:
```

## antib_presc_af_cul___1 (column)

```
210 [antib_presc_af_cul] 30. Provide a list of antibiotics prescribed checkbox
following receipt of culture and sensitivity
1 antib_presc_af_cul___1 Amikacin
Show the field ONLY if:
results. (Select Multiple)
```

## antib_presc_af_cul___2 (column)

```
Show the field ONLY if:
results. (Select Multiple)
[antib_aft_culture]='1' 2 antib_presc_af_cul___2 Amoxicillin
3 antib_presc_af_cul___3 Amoxicillin/Clav
acid
```

## antib_presc_af_cul___3 (column)

```
results. (Select Multiple)
[antib_aft_culture]='1' 2 antib_presc_af_cul___2 Amoxicillin
3 antib_presc_af_cul___3 Amoxicillin/Clav
acid
4 antib_presc_af_cul___4 Ampicillin
```

## antib_presc_af_cul___4 (column)

```
3 antib_presc_af_cul___3 Amoxicillin/Clav
acid
4 antib_presc_af_cul___4 Ampicillin
5 antib_presc_af_cul___5 Ampicillin/Sulba
6 antib_presc_af_cul___6 Azithromycin
```

## antib_presc_af_cul___5 (column)

```
acid
4 antib_presc_af_cul___4 Ampicillin
5 antib_presc_af_cul___5 Ampicillin/Sulba
6 antib_presc_af_cul___6 Azithromycin
7 antib_presc_af_cul___7 Aztreonam
```

## antib_presc_af_cul___6 (column)

```
4 antib_presc_af_cul___4 Ampicillin
5 antib_presc_af_cul___5 Ampicillin/Sulba
6 antib_presc_af_cul___6 Azithromycin
7 antib_presc_af_cul___7 Aztreonam
8 antib_presc_af_cul___8 Cefepime
```

## antib_presc_af_cul___7 (column)

```
5 antib_presc_af_cul___5 Ampicillin/Sulba
6 antib_presc_af_cul___6 Azithromycin
7 antib_presc_af_cul___7 Aztreonam
8 antib_presc_af_cul___8 Cefepime
9 antib_presc_af_cul___9 Cefixime
```

## antib_presc_af_cul___8 (column)

```
6 antib_presc_af_cul___6 Azithromycin
7 antib_presc_af_cul___7 Aztreonam
8 antib_presc_af_cul___8 Cefepime
9 antib_presc_af_cul___9 Cefixime
10 antib_presc_af_cul___10 Cefotaxime
```

## antib_presc_af_cul___9 (column)

```
7 antib_presc_af_cul___7 Aztreonam
8 antib_presc_af_cul___8 Cefepime
9 antib_presc_af_cul___9 Cefixime
10 antib_presc_af_cul___10 Cefotaxime
11 antib_presc_af_cul___11 Cefoxitin
```

## antib_presc_af_cul___10 (column)

```
8 antib_presc_af_cul___8 Cefepime
9 antib_presc_af_cul___9 Cefixime
10 antib_presc_af_cul___10 Cefotaxime
11 antib_presc_af_cul___11 Cefoxitin
12 antib_presc_af_cul___12 Ceftazidime
```

## antib_presc_af_cul___11 (column)

```
9 antib_presc_af_cul___9 Cefixime
10 antib_presc_af_cul___10 Cefotaxime
11 antib_presc_af_cul___11 Cefoxitin
12 antib_presc_af_cul___12 Ceftazidime
13 antib_presc_af_cul___13 Ceftriaxone
```

## antib_presc_af_cul___12 (column)

```
10 antib_presc_af_cul___10 Cefotaxime
11 antib_presc_af_cul___11 Cefoxitin
12 antib_presc_af_cul___12 Ceftazidime
13 antib_presc_af_cul___13 Ceftriaxone
14 antib_presc_af_cul___14 Ceftriaxone-
```

## antib_presc_af_cul___13 (column)

```
11 antib_presc_af_cul___11 Cefoxitin
12 antib_presc_af_cul___12 Ceftazidime
13 antib_presc_af_cul___13 Ceftriaxone
14 antib_presc_af_cul___14 Ceftriaxone-
salbactam
```

## antib_presc_af_cul___14 (column)

```
12 antib_presc_af_cul___12 Ceftazidime
13 antib_presc_af_cul___13 Ceftriaxone
14 antib_presc_af_cul___14 Ceftriaxone-
salbactam
15 antib_presc_af_cul___15 Cefuroxime
```

## antib_presc_af_cul___15 (column)

```
14 antib_presc_af_cul___14 Ceftriaxone-
salbactam
15 antib_presc_af_cul___15 Cefuroxime
16 antib_presc_af_cul___16 Chlorampenicol
17 antib_presc_af_cul___17 Ciprofloxacin
```

## antib_presc_af_cul___16 (column)

```
salbactam
15 antib_presc_af_cul___15 Cefuroxime
16 antib_presc_af_cul___16 Chlorampenicol
17 antib_presc_af_cul___17 Ciprofloxacin
18 antib_presc_af_cul___18 Clindamycin
```

## antib_presc_af_cul___17 (column)

```
15 antib_presc_af_cul___15 Cefuroxime
16 antib_presc_af_cul___16 Chlorampenicol
17 antib_presc_af_cul___17 Ciprofloxacin
18 antib_presc_af_cul___18 Clindamycin
19 antib_presc_af_cul___19 Cofotaxime
```

## antib_presc_af_cul___18 (column)

```
16 antib_presc_af_cul___16 Chlorampenicol
17 antib_presc_af_cul___17 Ciprofloxacin
18 antib_presc_af_cul___18 Clindamycin
19 antib_presc_af_cul___19 Cofotaxime
20 antib_presc_af_cul___20 Doripenem
```

## antib_presc_af_cul___19 (column)

```
17 antib_presc_af_cul___17 Ciprofloxacin
18 antib_presc_af_cul___18 Clindamycin
19 antib_presc_af_cul___19 Cofotaxime
20 antib_presc_af_cul___20 Doripenem
21 antib_presc_af_cul___21 Doxycycline
```

## antib_presc_af_cul___20 (column)

```
18 antib_presc_af_cul___18 Clindamycin
19 antib_presc_af_cul___19 Cofotaxime
20 antib_presc_af_cul___20 Doripenem
21 antib_presc_af_cul___21 Doxycycline
22 antib_presc_af_cul___22 Ertapenem
```

## antib_presc_af_cul___21 (column)

```
19 antib_presc_af_cul___19 Cofotaxime
20 antib_presc_af_cul___20 Doripenem
21 antib_presc_af_cul___21 Doxycycline
22 antib_presc_af_cul___22 Ertapenem
23 antib_presc_af_cul___23 Erythromycin
```

## antib_presc_af_cul___22 (column)

```
20 antib_presc_af_cul___20 Doripenem
21 antib_presc_af_cul___21 Doxycycline
22 antib_presc_af_cul___22 Ertapenem
23 antib_presc_af_cul___23 Erythromycin
24 antib_presc_af_cul___24 Gentamicin
```

## antib_presc_af_cul___23 (column)

```
21 antib_presc_af_cul___21 Doxycycline
22 antib_presc_af_cul___22 Ertapenem
23 antib_presc_af_cul___23 Erythromycin
24 antib_presc_af_cul___24 Gentamicin
25 antib_presc_af_cul___25 Imipenem
```

## antib_presc_af_cul___24 (column)

```
22 antib_presc_af_cul___22 Ertapenem
23 antib_presc_af_cul___23 Erythromycin
24 antib_presc_af_cul___24 Gentamicin
25 antib_presc_af_cul___25 Imipenem
26 antib_presc_af_cul___26 Levofloxacin
```

## antib_presc_af_cul___25 (column)

```
23 antib_presc_af_cul___23 Erythromycin
24 antib_presc_af_cul___24 Gentamicin
25 antib_presc_af_cul___25 Imipenem
26 antib_presc_af_cul___26 Levofloxacin
27 antib_presc_af_cul___27 Linezolid
```

## antib_presc_af_cul___26 (column)

```
24 antib_presc_af_cul___24 Gentamicin
25 antib_presc_af_cul___25 Imipenem
26 antib_presc_af_cul___26 Levofloxacin
27 antib_presc_af_cul___27 Linezolid
28 antib_presc_af_cul___28 Meropenem
```

## antib_presc_af_cul___27 (column)

```
25 antib_presc_af_cul___25 Imipenem
26 antib_presc_af_cul___26 Levofloxacin
27 antib_presc_af_cul___27 Linezolid
28 antib_presc_af_cul___28 Meropenem
29 antib_presc_af_cul___29 Nalidixic acid
```

## antib_presc_af_cul___28 (column)

```
26 antib_presc_af_cul___26 Levofloxacin
27 antib_presc_af_cul___27 Linezolid
28 antib_presc_af_cul___28 Meropenem
29 antib_presc_af_cul___29 Nalidixic acid
30 antib_presc_af_cul___30 Nitrofurantoin
```

## antib_presc_af_cul___29 (column)

```
27 antib_presc_af_cul___27 Linezolid
28 antib_presc_af_cul___28 Meropenem
29 antib_presc_af_cul___29 Nalidixic acid
30 antib_presc_af_cul___30 Nitrofurantoin
31 antib_presc_af_cul___31 Oxacillin
```

## antib_presc_af_cul___30 (column)

```
28 antib_presc_af_cul___28 Meropenem
29 antib_presc_af_cul___29 Nalidixic acid
30 antib_presc_af_cul___30 Nitrofurantoin
31 antib_presc_af_cul___31 Oxacillin
32 antib_presc_af_cul___32 Penicillin G
```

## antib_presc_af_cul___31 (column)

```
29 antib_presc_af_cul___29 Nalidixic acid
30 antib_presc_af_cul___30 Nitrofurantoin
31 antib_presc_af_cul___31 Oxacillin
32 antib_presc_af_cul___32 Penicillin G
33 antib_presc_af_cul___33 Piperacillin
```

## antib_presc_af_cul___32 (column)

```
30 antib_presc_af_cul___30 Nitrofurantoin
31 antib_presc_af_cul___31 Oxacillin
32 antib_presc_af_cul___32 Penicillin G
33 antib_presc_af_cul___33 Piperacillin
34 antib_presc_af_cul___34 Piperacillin
```

## antib_presc_af_cul___33 (column)

```
31 antib_presc_af_cul___31 Oxacillin
32 antib_presc_af_cul___32 Penicillin G
33 antib_presc_af_cul___33 Piperacillin
34 antib_presc_af_cul___34 Piperacillin
tazobactam
```

## antib_presc_af_cul___34 (column)

```
32 antib_presc_af_cul___32 Penicillin G
33 antib_presc_af_cul___33 Piperacillin
34 antib_presc_af_cul___34 Piperacillin
tazobactam
35 antib_presc_af_cul___35 Rifampin
```

## antib_presc_af_cul___35 (column)

```
34 antib_presc_af_cul___34 Piperacillin
tazobactam
35 antib_presc_af_cul___35 Rifampin
36 antib_presc_af_cul___36 Streptomycin
37 antib_presc_af_cul___37 Tetracycline
```

## antib_presc_af_cul___36 (column)

```
tazobactam
35 antib_presc_af_cul___35 Rifampin
36 antib_presc_af_cul___36 Streptomycin
37 antib_presc_af_cul___37 Tetracycline
https://idiredcap.idi.co.ug/redcap_v14.7.4/Design/data_dictionary_codebook.php?pid=147 25/48
```

## antib_presc_af_cul___37 (column)

```
35 antib_presc_af_cul___35 Rifampin
36 antib_presc_af_cul___36 Streptomycin
37 antib_presc_af_cul___37 Tetracycline
https://idiredcap.idi.co.ug/redcap_v14.7.4/Design/data_dictionary_codebook.php?pid=147 25/48
9/17/25, 11:25 AM GHS-CAMO-Net Project 3 Additional Data Collection | REDCap
```

## antib_presc_af_cul___38 (column)

```
https://idiredcap.idi.co.ug/redcap_v14.7.4/Design/data_dictionary_codebook.php?pid=147 25/48
9/17/25, 11:25 AM GHS-CAMO-Net Project 3 Additional Data Collection | REDCap
38 antib_presc_af_cul___38 Tigecycline
39 antib_presc_af_cul___39 Trimethoprim/
Sulfamethoxazo
```

## antib_presc_af_cul___39 (column)

```
9/17/25, 11:25 AM GHS-CAMO-Net Project 3 Additional Data Collection | REDCap
38 antib_presc_af_cul___38 Tigecycline
39 antib_presc_af_cul___39 Trimethoprim/
Sulfamethoxazo
40 antib_presc_af_cul___40 Vancomycin
```

## antib_presc_af_cul___40 (column)

```
39 antib_presc_af_cul___39 Trimethoprim/
Sulfamethoxazo
40 antib_presc_af_cul___40 Vancomycin
41 antib_presc_af_cul___41 Others
211 [presc_cul_amikacin] Amikacin missed doses text (number)
```

## antib_presc_af_cul___41 (column)

```
Sulfamethoxazo
40 antib_presc_af_cul___40 Vancomycin
41 antib_presc_af_cul___41 Others
211 [presc_cul_amikacin] Amikacin missed doses text (number)
Show the field ONLY if:
```

## presc_cul_amikacin (column)

```
40 antib_presc_af_cul___40 Vancomycin
41 antib_presc_af_cul___41 Others
211 [presc_cul_amikacin] Amikacin missed doses text (number)
Show the field ONLY if:
[antib_presc_af_cul(1)]
```

## presc_cul_amoxiclav (column)

```
[antib_presc_af_cul(2)]
='1'
213 [presc_cul_amoxiclav] Amoxicillin/Clavulanic acid missed doses text (number)
Show the field ONLY if:
[antib_presc_af_cul(3)]
```

## presc_cul_ampicillin (column)

```
[antib_presc_af_cul(3)]
='1'
214 [presc_cul_ampicillin] Ampicillin missed doses text (number)
Show the field ONLY if:
[antib_presc_af_cul(4)]
```

## presc_cul_aztreonam (column)

```
[antib_presc_af_cul(6)]
='1'
217 [presc_cul_aztreonam] Aztreonam missed doses text (number)
Show the field ONLY if:
[antib_presc_af_cul(7)]
```

## presc_cul_cefepime (column)

```
[antib_presc_af_cul(7)]
='1'
218 [presc_cul_cefepime] Cefepime missed doses text (number)
Show the field ONLY if:
[antib_presc_af_cul(8)]
```

## presc_cul_cefixime (column)

```
[antib_presc_af_cul(8)]
='1'
219 [presc_cul_cefixime] Cefixime missed doses text (number)
Show the field ONLY if:
[antib_presc_af_cul(9)]
```

## presc_cul_cefotaxime (column)

```
[antib_presc_af_cul(9)]
='1'
220 [presc_cul_cefotaxime] Cefotaxime missed doses text (number)
Show the field ONLY if:
[antib_presc_af_cul(10)]
```

## presc_cul_cefoxitin (column)

```
[antib_presc_af_cul(10)]
='1'
221 [presc_cul_cefoxitin] Cefoxitin missed doses text (number)
Show the field ONLY if:
[antib_presc_af_cul(11)]
```

## presc_cul_cefuroxime (column)

```
[antib_presc_af_cul(14)]
='1'
225 [presc_cul_cefuroxime] Cefuroxime missed doses text (number)
Show the field ONLY if:
[antib_presc_af_cul(15)]
```

## presc_cul_cofotaxime (column)

```
[antib_presc_af_cul(18)]
='1'
229 [presc_cul_cofotaxime] Cofotaxime missed doses text (number)
Show the field ONLY if:
[antib_presc_af_cul(19)]
```

## presc_cul_doripenem (column)

```
[antib_presc_af_cul(19)]
='1'
230 [presc_cul_doripenem] Doripenem missed doses text (number)
Show the field ONLY if:
[antib_presc_af_cul(20)]
```

## presc_cul_ertapenem (column)

```
[antib_presc_af_cul(21)]
='1'
232 [presc_cul_ertapenem] Ertapenem missed doses text (number)
Show the field ONLY if:
[antib_presc_af_cul(22)]
```

## presc_cul_gentamicin (column)

```
[antib_presc_af_cul(23)]
='1'
234 [presc_cul_gentamicin] Gentamicin missed doses text (number)
Show the field ONLY if:
[antib_presc_af_cul(24)]
```

## presc_cul_imipenem (column)

```
[antib_presc_af_cul(24)]
='1'
235 [presc_cul_imipenem] Imipenem missed doses text (number)
Show the field ONLY if:
[antib_presc_af_cul(25)]
```

## presc_cul_linezolid (column)

```
[antib_presc_af_cul(26)]
='1'
237 [presc_cul_linezolid] Linezolid missed doses text (number)
Show the field ONLY if:
[antib_presc_af_cul(27)]
```

## presc_cul_meropenem (column)

```
[antib_presc_af_cul(27)]
='1'
238 [presc_cul_meropenem] Meropenem missed doses text (number)
Show the field ONLY if:
[antib_presc_af_cul(28)]
```

## presc_cul_oxacillin (column)

```
[antib_presc_af_cul(30)]
='1'
241 [presc_cul_oxacillin] Oxacillin missed doses text (number)
Show the field ONLY if:
[antib_presc_af_cul(31)]
```

## presc_cul_pen_g (column)

```
[antib_presc_af_cul(31)]
='1'
242 [presc_cul_pen_g] Penicillin G missed doses text (number)
Show the field ONLY if:
[antib_presc_af_cul(32)]
```

## presc_cul_rifampin (column)

```
[antib_presc_af_cul(34)]
='1'
245 [presc_cul_rifampin] Rifampicin missed doses text (number)
https://idiredcap.idi.co.ug/redcap_v14.7.4/Design/data_dictionary_codebook.php?pid=147 28/48
9/17/25, 11:25 AM GHS-CAMO-Net Project 3 Additional Data Collection | REDCap
```

## presc_cul_sxt (column)

```
[antib_presc_af_cul(38)]
='1'
249 [presc_cul_sxt] Trimethoprim/ Sulfamethoxazole missed doses text (number)
Show the field ONLY if:
[antib_presc_af_cul(39)]
```

## presc_cul_vancomycin (column)

```
[antib_presc_af_cul(39)]
='1'
250 [presc_cul_vancomycin] Vancomycin missed doses text (number)
Show the field ONLY if:
[antib_presc_af_cul(40)]
```

## other_antibiotic2 (column)

```
[antib_presc_af_cul(40)]
='1'
251 [other_antibiotic2] Other antibiotic text
Show the field ONLY if:
[antib_presc_af_cul(41)]
```

## missed_other (column)

```
[antib_presc_af_cul(41)]
='1'
252 [missed_other] Other missed doses text (number)
Show the field ONLY if:
[antib_presc_af_cul(41)]
```

## repeat_culture (column)

```
[antib_presc_af_cul(41)]
='1'
253 [repeat_culture] 31. Was culture repeated? yesno
1 Yes
Show the field ONLY if:
```

## date_rep_cult (column)

```
[culture_and_sensitivity] 0 No
='1'
254 [date_rep_cult] 32. If yes state date when. text (date_dmy)
Show the field ONLY if:
[repeat_culture]='1'
```

## growth_rep (column)

```
Show the field ONLY if:
[repeat_culture]='1'
255 [growth_rep] 33. Was there growth? yesno
1 Yes
Show the field ONLY if:
```

## num_organis (column)

```
Show the field ONLY if:
[repeat_culture]='1' 0 No
256 [num_organis] 34a. How many organisms were isolated? radio
1 1
Show the field ONLY if:
```

## firs_rep_organis (column)

```
[growth_rep]='1' 2 2
3 3
257 [firs_rep_organis] 34b. First organism isolated text
Show the field ONLY if:
[num_organis]>=1
```

## ast_anti11___1 (column)

```
9/17/25, 11:25 AM GHS-CAMO-Net Project 3 Additional Data Collection | REDCap
258 [ast_anti11] 34c. Antibiotics set for AST checkbox
1 ast_anti11___1 Amikacin
Show the field ONLY if:
[num_organis]>=1 2 ast_anti11___2 Amoxicillin
```

## ast_anti11___2 (column)

```
1 ast_anti11___1 Amikacin
Show the field ONLY if:
[num_organis]>=1 2 ast_anti11___2 Amoxicillin
3 ast_anti11___3 Amoxicillin/Clavulanic
acid
```

## ast_anti11___3 (column)

```
Show the field ONLY if:
[num_organis]>=1 2 ast_anti11___2 Amoxicillin
3 ast_anti11___3 Amoxicillin/Clavulanic
acid
4 ast_anti11___4 Ampicillin
```

## ast_anti11___4 (column)

```
3 ast_anti11___3 Amoxicillin/Clavulanic
acid
4 ast_anti11___4 Ampicillin
5 ast_anti11___5 Ampicillin/Sulbactam
6 ast_anti11___6 Azithromycin
```

## ast_anti11___5 (column)

```
acid
4 ast_anti11___4 Ampicillin
5 ast_anti11___5 Ampicillin/Sulbactam
6 ast_anti11___6 Azithromycin
7 ast_anti11___7 Aztreonam
```

## ast_anti11___6 (column)

```
4 ast_anti11___4 Ampicillin
5 ast_anti11___5 Ampicillin/Sulbactam
6 ast_anti11___6 Azithromycin
7 ast_anti11___7 Aztreonam
8 ast_anti11___8 Cefepime
```

## ast_anti11___7 (column)

```
5 ast_anti11___5 Ampicillin/Sulbactam
6 ast_anti11___6 Azithromycin
7 ast_anti11___7 Aztreonam
8 ast_anti11___8 Cefepime
9 ast_anti11___9 Cefixime
```

## ast_anti11___8 (column)

```
6 ast_anti11___6 Azithromycin
7 ast_anti11___7 Aztreonam
8 ast_anti11___8 Cefepime
9 ast_anti11___9 Cefixime
10 ast_anti11___10 Cefotaxime
```

## ast_anti11___9 (column)

```
7 ast_anti11___7 Aztreonam
8 ast_anti11___8 Cefepime
9 ast_anti11___9 Cefixime
10 ast_anti11___10 Cefotaxime
11 ast_anti11___11 Cefoxitin
```

## ast_anti11___10 (column)

```
8 ast_anti11___8 Cefepime
9 ast_anti11___9 Cefixime
10 ast_anti11___10 Cefotaxime
11 ast_anti11___11 Cefoxitin
12 ast_anti11___12 Ceftazidime
```

## ast_anti11___11 (column)

```
9 ast_anti11___9 Cefixime
10 ast_anti11___10 Cefotaxime
11 ast_anti11___11 Cefoxitin
12 ast_anti11___12 Ceftazidime
13 ast_anti11___13 Ceftriaxone
```

## ast_anti11___12 (column)

```
10 ast_anti11___10 Cefotaxime
11 ast_anti11___11 Cefoxitin
12 ast_anti11___12 Ceftazidime
13 ast_anti11___13 Ceftriaxone
14 ast_anti11___14 Ceftriaxone-
```

## ast_anti11___13 (column)

```
11 ast_anti11___11 Cefoxitin
12 ast_anti11___12 Ceftazidime
13 ast_anti11___13 Ceftriaxone
14 ast_anti11___14 Ceftriaxone-
salbactam
```

## ast_anti11___14 (column)

```
12 ast_anti11___12 Ceftazidime
13 ast_anti11___13 Ceftriaxone
14 ast_anti11___14 Ceftriaxone-
salbactam
15 ast_anti11___15 Cefuroxime
```

## ast_anti11___15 (column)

```
14 ast_anti11___14 Ceftriaxone-
salbactam
15 ast_anti11___15 Cefuroxime
16 ast_anti11___16 Chlorampenicol
17 ast_anti11___17 Ciprofloxacin
```

## ast_anti11___16 (column)

```
salbactam
15 ast_anti11___15 Cefuroxime
16 ast_anti11___16 Chlorampenicol
17 ast_anti11___17 Ciprofloxacin
18 ast_anti11___18 Clindamycin
```

## ast_anti11___17 (column)

```
15 ast_anti11___15 Cefuroxime
16 ast_anti11___16 Chlorampenicol
17 ast_anti11___17 Ciprofloxacin
18 ast_anti11___18 Clindamycin
19 ast_anti11___19 Cofotaxime
```

## ast_anti11___18 (column)

```
16 ast_anti11___16 Chlorampenicol
17 ast_anti11___17 Ciprofloxacin
18 ast_anti11___18 Clindamycin
19 ast_anti11___19 Cofotaxime
20 ast_anti11___20 Doripenem
```

## ast_anti11___19 (column)

```
17 ast_anti11___17 Ciprofloxacin
18 ast_anti11___18 Clindamycin
19 ast_anti11___19 Cofotaxime
20 ast_anti11___20 Doripenem
21 ast_anti11___21 Doxycycline
```

## ast_anti11___20 (column)

```
18 ast_anti11___18 Clindamycin
19 ast_anti11___19 Cofotaxime
20 ast_anti11___20 Doripenem
21 ast_anti11___21 Doxycycline
22 ast_anti11___22 Ertapenem
```

## ast_anti11___21 (column)

```
19 ast_anti11___19 Cofotaxime
20 ast_anti11___20 Doripenem
21 ast_anti11___21 Doxycycline
22 ast_anti11___22 Ertapenem
23 ast_anti11___23 Erythromycin
```

## ast_anti11___22 (column)

```
20 ast_anti11___20 Doripenem
21 ast_anti11___21 Doxycycline
22 ast_anti11___22 Ertapenem
23 ast_anti11___23 Erythromycin
24 ast_anti11___24 Gentamicin
```

## ast_anti11___23 (column)

```
21 ast_anti11___21 Doxycycline
22 ast_anti11___22 Ertapenem
23 ast_anti11___23 Erythromycin
24 ast_anti11___24 Gentamicin
25 ast_anti11___25 Imipenem
```

## ast_anti11___24 (column)

```
22 ast_anti11___22 Ertapenem
23 ast_anti11___23 Erythromycin
24 ast_anti11___24 Gentamicin
25 ast_anti11___25 Imipenem
26 ast_anti11___26 Levofloxacin
```

## ast_anti11___25 (column)

```
23 ast_anti11___23 Erythromycin
24 ast_anti11___24 Gentamicin
25 ast_anti11___25 Imipenem
26 ast_anti11___26 Levofloxacin
27 ast_anti11___27 Linezolid
```

## ast_anti11___26 (column)

```
24 ast_anti11___24 Gentamicin
25 ast_anti11___25 Imipenem
26 ast_anti11___26 Levofloxacin
27 ast_anti11___27 Linezolid
28 ast_anti11___28 Meropenem
```

## ast_anti11___27 (column)

```
25 ast_anti11___25 Imipenem
26 ast_anti11___26 Levofloxacin
27 ast_anti11___27 Linezolid
28 ast_anti11___28 Meropenem
29 ast_anti11___29 Nalidixic acid
```

## ast_anti11___28 (column)

```
26 ast_anti11___26 Levofloxacin
27 ast_anti11___27 Linezolid
28 ast_anti11___28 Meropenem
29 ast_anti11___29 Nalidixic acid
30 ast_anti11___30 Nitrofurantoin
```

## ast_anti11___29 (column)

```
27 ast_anti11___27 Linezolid
28 ast_anti11___28 Meropenem
29 ast_anti11___29 Nalidixic acid
30 ast_anti11___30 Nitrofurantoin
31 ast_anti11___31 Oxacillin
```

## ast_anti11___30 (column)

```
28 ast_anti11___28 Meropenem
29 ast_anti11___29 Nalidixic acid
30 ast_anti11___30 Nitrofurantoin
31 ast_anti11___31 Oxacillin
32 ast_anti11___32 Penicillin G
```

## ast_anti11___31 (column)

```
29 ast_anti11___29 Nalidixic acid
30 ast_anti11___30 Nitrofurantoin
31 ast_anti11___31 Oxacillin
32 ast_anti11___32 Penicillin G
33 ast_anti11___33 Piperacillin
```

## ast_anti11___32 (column)

```
30 ast_anti11___30 Nitrofurantoin
31 ast_anti11___31 Oxacillin
32 ast_anti11___32 Penicillin G
33 ast_anti11___33 Piperacillin
34 ast_anti11___34 Piperacillin
```

## ast_anti11___33 (column)

```
31 ast_anti11___31 Oxacillin
32 ast_anti11___32 Penicillin G
33 ast_anti11___33 Piperacillin
34 ast_anti11___34 Piperacillin
tazobactam
```

## ast_anti11___34 (column)

```
32 ast_anti11___32 Penicillin G
33 ast_anti11___33 Piperacillin
34 ast_anti11___34 Piperacillin
tazobactam
35 ast_anti11___35 Rifampin
```

## ast_anti11___35 (column)

```
34 ast_anti11___34 Piperacillin
tazobactam
35 ast_anti11___35 Rifampin
36 ast_anti11___36 Streptomycin
37 ast_anti11___37 Tetracycline
```

## ast_anti11___36 (column)

```
tazobactam
35 ast_anti11___35 Rifampin
36 ast_anti11___36 Streptomycin
37 ast_anti11___37 Tetracycline
38 ast_anti11___38 Tigecycline
```

## ast_anti11___37 (column)

```
35 ast_anti11___35 Rifampin
36 ast_anti11___36 Streptomycin
37 ast_anti11___37 Tetracycline
38 ast_anti11___38 Tigecycline
39 ast_anti11___39 Trimethoprim/
```

## ast_anti11___38 (column)

```
36 ast_anti11___36 Streptomycin
37 ast_anti11___37 Tetracycline
38 ast_anti11___38 Tigecycline
39 ast_anti11___39 Trimethoprim/
Sulfamethoxazole
```

## ast_anti11___39 (column)

```
37 ast_anti11___37 Tetracycline
38 ast_anti11___38 Tigecycline
39 ast_anti11___39 Trimethoprim/
Sulfamethoxazole
40 ast_anti11___40 Vancomycin
```

## ast_anti11___40 (column)

```
39 ast_anti11___39 Trimethoprim/
Sulfamethoxazole
40 ast_anti11___40 Vancomycin
https://idiredcap.idi.co.ug/redcap_v14.7.4/Design/data_dictionary_codebook.php?pid=147 30/48
9/17/25, 11:25 AM GHS-CAMO-Net Project 3 Additional Data Collection | REDCap
```

## ast_anti11___41 (column)

```
https://idiredcap.idi.co.ug/redcap_v14.7.4/Design/data_dictionary_codebook.php?pid=147 30/48
9/17/25, 11:25 AM GHS-CAMO-Net Project 3 Additional Data Collection | REDCap
41 ast_anti11___41 Others1
42 ast_anti11___42 Others2
259 [firsrep_amikacin] Amikacin radio (Matrix)
```

## ast_anti11___42 (column)

```
9/17/25, 11:25 AM GHS-CAMO-Net Project 3 Additional Data Collection | REDCap
41 ast_anti11___41 Others1
42 ast_anti11___42 Others2
259 [firsrep_amikacin] Amikacin radio (Matrix)
1 Resistant
```

## firsrep_amikacin (column)

```
41 ast_anti11___41 Others1
42 ast_anti11___42 Others2
259 [firsrep_amikacin] Amikacin radio (Matrix)
1 Resistant
Show the field ONLY if:
```

## firsrep_amoxicillin (column)

```
[ast_anti11(1)]='1' 2 Intermediate
3 Susceptible
260 [firsrep_amoxicillin] Amoxicillin radio (Matrix)
1 Resistant
Show the field ONLY if:
```

## firsrep_amoxiclav (column)

```
[ast_anti11(2)]='1' 2 Intermediate
3 Susceptible
261 [firsrep_amoxiclav] Amoxicillin/Clavulanic acid radio (Matrix)
1 Resistant
Show the field ONLY if:
```

## firsrep_ampicillin (column)

```
[ast_anti11(3)]='1' 2 Intermediate
3 Susceptible
262 [firsrep_ampicillin] Ampicillin radio (Matrix)
1 Resistant
Show the field ONLY if:
```

## firsrep_azithromycin (column)

```
[ast_anti11(5)]='1'
3 Susceptible
264 [firsrep_azithromycin] Azithromycin radio (Matrix)
1 Resistant
Show the field ONLY if:
```

## firsrep_aztreonam (column)

```
[ast_anti11(6)]='1' 2 Intermediate
3 Susceptible
265 [firsrep_aztreonam] Aztreonam radio (Matrix)
1 Resistant
Show the field ONLY if:
```

## firsrep_cefepime (column)

```
[ast_anti11(7)]='1' 2 Intermediate
3 Susceptible
266 [firsrep_cefepime] Cefepime radio (Matrix)
1 Resistant
Show the field ONLY if:
```

## firsrep_cefixime (column)

```
[ast_anti11(8)]='1' 2 Intermediate
3 Susceptible
267 [firsrep_cefixime] Cefixime radio (Matrix)
1 Resistant
Show the field ONLY if:
```

## firsrep_cefotaxime (column)

```
[ast_anti11(9)]='1' 2 Intermediate
3 Susceptible
268 [firsrep_cefotaxime] Cefotaxime radio (Matrix)
1 Resistant
Show the field ONLY if:
```

## firsrep_cefoxitin (column)

```
[ast_anti11(10)]='1' 2 Intermediate
3 Susceptible
269 [firsrep_cefoxitin] Cefoxitin radio (Matrix)
https://idiredcap.idi.co.ug/redcap_v14.7.4/Design/data_dictionary_codebook.php?pid=147 31/48
9/17/25, 11:25 AM GHS-CAMO-Net Project 3 Additional Data Collection | REDCap
```

## firsrep_ceftazidime (column)

```
2 Intermediate
3 Susceptible
270 [firsrep_ceftazidime] Ceftazidime radio (Matrix)
1 Resistant
Show the field ONLY if:
```

## firsrep_ceftriaxone (column)

```
[ast_anti11(12)]='1' 2 Intermediate
3 Susceptible
271 [firsrep_ceftriaxone] Ceftriaxone radio (Matrix)
1 Resistant
Show the field ONLY if:
```

## firsrep_cefsalbactam (column)

```
[ast_anti11(13)]='1' 2 Intermediate
3 Susceptible
272 [firsrep_cefsalbactam] Ceftriaxone-salbactam radio (Matrix)
1 Resistant
Show the field ONLY if:
```

## firsrep_cefuroxime (column)

```
[ast_anti11(14)]='1' 2 Intermediate
3 Susceptible
273 [firsrep_cefuroxime] Cefuroxime radio (Matrix)
1 Resistant
Show the field ONLY if:
```

## firsrep_clindamycin (column)

```
[ast_anti11(17)]='1'
3 Susceptible
276 [firsrep_clindamycin] Clindamycin radio (Matrix)
1 Resistant
Show the field ONLY if:
```

## firsrep_cofotaxime (column)

```
[ast_anti11(18)]='1' 2 Intermediate
3 Susceptible
277 [firsrep_cofotaxime] Cofotaxime radio (Matrix)
1 Resistant
Show the field ONLY if:
```

## firsrep_doripenem (column)

```
[ast_anti11(19)]='1' 2 Intermediate
3 Susceptible
278 [firsrep_doripenem] Doripenem radio (Matrix)
1 Resistant
Show the field ONLY if:
```

## firsrep_doxycycline (column)

```
[ast_anti11(20)]='1' 2 Intermediate
3 Susceptible
279 [firsrep_doxycycline] Doxycycline radio (Matrix)
1 Resistant
Show the field ONLY if:
```

## firsrep_ertapenem (column)

```
https://idiredcap.idi.co.ug/redcap_v14.7.4/Design/data_dictionary_codebook.php?pid=147 32/48
9/17/25, 11:25 AM GHS-CAMO-Net Project 3 Additional Data Collection | REDCap
280 [firsrep_ertapenem] Ertapenem radio (Matrix)
1 Resistant
Show the field ONLY if:
```

## firsrep_erythromycin (column)

```
[ast_anti11(22)]='1' 2 Intermediate
3 Susceptible
281 [firsrep_erythromycin] Erythromycin radio (Matrix)
1 Resistant
Show the field ONLY if:
```

## firsrep_gentamicin (column)

```
[ast_anti11(23)]='1' 2 Intermediate
3 Susceptible
282 [firsrep_gentamicin] Gentamicin radio (Matrix)
1 Resistant
Show the field ONLY if:
```

## firsrep_imipenem (column)

```
[ast_anti11(24)]='1' 2 Intermediate
3 Susceptible
283 [firsrep_imipenem] Imipenem radio (Matrix)
1 Resistant
Show the field ONLY if:
```

## firsrep_levofloxacin (column)

```
[ast_anti11(25)]='1' 2 Intermediate
3 Susceptible
284 [firsrep_levofloxacin] Levofloxacin radio (Matrix)
1 Resistant
Show the field ONLY if:
```

## firsrep_linezolid (column)

```
[ast_anti11(26)]='1' 2 Intermediate
3 Susceptible
285 [firsrep_linezolid] Linezolid radio (Matrix)
1 Resistant
Show the field ONLY if:
```

## firsrep_meropenem (column)

```
[ast_anti11(27)]='1' 2 Intermediate
3 Susceptible
286 [firsrep_meropenem] Meropenem radio (Matrix)
1 Resistant
Show the field ONLY if:
```

## firsrep_oxacillin (column)

```
[ast_anti11(30)]='1'
3 Susceptible
289 [firsrep_oxacillin] Oxacillin radio (Matrix)
1 Resistant
Show the field ONLY if:
```

## firsrep_pen_g (column)

```
https://idiredcap.idi.co.ug/redcap_v14.7.4/Design/data_dictionary_codebook.php?pid=147 33/48
9/17/25, 11:25 AM GHS-CAMO-Net Project 3 Additional Data Collection | REDCap
290 [firsrep_pen_g] Penicillin G radio (Matrix)
1 Resistant
Show the field ONLY if:
```

## firsrep_piperacillin (column)

```
[ast_anti11(32)]='1' 2 Intermediate
3 Susceptible
291 [firsrep_piperacillin] Piperacillin radio (Matrix)
1 Resistant
Show the field ONLY if:
```

## firsrep_rifampin (column)

```
[ast_anti11(34)]='1'
3 Susceptible
293 [firsrep_rifampin] Rifampin radio (Matrix)
1 Resistant
Show the field ONLY if:
```

## firsrep_streptomycin (column)

```
[ast_anti11(35)]='1' 2 Intermediate
3 Susceptible
294 [firsrep_streptomycin] Streptomycin radio (Matrix)
1 Resistant
Show the field ONLY if:
```

## firsrep_tetracycline (column)

```
[ast_anti11(36)]='1' 2 Intermediate
3 Susceptible
295 [firsrep_tetracycline] Tetracycline radio (Matrix)
1 Resistant
Show the field ONLY if:
```

## firsrep_tigecycline (column)

```
[ast_anti11(37)]='1' 2 Intermediate
3 Susceptible
296 [firsrep_tigecycline] Tigecycline radio (Matrix)
1 Resistant
Show the field ONLY if:
```

## firsrep_sxt (column)

```
[ast_anti11(38)]='1' 2 Intermediate
3 Susceptible
297 [firsrep_sxt] Trimethoprim/ Sulfamethoxazole radio (Matrix)
1 Resistant
Show the field ONLY if:
```

## firsrep_vancomycin (column)

```
[ast_anti11(39)]='1' 2 Intermediate
3 Susceptible
298 [firsrep_vancomycin] Vancomycin radio (Matrix)
1 Resistant
Show the field ONLY if:
```

## firsrep_othe (column)

```
[ast_anti11(40)]='1' 2 Intermediate
3 Susceptible
299 [firsrep_othe] Other antibiotic, please specify text
Show the field ONLY if:
[ast_anti11(41)]='1'
```

## firsrep_oth_ast (column)

```
Show the field ONLY if:
[ast_anti11(41)]='1'
300 [firsrep_oth_ast] Other antibiotic AST results radio
1 Resistant
Show the field ONLY if:
```

## firsrep_oth2_name (column)

```
[ast_anti11(41)]='1' 2 Intermediate
3 Susceptible
301 [firsrep_oth2_name] Other antibiotic, please specify text
https://idiredcap.idi.co.ug/redcap_v14.7.4/Design/data_dictionary_codebook.php?pid=147 34/48
9/17/25, 11:25 AM GHS-CAMO-Net Project 3 Additional Data Collection | REDCap
```

## firsrep_oth2_ast (column)

```
Show the field ONLY if:
[ast_anti11(42)]='1'
302 [firsrep_oth2_ast] Other antibiotic AST results radio
1 Resistant
Show the field ONLY if:
```

## sec_rep_organis (column)

```
[ast_anti11(42)]='1' 2 Intermediate
3 Susceptible
303 [sec_rep_organis] 34d. Second organism isolated text
Show the field ONLY if:
[num_organis]>=2
```

## ast_anti22___1 (column)

```
[num_organis]>=2
304 [ast_anti22] 34e. Antibiotics set for AST checkbox
1 ast_anti22___1 Amikacin
Show the field ONLY if:
[num_organis]>=2 2 ast_anti22___2 Amoxicillin
```

## ast_anti22___2 (column)

```
1 ast_anti22___1 Amikacin
Show the field ONLY if:
[num_organis]>=2 2 ast_anti22___2 Amoxicillin
3 ast_anti22___3 Amoxicillin/Clavulanic
acid
```

## ast_anti22___3 (column)

```
Show the field ONLY if:
[num_organis]>=2 2 ast_anti22___2 Amoxicillin
3 ast_anti22___3 Amoxicillin/Clavulanic
acid
4 ast_anti22___4 Ampicillin
```

## ast_anti22___4 (column)

```
3 ast_anti22___3 Amoxicillin/Clavulanic
acid
4 ast_anti22___4 Ampicillin
5 ast_anti22___5 Ampicillin/Sulbactam
6 ast_anti22___6 Azithromycin
```

## ast_anti22___5 (column)

```
acid
4 ast_anti22___4 Ampicillin
5 ast_anti22___5 Ampicillin/Sulbactam
6 ast_anti22___6 Azithromycin
7 ast_anti22___7 Aztreonam
```

## ast_anti22___6 (column)

```
4 ast_anti22___4 Ampicillin
5 ast_anti22___5 Ampicillin/Sulbactam
6 ast_anti22___6 Azithromycin
7 ast_anti22___7 Aztreonam
8 ast_anti22___8 Cefepime
```

## ast_anti22___7 (column)

```
5 ast_anti22___5 Ampicillin/Sulbactam
6 ast_anti22___6 Azithromycin
7 ast_anti22___7 Aztreonam
8 ast_anti22___8 Cefepime
9 ast_anti22___9 Cefixime
```

## ast_anti22___8 (column)

```
6 ast_anti22___6 Azithromycin
7 ast_anti22___7 Aztreonam
8 ast_anti22___8 Cefepime
9 ast_anti22___9 Cefixime
10 ast_anti22___10 Cefotaxime
```

## ast_anti22___9 (column)

```
7 ast_anti22___7 Aztreonam
8 ast_anti22___8 Cefepime
9 ast_anti22___9 Cefixime
10 ast_anti22___10 Cefotaxime
11 ast_anti22___11 Cefoxitin
```

## ast_anti22___10 (column)

```
8 ast_anti22___8 Cefepime
9 ast_anti22___9 Cefixime
10 ast_anti22___10 Cefotaxime
11 ast_anti22___11 Cefoxitin
12 ast_anti22___12 Ceftazidime
```

## ast_anti22___11 (column)

```
9 ast_anti22___9 Cefixime
10 ast_anti22___10 Cefotaxime
11 ast_anti22___11 Cefoxitin
12 ast_anti22___12 Ceftazidime
13 ast_anti22___13 Ceftriaxone
```

## ast_anti22___12 (column)

```
10 ast_anti22___10 Cefotaxime
11 ast_anti22___11 Cefoxitin
12 ast_anti22___12 Ceftazidime
13 ast_anti22___13 Ceftriaxone
14 ast_anti22___14 Ceftriaxone-
```

## ast_anti22___13 (column)

```
11 ast_anti22___11 Cefoxitin
12 ast_anti22___12 Ceftazidime
13 ast_anti22___13 Ceftriaxone
14 ast_anti22___14 Ceftriaxone-
salbactam
```

## ast_anti22___14 (column)

```
12 ast_anti22___12 Ceftazidime
13 ast_anti22___13 Ceftriaxone
14 ast_anti22___14 Ceftriaxone-
salbactam
15 ast_anti22___15 Cefuroxime
```

## ast_anti22___15 (column)

```
14 ast_anti22___14 Ceftriaxone-
salbactam
15 ast_anti22___15 Cefuroxime
16 ast_anti22___16 Chlorampenicol
17 ast_anti22___17 Ciprofloxacin
```

## ast_anti22___16 (column)

```
salbactam
15 ast_anti22___15 Cefuroxime
16 ast_anti22___16 Chlorampenicol
17 ast_anti22___17 Ciprofloxacin
18 ast_anti22___18 Clindamycin
```

## ast_anti22___17 (column)

```
15 ast_anti22___15 Cefuroxime
16 ast_anti22___16 Chlorampenicol
17 ast_anti22___17 Ciprofloxacin
18 ast_anti22___18 Clindamycin
19 ast_anti22___19 Cofotaxime
```

## ast_anti22___18 (column)

```
16 ast_anti22___16 Chlorampenicol
17 ast_anti22___17 Ciprofloxacin
18 ast_anti22___18 Clindamycin
19 ast_anti22___19 Cofotaxime
20 ast_anti22___20 Doripenem
```

## ast_anti22___19 (column)

```
17 ast_anti22___17 Ciprofloxacin
18 ast_anti22___18 Clindamycin
19 ast_anti22___19 Cofotaxime
20 ast_anti22___20 Doripenem
21 ast_anti22___21 Doxycycline
```

## ast_anti22___20 (column)

```
18 ast_anti22___18 Clindamycin
19 ast_anti22___19 Cofotaxime
20 ast_anti22___20 Doripenem
21 ast_anti22___21 Doxycycline
22 ast_anti22___22 Ertapenem
```

## ast_anti22___21 (column)

```
19 ast_anti22___19 Cofotaxime
20 ast_anti22___20 Doripenem
21 ast_anti22___21 Doxycycline
22 ast_anti22___22 Ertapenem
23 ast_anti22___23 Erythromycin
```

## ast_anti22___22 (column)

```
20 ast_anti22___20 Doripenem
21 ast_anti22___21 Doxycycline
22 ast_anti22___22 Ertapenem
23 ast_anti22___23 Erythromycin
24 ast_anti22___24 Gentamicin
```

## ast_anti22___23 (column)

```
21 ast_anti22___21 Doxycycline
22 ast_anti22___22 Ertapenem
23 ast_anti22___23 Erythromycin
24 ast_anti22___24 Gentamicin
25 ast_anti22___25 Imipenem
```

## ast_anti22___24 (column)

```
22 ast_anti22___22 Ertapenem
23 ast_anti22___23 Erythromycin
24 ast_anti22___24 Gentamicin
25 ast_anti22___25 Imipenem
26 ast_anti22___26 Levofloxacin
```

## ast_anti22___25 (column)

```
23 ast_anti22___23 Erythromycin
24 ast_anti22___24 Gentamicin
25 ast_anti22___25 Imipenem
26 ast_anti22___26 Levofloxacin
27 ast_anti22___27 Linezolid
```

## ast_anti22___26 (column)

```
24 ast_anti22___24 Gentamicin
25 ast_anti22___25 Imipenem
26 ast_anti22___26 Levofloxacin
27 ast_anti22___27 Linezolid
28 ast_anti22___28 Meropenem
```

## ast_anti22___27 (column)

```
25 ast_anti22___25 Imipenem
26 ast_anti22___26 Levofloxacin
27 ast_anti22___27 Linezolid
28 ast_anti22___28 Meropenem
29 ast_anti22___29 Nalidixic acid
```

## ast_anti22___28 (column)

```
26 ast_anti22___26 Levofloxacin
27 ast_anti22___27 Linezolid
28 ast_anti22___28 Meropenem
29 ast_anti22___29 Nalidixic acid
30 ast_anti22___30 Nitrofurantoin
```

## ast_anti22___29 (column)

```
27 ast_anti22___27 Linezolid
28 ast_anti22___28 Meropenem
29 ast_anti22___29 Nalidixic acid
30 ast_anti22___30 Nitrofurantoin
31 ast_anti22___31 Oxacillin
```

## ast_anti22___30 (column)

```
28 ast_anti22___28 Meropenem
29 ast_anti22___29 Nalidixic acid
30 ast_anti22___30 Nitrofurantoin
31 ast_anti22___31 Oxacillin
32 ast_anti22___32 Penicillin G
```

## ast_anti22___31 (column)

```
29 ast_anti22___29 Nalidixic acid
30 ast_anti22___30 Nitrofurantoin
31 ast_anti22___31 Oxacillin
32 ast_anti22___32 Penicillin G
33 ast_anti22___33 Piperacillin
```

## ast_anti22___32 (column)

```
30 ast_anti22___30 Nitrofurantoin
31 ast_anti22___31 Oxacillin
32 ast_anti22___32 Penicillin G
33 ast_anti22___33 Piperacillin
https://idiredcap.idi.co.ug/redcap_v14.7.4/Design/data_dictionary_codebook.php?pid=147 35/48
```

## ast_anti22___33 (column)

```
31 ast_anti22___31 Oxacillin
32 ast_anti22___32 Penicillin G
33 ast_anti22___33 Piperacillin
https://idiredcap.idi.co.ug/redcap_v14.7.4/Design/data_dictionary_codebook.php?pid=147 35/48
9/17/25, 11:25 AM GHS-CAMO-Net Project 3 Additional Data Collection | REDCap
```

## ast_anti22___34 (column)

```
https://idiredcap.idi.co.ug/redcap_v14.7.4/Design/data_dictionary_codebook.php?pid=147 35/48
9/17/25, 11:25 AM GHS-CAMO-Net Project 3 Additional Data Collection | REDCap
34 ast_anti22___34 Piperacillin
tazobactam
35 ast_anti22___35 Rifampin
```

## ast_anti22___35 (column)

```
34 ast_anti22___34 Piperacillin
tazobactam
35 ast_anti22___35 Rifampin
36 ast_anti22___36 Streptomycin
37 ast_anti22___37 Tetracycline
```

## ast_anti22___36 (column)

```
tazobactam
35 ast_anti22___35 Rifampin
36 ast_anti22___36 Streptomycin
37 ast_anti22___37 Tetracycline
38 ast_anti22___38 Tigecycline
```

## ast_anti22___37 (column)

```
35 ast_anti22___35 Rifampin
36 ast_anti22___36 Streptomycin
37 ast_anti22___37 Tetracycline
38 ast_anti22___38 Tigecycline
39 ast_anti22___39 Trimethoprim/
```

## ast_anti22___38 (column)

```
36 ast_anti22___36 Streptomycin
37 ast_anti22___37 Tetracycline
38 ast_anti22___38 Tigecycline
39 ast_anti22___39 Trimethoprim/
Sulfamethoxazole
```

## ast_anti22___39 (column)

```
37 ast_anti22___37 Tetracycline
38 ast_anti22___38 Tigecycline
39 ast_anti22___39 Trimethoprim/
Sulfamethoxazole
40 ast_anti22___40 Vancomycin
```

## ast_anti22___40 (column)

```
39 ast_anti22___39 Trimethoprim/
Sulfamethoxazole
40 ast_anti22___40 Vancomycin
41 ast_anti22___41 Others1
42 ast_anti22___42 Others2
```

## ast_anti22___41 (column)

```
Sulfamethoxazole
40 ast_anti22___40 Vancomycin
41 ast_anti22___41 Others1
42 ast_anti22___42 Others2
305 [secrep_amikacin] Amikacin radio (Matrix)
```

## ast_anti22___42 (column)

```
40 ast_anti22___40 Vancomycin
41 ast_anti22___41 Others1
42 ast_anti22___42 Others2
305 [secrep_amikacin] Amikacin radio (Matrix)
1 Resistant
```

## secrep_amikacin (column)

```
41 ast_anti22___41 Others1
42 ast_anti22___42 Others2
305 [secrep_amikacin] Amikacin radio (Matrix)
1 Resistant
Show the field ONLY if:
```

## secrep_amoxicillin (column)

```
[ast_anti22(1)]='1' 2 Intermediate
3 Susceptible
306 [secrep_amoxicillin] Amoxicillin radio (Matrix)
1 Resistant
Show the field ONLY if:
```

## secrep_amoxiclav (column)

```
[ast_anti22(2)]='1' 2 Intermediate
3 Susceptible
307 [secrep_amoxiclav] Amoxicillin/Clavulanic acid radio (Matrix)
1 Resistant
Show the field ONLY if:
```

## secrep_ampicillin (column)

```
[ast_anti22(3)]='1' 2 Intermediate
3 Susceptible
308 [secrep_ampicillin] Ampicillin radio (Matrix)
1 Resistant
Show the field ONLY if:
```

## secrep_amp_sulbactam (column)

```
[ast_anti22(4)]='1' 2 Intermediate
3 Susceptible
309 [secrep_amp_sulbactam] Ampicillin/Sulbactam radio (Matrix)
1 Resistant
Show the field ONLY if:
```

## secrep_azithromycin (column)

```
[ast_anti22(5)]='1' 2 Intermediate
3 Susceptible
310 [secrep_azithromycin] Azithromycin radio (Matrix)
1 Resistant
Show the field ONLY if:
```

## secrep_aztreonam (column)

```
[ast_anti22(6)]='1' 2 Intermediate
3 Susceptible
311 [secrep_aztreonam] Aztreonam radio (Matrix)
1 Resistant
Show the field ONLY if:
```

## secrep_cefepime (column)

```
[ast_anti22(7)]='1' 2 Intermediate
3 Susceptible
312 [secrep_cefepime] Cefepime radio (Matrix)
1 Resistant
Show the field ONLY if:
```

## secrep_cefixime (column)

```
[ast_anti22(8)]='1' 2 Intermediate
3 Susceptible
313 [secrep_cefixime] Cefixime radio (Matrix)
https://idiredcap.idi.co.ug/redcap_v14.7.4/Design/data_dictionary_codebook.php?pid=147 36/48
9/17/25, 11:25 AM GHS-CAMO-Net Project 3 Additional Data Collection | REDCap
```

## secrep_cefotaxime (column)

```
2 Intermediate
3 Susceptible
314 [secrep_cefotaxime] Cefotaxime radio (Matrix)
1 Resistant
Show the field ONLY if:
```

## secrep_cefoxitin (column)

```
[ast_anti22(10)]='1' 2 Intermediate
3 Susceptible
315 [secrep_cefoxitin] Cefoxitin radio (Matrix)
1 Resistant
Show the field ONLY if:
```

## secrep_ceftazidime (column)

```
[ast_anti22(11)]='1' 2 Intermediate
3 Susceptible
316 [secrep_ceftazidime] Ceftazidime radio (Matrix)
1 Resistant
Show the field ONLY if:
```

## secrep_ceftriaxone (column)

```
[ast_anti22(12)]='1' 2 Intermediate
3 Susceptible
317 [secrep_ceftriaxone] Ceftriaxone radio (Matrix)
1 Resistant
Show the field ONLY if:
```

## secrep_cefsalbactam (column)

```
[ast_anti22(13)]='1' 2 Intermediate
3 Susceptible
318 [secrep_cefsalbactam] Ceftriaxone-salbactam radio (Matrix)
1 Resistant
Show the field ONLY if:
```

## secrep_cefuroxime (column)

```
[ast_anti22(14)]='1' 2 Intermediate
3 Susceptible
319 [secrep_cefuroxime] Cefuroxime radio (Matrix)
1 Resistant
Show the field ONLY if:
```

## secrep_ciprofloxacin (column)

```
[ast_anti22(16)]='1'
3 Susceptible
321 [secrep_ciprofloxacin] Ciprofloxacin radio (Matrix)
1 Resistant
Show the field ONLY if:
```

## secrep_clindamycin (column)

```
[ast_anti22(17)]='1' 2 Intermediate
3 Susceptible
322 [secrep_clindamycin] Clindamycin radio (Matrix)
1 Resistant
Show the field ONLY if:
```

## secrep_cofotaxime (column)

```
[ast_anti22(18)]='1' 2 Intermediate
3 Susceptible
323 [secrep_cofotaxime] Cofotaxime radio (Matrix)
1 Resistant
Show the field ONLY if:
```

## secrep_doripenem (column)

```
https://idiredcap.idi.co.ug/redcap_v14.7.4/Design/data_dictionary_codebook.php?pid=147 37/48
9/17/25, 11:25 AM GHS-CAMO-Net Project 3 Additional Data Collection | REDCap
324 [secrep_doripenem] Doripenem radio (Matrix)
1 Resistant
Show the field ONLY if:
```

## secrep_doxycycline (column)

```
[ast_anti22(20)]='1' 2 Intermediate
3 Susceptible
325 [secrep_doxycycline] Doxycycline radio (Matrix)
1 Resistant
Show the field ONLY if:
```

## secrep_ertapenem (column)

```
[ast_anti22(21)]='1' 2 Intermediate
3 Susceptible
326 [secrep_ertapenem] Ertapenem radio (Matrix)
1 Resistant
Show the field ONLY if:
```

## secrep_erythromycin (column)

```
[ast_anti22(22)]='1' 2 Intermediate
3 Susceptible
327 [secrep_erythromycin] Erythromycin radio (Matrix)
1 Resistant
Show the field ONLY if:
```

## secrep_gentamicin (column)

```
[ast_anti22(23)]='1' 2 Intermediate
3 Susceptible
328 [secrep_gentamicin] Gentamicin radio (Matrix)
1 Resistant
Show the field ONLY if:
```

## secrep_imipenem (column)

```
[ast_anti22(24)]='1' 2 Intermediate
3 Susceptible
329 [secrep_imipenem] Imipenem radio (Matrix)
1 Resistant
Show the field ONLY if:
```

## secrep_levofloxacin (column)

```
[ast_anti22(25)]='1' 2 Intermediate
3 Susceptible
330 [secrep_levofloxacin] Levofloxacin radio (Matrix)
1 Resistant
Show the field ONLY if:
```

## secrep_linezolid (column)

```
[ast_anti22(26)]='1' 2 Intermediate
3 Susceptible
331 [secrep_linezolid] Linezolid radio (Matrix)
1 Resistant
Show the field ONLY if:
```

## secrep_meropenem (column)

```
[ast_anti22(27)]='1' 2 Intermediate
3 Susceptible
332 [secrep_meropenem] Meropenem radio (Matrix)
1 Resistant
Show the field ONLY if:
```

## secrep_nalidixicacid (column)

```
[ast_anti22(28)]='1' 2 Intermediate
3 Susceptible
333 [secrep_nalidixicacid] Nalidixic acid radio (Matrix)
1 Resistant
Show the field ONLY if:
```

## secrep_oxacillin (column)

```
[ast_anti22(30)]='1'
3 Susceptible
335 [secrep_oxacillin] Oxacillin radio (Matrix)
1 Resistant
Show the field ONLY if:
```

## secrep_pen_g (column)

```
[ast_anti22(31)]='1' 2 Intermediate
3 Susceptible
336 [secrep_pen_g] Penicillin G radio (Matrix)
1 Resistant
Show the field ONLY if:
```

## secrep_piperacillin (column)

```
[ast_anti22(32)]='1' 2 Intermediate
3 Susceptible
337 [secrep_piperacillin] Piperacillin radio (Matrix)
1 Resistant
Show the field ONLY if:
```

## secrep_rifampin (column)

```
[ast_anti22(34)]='1'
3 Susceptible
339 [secrep_rifampin] Rifampin radio (Matrix)
1 Resistant
Show the field ONLY if:
```

## secrep_streptomycin (column)

```
[ast_anti22(35)]='1' 2 Intermediate
3 Susceptible
340 [secrep_streptomycin] Streptomycin radio (Matrix)
1 Resistant
Show the field ONLY if:
```

## secrep_tetracycline (column)

```
[ast_anti22(36)]='1' 2 Intermediate
3 Susceptible
341 [secrep_tetracycline] Tetracycline radio (Matrix)
1 Resistant
Show the field ONLY if:
```

## secrep_tigecycline (column)

```
[ast_anti22(37)]='1' 2 Intermediate
3 Susceptible
342 [secrep_tigecycline] Tigecycline radio (Matrix)
1 Resistant
Show the field ONLY if:
```

## secrep_sxt (column)

```
[ast_anti22(38)]='1' 2 Intermediate
3 Susceptible
343 [secrep_sxt] Trimethoprim/ Sulfamethoxazole radio (Matrix)
1 Resistant
Show the field ONLY if:
```

## secrep_vancomycin (column)

```
https://idiredcap.idi.co.ug/redcap_v14.7.4/Design/data_dictionary_codebook.php?pid=147 39/48
9/17/25, 11:25 AM GHS-CAMO-Net Project 3 Additional Data Collection | REDCap
344 [secrep_vancomycin] Vancomycin radio (Matrix)
1 Resistant
Show the field ONLY if:
```

## secrep_othe (column)

```
[ast_anti22(40)]='1' 2 Intermediate
3 Susceptible
345 [secrep_othe] Other antibiotic, please specify text
Show the field ONLY if:
[ast_anti22(41)]='1'
```

## secrep_oth_ast (column)

```
Show the field ONLY if:
[ast_anti22(41)]='1'
346 [secrep_oth_ast] Other antibiotic AST results radio
1 Resistant
Show the field ONLY if:
```

## secrep_oth2_name (column)

```
[ast_anti22(41)]='1' 2 Intermediate
3 Susceptible
347 [secrep_oth2_name] Other antibiotic, please specify text
Show the field ONLY if:
[ast_anti22(42)]='1'
```

## secrep_oth2_ast (column)

```
Show the field ONLY if:
[ast_anti22(42)]='1'
348 [secrep_oth2_ast] Other antibiotic AST results radio
1 Resistant
Show the field ONLY if:
```

## third_rep_organis (column)

```
[ast_anti22(42)]='1' 2 Intermediate
3 Susceptible
349 [third_rep_organis] 34f. Third organism isolated text
Show the field ONLY if:
[num_organis]>=3
```

## ast_anti33___1 (column)

```
[num_organis]>=3
350 [ast_anti33] 34g. Antibiotics set for AST checkbox
1 ast_anti33___1 Amikacin
Show the field ONLY if:
[num_organis]>=3 2 ast_anti33___2 Amoxicillin
```

## ast_anti33___2 (column)

```
1 ast_anti33___1 Amikacin
Show the field ONLY if:
[num_organis]>=3 2 ast_anti33___2 Amoxicillin
3 ast_anti33___3 Amoxicillin/Clavulanic
acid
```

## ast_anti33___3 (column)

```
Show the field ONLY if:
[num_organis]>=3 2 ast_anti33___2 Amoxicillin
3 ast_anti33___3 Amoxicillin/Clavulanic
acid
4 ast_anti33___4 Ampicillin
```

## ast_anti33___4 (column)

```
3 ast_anti33___3 Amoxicillin/Clavulanic
acid
4 ast_anti33___4 Ampicillin
5 ast_anti33___5 Ampicillin/Sulbactam
6 ast_anti33___6 Azithromycin
```

## ast_anti33___5 (column)

```
acid
4 ast_anti33___4 Ampicillin
5 ast_anti33___5 Ampicillin/Sulbactam
6 ast_anti33___6 Azithromycin
7 ast_anti33___7 Aztreonam
```

## ast_anti33___6 (column)

```
4 ast_anti33___4 Ampicillin
5 ast_anti33___5 Ampicillin/Sulbactam
6 ast_anti33___6 Azithromycin
7 ast_anti33___7 Aztreonam
8 ast_anti33___8 Cefepime
```

## ast_anti33___7 (column)

```
5 ast_anti33___5 Ampicillin/Sulbactam
6 ast_anti33___6 Azithromycin
7 ast_anti33___7 Aztreonam
8 ast_anti33___8 Cefepime
9 ast_anti33___9 Cefixime
```

## ast_anti33___8 (column)

```
6 ast_anti33___6 Azithromycin
7 ast_anti33___7 Aztreonam
8 ast_anti33___8 Cefepime
9 ast_anti33___9 Cefixime
10 ast_anti33___10 Cefotaxime
```

## ast_anti33___9 (column)

```
7 ast_anti33___7 Aztreonam
8 ast_anti33___8 Cefepime
9 ast_anti33___9 Cefixime
10 ast_anti33___10 Cefotaxime
11 ast_anti33___11 Cefoxitin
```

## ast_anti33___10 (column)

```
8 ast_anti33___8 Cefepime
9 ast_anti33___9 Cefixime
10 ast_anti33___10 Cefotaxime
11 ast_anti33___11 Cefoxitin
12 ast_anti33___12 Ceftazidime
```

## ast_anti33___11 (column)

```
9 ast_anti33___9 Cefixime
10 ast_anti33___10 Cefotaxime
11 ast_anti33___11 Cefoxitin
12 ast_anti33___12 Ceftazidime
13 ast_anti33___13 Ceftriaxone
```

## ast_anti33___12 (column)

```
10 ast_anti33___10 Cefotaxime
11 ast_anti33___11 Cefoxitin
12 ast_anti33___12 Ceftazidime
13 ast_anti33___13 Ceftriaxone
14 ast_anti33___14 Ceftriaxone-
```

## ast_anti33___13 (column)

```
11 ast_anti33___11 Cefoxitin
12 ast_anti33___12 Ceftazidime
13 ast_anti33___13 Ceftriaxone
14 ast_anti33___14 Ceftriaxone-
salbactam
```

## ast_anti33___14 (column)

```
12 ast_anti33___12 Ceftazidime
13 ast_anti33___13 Ceftriaxone
14 ast_anti33___14 Ceftriaxone-
salbactam
15 ast_anti33___15 Cefuroxime
```

## ast_anti33___15 (column)

```
14 ast_anti33___14 Ceftriaxone-
salbactam
15 ast_anti33___15 Cefuroxime
16 ast_anti33___16 Chlorampenicol
17 ast_anti33___17 Ciprofloxacin
```

## ast_anti33___16 (column)

```
salbactam
15 ast_anti33___15 Cefuroxime
16 ast_anti33___16 Chlorampenicol
17 ast_anti33___17 Ciprofloxacin
18 ast_anti33___18 Clindamycin
```

## ast_anti33___17 (column)

```
15 ast_anti33___15 Cefuroxime
16 ast_anti33___16 Chlorampenicol
17 ast_anti33___17 Ciprofloxacin
18 ast_anti33___18 Clindamycin
19 ast_anti33___19 Cofotaxime
```

## ast_anti33___18 (column)

```
16 ast_anti33___16 Chlorampenicol
17 ast_anti33___17 Ciprofloxacin
18 ast_anti33___18 Clindamycin
19 ast_anti33___19 Cofotaxime
20 ast_anti33___20 Doripenem
```

## ast_anti33___19 (column)

```
17 ast_anti33___17 Ciprofloxacin
18 ast_anti33___18 Clindamycin
19 ast_anti33___19 Cofotaxime
20 ast_anti33___20 Doripenem
21 ast_anti33___21 Doxycycline
```

## ast_anti33___20 (column)

```
18 ast_anti33___18 Clindamycin
19 ast_anti33___19 Cofotaxime
20 ast_anti33___20 Doripenem
21 ast_anti33___21 Doxycycline
https://idiredcap.idi.co.ug/redcap_v14.7.4/Design/data_dictionary_codebook.php?pid=147 40/48
```

## ast_anti33___21 (column)

```
19 ast_anti33___19 Cofotaxime
20 ast_anti33___20 Doripenem
21 ast_anti33___21 Doxycycline
https://idiredcap.idi.co.ug/redcap_v14.7.4/Design/data_dictionary_codebook.php?pid=147 40/48
9/17/25, 11:25 AM GHS-CAMO-Net Project 3 Additional Data Collection | REDCap
```

## ast_anti33___22 (column)

```
https://idiredcap.idi.co.ug/redcap_v14.7.4/Design/data_dictionary_codebook.php?pid=147 40/48
9/17/25, 11:25 AM GHS-CAMO-Net Project 3 Additional Data Collection | REDCap
22 ast_anti33___22 Ertapenem
23 ast_anti33___23 Erythromycin
24 ast_anti33___24 Gentamicin
```

## ast_anti33___23 (column)

```
9/17/25, 11:25 AM GHS-CAMO-Net Project 3 Additional Data Collection | REDCap
22 ast_anti33___22 Ertapenem
23 ast_anti33___23 Erythromycin
24 ast_anti33___24 Gentamicin
25 ast_anti33___25 Imipenem
```

## ast_anti33___24 (column)

```
22 ast_anti33___22 Ertapenem
23 ast_anti33___23 Erythromycin
24 ast_anti33___24 Gentamicin
25 ast_anti33___25 Imipenem
26 ast_anti33___26 Levofloxacin
```

## ast_anti33___25 (column)

```
23 ast_anti33___23 Erythromycin
24 ast_anti33___24 Gentamicin
25 ast_anti33___25 Imipenem
26 ast_anti33___26 Levofloxacin
27 ast_anti33___27 Linezolid
```

## ast_anti33___26 (column)

```
24 ast_anti33___24 Gentamicin
25 ast_anti33___25 Imipenem
26 ast_anti33___26 Levofloxacin
27 ast_anti33___27 Linezolid
28 ast_anti33___28 Meropenem
```

## ast_anti33___27 (column)

```
25 ast_anti33___25 Imipenem
26 ast_anti33___26 Levofloxacin
27 ast_anti33___27 Linezolid
28 ast_anti33___28 Meropenem
29 ast_anti33___29 Nalidixic acid
```

## ast_anti33___28 (column)

```
26 ast_anti33___26 Levofloxacin
27 ast_anti33___27 Linezolid
28 ast_anti33___28 Meropenem
29 ast_anti33___29 Nalidixic acid
30 ast_anti33___30 Nitrofurantoin
```

## ast_anti33___29 (column)

```
27 ast_anti33___27 Linezolid
28 ast_anti33___28 Meropenem
29 ast_anti33___29 Nalidixic acid
30 ast_anti33___30 Nitrofurantoin
31 ast_anti33___31 Oxacillin
```

## ast_anti33___30 (column)

```
28 ast_anti33___28 Meropenem
29 ast_anti33___29 Nalidixic acid
30 ast_anti33___30 Nitrofurantoin
31 ast_anti33___31 Oxacillin
32 ast_anti33___32 Penicillin G
```

## ast_anti33___31 (column)

```
29 ast_anti33___29 Nalidixic acid
30 ast_anti33___30 Nitrofurantoin
31 ast_anti33___31 Oxacillin
32 ast_anti33___32 Penicillin G
33 ast_anti33___33 Piperacillin
```

## ast_anti33___32 (column)

```
30 ast_anti33___30 Nitrofurantoin
31 ast_anti33___31 Oxacillin
32 ast_anti33___32 Penicillin G
33 ast_anti33___33 Piperacillin
34 ast_anti33___34 Piperacillin
```

## ast_anti33___33 (column)

```
31 ast_anti33___31 Oxacillin
32 ast_anti33___32 Penicillin G
33 ast_anti33___33 Piperacillin
34 ast_anti33___34 Piperacillin
tazobactam
```

## ast_anti33___34 (column)

```
32 ast_anti33___32 Penicillin G
33 ast_anti33___33 Piperacillin
34 ast_anti33___34 Piperacillin
tazobactam
35 ast_anti33___35 Rifampin
```

## ast_anti33___35 (column)

```
34 ast_anti33___34 Piperacillin
tazobactam
35 ast_anti33___35 Rifampin
36 ast_anti33___36 Streptomycin
37 ast_anti33___37 Tetracycline
```

## ast_anti33___36 (column)

```
tazobactam
35 ast_anti33___35 Rifampin
36 ast_anti33___36 Streptomycin
37 ast_anti33___37 Tetracycline
38 ast_anti33___38 Tigecycline
```

## ast_anti33___37 (column)

```
35 ast_anti33___35 Rifampin
36 ast_anti33___36 Streptomycin
37 ast_anti33___37 Tetracycline
38 ast_anti33___38 Tigecycline
39 ast_anti33___39 Trimethoprim/
```

## ast_anti33___38 (column)

```
36 ast_anti33___36 Streptomycin
37 ast_anti33___37 Tetracycline
38 ast_anti33___38 Tigecycline
39 ast_anti33___39 Trimethoprim/
Sulfamethoxazole
```

## ast_anti33___39 (column)

```
37 ast_anti33___37 Tetracycline
38 ast_anti33___38 Tigecycline
39 ast_anti33___39 Trimethoprim/
Sulfamethoxazole
40 ast_anti33___40 Vancomycin
```

## ast_anti33___40 (column)

```
39 ast_anti33___39 Trimethoprim/
Sulfamethoxazole
40 ast_anti33___40 Vancomycin
41 ast_anti33___41 Others1
42 ast_anti33___42 Others2
```

## ast_anti33___41 (column)

```
Sulfamethoxazole
40 ast_anti33___40 Vancomycin
41 ast_anti33___41 Others1
42 ast_anti33___42 Others2
351 [thirdrep_amikacin] Amikacin radio (Matrix)
```

## ast_anti33___42 (column)

```
40 ast_anti33___40 Vancomycin
41 ast_anti33___41 Others1
42 ast_anti33___42 Others2
351 [thirdrep_amikacin] Amikacin radio (Matrix)
1 Resistant
```

## thirdrep_amikacin (column)

```
41 ast_anti33___41 Others1
42 ast_anti33___42 Others2
351 [thirdrep_amikacin] Amikacin radio (Matrix)
1 Resistant
Show the field ONLY if:
```

## thirdrep_amoxicillin (column)

```
[ast_anti33(1)]='1' 2 Intermediate
3 Susceptible
352 [thirdrep_amoxicillin] Amoxicillin radio (Matrix)
1 Resistant
Show the field ONLY if:
```

## thirdrep_amoxiclav (column)

```
[ast_anti33(2)]='1' 2 Intermediate
3 Susceptible
353 [thirdrep_amoxiclav] Amoxicillin/Clavulanic acid radio (Matrix)
1 Resistant
Show the field ONLY if:
```

## thirdrep_ampicillin (column)

```
[ast_anti33(3)]='1' 2 Intermediate
3 Susceptible
354 [thirdrep_ampicillin] Ampicillin radio (Matrix)
1 Resistant
Show the field ONLY if:
```

## thirdrep_aztreonam (column)

```
2 Intermediate
3 Susceptible
357 [thirdrep_aztreonam] Aztreonam radio (Matrix)
1 Resistant
Show the field ONLY if:
```

## thirdrep_cefepime (column)

```
[ast_anti33(7)]='1' 2 Intermediate
3 Susceptible
358 [thirdrep_cefepime] Cefepime radio (Matrix)
1 Resistant
Show the field ONLY if:
```

## thirdrep_cefixime (column)

```
[ast_anti33(8)]='1' 2 Intermediate
3 Susceptible
359 [thirdrep_cefixime] Cefixime radio (Matrix)
1 Resistant
Show the field ONLY if:
```

## thirdrep_cefotaxime (column)

```
[ast_anti33(9)]='1' 2 Intermediate
3 Susceptible
360 [thirdrep_cefotaxime] Cefotaxime radio (Matrix)
1 Resistant
Show the field ONLY if:
```

## thirdrep_cefoxitin (column)

```
[ast_anti33(10)]='1' 2 Intermediate
3 Susceptible
361 [thirdrep_cefoxitin] Cefoxitin radio (Matrix)
1 Resistant
Show the field ONLY if:
```

## thirdrep_ceftazidime (column)

```
[ast_anti33(11)]='1' 2 Intermediate
3 Susceptible
362 [thirdrep_ceftazidime] Ceftazidime radio (Matrix)
1 Resistant
Show the field ONLY if:
```

## thirdrep_ceftriaxone (column)

```
[ast_anti33(12)]='1' 2 Intermediate
3 Susceptible
363 [thirdrep_ceftriaxone] Ceftriaxone radio (Matrix)
1 Resistant
Show the field ONLY if:
```

## thirdrep_cefuroxime (column)

```
[ast_anti33(14)]='1'
3 Susceptible
365 [thirdrep_cefuroxime] Cefuroxime radio (Matrix)
1 Resistant
Show the field ONLY if:
```

## thirdrep_clindamycin (column)

```
[ast_anti33(17)]='1'
3 Susceptible
368 [thirdrep_clindamycin] Clindamycin radio (Matrix)
1 Resistant
Show the field ONLY if:
```

## thirdrep_cofotaxime (column)

```
[ast_anti33(18)]='1' 2 Intermediate
3 Susceptible
369 [thirdrep_cofotaxime] Cofotaxime radio (Matrix)
1 Resistant
Show the field ONLY if:
```

## thirdrep_doripenem (column)

```
[ast_anti33(19)]='1' 2 Intermediate
3 Susceptible
370 [thirdrep_doripenem] Doripenem radio (Matrix)
1 Resistant
Show the field ONLY if:
```

## thirdrep_doxycycline (column)

```
[ast_anti33(20)]='1' 2 Intermediate
3 Susceptible
371 [thirdrep_doxycycline] Doxycycline radio (Matrix)
1 Resistant
Show the field ONLY if:
```

## thirdrep_ertapenem (column)

```
[ast_anti33(21)]='1' 2 Intermediate
3 Susceptible
372 [thirdrep_ertapenem] Ertapenem radio (Matrix)
1 Resistant
Show the field ONLY if:
```

## thirdrep_gentamicin (column)

```
[ast_anti33(23)]='1'
3 Susceptible
374 [thirdrep_gentamicin] Gentamicin radio (Matrix)
1 Resistant
Show the field ONLY if:
```

## thirdrep_imipenem (column)

```
[ast_anti33(24)]='1' 2 Intermediate
3 Susceptible
375 [thirdrep_imipenem] Imipenem radio (Matrix)
1 Resistant
Show the field ONLY if:
```

## thirdrep_linezolid (column)

```
https://idiredcap.idi.co.ug/redcap_v14.7.4/Design/data_dictionary_codebook.php?pid=147 43/48
9/17/25, 11:25 AM GHS-CAMO-Net Project 3 Additional Data Collection | REDCap
377 [thirdrep_linezolid] Linezolid radio (Matrix)
1 Resistant
Show the field ONLY if:
```

## thirdrep_meropenem (column)

```
[ast_anti33(27)]='1' 2 Intermediate
3 Susceptible
378 [thirdrep_meropenem] Meropenem radio (Matrix)
1 Resistant
Show the field ONLY if:
```

## thirdrep_oxacillin (column)

```
[ast_anti33(30)]='1'
3 Susceptible
381 [thirdrep_oxacillin] Oxacillin radio (Matrix)
1 Resistant
Show the field ONLY if:
```

## thirdrep_pen_g (column)

```
[ast_anti33(31)]='1' 2 Intermediate
3 Susceptible
382 [thirdrep_pen_g] Penicillin G radio (Matrix)
1 Resistant
Show the field ONLY if:
```

## thirdrep_rifampin (column)

```
[ast_anti33(34)]='1'
3 Susceptible
385 [thirdrep_rifampin] Rifampin radio (Matrix)
1 Resistant
Show the field ONLY if:
```

## thirdrep_tigecycline (column)

```
[ast_anti33(37)]='1'
3 Susceptible
388 [thirdrep_tigecycline] Tigecycline radio (Matrix)
1 Resistant
Show the field ONLY if:
```

## thirdrep_sxt (column)

```
[ast_anti33(38)]='1' 2 Intermediate
3 Susceptible
389 [thirdrep_sxt] Trimethoprim/ Sulfamethoxazole radio (Matrix)
1 Resistant
Show the field ONLY if:
```

## thirdrep_vancomycin (column)

```
[ast_anti33(39)]='1' 2 Intermediate
3 Susceptible
390 [thirdrep_vancomycin] Vancomycin radio (Matrix)
1 Resistant
Show the field ONLY if:
```

## thirdrep_othe (column)

```
[ast_anti33(40)]='1' 2 Intermediate
3 Susceptible
391 [thirdrep_othe] Other antibiotic, please specify text
Show the field ONLY if:
[ast_anti33(41)]='1'
```

## thirdrep_oth_ast (column)

```
Show the field ONLY if:
[ast_anti33(41)]='1'
392 [thirdrep_oth_ast] Other antibiotic AST results radio
1 Resistant
Show the field ONLY if:
```

## thirdrep_oth2_name (column)

```
[ast_anti33(41)]='1' 2 Intermediate
3 Susceptible
393 [thirdrep_oth2_name] Other antibiotic, please specify text
Show the field ONLY if:
[ast_anti33(42)]='1'
```

## thirdrep_oth2_ast (column)

```
Show the field ONLY if:
[ast_anti33(42)]='1'
394 [thirdrep_oth2_ast] Other antibiotic AST results radio
1 Resistant
Show the field ONLY if:
```

## complications (column)

```
[ast_anti33(42)]='1' 2 Intermediate
3 Susceptible
395 [complications] 35a. Did the patient get any complications yesno
during admission?
1 Yes
```

## comp_system___1 (column)

```
396 [comp_system] 35c. Select affected body system affected by checkbox
complication.
1 comp_system___1 Central Nervous
Show the field ONLY if:
System
```

## comp_system___2 (column)

```
System
[complications]='1'
2 comp_system___2 Gastrointestinal
system
3 comp_system___3 Respiratory system
```

## comp_system___3 (column)

```
2 comp_system___2 Gastrointestinal
system
3 comp_system___3 Respiratory system
4 comp_system___4 Genital Urinary
System
```

## comp_system___4 (column)

```
system
3 comp_system___3 Respiratory system
4 comp_system___4 Genital Urinary
System
5 comp_system___5 Musculoskeletal
```

## comp_system___5 (column)

```
4 comp_system___4 Genital Urinary
System
5 comp_system___5 Musculoskeletal
system
6 comp_system___6 Cardiovascular
```

## comp_system___6 (column)

```
5 comp_system___5 Musculoskeletal
system
6 comp_system___6 Cardiovascular
system
7 comp_system___7 Integumentary
```

## comp_system___7 (column)

```
6 comp_system___6 Cardiovascular
system
7 comp_system___7 Integumentary
https://idiredcap.idi.co.ug/redcap_v14.7.4/Design/data_dictionary_codebook.php?pid=147 45/48
9/17/25, 11:25 AM GHS-CAMO-Net Project 3 Additional Data Collection | REDCap
```

## comp_system___8 (column)

```
https://idiredcap.idi.co.ug/redcap_v14.7.4/Design/data_dictionary_codebook.php?pid=147 45/48
9/17/25, 11:25 AM GHS-CAMO-Net Project 3 Additional Data Collection | REDCap
8 comp_system___8 Reproductive
system
397 [comp_cns] State the complication as indicated on patient text
```

## comp_cns (column)

```
8 comp_system___8 Reproductive
system
397 [comp_cns] State the complication as indicated on patient text
file (Central Nervous System)
Show the field ONLY if:
```

## comp_git (column)

```
Show the field ONLY if:
[comp_system(1)]='1'
398 [comp_git] State the complication as indicated on patient text
file (Gastrointestinal system)
Show the field ONLY if:
```

## comp_resp (column)

```
Show the field ONLY if:
[comp_system(2)]='1'
399 [comp_resp] State the complication as indicated on patient text
file (Respiratory system)
Show the field ONLY if:
```

## comp_genital (column)

```
Show the field ONLY if:
[comp_system(3)]='1'
400 [comp_genital] State the complication as indicated on patient text
file (Genital Urinary System)
Show the field ONLY if:
```

## comp_musculo (column)

```
Show the field ONLY if:
[comp_system(4)]='1'
401 [comp_musculo] State the complication as indicated on patient text
file (Musculoskeletal system)
Show the field ONLY if:
```

## comp_cardio (column)

```
Show the field ONLY if:
[comp_system(5)]='1'
402 [comp_cardio] State the complication as indicated on patient text
file (Cardiovascular system)
Show the field ONLY if:
```

## comp_integ (column)

```
Show the field ONLY if:
[comp_system(6)]='1'
403 [comp_integ] State the complication as indicated on patient text
file (Integumentary)
Show the field ONLY if:
```

## treatment_outcome (column)

```
Show the field ONLY if:
[comp_system(8)]='1'
405 [treatment_outcome] 36. Treatment outcome radio, Required
1 Recovered
2 Recovered with complications
```

## diag_death_file (column)

```
5 Clinical detorioration
6 Died
406 [diag_death_file] State diagnosis at death on patient file text, Required
Show the field ONLY if:
[treatment_outcome]
```

## cause_death (column)

```
[treatment_outcome]
='6'
407 [cause_death] What was the cause of death? text
Show the field ONLY if:
[treatment_outcome]
```

## date_death (column)

```
[treatment_outcome]
='6'
408 [date_death] Date of death text (date_dmy), Required
Show the field ONLY if:
[treatment_outcome]
```

## diag_disch_syst___1 (column)

```
='6'
409 [diag_disch_syst] Diagnosis (Select affected body system) checkbox
1 diag_disch_syst___1 Central Nervous
Show the field ONLY if:
System
```

## diag_disch_syst___2 (column)

```
9/17/25, 11:25 AM GHS-CAMO-Net Project 3 Additional Data Collection | REDCap
me]='2' or [treatment_o
2 diag_disch_syst___2 Gastrointestinal
utcome]='3' or [treatme
system
```

## diag_disch_syst___3 (column)

```
system
nt_outcome]='4' or [trea
tment_outcome]='4' 3 diag_disch_syst___3 Respiratory
system
4 diag_disch_syst___4 Genital Urinary
```

## diag_disch_syst___4 (column)

```
tment_outcome]='4' 3 diag_disch_syst___3 Respiratory
system
4 diag_disch_syst___4 Genital Urinary
System
5 diag_disch_syst___5 Musculoskeletal
```

## diag_disch_syst___5 (column)

```
4 diag_disch_syst___4 Genital Urinary
System
5 diag_disch_syst___5 Musculoskeletal
system
6 diag_disch_syst___6 Cardiovascular
```

## diag_disch_syst___6 (column)

```
5 diag_disch_syst___5 Musculoskeletal
system
6 diag_disch_syst___6 Cardiovascular
system
7 diag_disch_syst___7 Intergumentary
```

## diag_disch_syst___7 (column)

```
6 diag_disch_syst___6 Cardiovascular
system
7 diag_disch_syst___7 Intergumentary
8 diag_disch_syst___8 Reproductive
system
```

## diag_disch_syst___8 (column)

```
system
7 diag_disch_syst___7 Intergumentary
8 diag_disch_syst___8 Reproductive
system
410 [disch_diag_cns] State diagnosis on patient file (Central Nervous text
```

## disch_diag_cns (column)

```
8 diag_disch_syst___8 Reproductive
system
410 [disch_diag_cns] State diagnosis on patient file (Central Nervous text
System)
Show the field ONLY if:
```

## disch_diag_git (column)

```
Show the field ONLY if:
[diag_disch_syst(1)]='1'
411 [disch_diag_git] State diagnosis on patient file (Gastrointestinal text
system)
Show the field ONLY if:
```

## disch_diag_resp (column)

```
Show the field ONLY if:
[diag_disch_syst(2)]='1'
412 [disch_diag_resp] State diagnosis on patient file (Respiratory text
system)
Show the field ONLY if:
```

## disch_diag_genital (column)

```
Show the field ONLY if:
[diag_disch_syst(3)]='1'
413 [disch_diag_genital] State diagnosis on patient file (Genital Urinary text
System)
Show the field ONLY if:
```

## disch_diag_musculo (column)

```
Show the field ONLY if:
[diag_disch_syst(4)]='1'
414 [disch_diag_musculo] State diagnosis on patient file (Musculoskeletal text
system)
Show the field ONLY if:
```

## disch_diag_cardio (column)

```
Show the field ONLY if:
[diag_disch_syst(5)]='1'
415 [disch_diag_cardio] State diagnosis on patient file (Cardiovascular text
system)
Show the field ONLY if:
```

## disch_diag_interg (column)

```
Show the field ONLY if:
[diag_disch_syst(6)]='1'
416 [disch_diag_interg] State diagnosis on patient file (Integumentary) text
Show the field ONLY if:
[diag_disch_syst(7)]='1'
```

## disch_diag_reprod (column)

```
Show the field ONLY if:
[diag_disch_syst(7)]='1'
417 [disch_diag_reprod] State diagnosis on patient file (Reproductive text
system)
Show the field ONLY if:
```

## date_at_discharge (column)

```
Show the field ONLY if:
[diag_disch_syst(8)]='1'
418 [date_at_discharge] Date (DD/MM/YYYY) text (date_dmy), Required
Show the field ONLY if:
[treatment_outcome]
```

## date_referral (column)

```
me]='2' or [treatment_o
utcome]='5'
419 [date_referral] Date of referral text (date_dmy)
Show the field ONLY if:
[treatment_outcome]
```

## infect_site (group)

```
1 Yes
0 No
13 [infect_site] 10. Site of Infection (Suspected based on checkbox
symptoms)
1 infect_site___1 Central Nervous
```

## site_based_sample (group)

```
7 infect_site___7 Integumentary
8 infect_site___8 Reproductive system
14 [site_based_sample] Site of infection (Based on sample collection) checkbox
Based on sample collection
1 site_based_sample___1 Central
```

## sec_site_infection (group)

```
system
9 site_based_sample___9 None
15 [sec_site_infection] 11. Site of infection (Confirmed by a positive checkbox
culture)
1 sec_site_infection___1 Central
```

## prio_antib_name (group)

```
2 No
3 Unknown
22 [prio_antib_name] 15b. If yes, indicate the antibiotics received. checkbox
1 prio_antib_name___1 Amikacin
Show the field ONLY if:
```

## diag_system (group)

```
days.
25 [date_diagn] 17. Date of diagnosis of infection text (date_dmy)
26 [diag_system] 18a. Affected body system (based on the checkbox
diagnosis)
1 diag_system___1 Central Nervous
```

## indwel_inst (group)

```
2 Positive
3 Unknown
36 [indwel_inst] 20a. Did the patient have any indwelling checkbox
instrument during this admission?
1 indwel_inst___1 Urinary catheter
```

## cormobidities (group)

```
1 Yes
0 No
39 [cormobidities] 20c. If yes indicate the underlying chronic co- checkbox
morbid conditions (Select Multiple)
1 cormobidities___1 Diabetes
```

## antibiotics_prescribed (group)

```
42 [antibiotics_prescribe 21b. If yes, list antibiotics prescribed. (Select checkbox
d] Multiple)
1 antibiotics_prescribed___1 Amikacin
Show the field ONLY if: 2 antibiotics_prescribed___2 Amoxicillin
[antibiotics]='1'
```

## clin_param (group)

```
antibiotics (or antibiotic prescription).
[antibiotics]='0'
45 [clin_param] 22. Which clinical parameters were monitored? checkbox
1 clin_param___1 Blood pressure (BP)
2 clin_param___2 Pulse
```

## bp_type (group)

```
(GCS)
7 clin_param___7 Other
46 [bp_type] Specify the BP checkbox
1 bp_type___1 Systolic BP
Show the field ONLY if:
```

## ast_anti1 (group)

```
Show the field ONLY if:
[organism_isolated]>=1
71 [ast_anti1] 27b. Antibiotics set for AST checkbox
1 ast_anti1___1 Amikacin
Show the field ONLY if:
```

## ast_anti2 (group)

```
Show the field ONLY if:
[organism_isolated]>=2
117 [ast_anti2] 27d. Antibiotics set for AST checkbox
1 ast_anti2___1 Amikacin
Show the field ONLY if:
```

## ast_anti3 (group)

```
Show the field ONLY if:
[organism_isolated]>=3
163 [ast_anti3] 27f. Antibiotics set for AST checkbox
1 ast_anti3___1 Amikacin
Show the field ONLY if:
```

## antib_presc_af_cul (group)

```
Show the field ONLY if:
[antib_aft_culture]='1'
210 [antib_presc_af_cul] 30. Provide a list of antibiotics prescribed checkbox
following receipt of culture and sensitivity
1 antib_presc_af_cul___1 Amikacin
```

## ast_anti11 (group)

```
https://idiredcap.idi.co.ug/redcap_v14.7.4/Design/data_dictionary_codebook.php?pid=147 29/48
9/17/25, 11:25 AM GHS-CAMO-Net Project 3 Additional Data Collection | REDCap
258 [ast_anti11] 34c. Antibiotics set for AST checkbox
1 ast_anti11___1 Amikacin
Show the field ONLY if:
```

## ast_anti22 (group)

```
Show the field ONLY if:
[num_organis]>=2
304 [ast_anti22] 34e. Antibiotics set for AST checkbox
1 ast_anti22___1 Amikacin
Show the field ONLY if:
```

## ast_anti33 (group)

```
Show the field ONLY if:
[num_organis]>=3
350 [ast_anti33] 34g. Antibiotics set for AST checkbox
1 ast_anti33___1 Amikacin
Show the field ONLY if:
```

## comp_system (group)

```
1 Yes
0 No
396 [comp_system] 35c. Select affected body system affected by checkbox
complication.
1 comp_system___1 Central Nervous
```

## diag_disch_syst (group)

```
[treatment_outcome]
='6'
409 [diag_disch_syst] Diagnosis (Select affected body system) checkbox
1 diag_disch_syst___1 Central Nervous
Show the field ONLY if:
```
