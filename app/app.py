from flask import Flask, render_template
# from data_processing import read_sensor_data, process_and_publish_data
from analysis_algorithms import process_soil_data, decision_support_system


from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    user_input = request.form.get('userInput')
    # Process the user input as needed (e.g., store in a variable)
    print(f'Received input: {user_input}')

    return f'Successfully received input: {user_input}'


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    moisture = float(request.form.get('moisture'))
    ph = float(request.form.get('ph'))
    nutrient = float(request.form.get('nutrient'))
    temperature = float(request.form.get('temperature'))
    # Process the user input as needed (e.g., store in a variable)
    user_input = process_soil_data(moisture,ph,nutrient,temperature) 
    # Redirect to the dashboard with the received input
    user_input = decision_support_system(user_input)
    print(user_input)
    return redirect(url_for('dashboard', user_input=user_input))


@app.route('/dashboard/<user_input>')
def dashboard(user_input):
    # Render the dashboard template with the received input
    return render_template('dashboard.html', decision=user_input)

# processed_data = process_soil_data(100,10,150.2,23)

# app = Flask(__name__)

# @app.route('/')
# def index():
#     # Read sensor data
#     # moisture, ph, nutrients, temperature, crop_health_data  
#     decision = decision_support_system(processed_data)

#     # Process and publish data
#     #  process_and_publish_data()
#     # decision_support_system()
#     # print(decision_support_system)
    
#     # Render the template with sensor data
#     return render_template('dashboard.html', decision=decision)
if __name__ == "__main__":
    app.run(debug=True)
