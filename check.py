# While it may seem that we have to test every single possibility and combination of variables
# That is not the case
# What we’ll be doing is examining every variation of output based on a single variable at a time
# We’ll only change one input at a time to ensure the output based on the change is correct
# If the expected change is correct but the output is wrong then it’s a simple problem of the 
# sum of all points is incorrect
#The only time where we need to calculate variations due to cross-contamination is when age is #a factor


#control case
sex:F age:41 cho:105 smo:N hdl:51 sbp:100 med:N out:1

# Age affects
sex:F age:24 cho:105 smo:N hdl:51 sbp:100 med:N out:<1
sex:F age:38 cho:105 smo:N hdl:51 sbp:100 med:N out:<1
sex:F age:43 cho:105 smo:N hdl:51 sbp:100 med:N out:1
sex:F age:48 cho:105 smo:N hdl:51 sbp:100 med:N out:1
sex:F age:52 cho:105 smo:N hdl:51 sbp:100 med:N out:2
sex:F age:57 cho:105 smo:N hdl:51 sbp:100 med:N out:4
sex:F age:61 cho:105 smo:N hdl:51 sbp:100 med:N out:6
sex:F age:66 cho:105 smo:N hdl:51 sbp:100 med:N out:8
sex:F age:71 cho:105 smo:N hdl:51 sbp:100 med:N out:10
sex:F age:76 cho:105 smo:N hdl:51 sbp:100 med:N out:12


# Cholesterol  (20-34)
sex:F age:23 cho:105 smo:N hdl:51 sbp:100 med:N out:<1
sex:F age:23 cho:165 smo:N hdl:51 sbp:100 med:N out:<1
sex:F age:23 cho:235 smo:N hdl:51 sbp:100 med:N out:<1
sex:F age:23 cho:279 smo:N hdl:51 sbp:100 med:N out:1
sex:F age:23 cho:300 smo:N hdl:51 sbp:100 med:N out:1

# Cholesterol  (35-39)
sex:F age:36 cho:105 smo:N hdl:51 sbp:100 med:N out:<1
sex:F age:36 cho:165 smo:N hdl:51 sbp:100 med:N out:1
sex:F age:36 cho:235 smo:N hdl:51 sbp:100 med:N out:1
sex:F age:36 cho:279 smo:N hdl:51 sbp:100 med:N out:2
sex:F age:36 cho:300 smo:N hdl:51 sbp:100 med:N out:3

# Cholesterol (40-44)
sex:F age:41 cho:105 smo:N hdl:51 sbp:100 med:N out:1
sex:F age:41 cho:165 smo:N hdl:51 sbp:100 med:N out:1
sex:F age:41 cho:235 smo:N hdl:51 sbp:100 med:N out:2
sex:F age:41 cho:279 smo:N hdl:51 sbp:100 med:N out:2
sex:F age:41 cho:300 smo:N hdl:51 sbp:100 med:N out:4

# Cholesterol (45-49)
sex:F age:46 cho:105 smo:N hdl:51 sbp:100 med:N out:1
sex:F age:46 cho:165 smo:N hdl:51 sbp:100 med:N out:2
sex:F age:46 cho:235 smo:N hdl:51 sbp:100 med:N out:4
sex:F age:46 cho:279 smo:N hdl:51 sbp:100 med:N out:5
sex:F age:46 cho:300 smo:N hdl:51 sbp:100 med:N out:8

#Cholesterol (50-54)
sex:F age:51 cho:105 smo:N hdl:51 sbp:100 med:N out:2
sex:F age:51 cho:165 smo:N hdl:51 sbp:100 med:N out:4
sex:F age:51 cho:235 smo:N hdl:51 sbp:100 med:N out:5
sex:F age:51 cho:279 smo:N hdl:51 sbp:100 med:N out:6
sex:F age:51 cho:300 smo:N hdl:51 sbp:100 med:N out:8

# Cholesterol (55-59)
sex:F age:56 cho:105 smo:N hdl:51 sbp:100 med:N out:4
sex:F age:56 cho:165 smo:N hdl:51 sbp:100 med:N out:6
sex:F age:56 cho:235 smo:N hdl:51 sbp:100 med:N out:8
sex:F age:56 cho:279 smo:N hdl:51 sbp:100 med:N out:10
sex:F age:56 cho:300 smo:N hdl:51 sbp:100 med:N out:12

#Cholesterol (60-64)
sex:F age:61 cho:105 smo:N hdl:51 sbp:100 med:N out:6
sex:F age:61 cho:165 smo:N hdl:51 sbp:100 med:N out:8
sex:F age:61 cho:235 smo:N hdl:51 sbp:100 med:N out:8
sex:F age:61 cho:279 smo:N hdl:51 sbp:100 med:N out:10
sex:F age:61 cho:300 smo:N hdl:51 sbp:100 med:N out:12

