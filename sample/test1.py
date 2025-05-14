import pandas as pd
import os
# Sample Data for Corporate Complaints about Water, EB, Garbage, and Roads with department info
data = {
    'complaint_text': [
        "The water supply in the office building is inconsistent and needs urgent attention.",
        "We received an unusually high electricity bill, and we suspect there is an error in the meter reading.",
        "Garbage collection in the industrial area is irregular, causing health hazards.",
        "The road leading to the office has numerous potholes, making it dangerous for employees to commute.",
        "The water supply has been contaminated, affecting the quality of water in the office.",
        "Our electricity meter has been malfunctioning, resulting in incorrect billing amounts.",
        "The garbage is not collected on time, and it's causing unpleasant odors in the office vicinity.",
        "The road near our office is blocked due to construction, causing traffic jams.",
        "Water pressure in the building is low, making it difficult to operate essential equipment.",
        "The electricity in the office keeps going off, disrupting our daily operations.",
        "The trash bins in our office parking lot are overflowing, and waste management is ineffective.",
        "The road near our headquarters is not properly maintained, causing vehicle damage.",
        "The water bill for the office is unusually high, and we need clarification on the charges.",
        "The office building experiences power outages too often, affecting productivity.",
        "The garbage collection service is unreliable, and we are constantly facing delays in disposal.",
        "There are dangerous potholes on the road that need immediate repair for the safety of commuters.",
        "The water supply pipes have burst multiple times, leading to disruptions in daily activities.",
        "We are being overcharged for electricity despite our office using minimal power.",
        "The waste collection in our industrial zone is erratic, leading to litter accumulation.",
        "The road near the office is filled with large potholes, making driving hazardous.",
        "The building’s water filtration system is malfunctioning, resulting in poor water quality.",
        "The electricity grid is unstable, causing frequent interruptions and power surges.",
        "The trash bins outside our building are often not emptied on time, creating a sanitation issue.",
        "There is severe traffic congestion on the road outside our office, leading to delays in employee commutes.",
        "We have low water pressure in the building, affecting essential services like bathrooms and kitchens.",
        "Our office received a bill with an inflated electricity charge. We need an audit of our consumption.",
        "The garbage collection trucks are too few, and they don't reach our area regularly.",
        "The road outside our office is riddled with potholes, making driving unsafe for employees.",
        "Water leaks have been reported in the office plumbing system multiple times over the past month.",
        "The electrical supply to the office building is erratic, and we need a reliable source.",
        "Garbage collection in our area is infrequent, leading to waste piling up on the streets.",
        "The road near our office is slippery during rainy weather, increasing the risk of accidents.",
        "The water bill for the office is unusually high, and we need an explanation for the charges.",
        "The electricity in our office is unreliable, and we need to install a backup system.",
        "The garbage collection service is insufficient, and trash piles up in the parking area.",
        "The road near our office is under construction, causing major delays for employees.",
        "The water supply system is outdated, and there are frequent interruptions in service.",
        "The electricity in the office keeps flickering, and the power grid is unstable.",
        "The waste collection in our area is inconsistent, causing garbage to accumulate in the streets.",
        "The road leading to the office has no proper lighting, making it unsafe at night.",
        "Water leaks in the office building are frequent, and plumbing repairs are needed immediately.",
        "The electricity meters in our office are faulty, resulting in excessive and inaccurate billing.",
        "Garbage collection is slow, and we need better waste management in our industrial area.",
        "The road near our building is not properly maintained, causing damage to our vehicles.",
        "The water supply in the office building is erratic and frequently stops without notice.",
        "The electricity supply is unreliable, and we need a more stable power source for our building.",
        "Garbage collection is inefficient, and trash bins are not emptied regularly.",
        "The road near our office has multiple cracks and potholes, which need urgent repair.",
        "We are experiencing frequent water supply interruptions, which affect the office operations.",
        "The electricity bill for the office is much higher than expected, and we need an audit.",
        "Garbage collection service is irregular, and waste is accumulating around the building.",
        "The road near our office is filled with potholes, causing car accidents.",
        "The water supply in our building has been shut off multiple times without prior notice.",
        "Electricity surges in our office are damaging equipment and causing disruptions.",
        "The garbage collection service is slow, and waste is piling up in the vicinity of the office.",
        "The road leading to our office is under construction, causing significant delays during commutes.",
        "The water supply system in the office needs urgent repairs to prevent future disruptions.",
        "We have been overcharged for electricity, and the billing system needs to be reviewed.",
        "The garbage bins are overflowing, and we are facing major hygiene issues in the office vicinity.",
        "The road near our office needs resurfacing, and traffic congestion is a major issue.",
        "The water supply in the office building is unreliable, leading to operational disruptions.",
        "There is a lack of consistent power supply to our office, and frequent outages are disrupting work.",
        "The garbage collection service is inconsistent, and waste is piling up around the building.",
        "The road near our office is in poor condition, and driving is hazardous.",
        "The water pressure in our office building is too low, and we need a better supply system.",
        "The electricity bill is consistently higher than expected, and we need clarification on charges.",
        "The garbage collection service is unreliable, and trash is not being picked up regularly.",
        "The road near the office needs urgent repairs, and it’s causing significant delays in commuting."
    ],
    'category': [
        'Water Supply', 'Electricity Bills (EB)', 'Garbage Collection', 'Roads', 'Water Supply', 'Electricity Bills (EB)', 'Garbage Collection', 'Roads',
        'Water Supply', 'Electricity Bills (EB)', 'Garbage Collection', 'Roads', 'Water Supply', 'Electricity Bills (EB)', 'Garbage Collection', 'Roads',
        'Water Supply', 'Electricity Bills (EB)', 'Garbage Collection', 'Roads', 'Water Supply', 'Electricity Bills (EB)', 'Garbage Collection', 'Roads',
        'Water Supply', 'Electricity Bills (EB)', 'Garbage Collection', 'Roads', 'Water Supply', 'Electricity Bills (EB)', 'Garbage Collection', 'Roads',
        'Water Supply', 'Electricity Bills (EB)', 'Garbage Collection', 'Roads', 'Water Supply', 'Electricity Bills (EB)', 'Garbage Collection', 'Roads',
        'Water Supply', 'Electricity Bills (EB)', 'Garbage Collection', 'Roads', 'Water Supply', 'Electricity Bills (EB)', 'Garbage Collection', 'Roads',
        'Water Supply', 'Electricity Bills (EB)', 'Garbage Collection', 'Roads', 'Water Supply', 'Electricity Bills (EB)', 'Garbage Collection', 'Roads',
        'Water Supply', 'Electricity Bills (EB)', 'Garbage Collection', 'Roads', 'Water Supply', 'Electricity Bills (EB)', 'Garbage Collection', 'Roads',
        'Water Supply', 'Electricity Bills (EB)', 'Garbage Collection', 'Roads', 'Water Supply', 'Electricity Bills (EB)', 'Garbage Collection', 'Roads',
        'Water Supply', 'Electricity Bills (EB)', 'Garbage Collection', 'Roads', 'Water Supply', 'Electricity Bills (EB)', 'Garbage Collection', 'Roads',
        'Water Supply', 'Electricity Bills (EB)', 'Garbage Collection', 'Roads', 'Water Supply', 'Electricity Bills (EB)', 'Garbage Collection', 'Roads',
        'Water Supply', 'Electricity Bills (EB)', 'Garbage Collection', 'Roads', 'Water Supply', 'Electricity Bills (EB)', 'Garbage Collection', 'Roads',
        'Water Supply', 'Electricity Bills (EB)', 'Garbage Collection', 'Roads', 'Water Supply', 'Electricity Bills (EB)', 'Garbage Collection', 'Roads',
        'Water Supply', 'Electricity Bills (EB)', 'Garbage Collection', 'Roads'
    ],
    'department': [
        'Water Department', 'Electricity Department', 'Waste Management Department', 'Public Works Department', 'Water Department', 'Electricity Department', 'Waste Management Department', 'Public Works Department',
        'Water Department', 'Electricity Department', 'Waste Management Department', 'Public Works Department', 'Water Department', 'Electricity Department', 'Waste Management Department', 'Public Works Department',
        'Water Department', 'Electricity Department', 'Waste Management Department', 'Public Works Department', 'Water Department', 'Electricity Department', 'Waste Management Department', 'Public Works Department',
        'Water Department', 'Electricity Department', 'Waste Management Department', 'Public Works Department', 'Water Department', 'Electricity Department', 'Waste Management Department', 'Public Works Department',
        'Water Department', 'Electricity Department', 'Waste Management Department', 'Public Works Department', 'Water Department', 'Electricity Department', 'Waste Management Department', 'Public Works Department',
        'Water Department', 'Electricity Department', 'Waste Management Department', 'Public Works Department', 'Water Department', 'Electricity Department', 'Waste Management Department', 'Public Works Department',
        'Water Department', 'Electricity Department', 'Waste Management Department', 'Public Works Department', 'Water Department', 'Electricity Department', 'Waste Management Department', 'Public Works Department',
        'Water Department', 'Electricity Department', 'Waste Management Department', 'Public Works Department', 'Water Department', 'Electricity Department', 'Waste Management Department', 'Public Works Department',
        'Water Department', 'Electricity Department', 'Waste Management Department', 'Public Works Department', 'Water Department', 'Electricity Department', 'Waste Management Department', 'Public Works Department',
        'Water Department', 'Electricity Department', 'Waste Management Department', 'Public Works Department', 'Water Department', 'Electricity Department', 'Waste Management Department', 'Public Works Department',
        'Water Department', 'Electricity Department', 'Waste Management Department', 'Public Works Department', 'Water Department', 'Electricity Department', 'Waste Management Department', 'Public Works Department'
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
csv_path = os.path.join("complaints_dataset1.csv")
df.to_csv(csv_path, index=False)

print("CSV file saved successfully!")
