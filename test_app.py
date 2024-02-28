import pytest
from app import app, get_sentiment_result

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_index(client):
    response = client.get('/')
    assert response.status_code == 200

def test_submit_feedback(client):
    data = {'feedback_text': 'This is a test feedback.'}
    response = client.post('/submitfeedback/', data=data, follow_redirects=True)
    assert response.status_code == 200

def test_submit_feedback_with_less_than_two_character(client):
    data = {'feedback_text': '.'}
    response = client.post('/submitfeedback/', data=data, follow_redirects=True)
    # Frontend also have validation for this, that's why it will never pass into 400 but loads the error message so it returns 200
    # But I tested without the frontend validation and the response is 400
    assert response.status_code == 200

def test_submit_feedback_with_more_than_one_thousand_character(client):
    data = {'feedback_text': 'Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim. Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu. In enim justo, rhoncus ut, imperdiet a, venenatis vitae, justo. Nullam dictum felis eu pede mollis pretium. Integer tincidunt. Cras dapibus. Vivamus elementum semper nisi. Aenean vulputate eleifend tellus. Aenean leo ligula, porttitor eu, consequat vitae, eleifend ac, enim. Aliquam lorem ante, dapibus in, viverra quis, feugiat a, tellus. Phasellus viverra nulla ut metus varius laoreet. Quisque rutrum. Aenean imperdiet. Etiam ultricies nisi vel augue. Curabitur ullamcorper ultricies nisi. Nam eget dui. Etiam rhoncus. Maecenas tempus, tellus eget condimentum rhoncus, sem quam semper libero, sit amet adipiscing sem neque sed ipsum. Nam quam nunc, blandit vel, luctus pulvinar, hendrerit id, lorem. Maecenas nec odio et ante tincidunt'}
    response = client.post('/submitfeedback/', data=data, follow_redirects=True)
    # Frontend also have validation for this, that's why it will never pass into 400 but loads the error message so it returns 200
    # But I tested without the frontend validation and the response is 400
    assert response.status_code == 200

def test_filtered_positive_feedback(client):
    response = client.get('/filteredfeedback?sentiment=Positive')
    assert response.status_code == 200

def test_filtered_negative_feedback(client):
    response = client.get('/filteredfeedback?sentiment=Negative')
    assert response.status_code == 200

def test_filtered_neutral_feedback(client):
    response = client.get('/filteredfeedback?sentiment=Neutral')
    assert response.status_code == 200

def test_filtered_feedback_with_random_string(client):
    response = client.get('/filteredfeedback?sentiment=www')
    assert response.status_code == 200

def test_filtered_feedback_with_empty_string(client):
    response = client.get('/filteredfeedback?sentiment=')
    assert response.status_code == 200

def test_sentiment_analysis_positive():
    feedback_text = "I love this product!"
    assert get_sentiment_result(feedback_text) == "Positive"

def test_sentiment_analysis_negative():
    feedback_text = "This product is terrible."
    assert get_sentiment_result(feedback_text) == "Negative"

def test_sentiment_analysis_neutral():
    feedback_text = "It's so so"
    assert get_sentiment_result(feedback_text) == "Neutral"

def test_sentiment_analysis_with_number():
    feedback_text = "123"
    assert get_sentiment_result(feedback_text) == "Neutral"
