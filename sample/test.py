import pandas as pd
import os

# Your data (first 100 entries for demonstration)
data = {
    'complaint_text': [
        "The water supply in our neighborhood is irregular and needs to be fixed urgently.",
        "The public transportation service is overcrowded and unreliable. Immediate action is needed.",
        "There is no proper sanitation in our area, making it unsafe for residents.",
        "I am being unfairly treated by my supervisor and demand immediate intervention.",
        "Our local hospital lacks medical supplies and staff. Patients are suffering.",
        "The roads are filled with potholes, causing damage to vehicles and accidents.",
        "There is no access to clean drinking water in rural areas.",
        "The garbage collection service is infrequent, creating a health hazard in our community.",
        "Emergency response times are slow, leading to avoidable harm during disasters.",
        "Lack of proper drainage systems is causing flooding in many neighborhoods.",
        "The local school is overcrowded, and students are not receiving adequate education.",
        "There is no street lighting in our neighborhood, making it unsafe at night.",
        "Our hospital is understaffed, and patients have to wait for hours for treatment.",
        "Public transportation is expensive and inefficient. It's difficult for people to commute.",
        "The roads are so bad that they are causing car accidents and damaging vehicles.",
        "The sewage system in our area is outdated and needs urgent repairs.",
        "We have insufficient emergency response services in our area, causing delays.",
        "The local police station is understaffed, leading to slow response times.",
        "There's a lack of affordable housing in our city, and the government is doing nothing.",
        "The water quality in our area is poor, and we are experiencing frequent outages.",
        "There are frequent power cuts, affecting the daily lives of residents.",
        "The healthcare facilities in our area are substandard and need improvement.",
        "Our city's waste management system is inefficient, leading to garbage piling up.",
        "There is a lack of basic healthcare facilities in rural areas, which is causing health issues.",
        "The local authorities are not doing enough to combat air pollution in the area.",
        "Our school lacks essential educational resources such as books and technology.",
        "There is frequent flooding in our area due to poorly maintained drainage systems.",
        "We have been waiting for proper road repairs for months, but nothing has been done.",
        "Our local library is outdated, and the resources are not up to date with modern education standards.",
        "The water supply in my neighborhood has been unreliable for months.",
        "Local health clinics are overcrowded, and it takes too long to receive treatment.",
        "The roads in my area are riddled with potholes, making travel dangerous.",
        "The traffic lights in my area are malfunctioning, causing major traffic jams.",
        "The garbage collection service is infrequent, and it’s a public health concern.",
        "There is no public transportation in rural areas, making it difficult for people to commute.",
        "The local park is poorly maintained and full of trash.",
        "We need more police patrols in our area to ensure safety.",
        "Our area lacks proper sanitation facilities, which is leading to an increase in diseases.",
        "The public library is closed for renovation, and there is no timeline for reopening.",
        "The medical facilities in our area are insufficient and need urgent attention.",
        "There’s a lack of pedestrian infrastructure in my city, making it unsafe for walking.",
        "There is frequent flooding in my area due to blocked drainage systems.",
        "The public transportation buses are old and uncomfortable.",
        "Our local school lacks proper classrooms for students.",
        "The roads in my neighborhood need urgent resurfacing.",
        "Our city's recycling program is poorly managed and needs better implementation.",
        "The healthcare center in our neighborhood doesn't have enough medical staff.",
        "There is no proper waste management in our city, and it’s becoming a significant issue.",
        "The local police station doesn't have enough resources to tackle crime effectively.",
        "The bus stop near my house is in disrepair, and the shelter is falling apart.",
        "The hospital in my area lacks essential medical supplies.",
        "We have to deal with constant power outages, disrupting our daily lives.",
        "The government is not addressing the rising number of homeless people in the city.",
        "Our local school is underfunded and lacks basic supplies for students.",
        "The drainage system in my neighborhood is clogged, causing waterlogging during rains.",
        "There are too many potholes on the roads, which is damaging vehicles.",
        "The government is not doing enough to ensure clean drinking water for all citizens.",
        "Our city has insufficient green spaces, and the parks are poorly maintained.",
        "There are no fire hydrants in my area, which is a major safety concern.",
        "The public hospitals are overcrowded, and it takes hours to receive treatment.",
        "We need more streetlights to ensure safety in our area at night.",
        "The roads near my house are flooded during every heavy rain.",
        "There is an increase in street crimes, and the police are not doing enough.",
        "My neighborhood has no access to reliable public transport, which is causing inconvenience.",
        "The parks in my area are filled with trash, and it’s becoming a public health issue.",
        "The sewage system in my city is outdated and needs urgent repairs.",
        "Our local school lacks basic safety measures, making it a hazard for students.",
        "The drainage system in my area is poor, leading to frequent waterlogging.",
        "The local healthcare facilities are not well-equipped to handle emergencies.",
        "We need more buses to provide better public transportation.",
        "The roads in my area are not maintained properly, leading to accidents.",
        "The lack of affordable housing is becoming a major issue in our city.",
        "Our local government is not addressing the issue of illegal dumping in the neighborhood.",
        "There is no proper healthcare infrastructure in rural areas.",
        "The medical staff at the local hospital is understaffed and overworked.",
        "There are too many stray animals in my area, and they pose a health hazard.",
        "The water supply is frequently contaminated, leading to health problems.",
        "The public restroom facilities in the city are dirty and poorly maintained.",
        "The public schools are overcrowded, and students do not have enough resources.",
        "There are not enough ambulances available during emergencies.",
        "Our area has insufficient street lighting, making it dangerous at night.",
        "The public transportation system in my city is unreliable and expensive.",
        "The public hospitals are understaffed, leading to long waiting times for patients.",
        "There are not enough community centers in our area.",
        "Our local government has not addressed the issue of noise pollution in residential areas.",
        "The emergency services in my city are slow and unresponsive.",
        "There is no proper recycling program in my neighborhood.",
        "The healthcare services in rural areas are severely lacking.",
        "The local police do not respond quickly to emergencies.",
        "We are facing a severe shortage of water in our area during the summer months.",
        "There are frequent traffic accidents due to poor road conditions.",
        "The local parks are unsafe for children due to lack of proper maintenance.",
        "Our local government is not doing enough to improve air quality.",
        "There is inadequate support for people with disabilities in public facilities.",
        "The public healthcare system is overcrowded and lacks essential resources."
    ],
    'category': [
        'Infrastructure', 'Public Safety', 'Health', 'Human Resources', 'Health',
        'Infrastructure', 'Public Health', 'Public Health', 'Public Safety', 'Infrastructure',
        'Education', 'Public Safety', 'Health', 'Public Transportation', 'Infrastructure', 'Health',
        'Public Safety', 'Human Resources', 'Housing', 'Health', 'Energy', 'Health', 'Waste Management',
        'Public Safety', 'Public Safety', 'Infrastructure', 'Public Health', 'Public Transportation',
        'Public Safety', 'Waste Management', 'Infrastructure', 'Education', 'Public Safety', 'Health',
        'Public Safety', 'Housing', 'Public Health', 'Public Safety', 'Education', 'Infrastructure',
        'Waste Management', 'Public Safety', 'Human Resources', 'Infrastructure', 'Public Health',
        'Public Safety', 'Housing', 'Education', 'Infrastructure', 'Health', 'Energy', 'Public Safety',
        'Public Safety', 'Health', 'Public Safety', 'Infrastructure', 'Public Safety', 'Public Safety',
        'Housing', 'Public Safety', 'Infrastructure', 'Public Health', 'Public Safety', 'Health',
        'Public Health', 'Waste Management', 'Human Resources', 'Waste Management', 'Health',
        'Public Safety', 'Infrastructure', 'Human Resources', 'Public Safety', 'Public Safety',
        'Infrastructure', 'Health', 'Education', 'Waste Management', 'Public Safety', 'Housing',
        'Public Health', 'Public Safety', 'Waste Management', 'Public Safety', 'Infrastructure',
        'Public Health', 'Waste Management', 'Waste Management', 'Health', 'Public Safety'
    ],
    'department': [
        'Public Works', 'Public Safety Department', 'Health Department', 'Human Resources', 'Health Department',
        'Public Works', 'Public Health Department', 'Public Health Department', 'Emergency Services',
        'Public Works', 'Education Department', 'Public Safety Department', 'Health Department',
        'Public Transportation', 'Public Works', 'Health Department', 'Public Safety Department', 'Human Resources',
        'Housing Department', 'Health Department', 'Energy Department', 'Health Department', 'Waste Management',
        'Public Safety Department', 'Public Safety Department', 'Public Works', 'Public Health Department',
        'Public Transportation', 'Public Safety Department', 'Waste Management', 'Infrastructure Department',
        'Education Department', 'Public Safety Department', 'Health Department', 'Public Safety Department',
        'Housing Department', 'Public Health Department', 'Public Safety Department', 'Public Education',
        'Waste Management', 'Infrastructure Department', 'Human Resources Department', 'Infrastructure Department',
        'Public Health', 'Public Safety Department', 'Public Safety Department', 'Health Department',
        'Infrastructure Department', 'Public Health Department', 'Public Safety Department', 'Housing Department',
        'Education Department', 'Infrastructure Department', 'Health Department', 'Energy Department',
        'Public Safety Department', 'Public Safety Department', 'Health Department', 'Public Safety Department',
        'Infrastructure Department', 'Public Safety Department', 'Public Safety Department', 'Housing Department',
        'Public Safety Department', 'Infrastructure Department', 'Public Health Department', 'Public Safety Department',
        'Health Department', 'Public Health Department', 'Waste Management'
    ]
}

# Ensure the lists are all of the same length
complaint_text_len = len(data['complaint_text'])
category_len = len(data['category'])
department_len = len(data['department'])

# Adjust category and department lists to match complaint_text length
if complaint_text_len != category_len:
    data['category'] = (data['category'] * (complaint_text_len // category_len + 1))[:complaint_text_len]
if complaint_text_len != department_len:
    data['department'] = (data['department'] * (complaint_text_len // department_len + 1))[:complaint_text_len]

# Create the DataFrame
df = pd.DataFrame(data)

# Save to CSV
csv_path = os.path.join("complaints_dataset.csv")
df.to_csv(csv_path, index=False)

print("CSV file saved successfully!")
