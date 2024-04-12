import streamlit as st
# in terminal run command: "streamlit run web.py" to run the web app

import functions

all_todos_list = functions.get_todos()

# we can make the page expands to full screen width bt stays responsive
st.set_page_config(layout="wide")


def add_new_todo():
    # st.session_state is a dict holding all values that users enters,
    # and these values are mapped by UNIQUE key that is defined when creating
    # a widget like text_input() for example
    this_todo = st.session_state['new_todo']
    # append this new to-do item to the list of todos (add line break also)
    all_todos_list.append(this_todo.capitalize() + "\n")
    # save the updated list back to external file also
    functions.write_todos(all_todos_list)
    # Reset or Clear the text input after adding the new to-do item
    # we can also use dot notation: st.session_state.new_todo = ""
    st.session_state['new_todo'] = ""


# The components below will be shown by order on the webpage
st.title("To-Do App")
st.subheader("This is a simple To-Do app")
# we can put html in st.write() but add the `unsafe_allow_html=True` to parse the syntax
st.write("This app increases your <strong><em>productivity</em></strong>.",
         unsafe_allow_html=True)

st.text_input(label="",
              placeholder="Enter a new to-do item...",
              on_change=add_new_todo, key='new_todo')

for index, todo in enumerate(all_todos_list):
    # st.checkbox() returns a boolean value indicating current state of the checkbox
    # to-do item to maintain uniqueness of key
    checkbox_value = st.checkbox(todo, key=todo)
    if checkbox_value:
        all_todos_list.pop(index)
        # save the updated list back to external file also
        functions.write_todos(all_todos_list)
        # Delete this checkbox from the session_state dict afterwards
        del st.session_state[todo]
        # refresh for checkbox change to be shown
        st.rerun()

