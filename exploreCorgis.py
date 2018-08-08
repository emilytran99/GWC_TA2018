import school_scores

list_of_record = school_scores.get_all()

#print first element in data set 
#print(list_of_record[0])

#print state name and year for each row 
for row in list_of_record:
	print("State:", row["State"]["Name"], "Year:", row["Year"])

#print out total test takers for each state per year 
for row in list_of_record:
	print("total test takers in", row["State"]["Name"], "in", row["Year"], "were", row["Total"]["Test-takers"])