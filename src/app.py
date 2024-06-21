from flask import Flask, request, render_template
from model import Model

app = Flask(__name__)


# Method 1: Via HTML Form
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        form_input = dict(request.form)
        print(form_input)

        # Modified code
        account_id = form_input['account_id']
        has_internet_service = form_input['has_internet_service']
        internet_type = form_input['internet_type']
        has_unlimited_data = form_input['has_unlimited_data']
        has_multiple_lines = form_input['has_multiple_lines']
        contract_type = form_input['contract_type']
        paperless_billing = form_input['paperless_billing']
        payment_method = form_input['payment_method']
        city = form_input['city']
        stream_tv = form_input['stream_tv']
        stream_movie = form_input['stream_movie']
        gender = form_input['gender']
        senior_citizen = form_input['senior_citizen']

        model_inputs = [ account_id,
    has_internet_service,
    internet_type,
    has_unlimited_data,
    has_multiple_lines,
    contract_type,
    paperless_billing,
    payment_method,
    stream_tv,
    stream_movie,
    gender,
    senior_citizen,
    city]
        prediction = Model().predict(model_inputs)

        if prediction  == 1:
            prediction_label = 'Joined'
        elif prediction  == 2:
            prediction_label = 'Stayed'
        elif prediction  == 3:
            prediction_label = 'Churned'
        else:
            prediction_label = 'unknown'

        print(Model().predict(model_inputs)) 
        return render_template('index.html', prediction=prediction_label)

    return render_template('index.html')


# Method 2: Via POST API
@app.route('/api/predict', methods=['POST'])
def predict():
    request_data = request.get_json()
    print(request_data)

    return {'success': False}, 500


if __name__ == '__main__':
    app.run(debug=True)