#Cholesterol (65-69)
sex:F age:66 cho:105 smo:N hdl:51 sbp:100 med:N out:8
sex:F age:66 cho:165 smo:N hdl:51 sbp:100 med:N out:10
sex:F age:66 cho:235 smo:N hdl:51 sbp:100 med:N out:12
sex:F age:66 cho:279 smo:N hdl:51 sbp:100 med:N out:16
sex:F age:66 cho:300 smo:N hdl:51 sbp:100 med:N out:20

#Cholesterol (70-74)
sex:F age:71 cho:105 smo:N hdl:51 sbp:100 med:N out:10
sex:F age:71 cho:165 smo:N hdl:51 sbp:100 med:N out:12
sex:F age:71 cho:235 smo:N hdl:51 sbp:100 med:N out:16
sex:F age:71 cho:279 smo:N hdl:51 sbp:100 med:N out:20
sex:F age:71 cho:300 smo:N hdl:51 sbp:100 med:N out:25

# Cholesterol (75-79)
sex:F age:76 cho:105 smo:N hdl:51 sbp:100 med:N out:12
sex:F age:76 cho:165 smo:N hdl:51 sbp:100 med:N out:16
sex:F age:76 cho:235 smo:N hdl:51 sbp:100 med:N out:20
sex:F age:76 cho:279 smo:N hdl:51 sbp:100 med:N out:25
sex:F age:76 cho:300 smo:N hdl:51 sbp:100 med:N out:30

#Smoker (no)
sex:F age:21 cho:105 smo:Y hdl:51 sbp:100 med:N out:<1
sex:F age:36 cho:105 smo:Y hdl:51 sbp:100 med:N out<1
sex:F age:41 cho:105 smo:Y hdl:51 sbp:100 med:N out:1
sex:F age:47 cho:105 smo:Y hdl:51 sbp:100 med:N out:1
sex:F age:51 cho:105 smo:Y hdl:51 sbp:100 med:N out:2
sex:F age:57 cho:105 smo:Y hdl:51 sbp:100 med:N out:4
sex:F age:61 cho:105 smo:Y hdl:51 sbp:100 med:N out:6
sex:F age:67 cho:105 smo:Y hdl:51 sbp:100 med:N out:8
sex:F age:71 cho:105 smo:Y hdl:51 sbp:100 med:N out:10
sex:F age:77 cho:105 smo:Y hdl:51 sbp:100 med:N out:12

#Smoker (yes)
sex:F age:21 cho:105 smo:Y hdl:51 sbp:100 med:N out:<1
sex:F age:36 cho:105 smo:Y hdl:51 sbp:100 med:N out:1
sex:F age:41 cho:105 smo:Y hdl:51 sbp:100 med:N out:2
sex:F age:47 cho:105 smo:Y hdl:51 sbp:100 med:N out:4
sex:F age:51 cho:105 smo:Y hdl:51 sbp:100 med:N out:5
sex:F age:57 cho:105 smo:Y hdl:51 sbp:100 med:N out:8
sex:F age:61 cho:105 smo:Y hdl:51 sbp:100 med:N out:8
sex:F age:67 cho:105 smo:Y hdl:51 sbp:100 med:N out:10
sex:F age:71 cho:105 smo:Y hdl:51 sbp:100 med:N out:12
sex:F age:77 cho:105 smo:Y hdl:51 sbp:100 med:N out:16


#HDL
sex:F age:41 cho:105 smo:N hdl:70 sbp:100 med:N out:<1
sex:F age:41 cho:105 smo:N hdl:51 sbp:100 med:N out:1
sex:F age:41 cho:105 smo:N hdl:45 sbp:100 med:N out:1
sex:F age:41 cho:105 smo:N hdl:37 sbp:100 med:N out:1


#Systolic Untreated
sex:F age:41 cho:105 smo:N hdl:51 sbp:100 med:N out:1
sex:F age:41 cho:105 smo:N hdl:51 sbp:121 med:N out:1
sex:F age:41 cho:105 smo:N hdl:51 sbp:134 med:N out:1
sex:F age:41 cho:105 smo:N hdl:51 sbp:142 med:N out:1
sex:F age:41 cho:105 smo:N hdl:51 sbp:180 med:N out:1

#Systolic Treated
sex:F age:41 cho:105 smo:N hdl:51 sbp:100 med:Y out:1
sex:F age:41 cho:105 smo:N hdl:51 sbp:121 med:Y out:1
sex:F age:41 cho:105 smo:N hdl:51 sbp:134 med:Y out:1
sex:F age:41 cho:105 smo:N hdl:51 sbp:142 med:Y out:1
sex:F age:41 cho:105 smo:N hdl:51 sbp:180 med:Y out:1




