import random
import pandas as pd

# Define a list of synthetic petitions across different categories and departments
petitions_data = [
    {"petition": "The road in our neighborhood is in terrible condition and needs urgent repair.", "category": "Infrastructure", "department": "Public Works"},
    {"petition": "We request more medical staff in the hospital to handle the growing patient load.", "category": "Health", "department": "Health Department"},
    {"petition": "There is a water scarcity issue in the region, urgent attention is needed.", "category": "Environment", "department": "Environmental Protection Agency"},
    {"petition": "The public park near our area is not safe due to poor lighting and maintenance.", "category": "Public Safety", "department": "Public Safety Department"},
    {"petition": "School admissions for the new academic year are being delayed. We need a solution immediately.", "category": "Education", "department": "Education Department"},
    {"petition": "The streets in our city are filled with garbage and need to be cleaned immediately.", "category": "Infrastructure", "department": "Public Works"},
    {"petition": "The hospital in our area lacks enough medical equipment and it's affecting patient care.", "category": "Health", "department": "Health Department"},
    {"petition": "A large amount of plastic waste is accumulating in our neighborhood, and there is no plan for recycling.", "category": "Environment", "department": "Environmental Protection Agency"},
    {"petition": "The playground in the local park is unsafe for children and needs repairs.", "category": "Public Safety", "department": "Public Safety Department"},
    {"petition": "The school year has been delayed due to administrative issues, and we demand a swift resolution.", "category": "Education", "department": "Education Department"},
    {"petition": "The roads are flooded after every heavy rain, making transportation difficult for all residents.", "category": "Infrastructure", "department": "Public Works"},
    {"petition": "The local health center is under-staffed and is struggling to provide adequate care.", "category": "Health", "department": "Health Department"},
    {"petition": "Trees are being cut down in our region without any replanting efforts, leading to environmental damage.", "category": "Environment", "department": "Environmental Protection Agency"},
    {"petition": "There have been several car accidents due to poor street lighting in our neighborhood.", "category": "Public Safety", "department": "Public Safety Department"},
    {"petition": "We need a better curriculum in schools that includes modern technologies and new-age subjects.", "category": "Education", "department": "Education Department"},
    {"petition": "Our community has been experiencing frequent power outages, and it's becoming unbearable.", "category": "Infrastructure", "department": "Public Works"},
    {"petition": "The local hospital's emergency department is understaffed and cannot handle the number of patients.", "category": "Health", "department": "Health Department"},
    {"petition": "Deforestation is happening rapidly in our region, and it needs to be stopped immediately.", "category": "Environment", "department": "Environmental Protection Agency"},
    {"petition": "The streets in our neighborhood are poorly lit, and it makes walking at night dangerous.", "category": "Public Safety", "department": "Public Safety Department"},
    {"petition": "There is a need for better extracurricular activities and programs in schools for students' holistic development.", "category": "Education", "department": "Education Department"},
    {"petition": "Potholes on the main roads are damaging vehicles and creating safety hazards.", "category": "Infrastructure", "department": "Public Works"},
    {"petition": "The local health center doesn't have the necessary equipment to treat chronic diseases.", "category": "Health", "department": "Health Department"},
    {"petition": "Plastic waste is being dumped into rivers, and it is affecting the local wildlife.", "category": "Environment", "department": "Environmental Protection Agency"},
    {"petition": "Pedestrian crossings are poorly marked, leading to accidents involving pedestrians.", "category": "Public Safety", "department": "Public Safety Department"},
    {"petition": "We need better career counseling services in schools to guide students in their future choices.", "category": "Education", "department": "Education Department"},
    {"petition": "Our city's roads are not maintained properly, leading to cracks and unsafe driving conditions.", "category": "Infrastructure", "department": "Public Works"},
    {"petition": "Our health system is not equipped to deal with mental health issues, and it's affecting people in our community.", "category": "Health", "department": "Health Department"},
    {"petition": "Illegal dumping of waste is occurring in our neighborhood, and it's causing a health hazard.", "category": "Environment", "department": "Environmental Protection Agency"},
    {"petition": "The public transportation system is unreliable and uncomfortable for passengers.", "category": "Public Safety", "department": "Public Safety Department"},
    {"petition": "Our schools lack modern educational tools and technologies, affecting students' learning experience.", "category": "Education", "department": "Education Department"},
    {"petition": "There are severe traffic jams every morning because of inadequate road planning in the city.", "category": "Infrastructure", "department": "Public Works"},
    {"petition": "Our local health center is not able to treat emergency cases due to lack of resources.", "category": "Health", "department": "Health Department"},
    {"petition": "The lack of proper waste management in our city is leading to garbage piling up on the streets.", "category": "Environment", "department": "Environmental Protection Agency"},
    {"petition": "The street lights in our area are constantly malfunctioning, leading to unsafe conditions at night.", "category": "Public Safety", "department": "Public Safety Department"},
    {"petition": "We need a new hospital in our region as the existing one is overcrowded and outdated.", "category": "Health", "department": "Health Department"},
    {"petition": "There is too much noise pollution in the city, especially near residential areas.", "category": "Environment", "department": "Environmental Protection Agency"},
    {"petition": "There are serious safety concerns in the local community center due to structural damage.", "category": "Public Safety", "department": "Public Safety Department"},
    {"petition": "The local education system needs reform to better prepare students for the job market.", "category": "Education", "department": "Education Department"},
]

# Generate 100 sample data points by repeating and shuffling the data
data = petitions_data * 5  # Repeat the data to make 100 examples
random.shuffle(data)  # Shuffle the data to add randomness

# Convert data to DataFrame
df = pd.DataFrame(data)

# Show the first few rows of the DataFrame
print(df.head(100))
df.to_csv('petitions_dataset.csv', index=False)

# Confirm that the CSV file is saved
print("Dataset saved to 'petitions_dataset.csv'")
