#Create an empty list
cloud_services = []

#Populate the list using the append using for loop

for i in ["IaaS", "PaaS" , "serverless" , "SaaS"]:
    cloud_services.append(i)

#Print the List and the Length
print(cloud_services)
print(len(cloud_services))

# Remove two services by index
cloud_services.pop(1)
cloud_services.pop(0)

# Print the updated list and its length
print(cloud_services)
print(len(cloud_services))
