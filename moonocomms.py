import streamlit as st  # type: ignore
import io

import base64
#Making PDF file
def generate_pdf(name, platform, username, characters_total, character_sheet, color_type, background_info, reference_link, add_note):
    buffer = io.BytesIO()

    #Title
    c.setFont("Helvetica-Bold", 16)
    c.drawString(190, height - 50, "Mooncomms Order Request")

    #Monospaced font for alignment
    c.setFont("Helvetica", 12)

    #Starting position
    start_y = height - 100
    line_height = 20

    label_x = 50
    colon_x = 150
    value_x = 160

    for i, label in enumerate(["Commissioner Name", "Contact Info", "Characters Total", "Character Sheets", "Coloring Type", "Background Info", "Reference Link"]):
        c.drawString(label_x, start_y - i * line_height, label + " :")  

    #Aligned labels and data
    c.drawString(label_x, start_y,     "Commissioner Name   " + name)
    c.drawString(label_x, start_y - 1*line_height, "Contact Info   " + platform + " | " + username)
    c.drawString(label_x, start_y - 2*line_height, "Characters Total   " + str(characters_total))
    c.drawString(label_x, start_y - 3*line_height, "Character Sheets   " + character_sheet)
    c.drawString(label_x, start_y - 4*line_height, "Coloring Type   " + color_type)
    c.drawString(label_x, start_y - 5*line_height, "Background Info   " + background_info)
    c.drawString(label_x, start_y - 6*line_height, "Reference Link   " + reference_link)

    if add_note:
        c.drawString(label_x, start_y - 8*line_height, "Commission Note: " + add_note)

    c.showPage()
    c.save()
    buffer.seek(0)
    return buffer

#Title and layout of the website
st.set_page_config(page_title="Mooncommsite", page_icon=":crescent_moon:", layout="centered")
st.title("★☎️Welcome to Mooncommsite!")
st.write("── .✦This is Moono's commission online order. Please read the TOS before submitting! If you have any issue or question, please DM me on my social media platforms. Thank you (˶ˆᗜˆ˵)❤️")

#Input form
with st.form("my_form"):
    name_input=st.text_input("What's your name?*")
    platform=st.radio("What platform do you use?*", ("Discord", "Instagram"))
    usr_input=st.text_input("Where can I contact you?*")
    help_text="Please, provide your Discord username (e.g., User#1234) or Instagram username (e.g., @username)."
    st.markdown(f'<p style="font-size: 12px; color: gray;">{help_text}</p>', unsafe_allow_html=True)

    # Number picker
    number = st.number_input(
        label="How many characters would you like to order?*",
        min_value=1,          
        max_value=10,        
        value=1,             
        step=1,      
        format="%d" 
    )

    #Mutiple choice
    st.write("What body sheet type of commission would you like to order?*")
    multi_select_options = ["Full Body", "Half Body", "Headshot", "Tall Chibi", "Small Chibi"]
    multi_select = st.multiselect("Select one or more options:", multi_select_options)
    help_text_multi="*For small chibi notes: available only in flat colored style.*"
    st.markdown(f'<p style="font-size: 12px; color: orange ;">{help_text_multi}</p>', unsafe_allow_html=True)
    
    st.write("How do you want your commission to be colored?*")
    color_options = ["Full Rendered", "Flat Colored", "Lineart"]
    color_select = st.selectbox("Select coloring type:", color_options)

    st.write("Would you like to add a background for your commission?* _(Will cost extra)_")
    background_options = ["Yes", "No"]
    background_select = st.radio("Select an option:", background_options)

    #Submission link and note
    link_input=st.text_input("Link your character reference here:*")
    help_text_link="*Please link your character reference in google drive and do not forget to set it to 'Anyone with the link can view' (e.g., Google Drive).*"
    st.markdown(f'<p style="font-size: 12px; color: orange;">{help_text_link}</p>', unsafe_allow_html=True)

    note_input=st.text_area("Commission Note (Optional):")
    help_text_note="Write any additional information or special requests for your commission."
    st.markdown(f'<p style="font-size: 12px; color: gray;">{help_text_note}</p>', unsafe_allow_html=True)
    
    #Submission button
    submit_button=st.form_submit_button(label="🛎️Order!")

#Submitted process
if submit_button:
    if name_input and usr_input and platform and number and multi_select and color_select and background_select and link_input:
        pdf_bytes = generate_pdf(name_input, platform, usr_input, number, ", ".join(multi_select), color_select, background_select, link_input, note_input)
        st.success("Yippee, you did it! Thank you for your order request. Please download your commission order request file and mail it to moonokotiru00@gmail.com!")
        
        #Download button
        st.download_button(label="📩Download Receipt", data=pdf_bytes, file_name=f"Mooncomms_Order_Submit_{name_input.replace(' ', '_')}.pdf", mime="application/pdf")
        st.balloons()
        st.write("*Please read and follow the next instructions to complete your commission order request*:")
        st.write("*1. Download the PDF file.*")
        st.write("*2. Send the PDF file to my 📧email: moonokotiru00@gmail.com*")
        st.write("*3. Please kindly wait for my reply and confirmation of your commission order request.*")
        st.write("*4. If I accept your request, I will contact you to discuss the details.*")
        st.write("*5. If I decline your request, I will also contact you from email to explain the reason.*")
        st.write("*6. Please do not change your username or contact info after submitting the request, as it may cause communication issues.*")
        st.write("*7. Please be patient and respectful during the commission process. Thank you for your understanding and cooperation ⸜(｡˃ ᵕ ˂ )⸝♡!*")
    else: 
        st.error("Please fill in all required fields before submitting your commission order request!")
    
#Social media links
st.logo(
    image="https://upload.wikimedia.org/wikipedia/commons/a/a5/Instagram_icon.png",
    link="https://www.instagram.com/moonolight00"
)
