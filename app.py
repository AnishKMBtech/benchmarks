import streamlit as st
from PIL import Image

# Load images
weights_comparison_img = Image.open('results/plots/weights_comparison.png')

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
In this post, we will analyze the differences in model weights.
""")

st.header("Weights Comparison")
st.write("""
In this section, we compare the mean absolute weights of the parameters for both the original and fine-tuned models. 
The bar graph below illustrates how the fine-tuning process has affected the model parameters. Although the differences are minor, they provide insights into the impact of fine-tuning.
""")
st.image(weights_comparison_img, caption='Comparison of Model Weights')

st.header("Conclusion")
st.write("""
In this blog post, we have compared the original and fine-tuned GPT-Neo models by analyzing their weights. 
The fine-tuning process has led to minor changes in the model parameters, as seen in the weights comparison.
By understanding these differences, we can make informed decisions about which model to use for specific tasks.
""")

st.header("About the Author")
st.write("""
This blog post was created as part of a project to benchmark the performance of language models. 
For more information, please visit the [project repository](https://github.com/AnishKMBtech).
""")
