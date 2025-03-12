# Geosense
Geosense is a disaster prediction and monitoring system, focused on detecting landslides by analyzing various environmental factors. It utilizes real-time data such as rainfall, topography, slope, and seismic activity to provide accurate early warnings and insights into landslide-prone regions. It also helps in relief measures using satellite imaging, a chatbot for answering queries and government support.

## Links

- [NASA LHASA](https://github.com/nasa/LHASA)
- [NASA SALaD](https://github.com/nasa/salad)
- [Twilio Calls and Messages](https://colab.research.google.com/drive/1qtunTEC9H98VvkscGc-gcxHzYOLp3rmc?usp=sharing)

# The Prediction Phase
# Features
* Real-time Data Collection: Gathers live data such as rainfall, topography, and slope to detect potential landslide risks.
  
* Environmental Analysis: Uses a combination of geographical factors and seismic data to create a comprehensive risk assessment.
  
* Self-Built Dataset: Uses detailed output tables with information like location, timestamp, latitude, longitude, depth, tilt, magnitude, temperature, humidity etc for prediction.
  
* Scalability: Can be adapted to various regions prone to natural disasters.
  
* Medical CHATBOT: Answers queries related to first aid and uses QGIS to give nearest hospital, blood bank locations.

* Predictive analysis ML model: 

# Process Flowchart
The below below clearly depicts the process flow involved in Geosense.

# Tech Stack Used
The tech stack used to build the app is as follows:

The Application:

* Google Firebase - To store and manage NGO data, ensuring efficient access and scalability.
* React and Capacitor - provides a powerful and flexible environment forbuilding and testing cross-platform apps.

Governement Organizations involved:

* QGIS - used to create, edit, visualize, analyze, and publish geospatial information.
* NGO DARPAN - a government platform listing over 100,000 active NGOs across India.

Software:
* Numpy - NumPy is a powerful Python library used for numerical computing.
* Pandas - A powerful Python library for data manipulation and analysis, providing data structures like DataFrames for easy handling of structured data.
* Requests - A simple and elegant HTTP library for Python, designed to make sending HTTP requests easy and user-friendly, allowing seamless integration with web APIs.
* Mapbox and Google Maps API  - A suite of APIs that enables developers to integrate Google Maps services into their applications, offering features like geolocation,directions, and places information for enhanced location-based experiences.

# Dataset used (SELF-BUILT)
This dataset contains the information of more than 560+ locations with latitude ad longitude specified. It also contains specific features of the land like tilt angle, magnitude, temperature, humidity, soil moisture, which effectively serves as a good dataset for landslide prediction analysis.

# Prediction Analysis Model
The dataset was first fed into the model. Using the RandomForest Classifier algorithm, we trained the mountaineous terrain regions of the world. The analysis model returned an accuracy of 81%.

# The Preparation phase
When a disaster is predicted, the app does the following:
1. Alerts nearby NGOs using data from NGO DARPAN.
2. Uses AI agents doctors and keeps them on standby. The agents also books train tickets to a nearby safe location.
3. Notifies the government and concerned ministries to provide relief fund and compensation and ask for evacuation help.
4. Classifies the zone as a 'RED ZONE' and uses basic algorithms to find the shortest and safest distance to a 'GREEN ZONE' (Safe zone).

# Algorithms used
1. Dijkstra's Algorithm : Calculates the shortest distance between the red zone and green zone.
2. A-Star Algorithm : A popular pathfinding and graph traversal algorithm that efficiently finds the shortest path from a start node to a target node by using heuristics.

# Google Maps API
After creating an API key, Google Maps APi was accessible. Using it we kept a source and a destination node to calculate the time to reach. An interactive map as a html file was also downloaded in our colab file locally.

We were also able to achieve directions for the destination.

# The Relief Phase
To manage the aftermath of the disaster, we have incorporated 3 strategies:
1. Medical ChatBot.
2. Satellite Imaging using QGIS.
3. Government Support.

# Medical Chatbot
A simple but efficient chatbot designed to answer basic queries about first aid and related health issues. When given a particular location, the chatbot will first identify the coordinates (latitude and longitude) of the location. Then it will find the nearest bloodbank, hospital, hotel, pharmacy, food store rations and any other safe landmark nearby so that the people can leverage it to their requirements.

The chatbot is basically fed with some general intents and the random module is used.
It has been trained with a book "The Gale encyclopedia of Medicine" by Jacqueline L. Longe trained by Llama 3.0.

# Satellite imaging using QGIS
The analysis performed here are:
1. Heatmap analyis for population density.
2. NASA Sentinel data.

In a more detailed version, satellite imaging also performs these unique features:
* Satellite Imagery Acquisition.
  
* Origin-Destination Matrix.
  
* Geospatial Data Extraction.
  
* Topographic Position Index.
  
* Terrain Stability Analysis.

# Conclusion
Our solution-Geosense, provides a quick and efficient way to predict landslides well in advance. Due to this, Geosense minimizes loss of life and property. By leveraging Google Maps and QGIS, we were successfully able to integrate relief features.





 
