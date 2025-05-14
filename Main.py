from flask import Flask, render_template, flash, request, session,send_file
from flask import render_template, redirect, url_for, request
#from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
#from werkzeug.utils import secure_filename
import datetime
import mysql.connector
import sys

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.classify import NaiveBayesClassifier
import pandas as pd
from nltk.sentiment import SentimentIntensityAnalyzer
from nltk import ne_chunk, pos_tag, word_tokenize
from nltk.tree import Tree

# Download necessary NLTK resources
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('vader_lexicon')
nltk.download('maxent_ne_chunker')
nltk.download('words')


app = Flask(__name__)
app.config['DEBUG']
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'

#-------------------------------------------------------------------------
# Read complaints from CSV file
def load_complaints_from_csv(file_path):
    return pd.read_csv(file_path)


# Preprocess text: Tokenize and remove stopwords
def preprocess_text(text):
    stop_words = set(stopwords.words('english'))
    words = word_tokenize(text)
    words = [w.lower() for w in words if w.isalpha() and w.lower() not in stop_words]
    return words


# Feature extraction for classification
def extract_features(text):
    words = preprocess_text(text)
    return {word: True for word in words}


# Train classifiers for category and department based on existing complaints
def train_classifiers(df):
    train_data_category = [(extract_features(complaint['complaint_text']), complaint['category']) for _, complaint in
                           df.iterrows()]
    train_data_department = [(extract_features(complaint['complaint_text']), complaint['department']) for _, complaint
                             in df.iterrows()]

    category_classifier = NaiveBayesClassifier.train(train_data_category)
    department_classifier = NaiveBayesClassifier.train(train_data_department)

    return category_classifier, department_classifier


# Predict category and department using the trained classifiers
def predict_category_and_department(complaint_text, category_classifier, department_classifier):
    features = extract_features(complaint_text)
    predicted_category = category_classifier.classify(features)
    predicted_department = department_classifier.classify(features)
    return predicted_category, predicted_department


# Function for analyzing sentiment using NLTK's SentimentIntensityAnalyzer
sia = SentimentIntensityAnalyzer()


# Function to categorize urgency based on sentiment scores
def categorize_urgency(sentiment_score):
    if sentiment_score <= -0.3:
        return 'High Urgency'
    elif sentiment_score <= 0:
        return 'Medium Urgency'
    else:
        return 'Low Urgency'


# Named Entity Recognition (NER) to extract named entities from text
def extract_named_entities(text):
    tokens = word_tokenize(text)
    tagged = pos_tag(tokens)
    tree = ne_chunk(tagged)

    named_entities = []
    for subtree in tree:
        if isinstance(subtree, Tree):  # It's a named entity
            entity = " ".join([word for word, tag in subtree])
            named_entities.append(entity)
    return named_entities


# Function to predict category, department, and urgency for a new complaint
def predict_for_user_input(df, user_complaint):
    category_classifier, department_classifier = train_classifiers(df)

    # Predict category and department
    predicted_category, predicted_department = predict_category_and_department(user_complaint, category_classifier,
                                                                               department_classifier)

    # Analyze sentiment for urgency
    sentiment_score = sia.polarity_scores(user_complaint)['compound']
    predicted_urgency = categorize_urgency(sentiment_score)

    # Extract named entities
    named_entities = extract_named_entities(user_complaint)

    return predicted_category, predicted_department, predicted_urgency, sentiment_score, named_entities


# Function to save analysis result to CSV file
def save_analysis_to_csv(df, user_complaint, predicted_category, predicted_department, predicted_urgency, output_file):
    result = {
        'complaint_text': user_complaint,
        'predicted_category': predicted_category,
        'predicted_department': predicted_department,
        'predicted_urgency': predicted_urgency
    }
    result_df = pd.DataFrame([result])

    # Append the result to the CSV file (or create a new one if not exist)
    result_df.to_csv(output_file, mode='a', header=not pd.io.common.file_exists(output_file), index=False)


#-------------------------------------------------------------------------






@app.route("/")
def homepage():

    return render_template('index.html')

@app.route("/admin")
def admin():

    return render_template('adlog.html')
@app.route("/ratview")
def ratview():
    id = request.args.get('id')
    session['ris']=id

    return render_template('rating.html')
@app.route("/userregister")
def userregister():

    return render_template('usreregister.html')
@app.route("/login")
def emp():
    return render_template('login.html')
@app.route("/userlogin")
def userlogin():
    return render_template('userlogin.html')
@app.route("/adminhome")
def adminhome():
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='empcomp')
    cur = conn.cursor()
    cur.execute("SELECT * FROM employee ")
    data = cur.fetchall()


    return render_template('adminhome.html', data=data)
@app.route("/emphome")
def emphome():
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='empcomp')
    # cursor = conn.cursor()
    cur = conn.cursor()
    cur.execute("SELECT * FROM complaint where status='complaint sent to officer'")
    data = cur.fetchall()
    return render_template('emphome.html',data=data)
@app.route("/userhome")
def userhome():
    return render_template('userhome.html')
