import streamlit as st

def show():
    st.sidebar.image("https://i.imgur.com/xbwZCPR.gif", use_column_width=True)
    st.title("Welcome to Pathology Page ⚕️")
   

    # Upload a document
    uploaded_file = st.file_uploader("Upload a document", type=["pdf", "docx", "txt"])

    if uploaded_file is not None:
        # Process the uploaded file
        st.write("File uploaded successfully!")
        file_details = {"Filename": uploaded_file.name, "FileType": uploaded_file.type, "FileSize": uploaded_file.size}
        st.write(file_details)

if __name__ == "__main__":
    show()