# # Male Tests

# Age affects    # Checked
sex:M age:24 cho:105 smo:N hdl:51 sbp:100 med:N out:<1
sex:M age:38 cho:105 smo:N hdl:51 sbp:100 med:N out:<1
sex:M age:43 cho:105 smo:N hdl:51 sbp:100 med:N out:1
sex:M age:48 cho:105 smo:N hdl:51 sbp:100 med:N out:1
sex:M age:52 cho:105 smo:N hdl:51 sbp:100 med:N out:2
sex:M age:57 cho:105 smo:N hdl:51 sbp:100 med:N out:4
sex:M age:61 cho:105 smo:N hdl:51 sbp:100 med:N out:6
sex:M age:66 cho:105 smo:N hdl:51 sbp:100 med:N out:8
sex:M age:71 cho:105 smo:N hdl:51 sbp:100 med:N out:10
sex:M age:76 cho:105 smo:N hdl:51 sbp:100 med:N out:12

# Cholesterol  (20-34)    # Checked
sex:M age:23 cho:105 smo:N hdl:51 sbp:100 med:N out:<1
sex:M age:23 cho:165 smo:N hdl:51 sbp:100 med:N out:<1
sex:M age:23 cho:235 smo:N hdl:51 sbp:100 med:N out:<1
sex:M age:23 cho:279 smo:N hdl:51 sbp:100 med:N out:1
sex:M age:23 cho:300 smo:N hdl:51 sbp:100 med:N out:1

# Cholesterol  (35-39)    # Checked
sex:M age:36 cho:105 smo:N hdl:51 sbp:100 med:N out:<1
sex:M age:36 cho:165 smo:N hdl:51 sbp:100 med:N out:1
sex:M age:36 cho:235 smo:N hdl:51 sbp:100 med:N out:1
sex:M age:36 cho:279 smo:N hdl:51 sbp:100 med:N out:2
sex:M age:36 cho:300 smo:N hdl:51 sbp:100 med:N out:3

# Cholesterol (40-44)    # Checked
sex:M age:41 cho:105 smo:N hdl:51 sbp:100 med:N out:1
sex:M age:41 cho:165 smo:N hdl:51 sbp:100 med:N out:1
sex:M age:41 cho:235 smo:N hdl:51 sbp:100 med:N out:2
sex:M age:41 cho:279 smo:N hdl:51 sbp:100 med:N out:2
sex:M age:41 cho:300 smo:N hdl:51 sbp:100 med:N out:4

# Cholesterol (45-49)    # Checked
sex:M age:46 cho:105 smo:N hdl:51 sbp:100 med:N out:1
sex:M age:46 cho:165 smo:N hdl:51 sbp:100 med:N out:2
sex:M age:46 cho:235 smo:N hdl:51 sbp:100 med:N out:4
sex:M age:46 cho:279 smo:N hdl:51 sbp:100 med:N out:5
sex:M age:46 cho:300 smo:N hdl:51 sbp:100 med:N out:8

# Cholesterol (50-54)    # Checked
sex:M age:51 cho:105 smo:N hdl:51 sbp:100 med:N out:2
sex:M age:51 cho:165 smo:N hdl:51 sbp:100 med:N out:4
sex:M age:51 cho:235 smo:N hdl:51 sbp:100 med:N out:5
sex:M age:51 cho:279 smo:N hdl:51 sbp:100 med:N out:6
sex:M age:51 cho:300 smo:N hdl:51 sbp:100 med:N out:8

# Cholesterol (55-59)    # Checked
sex:M age:56 cho:105 smo:N hdl:51 sbp:100 med:N out:4
sex:M age:56 cho:165 smo:N hdl:51 sbp:100 med:N out:6
sex:M age:56 cho:235 smo:N hdl:51 sbp:100 med:N out:8
sex:M age:56 cho:279 smo:N hdl:51 sbp:100 med:N out:10
sex:M age:56 cho:300 smo:N hdl:51 sbp:100 med:N out:12

# Cholesterol (60-64)    # Checked
sex:M age:61 cho:105 smo:N hdl:51 sbp:100 med:N out:6
sex:M age:61 cho:165 smo:N hdl:51 sbp:100 med:N out:8
sex:M age:61 cho:235 smo:N hdl:51 sbp:100 med:N out:8
sex:M age:61 cho:279 smo:N hdl:51 sbp:100 med:N out:10
sex:M age:61 cho:300 smo:N hdl:51 sbp:100 med:N out:12

