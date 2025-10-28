import streamlit as st
from langchain.prompts import PromptTemplate
from langchain.llms import CTransformers

# =========================================================
# Function: getLLamaresponse
# Purpose : Generate a blog using the LLaMA 2 model based on
#           user inputs such as topic, length, and audience.
# =========================================================
def getLLamaresponse(input_text, no_words, blog_style):
    """
    Generates a blog post using the LLaMA 2 model based on user input.

    Parameters
    ----------
    input_text : str
        The main topic or theme of the blog.
    no_words : int
        Desired word count for the generated blog.
    blog_style : str
        The target audience or writing style for the blog (e.g., Researchers, Data Scientist, etc.)

    Returns
    -------
    str
        The generated blog content as a text string.
    """

    # -----------------------------------------------------
    # Step 1: Initialize the LLaMA 2 model
    # -----------------------------------------------------
    # - Using `CTransformers` allows running the model locally without API calls.
    # - The q8_0 quantized version is chosen to balance performance and efficiency.
    # - 'temperature' controls creativity; a lower value (0.01) ensures focused and factual output.
    # -----------------------------------------------------
    llm = CTransformers(
        model='models/llama-2-7b-chat.ggmlv3.q8_0.bin',
        model_type='llama',
        config={
            'max_new_tokens': 256,  # Limits output length to avoid overly long responses
            'temperature': 0.01     # Low temperature → deterministic and consistent output
        }
    )

    # -----------------------------------------------------
    # Step 2: Define the Prompt Template
    # -----------------------------------------------------
    # - Templates ensure consistent structure for prompts.
    # - Variables {blog_style}, {input_text}, and {no_words} are dynamically inserted.
    # -----------------------------------------------------
    template = """
    Write a blog for {blog_style} job profile for a topic {input_text}
    within {no_words} words.
    """

    prompt = PromptTemplate(
        input_variables=["blog_style", "input_text", "no_words"],
        template=template
    )

    # -----------------------------------------------------
    # Step 3: Generate the response
    # -----------------------------------------------------
    # - The formatted prompt is passed into the model.
    # - Response is then printed (for debugging) and returned.
    # -----------------------------------------------------
    response = llm(prompt.format(
        blog_style=blog_style,
        input_text=input_text,
        no_words=no_words
    ))

    print(response)  # Useful for console debugging
    return response


# =========================================================
# Streamlit App Configuration
# =========================================================
st.set_page_config(
    page_title="Generate Blogs",
    page_icon='🤖',
    layout='centered',
    initial_sidebar_state='collapsed'
)

# =========================================================
# Page Layout and User Inputs
# =========================================================
st.header("Generate Blogs 🤖")

# Prompt user for blog topic
input_text = st.text_input("Enter the Blog Topic")

# Create two columns for word count and audience type
col1, col2 = st.columns([5, 5])

with col1:
    no_words = st.text_input('Number of Words')

with col2:
    blog_style = st.selectbox(
        'Writing the blog for',
        ('Researchers', 'Data Scientist', 'Common People'),
        index=0
    )

# Submit button to generate content
submit = st.button("Generate")

# =========================================================
# Display Generated Response
# =========================================================
if submit:
    # When the user clicks 'Generate', the model produces a blog post
    st.write(getLLamaresponse(input_text, no_words, blog_style))
