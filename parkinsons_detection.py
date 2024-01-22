import numpy as np
import pickle
import streamlit as st


loaded_model=pickle.load(open('trained_modell.pkl', 'rb'))


def parkinson_prediction(input_data):
    

    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)
 

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0] == 0):
      return 'The Person does not have Parkinsons Disease'
    else:
      return 'The Person has Parkinsons'
  
    
  
def main():
    
    
    # giving a title
    st.title('Parkinson Prediction Web App')
    
    
    # getting the input data from the user
    
    
    MDVP_Fo_Hz = st.number_input('MDVP_Fo(Hz)')
    MDVP_Fhi_Hz= st.number_input('MDVP_Fhi(Hz)')
    MDVP_Flo_Hz= st.number_input('MDVP_Flo(Hz)')
    MDVP_Jitter_percentage= st.number_input('MDVP_Jitterpercentage')
    MDVP_Jitter_Abs= st.number_input('MDVP_Jitter(Abs)')
    Jitter_DDP=st.number_input('Jitter_DDP')
    MDVP_Shimmer= st.number_input('MDVP_Shimmer ')
    Shimmer_APQ3=st.number_input('Shimmer_APQ3')
    Shimmer_APQ5=st.number_input('Shimmer_APQ5')
    MDVP_APQ=st.number_input('MDVP_APQ')
    Shimmer_DDA=st.number_input(' Shimmer_DDA')
    NHR=st.number_input(' NHR ')
    HNR= st.number_input('HNR')
    RPDE=st.number_input(' RPDE ')
    DFA=st.number_input(' DFA ')
    spread1 = st.number_input(' spread1 ')
    spread2 = st.number_input(' spread2 ')
    D2=st.number_input(' D2')
   
   
              
    
    
    # code for Prediction
    diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Parkinsons Test Result'):
        diagnosis = parkinson_prediction([[MDVP_Fo_Hz,MDVP_Fhi_Hz,MDVP_Flo_Hz,MDVP_Jitter_percentage,MDVP_Jitter_Abs,Jitter_DDP,MDVP_Shimmer,Shimmer_APQ3,Shimmer_APQ5,MDVP_APQ,Shimmer_DDA,NHR,HNR ,RPDE,DFA,spread1,spread2,D2]])
        
        
    st.success(diagnosis)
    
    
    
    
    
if __name__ == '__main__':
    main()
