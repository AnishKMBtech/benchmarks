import streamlit as st
from PIL import Image

# Load images
weights_comparison_img = Image.open('results/plots/weights_comparison.png')
original_conf_matrix_img = Image.open('results/plots/original_model_confusion_matrix.png')
finetuned_conf_matrix_img = Image.open('results/plots/fine-tuned_model_confusion_matrix.png')

# Set page configuration
st.set_page_config(page_title="Model Comparison Blog", layout="wide")

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
st.title("Model Comparison Blog: Original vs Fine-Tuned")

st.header("Introduction")
st.write("""
Welcome to this blog post where we compare the performance of two language models: the original GPT-Neo model and a fine-tuned version of the same model. 
In this post, we will analyze the differences in model weights and evaluate their performance using confusion matrices.
""")

st.header("Weights Comparison")
st.write("""
In this section, we compare the mean absolute weights of the parameters for both the original and fine-tuned models. 
The bar graph below illustrates how the fine-tuning process has affected the model parameters.
""")
st.image(weights_comparison_img, caption='Comparison of Model Weights')

st.header("Confusion Matrices")
st.write("""
The confusion matrices below provide a visual representation of the performance of both models on a sample dataset. 
These matrices show the number of correct and incorrect predictions made by each model, helping us understand their strengths and weaknesses.
""")
col1, col2 = st.columns(2)

with col1:
    st.subheader("Original Model")
    st.image(original_conf_matrix_img, caption='Original Model Confusion Matrix')

with col2:
    st.subheader("Fine-Tuned Model")
    st.image(finetuned_conf_matrix_img, caption='Fine-Tuned Model Confusion Matrix')

st.header("Conclusion")
st.write("""
In this blog post, we have compared the original and fine-tuned GPT-Neo models by analyzing their weights and performance on a sample dataset. 
The fine-tuning process has led to changes in the model parameters, as seen in the weights comparison, and has impacted the model's performance, as shown in the confusion matrices.
By understanding these differences, we can make informed decisions about which model to use for specific tasks.
""")

st.header("About the Author")
st.write("""
This blog post was created as part of a project to benchmark the performance of language models. 
For more information, please visit the [project repository](https://github.com/AnishKMBtech).
""")
