import streamlit as st

def show():
    st.sidebar.image("https://i.imgur.com/xbwZCPR.gif", use_column_width=True)
    st.markdown("<h1 style='color: #F51506;'>Welcome to ScanTec!</h1>", unsafe_allow_html=True)
    st.subheader("Revolutionizing the way you scan")

    # Display the PNG image
    image_path = "han.png"  # Replace with your PNG image path
    st.image(image_path, caption="Advanced scan using SCANTEC",width=450)



    st.write("""
       ScanTec is a new medical diagnostic system that combines two functionalities: fracture detection in X-ray images and pathology report interpretation. It utilizes existing technologies like deep learning and OCR to automate tasks and improve efficiency and accuracy in medical diagnosis.

       Here are the key strengths of ScanTec:

       - Integrates existing technologies for a unified platform.
       - Leverages widely available tools for scalability and implementation across various healthcare settings.
       - Provides a comprehensive approach to diagnostics by combining fracture detection and pathology report analysis.
       - Enhances accuracy and efficiency in diagnosis leading to better patient outcomes.
       - Aligns with the trend of precision medicine and patient-centered care.
    """)

    # Add some text for the heading and description
    st.header("Pathology with OCR Method")
    image_path = "path.png"  # Replace with your image path
    st.image(image_path, caption="This is a sample image", width=450)


    st.write("""
    **Introduction to OCR in Pathology**

    Optical Character Recognition (OCR) is a pivotal technology in modern pathology, enabling the digital conversion of printed or handwritten text from medical documents into machine-readable data. This method streamlines the analysis and storage of vast amounts of medical records, enhancing the efficiency and accuracy of diagnostics and research.

    **How OCR Enhances Pathology**

    1. **Efficient Data Management**: OCR automates the extraction of text from pathology reports, eliminating manual data entry and reducing the risk of errors.
    2. **Improved Access to Information**: Digital text can be easily searched, categorized, and retrieved, facilitating quick access to patient histories and pathology findings.
    3. **Enhanced Research Capabilities**: By converting historical medical documents into digital formats, OCR supports large-scale data analysis and research, leading to better understanding and advancements in medical science.
    4. **Integration with Electronic Health Records (EHRs)**: OCR seamlessly integrates with EHR systems, ensuring that pathology results are accurately recorded and accessible within a patient's comprehensive medical profile.

             
    """)
    # Add some text for the heading and description
    st.header("X-ray Analysis with Machine Learning")

    image_path = "xray.png"  # Replace with your image path
    st.image(image_path, caption="This is a sample image", width=450)

    st.write("""
    **Introduction to Machine Learning in X-ray Analysis**

    Machine learning (ML) is revolutionizing the field of radiology, especially in the analysis of X-ray images. ML algorithms can process vast amounts of data, identify patterns, and make predictions, significantly enhancing the accuracy and efficiency of diagnostics.

    **How Machine Learning Enhances X-ray Analysis**

    1. **Automated Image Interpretation**: ML models can analyze X-ray images to detect abnormalities such as fractures, tumors, or infections, reducing the burden on radiologists and speeding up the diagnostic process.
    2. **Improved Diagnostic Accuracy**: By training on large datasets of X-ray images, ML algorithms can achieve high levels of accuracy, often surpassing human performance in identifying certain conditions.
    3. **Predictive Analytics**: ML can predict patient outcomes based on historical data, helping doctors make informed decisions about treatment plans and prognoses.
    4. **Integration with Clinical Workflows**: ML tools can be integrated into existing radiology systems, providing real-time assistance to radiologists and ensuring that X-ray analyses are comprehensive and accurate.

    """)

if __name__ == "__main__":
    show()
