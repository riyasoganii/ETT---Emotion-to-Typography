# ETT-Emotion-to-Typography

Inspired by other relevant research in this domain, we propose a multisensory experience that enables users to better convey their emotions through words by composing typography using emotion detection. We built a typography-emotion dataset by conducting a user survey and analysis of existing data. Following it with the construction of an emotion detection model capable of taking real-time snapshots of the user and detecting their emotion as they give a text input to the model. The final result is an ETT (Emotion-to-Typography) model, which takes emotions and text as input, and prints typography accordingly. 

Steps to run:

1. To build and train the FER model

! python traincnn.py

This will create two files - model.json and weights.h5

2. To run the FER model (takes user text and webcam input, runs webcam images through model)

! python FER.py

The photos taken will be saved as photo.jpeg. The emotions detected will be saved in emotion.txt. The text input will be saved in text.txt.

3. To generate the typography

! python typographyGenerator.py

The typography will appear in a new window titled 'Typography'.

NOTE: the fer2013.csv dataset must be installed.
NOTE: When entering user text, input one word at a time. End the sentence with a fullstop
