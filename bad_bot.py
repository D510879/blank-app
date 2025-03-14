import streamlit as st

# Define bad chatbot responses
def chatbot_response(user_input):
    responses = {
        "deadline": "Check the university website for deadlines.",
        "mental health": "Visit the student support website.",
        "print coursework": "I don't understand.",
        "study room": "What is your student ID?",  # Fails to remember context
    }
    
    # Poor natural language handling (rigid responses)
    for key in responses:
        if key in user_input.lower():
            return responses[key]
    return "I'm sorry, I don't understand. Please check the university website."

# Streamlit UI
st.set_page_config(page_title="University Helpdesk", layout="wide")

# Sidebar navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to:", ["Home", "FAQ", "Chatbot", "Contact Us"])

if page == "Home":
    st.title("University Helpdesk - Beta Version")
    st.write("Welcome to the university helpdesk. Use the menu to find information or chat with the bot.")
    
    # Poor layout example
    st.markdown("**Common Questions:**")
    st.write("- Where can I print my coursework? (No link provided)")
    st.write("- How do I book a study room? (Hidden in FAQ)")
    st.write("- How can I contact IT? (Try guessing under 'Contact Us')")
    
elif page == "FAQ":
    st.title("Frequently Asked Questions")
    
    # Poorly structured FAQ page
    st.write("Q: How do I reset my password?")
    st.write("A: Try the IT support page.")
    
    st.write("Q: Where can I get mental health support?")
    st.write("A: Visit the student support website. (No link provided)")
    
elif page == "Chatbot":
    st.title("University Helpdesk Chatbot")
    st.write("Ask a question and the chatbot will try to assist you.")
    
    user_input = st.text_input("Type your question here:")
    if user_input:
        response = chatbot_response(user_input)
        st.write(f"Chatbot: {response}")
        
elif page == "Contact Us":
    st.title("Contact Information")
    
    # Poorly structured contact info
    st.write("For IT issues, check the FAQ.")
    st.write("For student support, visit the student support website.")
