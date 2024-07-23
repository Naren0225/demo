# import streamlit as st

# def show():
#     st.sidebar.image("https://i.imgur.com/xbwZCPR.gif", use_column_width=True)
#     st.title("About Page")
#     st.write("Welcome to the About Page!")
    
# if __name__ == "__main__":
#     show()

import streamlit as st

def show():
    st.sidebar.image("https://i.imgur.com/xbwZCPR.gif", use_column_width=True)
    
    # HTML and CSS for the images with background
    st.markdown("""
        <style>
        .image-container {
            display: flex;
            justify-content: space-around;
        }
        .background {
            background-color: #f0f0f0;  /* Change this to the desired background color */
            padding: 20px;
            border-radius: 10px;
            display: inline-block;
        }
        .background img {
            border-radius: 10px;
        }
        </style>
        <div class="image-container">
            <div class="background">
                <img src="https://i.imgur.com/xbwZCPR.gif" width="300">
            </div>
            <div class="background">
                <img src="https://i.imgur.com/xbwZCPR.gif" width="300">
            </div>
        </div>
    """, unsafe_allow_html=True)

    
if __name__ == "__main__":
    show()
