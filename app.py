import configparser
import json
from data_utils import *
from flask import Flask, render_template, request, redirect, Response, jsonify


app = Flask(__name__)


@app.route("/home", methods=['POST', 'GET'])
def index():

    return render_template('index1.html')


@app.route("/maps", methods=['POST', 'GET'])
def data_maps():
    """
        Regional Content / Maps page
    """
    config = configparser.ConfigParser()
    config.read('config.ini')
    real_estate_dataset = config['DATA']['INPUT_CSV_1']
    #df = prepare_data(real_estate_dataset)
    df = pd.read_csv('data/parcoord_state_group.csv', encoding='latin-1')
    data = get_rent_mean_per_state(df)
    data = {'init_data': data}
    return render_template('index.html', data=data)


@app.route("/radar_chart", methods=['POST', 'GET'])
def radar_chart():
    """
        Regional Content / Maps page
    """
    config = configparser.ConfigParser()
    config.read('config.ini')
    real_estate_dataset = config['DATA']['INPUT_CSV_1']
    #df = prepare_data(real_estate_dataset)
    df = pd.read_csv('data/parcoord_state_group.csv', encoding='latin-1')
    data = get_rent_mean_per_state(df)
    data = {'init_data': data}
    return render_template('radar_chart.html', data=data)


@app.route("/corr_heat_map", methods=['POST', 'GET'])
def corr_heat_map():
    """
        Regional Content / Maps page
    """
    config = configparser.ConfigParser()
    config.read('config.ini')
    real_estate_dataset = config['DATA']['INPUT_CSV_1']
    #df = prepare_data(real_estate_dataset)
    df = pd.read_csv('data/parcoord_state_group.csv', encoding='latin-1')
    data = get_rent_mean_per_state(df)
    data = {'init_data': data}
    return render_template('heat_map.html', data=data)


@app.route("/scatterplot", methods=['POST', 'GET'])
def scatterplot():
    """
        Regional Content / Maps page
    """
    config = configparser.ConfigParser()
    config.read('config.ini')
    real_estate_dataset = config['DATA']['INPUT_CSV_1']
    #df = prepare_data(real_estate_dataset)
    df = pd.read_csv('data/parcoord_state_group.csv', encoding='latin-1')
    data = get_rent_mean_per_state(df)
    data = {'init_data': data}
    return render_template('scatterplot.html', data=data)


@app.route("/par_coord", methods=['POST', 'GET'])
def par_coord():
    """
        Regional Content / Maps page
    """
    config = configparser.ConfigParser()
    config.read('config.ini')
    real_estate_dataset = config['DATA']['INPUT_CSV_1']
    #df = prepare_data(real_estate_dataset)
    df = pd.read_csv('data/parcoord_state_group.csv', encoding='latin-1')
    data = get_rent_mean_per_state(df)
    data = {'init_data': data}
    return render_template('par_coord.html', data=data)


@app.route("/percent_circles", methods=['POST', 'GET'])
def percent_circles():
    """
        Regional Content / Maps page
    """
    config = configparser.ConfigParser()
    config.read('config.ini')
    real_estate_dataset = config['DATA']['INPUT_CSV_1']
    #df = prepare_data(real_estate  _dataset)
    df = pd.read_csv('data/parcoord_state_group.csv', encoding='latin-1')
    data = get_rent_mean_per_state(df)
    data = {'init_data': data}
    return render_template('percent_circles.html', data=data)


if __name__ == "__main__":
    app.run(debug=True)