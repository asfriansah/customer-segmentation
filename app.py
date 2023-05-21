import streamlit as st
import pickle
import numpy as np

def main():
    background = """<div style = 'background-colour:black'; padding:13px>
                    <h2 style = 'text-align: center'>Customer Segmentation</h2>
                    </div>"""
    st.markdown(background, unsafe_allow_html=True)

    left, right = st.columns((2,2))
    gender = left.selectbox('Gender',('Male','Female'))
    marital = left.selectbox('Marital Status',('Single','Non-Single'))
    age = right.number_input('Age',0,100)
    education = left.selectbox('Education',('High School','University','Graduate','Others/Unknown'))
    income = right.number_input('Yearly Income ($K)',0,1000)
    occupation = left.selectbox('Occupation',('Unemployed/Unskilled','Skilled Employee/Official','Management/Self-employed/Highly Qualified Employed/Officer'))
    settle = right.selectbox('Settlement Size',('Small City','Mid-Size City','Big City'))
    button = st.button('Predict')

    if button:
        result = predict(gender,marital,age,education,income,occupation,settle)
        st.success(f'This type of customer is {result}')

st.markdown("""<style>
                    [data-testid=stSidebar] {
                        background-color: #b0a17f;
                    }
                </style>
                """, unsafe_allow_html=True)
with st.sidebar:
    st.subheader('About')
    desc = """<div style="text-align: justify;">
                    This is an application to predict the segmentation of customers based on their demographic 
                    profile. This application is based on data from visitors to a mall. 
                    Processed using the K-Means unsupervised learning algorithm model. 
                    The result is that customers are divided into 6 clusters.
              </div>
              <div style="text-align: justify;">
                    <ol>
                        <li>Cluster 0 : <b>Low-earning single men</b></li>
                        <li>Cluster 1 : <b>Low-earning non-single women</b></li>
                        <li>Cluster 2 : <b>High-earning non-single women</b></li>
                        <li>Cluster 3 : <b>High-earning single men</b></li>
                        <li>Cluster 4 : <b>Avarage-earning non-single men</b></li>
                        <li>Cluster 5 : <b>Low-earning single women</b></li>
                    </ol>
              </div>"""
    st.markdown(desc, unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1,6,1])
    with col1:
        st.write("")

    with col2:
        st.write("")

    with col3:
        st.write("")
    
    title_alignment = """<h4 style = 'text-align: center'>created 2023 by andri asfriansah</h4>"""
    st.markdown(title_alignment, unsafe_allow_html=True)

with open('model/segmentation.pkl','rb') as file:
    model = pickle.load(file)

def predict(gender,marital,age,education,income,occupation,settle):
    sex = 0 if gender == 'Male' else 1
    mar = 0 if marital == 'Single' else 1
    edu = 1 if education == 'High School' else 2 if education == 'University' else 3 if education == 'Graduate' else 0
    occu = 0 if occupation == 'Unemployed/Unskilled' else 1 if occupation == 'Skilled Employee/Official' else 2
    setle = 0 if settle == 'Small City' else 1 if occupation == 'Mid-Size City' else 2  
    inc = income * 1000

    predictor = np.array([sex,mar,int(age),edu,int(inc),occu,setle])
    predictor1 = predictor.reshape(1, -1) 
    predictor1 = predictor1.astype(int)
    #predictor_scal = scal.transform(predictor1)
    prediction = model.predict(predictor1)

    if prediction == 0:
        verdict = 'Low-earning single men'
    elif prediction == 1:
        verdict = 'Low-earning non-single women'
    elif prediction == 2:
        verdict = 'High-earning non-single women'
    elif prediction == 3:
        verdict = 'High-earning single men'
    elif prediction == 4:
        verdict = 'Avarage-earning non-single men'
    else:
        verdict = 'Low-earning single women'

    return verdict


if __name__ == "__main__":
    main()