@app.route("/empregister")
def empregister():
    return render_template('register.html')
@app.route("/viewuser")
def viewuser():
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='empcomp')
    # cursor = conn.cursor()
    cur = conn.cursor()
    cur.execute("SELECT * FROM register ")
    data = cur.fetchall()

    return render_template('viewuser.html',data=data)



@app.route("/adminlogin", methods=['GET', 'POST'])
def adminlogin():
    error = None
    if request.method == 'POST':
       if request.form['uname'] == 'admin' or request.form['password'] == 'admin':

           conn = mysql.connector.connect(user='root', password='', host='localhost', database='empcomp')
           # cursor = conn.cursor()
           cur = conn.cursor()
           cur.execute("SELECT * FROM employee ")
           data = cur.fetchall()

           return render_template('adminhome.html',data=data)

       else:
        return render_template('index.html', error=error)


@app.route("/emplogin", methods=['GET', 'POST'])
def emplogin():
    error = None
    if request.method == 'POST':
        username = request.form['uname']
        password = request.form['password']
        session['fname'] = request.form['uname']

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='empcomp')
        cursor = conn.cursor()
        cursor.execute("SELECT * from employee where uname='" + username + "' and password='" + password + "'")
        data = cursor.fetchone()
        if data is None:
            alert = 'Username or Password is wrong'
            return render_template('goback.html', data=alert)
        else:
            print(data[0])
            session['uid'] = data[0]
            conn = mysql.connector.connect(user='root', password='', host='localhost', database='empcomp')
            # cursor = conn.cursor()
            cur = conn.cursor()
            cur.execute("SELECT * FROM complaint where status='complaint sent to officer'")
            data = cur.fetchall()

            return render_template('emphome.html', data=data)

@app.route("/uslogin", methods=['GET', 'POST'])
def uslogin():
    error = None
    if request.method == 'POST':
        username = request.form['uname']
        password = request.form['password']
        session['uname'] = request.form['uname']

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='empcomp')
        cursor = conn.cursor()
        cursor.execute("SELECT * from register where uname='" + username + "' and password='" + password + "'")
        data = cursor.fetchone()
        if data is None:
            alert = 'Username or Password is wrong'
            return render_template('goback.html', data=alert)
        else:
            print(data[0])
            session['usid'] = data[0]
            conn = mysql.connector.connect(user='root', password='', host='localhost', database='empcomp')
            # cursor = conn.cursor()
            cur = conn.cursor()
            cur.execute("SELECT * FROM register where uname='" + username + "' and password='" + password + "'")
            data = cur.fetchall()

            return render_template('userhome.html', data=data)

@app.route("/register", methods=['GET', 'POST'])
def register():
    if request.method == 'POST':

        name1 = request.form['name']
        gender = request.form['gender']

        email = request.form['email']

        phone = request.form['phone']



        address = request.form['address']
        uname = request.form['uname']
        password = request.form['password']
        dept = request.form['dept']
        qual = request.form['qual']
        place = request.form['place']


        conn = mysql.connector.connect(user='root', password='', host='localhost', database='empcomp')
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO employee VALUES ('','" + name1 + "','" + gender + "','"+ email+"','"+phone+"','" + qual + "','" + dept + "','"+address+"','"+place+"','"+uname+"','"+password+"')")
        conn.commit()
        conn.close()


    return render_template('login.html')
@app.route("/usregister", methods=['GET', 'POST'])
def usregister():
    if request.method == 'POST':

        name1 = request.form['name']
        gender = request.form['gender']

        email = request.form['email']

        phone = request.form['phone']



        address = request.form['address']
        uname = request.form['uname']
        password = request.form['password']

        place = request.form['place']


        conn = mysql.connector.connect(user='root', password='', host='localhost', database='empcomp')
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO register VALUES ('','" + name1 + "','" + gender + "','"+ email+"','"+phone+"','"+address+"','"+place+"','"+uname+"','"+password+"')")
        conn.commit()
        conn.close()


    return render_template('userlogin.html')


@app.route("/complaint", methods=['GET', 'POST'])
def complaint():
    if request.method == 'POST':

        dept = ''
        cctype = request.form['ctype']

        location = request.form['location']

        date = request.form['date']
        uname= session['uname']



        details = request.form['details']
        file = request.files['file']
        file.save("static/upload/" + file.filename)
        # Load complaints data from CSV file (replace 'complaints.csv' with your file)
        input_csv = 'combined_file.csv'
        df = load_complaints_from_csv(input_csv)

        # Get user input (complaint text)
        user_complaint = details

        # Get predictions
        predicted_category, predicted_department, predicted_urgency, sentiment_score, named_entities = predict_for_user_input(
            df, user_complaint)

        # Output the results
        print("\nAnalysis for User Petition:")
        print(f"User Petition: {user_complaint}")
        print(f"Predicted Category: {predicted_category}")
        print(f"Predicted Department: {predicted_department}")
        print(f"Sentiment Score: {sentiment_score}")
        print(f"Urgency: {predicted_urgency}")
        print(f"Named Entities: {named_entities}")

        # Save the results back to a CSV file
        output_csv = 'processed_complaints.csv'  # Change this to your desired output file
        save_analysis_to_csv(df, user_complaint, predicted_category, predicted_department, predicted_urgency,
                             output_csv)
        print(f"Results saved to {output_csv}")





        conn = mysql.connector.connect(user='root', password='', host='localhost', database='empcomp')
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO complaint VALUES ('','" + uname + "','" + str(predicted_category) + "','"+ cctype+"','"+location+"','" + date + "','" + details + "','"+file.filename+"','','','"+str(predicted_urgency)+"','','','')")
        conn.commit()
        conn.close()


    return render_template('userhome.html')