# Cholesterol (65-69)    # Checked
sex:M age:66 cho:105 smo:N hdl:51 sbp:100 med:N out:8
sex:M age:66 cho:165 smo:N hdl:51 sbp:100 med:N out:10
sex:M age:66 cho:235 smo:N hdl:51 sbp:100 med:N out:10
sex:M age:66 cho:279 smo:N hdl:51 sbp:100 med:N out:12
sex:M age:66 cho:300 smo:N hdl:51 sbp:100 med:N out:16

# Cholesterol (70-74)    # Checked
sex:M age:71 cho:105 smo:N hdl:51 sbp:100 med:N out:10
sex:M age:71 cho:165 smo:N hdl:51 sbp:100 med:N out:10
sex:M age:71 cho:235 smo:N hdl:51 sbp:100 med:N out:10
sex:M age:71 cho:279 smo:N hdl:51 sbp:100 med:N out:12
sex:M age:71 cho:300 smo:N hdl:51 sbp:100 med:N out:12

# Cholesterol (75-79)    # Checked
sex:M age:76 cho:105 smo:N hdl:51 sbp:100 med:N out:12
sex:M age:76 cho:165 smo:N hdl:51 sbp:100 med:N out:12
sex:M age:76 cho:235 smo:N hdl:51 sbp:100 med:N out:12
sex:M age:76 cho:279 smo:N hdl:51 sbp:100 med:N out:16
sex:M age:76 cho:300 smo:N hdl:51 sbp:100 med:N out:16

# Smoker (NO)   # Checked
sex:M age:21 cho:105 smo:N hdl:51 sbp:100 med:N out:<1
sex:M age:36 cho:105 smo:N hdl:51 sbp:100 med:N out:<1
sex:M age:41 cho:105 smo:N hdl:51 sbp:100 med:N out:<1
sex:M age:47 cho:105 smo:N hdl:51 sbp:100 med:N out:1
sex:M age:51 cho:105 smo:N hdl:51 sbp:100 med:N out:2
sex:M age:57 cho:105 smo:N hdl:51 sbp:100 med:N out:4
sex:M age:61 cho:105 smo:N hdl:51 sbp:100 med:N out:6
sex:M age:67 cho:105 smo:N hdl:51 sbp:100 med:N out:8
sex:M age:71 cho:105 smo:N hdl:51 sbp:100 med:N out:10
sex:M age:77 cho:105 smo:N hdl:51 sbp:100 med:N out:12

# Smoker (yes)    # Checked
sex:M age:21 cho:105 smo:Y hdl:51 sbp:100 med:N out:<1
sex:M age:36 cho:105 smo:Y hdl:51 sbp:100 med:N out:1
sex:M age:41 cho:105 smo:Y hdl:51 sbp:100 med:N out:2
sex:M age:47 cho:105 smo:Y hdl:51 sbp:100 med:N out:2
sex:M age:51 cho:105 smo:Y hdl:51 sbp:100 med:N out:5
sex:M age:57 cho:105 smo:Y hdl:51 sbp:100 med:N out:5
sex:M age:61 cho:105 smo:Y hdl:51 sbp:100 med:N out:8
sex:M age:67 cho:105 smo:Y hdl:51 sbp:100 med:N out:10
sex:M age:71 cho:105 smo:Y hdl:51 sbp:100 med:N out:12
sex:M age:77 cho:105 smo:Y hdl:51 sbp:100 med:N out:16

# HDL    # Checked
sex:M age:41 cho:105 smo:N hdl:70 sbp:100 med:N out:<1
sex:M age:41 cho:105 smo:N hdl:51 sbp:100 med:N out:<1
sex:M age:41 cho:105 smo:N hdl:45 sbp:100 med:N out:1
sex:M age:41 cho:105 smo:N hdl:37 sbp:100 med:N out:1

# Systolic Untreated    # Checked
sex:M age:41 cho:105 smo:N hdl:51 sbp:100 med:N out:1
sex:M age:41 cho:105 smo:N hdl:51 sbp:121 med:N out:1
sex:M age:41 cho:105 smo:N hdl:51 sbp:134 med:N out:1
sex:M age:41 cho:105 smo:N hdl:51 sbp:142 med:N out:1
sex:M age:41 cho:105 smo:N hdl:51 sbp:180 med:N out:1

# Systolic Treated    # Checked
sex:M age:41 cho:105 smo:N hdl:51 sbp:100 med:Y out:1
sex:M age:41 cho:105 smo:N hdl:51 sbp:121 med:Y out:1
sex:M age:41 cho:105 smo:N hdl:51 sbp:134 med:Y out:1
sex:M age:41 cho:105 smo:N hdl:51 sbp:142 med:Y out:1
sex:M age:41 cho:105 smo:N hdl:51 sbp:180 med:Y out:1


