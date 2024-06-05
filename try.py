import pandas as pd
import json
import numpy as np
import random
import os

from flask import Flask, render_template, request, jsonify,g,session
app = Flask(__name__)

global flag




@app.route('/')
def index():
    return render_template('index.html')
@app.route('/default')
def default():
    return render_template('default.html')

@app.route('/polarArea')
def polarArea():
    if os.path.exists('C:/Users/siddhanta/PycharmProjects/EduViz/adm_data.csv'):
        admission_df = pd.read_csv('adm_data.csv', index_col=0)
        column_names = list(admission_df.columns)
    else:
        return 'No file provided', 400


    sub_data = []
    label_list=[]
    for column in admission_df.columns:
        numeric_column = pd.to_numeric(admission_df[column], errors='coerce')
        if numeric_column.notna().all():
            label_list.append(column)
            total = sum(admission_df[column])
            length = len(admission_df[column])
            average = total / length
            sub_data.append(average)
    final_list = [{
        'label': "d1",
        'data': list(sub_data)
    }]
    # print(column_names)
    # print(final_list)

    return render_template('New_polarArea.html',labels=label_list,datasets=final_list)




@app.route('/floatBar')
def floatBar():
    if os.path.exists('C:/Users/siddhanta/PycharmProjects/EduViz/adm_data.csv'):
        admission_df = pd.read_csv('adm_data.csv', index_col=0)
        column_names = list(admission_df.columns)
    else:
        return 'No file provided', 400
    final_list=[]
    for column in admission_df.columns:
        numeric_column = pd.to_numeric(admission_df[column], errors='coerce')
        if numeric_column.notna().all():
            sub_data = [min(admission_df[column]),max(admission_df[column])]
            final_list.append({
                'label': column,
                'data': sub_data
            })
    print(column_names)
    print(final_list)

    return render_template('New_floatingBar.html',labels=['Average'],datasets=final_list)



@app.route('/horizontalBarChart')
def horizontalBarChart():
    if os.path.exists('C:/Users/siddhanta/PycharmProjects/EduViz/adm_data.csv'):
        admission_df = pd.read_csv('adm_data.csv', index_col=0)
        column_names = list(admission_df.columns)
    else:
        return 'No file provided', 400
    datasets = []
    # for column in admission_df.columns:
    #     dataset = {
    #         'label': column,
    #         'data': list(admission_df[column])
    #     }
    #     datasets.append(dataset)
    # final_list = datasets
    # print(final_list)
    sub_data = []
    for column in admission_df.columns:
        numeric_column = pd.to_numeric(admission_df[column], errors='coerce')
        if numeric_column.notna().all():
            total = sum(admission_df[column])
            length = len(admission_df[column])
            average = total / length
            sub_data.append(average)
    final_list = [{
        'label': list(admission_df.columns),
        'data': list(sub_data)
    }]
    print(final_list)

    return render_template('New_horizontalBarChart.html',labels=column_names,datasets=final_list)





@app.route('/multiAxis')
def multiAxis():
    if os.path.exists('C:/Users/siddhanta/PycharmProjects/EduViz/adm_data.csv'):
        admission_df = pd.read_csv('adm_data.csv', index_col=0)
        column_names = list(admission_df.columns)
    else:
        return 'No file provided', 400
    datasets = []
    c=1
    for column in admission_df.columns:
        numeric_column = pd.to_numeric(admission_df[column], errors='coerce')
        if numeric_column.notna().all():
            id='y'+str(c)
            dataset = {
                'label': column,
                'data': list(admission_df[column]),
                'yAxisID': id
            }
            datasets.append(dataset)
            c+=1
    final_list = datasets
    print(final_list)

    return render_template('New_multiAxis.html',labels=[1,2,3,4,5,6,7,8,9,10],datasets=final_list)





@app.route('/donught')
def donught():
    if os.path.exists('C:/Users/siddhanta/PycharmProjects/EduViz/adm_data.csv'):
        admission_df = pd.read_csv('adm_data.csv', index_col=0)
        column_names = list(admission_df.columns)
    else:
        return 'No file provided', 400
    datasets = []
    sub_data=[]
    label_list=[]
    for column in admission_df.columns:
        numeric_column = pd.to_numeric(admission_df[column], errors='coerce')
        if numeric_column.notna().all():
            total=sum(admission_df[column])
            length=len(admission_df[column])
            average=total/length
            sub_data.append(average)
            label_list.append(column)
    final_list = [{
        'label': 'AverageSet',
        'data': sub_data
    }]
    print(final_list)

    return render_template('New_donught.html',labels=label_list,datasets=final_list)



@app.route('/pieChart')
def pieChart():
    if os.path.exists('C:/Users/siddhanta/PycharmProjects/EduViz/adm_data.csv'):
        admission_df = pd.read_csv('adm_data.csv', index_col=0)
        column_names = list(admission_df.columns)
    else:
        return 'No file provided', 400
    datasets = []
    sub_data=[]
    ll=[]
    for column in admission_df.columns:
        numeric_column = pd.to_numeric(admission_df[column], errors='coerce')
        if numeric_column.notna().all():
            total=sum(admission_df[column])
            length=len(admission_df[column])
            average=total/length
            sub_data.append(average)
            ll.append(column)
    final_list = [{
        'label':"AverageSet",
        'data': list(sub_data)
    }]
    print(final_list)

    return render_template('New_pieChart.html',labels=ll,datasets=final_list)




@app.route('/lineChartDataset')
def lineChartDataset():
    if os.path.exists('C:/Users/siddhanta/PycharmProjects/EduViz/adm_data.csv'):
        admission_df = pd.read_csv('adm_data.csv', index_col=0)
        column_names = list(admission_df.columns)
    else:
        return 'No file provided', 400
    final_list=[]
    admission_df = pd.read_csv('adm_data.csv')
    num_rows_per_part = len(admission_df) // 9
    divided_parts = []
    for i in range(9):
        start_index = i * num_rows_per_part
        end_index = (i + 1) * num_rows_per_part
        part = admission_df.iloc[start_index:end_index]
        divided_parts.append(part)
    if len(admission_df) % 9 != 0:
        last_part = admission_df.iloc[end_index:]
        divided_parts.append(last_part)
    part_averages = []

    for part in divided_parts:
        numeric_cols = part.apply(lambda col: pd.to_numeric(col, errors='coerce').notna().all())
        part_mean = part.loc[:, numeric_cols].mean()
        part_averages.append(part_mean)
    label_list= numeric_cols[numeric_cols].index.tolist()
    all_subpart_lists = [part_avg.to_list() for part_avg in part_averages]
    print(len(all_subpart_lists), len(label_list))
    p=1
    for i in range(len(all_subpart_lists)):
        x="d"+str(p)
        d={
        'label': x,
        'data': all_subpart_lists[i],
        'fill':random.randint(-1,6)
        }
        final_list.append(d)
        p+=1
    print(final_list)

    return render_template('New_lineChartDataset.html',labels=[1,2,3,4,5,6,7,8,9],datasets=final_list)

@app.route('/upload', methods=['POST'])
def upload():
    flag=0
    if 'file' in request.files:
        file = request.files['file']
        # Rename the file as 'amd_data.csv'
        file.filename = 'adm_data.csv'
        # Specify your desired location to save the file
        file_path = os.path.join('C:/Users/siddhanta/PycharmProjects/EduViz', file.filename)
        if os.path.exists(file_path):
            os.remove(file_path)
        file.save(file_path)
        flag=1
        return 'uploaded successfully',200
    else:
        return 'No file provided', 400



if __name__ == '__main__':
    app.run(debug=True)











