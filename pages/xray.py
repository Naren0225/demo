import streamlit as st

def show():
    st.sidebar.image("https://i.imgur.com/xbwZCPR.gif", use_column_width=True)
    st.title("Welcome to the X-Ray Page 🩻")

    # Upload an X-Ray image
    uploaded_file = st.file_uploader("Upload an X-Ray image", type=["png", "jpg", "jpeg"])

    if uploaded_file is not None:
        # Display the uploaded image
        st.image(uploaded_file, caption="Uploaded X-Ray Image", use_column_width=True)
        st.write("File uploaded successfully!")
        file_details = {"Filename": uploaded_file.name, "FileType": uploaded_file.type, "FileSize": uploaded_file.size}
        st.write(file_details)

if __name__ == "__main__":
    show()
