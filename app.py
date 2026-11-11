import streamlit as st
import pickle
import numpy as np
import sklearn


st.title('employee-attritions')

age = st.number_input("Age", min_value=None, max_value=None,
                 value="min", step = 1, format=None, key=None, help=None, on_change="rerun", args=None,
                   kwargs=None, placeholder=None, disabled=False, required=False, label_visibility="visible",
                 icon=None, width="stretch", bind=None, persist_state=None)

Gender = st.number_input("Gender", min_value = 0, max_value = 1,
                 value="min", step = 1, format=None, key=None, help=None, on_change="rerun", args=None,
                   kwargs=None, placeholder=None, disabled=False, required=False, label_visibility="visible",
                 icon=None, width="stretch", bind=None, persist_state=None)

Marital_Status = st.number_input("Marital_Status", min_value=None, max_value=None,
                 value="min", step=None, format=None, key=None, help=None, on_change="rerun", args=None,
                   kwargs=None, placeholder=None, disabled=False, required=False, label_visibility="visible",
                 icon=None, width="stretch", bind=None, persist_state=None)

Department = st.number_input("Department", min_value=None, max_value=None,
                 value="min", step=None, format=None, key=None, help=None, on_change="rerun", args=None,
                   kwargs=None, placeholder=None, disabled=False, required=False, label_visibility="visible",
                 icon=None, width="stretch", bind=None, persist_state=None)

Job_Role = st.number_input("Job_Role", min_value=None, max_value=None,
                 value="min", step=None, format=None, key=None, help=None, on_change="rerun", args=None,
                   kwargs=None, placeholder=None, disabled=False, required=False, label_visibility="visible",
                 icon=None, width="stretch", bind=None, persist_state=None)

Job_Level = st.number_input("Job_Level", min_value=None, max_value=None,
                 value="min", step=None, format=None, key=None, help=None, on_change="rerun", args=None,
                   kwargs=None, placeholder=None, disabled=False, required=False, label_visibility="visible",
                 icon=None, width="stretch", bind=None, persist_state=None)

Monthly_Income = st.number_input("Monthly_Income", min_value=None, max_value=None,
                 value="min", step=None, format=None, key=None, help=None, on_change="rerun", args=None,
                   kwargs=None, placeholder=None, disabled=False, required=False, label_visibility="visible",
                 icon=None, width="stretch", bind=None, persist_state=None)


Hourly_Rate = st.number_input("Hourly_Rate", min_value=None, max_value=None,
                 value="min", step=None, format=None, key=None, help=None, on_change="rerun", args=None,
                   kwargs=None, placeholder=None, disabled=False, required=False, label_visibility="visible",
                 icon=None, width="stretch", bind=None, persist_state=None)



Years_at_Company = st.number_input("Years_at_Company", min_value=None, max_value=None,
                 value="min", step=None, format=None, key=None, help=None, on_change="rerun", args=None,
                   kwargs=None, placeholder=None, disabled=False, required=False, label_visibility="visible",
                 icon=None, width="stretch", bind=None, persist_state=None)



Years_in_Current_Role = st.number_input("Years_in_Current_Role", min_value=None, max_value=None,
                 value="min", step=None, format=None, key=None, help=None, on_change="rerun", args=None,
                   kwargs=None, placeholder=None, disabled=False, required=False, label_visibility="visible",
                 icon=None, width="stretch", bind=None, persist_state=None)


Years_Since_Last_Promotion = st.number_input("Years_Since_Last_Promotion", min_value=None, max_value=None,
                 value="min", step=None, format=None, key=None, help=None, on_change="rerun", args=None,
                   kwargs=None, placeholder=None, disabled=False, required=False, label_visibility="visible",
                 icon=None, width="stretch", bind=None, persist_state=None)


Work_Life_Balance = st.number_input("Work_Life_Balance", min_value=None, max_value=None,
                 value="min", step=None, format=None, key=None, help=None, on_change="rerun", args=None,
                   kwargs=None, placeholder=None, disabled=False, required=False, label_visibility="visible",
                 icon=None, width="stretch", bind=None, persist_state=None)


Job_Satisfaction = st.number_input("Job_Satisfaction", min_value=None, max_value=None,
                 value="min", step=None, format=None, key=None, help=None, on_change="rerun", args=None,
                   kwargs=None, placeholder=None, disabled=False, required=False, label_visibility="visible",
                 icon=None, width="stretch", bind=None, persist_state=None)


Performance_Rating = st.number_input("Performance_Rating", min_value=None, max_value=None,
                 value="min", step=None, format=None, key=None, help=None, on_change="rerun", args=None,
                   kwargs=None, placeholder=None, disabled=False, required=False, label_visibility="visible",
                 icon=None, width="stretch", bind=None, persist_state=None)


