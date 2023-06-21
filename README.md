# Student Score Prediction

This web application predicts a student's score based on the number of study hours per day. It utilizes a linear regression model trained on a dataset of students' study hours and scores.

## Usage

1. Clone the Repository:

   ```shell
   git clone https://github.com/your-username/student-score-prediction.git

2. Change to the Project Directory:
     cd student-score-prediction

3. Install the Required Dependencies:
    pip install -r requirements.txt

4. Prepare the Dataset:
Create a CSV file named Supervised.csv with two columns: "Hours" and "Scores". Each row should represent a student's study hours and corresponding score.
Place the CSV file in the Dataset directory.

5. Run the Streamlit App:
    streamlit run app.py

6. Open the App in your Web Browser:
The app will open automatically in a new tab. If not, you can access it by visiting [http://localhost:8501](https://huggingface.co/spaces/Saaquib/student-score) in your web browser.

7.  Use the App:
Explore the EDA section to view summary statistics and a scatter plot of the dataset, providing insights into the relationship between study hours and scores.
In the Student Score Prediction section, enter the number of study hours for a student and click "Enter".
The app will display the predicted score for the given number of study hours.








