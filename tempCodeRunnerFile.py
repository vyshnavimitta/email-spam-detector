import streamlit as st
import joblib

# Load the trained model
model = joblib.load('spam_detector_model.pkl')

# Set up the Streamlit app
st.title("📧 Email Spam Detector")
st.write("This app predicts whether an email is spam or ham (not spam) using a machine learning model.")

# Input text area for email
email_text = st.text_area("Enter the email text:", height=200)

if st.button("Check Spam"):
    if email_text:
        # Make prediction
        prediction = model.predict([email_text])
        
        # Display result
        if prediction[0] == 1:
            st.error("🚨 This email is classified as SPAM!")
        else:
            st.success("✅ This email is classified as HAM (not spam)!")
    else:
        st.warning("Please enter some text to analyze.")

# Add some information about the app
st.markdown("---")
st.markdown("""
### About
- This model uses a Naive Bayes classifier with CountVectorizer
- Trained on a dataset of 5572 emails
- Achieves ~98% accuracy in spam detection
""")