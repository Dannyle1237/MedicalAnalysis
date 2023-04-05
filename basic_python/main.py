import database_func as dbf

#How to print values from database
#dbf.printQuery('''SELECT * FROM Disease''')
dbf.printQuery('''SELECT * FROM Combination''')

# #How to get values
# diseases = dbf.storeQueryToVar('''SELECT * FROM Disease''')
# print("Diseases from DB stored:\n" + str(diseases))
# #Everything in a database is stored in a tuple(list), so you'll
# #need to pull it out to store as a single value
# new_diseases = []
# for value in diseases:
#     new_diseases.append(value[0])
# diseases = new_diseases
# print("New diseases from cleaning query:\n" + str(diseases))