Training_Hours_Last_Year = st.number_input("Training_Hours_Last_Year", min_value=None, max_value=None,
                 value="min", step=None, format=None, key=None, help=None, on_change="rerun", args=None,
                   kwargs=None, placeholder=None, disabled=False, required=False, label_visibility="visible",
                 icon=None, width="stretch", bind=None, persist_state=None)


Overtime = st.number_input("Overtime", min_value=None, max_value=None,
                 value="min", step=None, format=None, key=None, help=None, on_change="rerun", args=None,
                   kwargs=None, placeholder=None, disabled=False, required=False, label_visibility="visible",
                 icon=None, width="stretch", bind=None, persist_state=None)


Project_Count = st.number_input("Project_Count", min_value=None, max_value=None,
                 value="min", step=None, format=None, key=None, help=None, on_change="rerun", args=None,
                   kwargs=None, placeholder=None, disabled=False, required=False, label_visibility="visible",
                 icon=None, width="stretch", bind=None, persist_state=None)


Average_Hours_Worked_Per_Week = st.number_input("Average_Hours_Worked_Per_Week", min_value=None, max_value=None,
                 value="min", step=None, format=None, key=None, help=None, on_change="rerun", args=None,
                   kwargs=None, placeholder=None, disabled=False, required=False, label_visibility="visible",
                 icon=None, width="stretch", bind=None, persist_state=None)


Absenteeism = st.number_input("Absenteeism", min_value=None, max_value=None,
                 value="min", step=None, format=None, key=None, help=None, on_change="rerun", args=None,
                   kwargs=None, placeholder=None, disabled=False, required=False, label_visibility="visible",
                 icon=None, width="stretch", bind=None, persist_state=None)

Work_Environment_Satisfaction = st.number_input("Work_Environment_Satisfaction", min_value=None, max_value=None,
                 value="min", step=None, format=None, key=None, help=None, on_change="rerun", args=None,
                   kwargs=None, placeholder=None, disabled=False, required=False, label_visibility="visible",
                 icon=None, width="stretch", bind=None, persist_state=None)

Relationship_with_Manager = st.number_input("Relationship_with_Manager", min_value=None, max_value=None,
                 value="min", step=None, format=None, key=None, help=None, on_change="rerun", args=None,
                   kwargs=None, placeholder=None, disabled=False, required=False, label_visibility="visible",
                 icon=None, width="stretch", bind=None, persist_state=None)


Job_Involvement = st.number_input("Job_Involvement", min_value=None, max_value=None,
                 value="min", step=None, format=None, key=None, help=None, on_change="rerun", args=None,
                   kwargs=None, placeholder=None, disabled=False, required=False, label_visibility="visible",
                 icon=None, width="stretch", bind=None, persist_state=None)


Distance_From_Home = st.number_input("Distance_From_Home", min_value=None, max_value=None,
                 value="min", step=None, format=None, key=None, help=None, on_change="rerun", args=None,
                   kwargs=None, placeholder=None, disabled=False, required=False, label_visibility="visible",
                 icon=None, width="stretch", bind=None, persist_state=None)


Number_of_Companies_Worked = st.number_input("Number_of_Companies_Worked", min_value=None, max_value=None,
                 value="min", step=None, format=None, key=None, help=None, on_change="rerun", args=None,
                   kwargs=None, placeholder=None, disabled=False, required=False, label_visibility="visible",
                 icon=None, width="stretch", bind=None, persist_state=None)


a = np.array([age, Gender,Marital_Status,
              Department,
              Job_Role,
              Job_Level,	
              Monthly_Income,
              Hourly_Rate,	
              Years_at_Company,	
              Years_in_Current_Role,
              Years_Since_Last_Promotion,
              Work_Life_Balance,
              Job_Satisfaction,
              Performance_Rating,
              Training_Hours_Last_Year,
              Overtime,
              Project_Count,
              Average_Hours_Worked_Per_Week,
              Absenteeism,
              Work_Environment_Satisfaction,
              Relationship_with_Manager,
              Job_Involvement,
              Distance_From_Home,
              Number_of_Companies_Worked], ndmin = 2)


with open('clsf.pkl','rb') as f:
    model = pickle.load(f)


if st.button('predict', key=None, help=None, on_click=None, args=None, 
             kwargs=None, type="secondary", icon=None, icon_position="left", 
             disabled=False, use_container_width=None, width="content", shortcut=None, wrap=None):
    predicted = model.predict(a)

    if predicted == np.array([0]):
      st.markdown("The employee is likely to stay")
    else:
      st.markdown("The employee is likely to leave")
    