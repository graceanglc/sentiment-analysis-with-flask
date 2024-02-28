import sqlite3
from flask import Flask, render_template, request, url_for, redirect, jsonify
from nltk.sentiment.vader import SentimentIntensityAnalyzer

from forms import SubmitFeedbackForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '3d276e7b-4e39-43ba-b3d1-0e687c798c72'

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

def serialize_feedback(row):
    return {
        'id': row['id'],
        'feedback_text': row['feedback_text'],
        'sentiment_result': row['sentiment_result']
    }

@app.route('/', methods=['GET'])
def index():
    conn = get_db_connection()
    cursor = reversed(list(conn.execute('SELECT * FROM Feedback').fetchall()))
    list_feedback = [serialize_feedback(row) for row in cursor]
    conn.close()
    return render_template('index.html', list_feedback=list_feedback)

@app.route('/filteredfeedback', methods=['GET'])
def get_filtered_feedback():
    sentiment = request.args.get('sentiment')
    conn = get_db_connection()
    cursor = conn.cursor()
    if sentiment and sentiment in ['Positive', 'Negative', 'Neutral']:
        cursor.execute('SELECT * FROM Feedback WHERE sentiment_result = ?', (sentiment,))
    else:
        cursor.execute('SELECT * FROM Feedback')
    filtered_feedback = [serialize_feedback(row) for row in reversed(cursor.fetchall())]
    conn.close()
    return render_template('index.html', list_feedback=filtered_feedback)

def get_sentiment_result(feedback_text):
    sentiment_analyzer = SentimentIntensityAnalyzer()
    sentiment_score = sentiment_analyzer.polarity_scores(feedback_text)
    sentiment_result = 'Neutral'
    if sentiment_score['compound'] >= 0.05:
        sentiment_result = 'Positive'
    elif sentiment_score['compound'] <= -0.05:
        sentiment_result = 'Negative'
    return sentiment_result

@app.route('/submitfeedback/', methods=('POST','GET'))
def submitfeedback():
    form = SubmitFeedbackForm(request.form)
    if request.method == "POST" and form.validate():
        form.errors.clear()
        feedback_text = form.feedback_text.data
        # Check if feedback_text meets length requirements
        if feedback_text is None or len(feedback_text) < 2 or len(feedback_text) > 1000:
            return jsonify({'error': 'Feedback text must be between 2 and 1000 characters.'}), 400
        sentiment_result = get_sentiment_result(feedback_text)
        conn = get_db_connection()
        conn.execute('INSERT INTO Feedback (feedback_text, sentiment_result) VALUES (?, ?)',
                        (feedback_text, sentiment_result))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))

    return render_template('submitfeedback.html', form=form, message='Feedback submitted successfully.')

if __name__ == '__main__':
    app.run(debug=True)