import streamlit as st
from PIL import Image

# Load images
weights_comparison_img = Image.open('results/plots/weights_comparison.png')
original_conf_matrix_img = Image.open('results/plots/original_model_confusion_matrix.png')
finetuned_conf_matrix_img = Image.open('results/plots/fine-tuned_model_confusion_matrix.png')

# Set page configuration
st.set_page_config(page_title="Model Comparison", layout="wide")

# CSS for animated gradient background
st.markdown(
    """
    <style>
    body {
        background: linear-gradient(45deg, #ff6b6b, #f06595, #cc5de8, #845ef7, #5c7cfa, #339af0, #22b8cf, #20c997, #51cf66, #94d82d, #fcc419, #ff922b, #ff6b6b);
        background-size: 400% 400%;
        animation: gradientBackground 15s ease infinite;
    }
    @keyframes gradientBackground {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Streamlit page layout
st.title("Model Comparison: Original vs Fine-Tuned")

st.header("Weights Comparison")
st.image(weights_comparison_img, caption='Comparison of Model Weights')

st.header("Confusion Matrices")
col1, col2 = st.columns(2)

with col1:
    st.subheader("Original Model")
    st.image(original_conf_matrix_img, caption='Original Model Confusion Matrix')

with col2:
    st.subheader("Fine-Tuned Model")
    st.image(finetuned_conf_matrix_img, caption='Fine-Tuned Model Confusion Matrix')
