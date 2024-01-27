import streamlit as st
import requests
import json


st.title("DialogSum:")
st.caption('Developer Name: **Prajwal S Yallur**')
st.caption('Developer Email: prajjusy@gmail.com')
st.header('A Dialogue Summarization Tool')



dialog_file = st.file_uploader("Upload a Dialogue file", type=["json"])

if st.button("Summarize") and dialog_file is not None:

    # Read the dialog from the file
    dialog = json.load(dialog_file)

    # Display the dialog to the user
    st.subheader("**JSON File Contents:**")
    st.json(dialog)
    st.markdown("\n\n\n\n\n")

    # Display the dialog to the user
    dialog["dialouge_formatted"] = dialog["dialouge"]
    dialog["dialouge_formatted"] = dialog["dialouge_formatted"].replace("\n", "\n\n")
    dialog["dialouge_formatted"] = dialog["dialouge_formatted"].replace("#Person1#", "**Person 1**")
    dialog["dialouge_formatted"] = dialog["dialouge_formatted"].replace("#Person2#", "**Person 2**")

    st.subheader("**Dialogue:**")
    st.markdown(dialog["dialouge_formatted"])
    st.markdown("\n\n\n\n\n")

    # Summarize the dialog using the REST API
    # Send the dialog to the REST API
    # payload = {"dialog": dialog}
    payload = {"input_sentence": dialog["dialouge"]}
    # response = requests.post("http://127.0.0.1:8080/summarize_dialog", data=payload)
    response = requests.post("http://127.0.0.1:8080/get_sentiment", data=payload)

    # Get the summary from the response
    # summary = response.json()["summary"]

    # Display the summary to the user
    # st.write(summary)

    st.subheader("**Sentiment:**")
    st.json(response.text)
