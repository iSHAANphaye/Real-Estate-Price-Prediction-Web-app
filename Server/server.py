# flask --app server run --debug

from flask import Flask, request, jsonify, render_template, send_from_directory
import util

app=Flask(__name__,template_folder=r'C:\Users\ishaan phaye\Desktop\VS Code\Data Science Projects\Real Estate Price Prediction\Real-Estate-Price-Prediction-Web-app\templates')

util.load_saved_artifacts()

@app.route('/static/<path:filename>')
def serve_static(filename):
    return send_from_directory('static', filename)

@app.route('/')
def starter():
    return render_template('app.html')

@app.route('/get_location_names')
def get_location_names():
    response=jsonify({
        'locations':util.get_location_names()
    })
    response.headers.add('Access-Control-Allow-Origin','*')
    
    return response

@app.route('/predict_home_price',methods=['POST'])
def predict_home_price():
    total_sqft = float(request.form['total_sqft'])
    location = request.form['location']
    bhk = int(request.form['bhk'])
    bath = int(request.form['bath'])

    response = jsonify({
        'estimated_price (in 10s lakhs)': util.get_estimated_price(location,total_sqft,bhk,bath)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

if __name__=='__main__':
    
    app.run(host='0.0.0.0',debug=True)
    app.run()