@app.route("/cview")
def cview():
    uname = session['uname']
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='empcomp')
    # cursor = conn.cursor()
    cur = conn.cursor()
    cur.execute("SELECT * FROM complaint where uname='"+uname+"'")
    data = cur.fetchall()

    return render_template('cview.html', data=data)
@app.route("/viewcomplaint")
def viewcomplaint():

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='empcomp')
    # cursor = conn.cursor()
    cur = conn.cursor()
    cur.execute("SELECT * FROM complaint where status=''")
    data = cur.fetchall()

    return render_template('viewcomplaint.html', data=data)
@app.route("/action")
def action():


         #categories=request.form['id']
         id=request.args.get('id')

         print(id)
         conn = mysql.connector.connect(user='root', password='', host='localhost', database='empcomp')
         cursor = conn.cursor()
         cursor.execute("select * from complaint where id='"+id+"'")
         data = cursor.fetchall()
         print(data)
         return render_template("action.html", data=data)
@app.route("/action1", methods=['GET', 'POST'])
def action1():
    if request.method == 'POST':


         #categories=request.form['id']
         id = request.form['id']
         cctype = request.form['ataken']

         print(id)
         conn = mysql.connector.connect(user='root', password='', host='localhost', database='empcomp')
         cursor = conn.cursor()
         cursor.execute("update complaint set status='"+ cctype +"' where id='"+ id +"'")
         conn.commit()
         conn.close()
         conn1 = mysql.connector.connect(user='root', password='', host='localhost', database='empcomp')

         cursor1 = conn1.cursor()
         cursor1.execute("select * from complaint ")
         data = cursor1.fetchall()
         return render_template("emphome.html", data=data)
@app.route("/view1")
def view1():


         #categories=request.form['id']
         id=request.args.get('id')

         print(id)
         conn = mysql.connector.connect(user='root', password='', host='localhost', database='empcomp')
         cursor = conn.cursor()
         cursor.execute("select * from complaint")
         data = cursor.fetchall()
         print(data)
         return render_template("view1.html", data=data)
@app.route("/actionass")
def actionass():


         #categories=request.form['id']
         id=request.args.get('id')



         print(id)
         conn = mysql.connector.connect(user='root', password='', host='localhost', database='empcomp')
         cursor = conn.cursor()
         cursor.execute("update complaint set status='complaint sent to officer' where id='" + id + "'")
         conn.commit()
         conn.close()
         conn1 = mysql.connector.connect(user='root', password='', host='localhost', database='empcomp')

         cursor1 = conn1.cursor()
         cursor1.execute("select * from complaint where status='' ")
         data = cursor1.fetchall()
         return render_template("viewcomplaint.html", data=data)
@app.route("/cview1")
def cview1():
    uname = session['fname']
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='empcomp')
    # cursor = conn.cursor()
    cur = conn.cursor()
    cur.execute("SELECT * FROM complaint ")
    data = cur.fetchall()

    return render_template('cview1.html', data=data)
@app.route("/feed", methods=['GET', 'POST'])
def feed():
    error = None
    if request.method == 'POST':
        id=session['ris']
        urate = request.form['rate']
        feed = request.form['feed']
        conn = mysql.connector.connect(user='root', password='', host='localhost', database='empcomp')
        cursor = conn.cursor()
        cursor.execute(
            "update complaint set urate='"+urate+"',feed='"+feed+"' where id='"+id+"'")
        conn.commit()
        conn.close()
        return render_template('cview.html')
@app.route("/cupload")
def cupload():


         #categories=request.form['id']
         id=request.args.get('id')




         return render_template("cupload.html", data=id)

@app.route("/ccupload", methods=['GET', 'POST'])
def ccupload():
    if request.method == 'POST':

        id = request.form['id']

        file = request.files['file']
        file.save("static/upload/" + file.filename)
        conn = mysql.connector.connect(user='root', password='', host='localhost', database='empcomp')
        cursor = conn.cursor()
        cursor.execute(
            "update complaint set urate='" + file.filename + "' where id='" + id + "'")
        conn.commit()
        conn.close()
        return render_template('view1.html')
@app.route("/dwnd")
def dwnd():


         #categories=request.form['id']
         id=request.args.get('id')
         print(id)
         path = 'static/upload/' + str(id)
         return send_file(path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)