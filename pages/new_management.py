import pandas as pd
import streamlit as st
from db1 import add_event, get_events, approve_event, update_event, delete_event, decline_event
def handle_event_action(event_id, action):
    """Handle approve/decline/edit/delete actions for the event."""
    if action == "approve":
        approve_event(event_id)
        st.success(f"Event ID {event_id} approved!")
    elif action == "decline":
        decline_event(event_id)
        st.success(f"Event ID {event_id} declined!")
    elif action == "edit":
        st.write(f"Editing Event ID {event_id}")
    elif action == "delete":
        delete_event(event_id)
        st.success(f"Event ID {event_id} deleted!")

def display_event_table_with_buttons(events, event_status):
    """Display event table with action buttons (approve, decline, edit, delete) in the same row."""
    if events:
        # Create a DataFrame for events
        df = pd.DataFrame(events, columns=['id', 'quiz_name', 'date', 'time', 'category', 'venue', 'location', 'organizer', 'genre', 'quiz_master', 'prize', 'contact_number', 'registration_link', 'other_details', 'status'])
        df['date'] = pd.to_datetime(df['date'], format='%Y-%m-%d', errors='coerce')
        df['date'] = df['date'].dt.date
        df = df.sort_values(by='date')
        df = df.reset_index(drop=True)
        # Display the column headings for clarity
        st.write(f"### {event_status} Events")
        col1, col2, col3, col4, col5, col6, col7, col8, col9, col10, col11, col12, col13, col14, col15 = st.columns([2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2])
        
        with col1:
            st.write("**Quiz Name**")
        with col2:
            st.write("**Date**")
        with col3:
            st.write("**Time**")
        with col4:
            st.write("**Category**")
        with col5:
            st.write("**Venue**")
        with col6:
            st.write("**Location**")
        with col7:
            st.write("**Organizer**")
        with col8:
            st.write("**Genre**")
        with col9:
            st.write("**Quiz Master**")
        with col10:
            st.write("**Prize**")
        with col11:
            st.write("**Contact Number**")
        with col12:
            st.write("**Registration Link**")
        with col13:
            st.write("**Other Details**")
        with col14:
            st.write("**Status**")
        with col15:
            st.write("**Actions**")
        
        # Iterate through the events to display each row with action buttons
        for idx, row in df.iterrows():
            event_id = row['id']
            col1, col2, col3, col4, col5, col6, col7, col8, col9, col10, col11, col12, col13, col14, col15 = st.columns([2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2])  # Adjust column widths
            
            with col1:
                st.write(row['quiz_name'])  # Display event name
            with col2:
                st.write(row['date'])  # Display event date
            with col3:
                st.write(row['time'])  # Display event time
            with col4:
                st.write(row['category'])  # Display event category
            with col5:
                st.write(row['venue'])  # Display event venue
            with col6:
                st.write(row['location'])  # Display event location
            with col7:
                st.write(row['organizer'])  # Display event organizer
            with col8:
                st.write(row['genre'])  # Display event genre
            with col9:
                st.write(row['quiz_master'])  # Display event quiz master
            with col10:
                st.write(row['prize'])  # Display event prize
            with col11:
                st.write(row['contact_number'])  # Display event contact number
            with col12:
                st.write(row['registration_link'])  # Display event registration link
            with col13:
                st.write(row['other_details'])  # Display other event details
            with col14:
                st.write(row['status'])  # Display event status
            with col15:
                # # Action buttons (Approve, Decline, Edit, Delete)
                # if st.button(f"Approve {event_id}", key=f"approve_{event_id}"):
                #     handle_event_action(event_id, "approve")
                # if st.button(f"Decline {event_id}", key=f"decline_{event_id}"):
                #     handle_event_action(event_id, "decline")
                # if st.button(f"Edit {event_id}", key=f"edit_{event_id}"):
                #     handle_event_action(event_id, "edit")
                # if st.button(f"Delete {event_id}", key=f"delete_{event_id}"):
                #     handle_event_action(event_id, "delete")
                # Action buttons (Approve, Decline, Edit, Delete)
                if st.button(f"Approve", key=f"approve_{event_id}"):
                    handle_event_action(event_id, "approve")
                if st.button(f"Decline", key=f"decline_{event_id}"):
                    handle_event_action(event_id, "decline")
                # if st.button(f"Edit", key=f"edit_{event_id}"):
                #     handle_event_action(event_id, "edit")
                # if st.button(f"Delete", key=f"delete_{event_id}"):
                #     handle_event_action(event_id, "delete")
                
    else:
        st.write(f"No {event_status} events to manage. :smiley: :smiley: :smiley:")

def display_pending_events_table(pending_events):
    """Display pending events with action buttons."""
    if pending_events:
        df_pending = pd.DataFrame(pending_events, columns=['id', 'quiz_name', 'date', 'time', 'category', 'venue', 'location', 'organizer', 'genre', 'quiz_master', 'prize', 'contact_number', 'registration_link', 'other_details', 'status'])
        df_pending['date'] = pd.to_datetime(df_pending['date'], format='%Y-%m-%d', errors='coerce')
        df_pending['date'] = df_pending['date'].dt.date
        df_pending = df_pending.sort_values(by='date')

        # Display the column headings for clarity
        st.write("### Pending Events")
        col1, col2, col3, col4, col5, col6, col7, col8, col9, col10, col11, col12, col13, col14, col15 = st.columns([2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2])
        
        with col1:
            st.write("**Quiz Name**")
        with col2:
            st.write("**Date**")
        with col3:
            st.write("**Time**")
        with col4:
            st.write("**Category**")
        with col5:
            st.write("**Venue**")
        with col6:
            st.write("**Location**")
        with col7:
            st.write("**Organizer**")
        with col8:
            st.write("**Genre**")
        with col9:
            st.write("**Quiz Master**")
        with col10:
            st.write("**Prize**")
        with col11:
            st.write("**Contact Number**")
        with col12:
            st.write("**Registration Link**")
        with col13:
            st.write("**Other Details**")
        with col14:
            st.write("**Status**")
        with col15:
            st.write("**Actions**")
        
        # Iterate through the events to display each row with action buttons
        for idx, row in df_pending.iterrows():
            event_id = row['id']
            col1, col2, col3, col4, col5, col6, col7, col8, col9, col10, col11, col12, col13, col14, col15 = st.columns([2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2])  # Adjust column widths
            
            with col1:
                st.write(row['quiz_name'])  # Display event name
            with col2:
                st.write(row['date'])  # Display event date
            with col3:
                st.write(row['time'])  # Display event time
            with col4:
                st.write(row['category'])  # Display event category
            with col5:
                st.write(row['venue'])  # Display event venue
            with col6:
                st.write(row['location'])  # Display event location
            with col7:
                st.write(row['organizer'])  # Display event organizer
            with col8:
                st.write(row['genre'])  # Display event genre
            with col9:
                st.write(row['quiz_master'])  # Display event quiz master
            with col10:
                st.write(row['prize'])  # Display event prize
            with col11:
                st.write(row['contact_number'])  # Display event contact number
            with col12:
                st.write(row['registration_link'])  # Display event registration link
            with col13:
                st.write(row['other_details'])  # Display other event details
            with col14:
                st.write(row['status'])  # Display event status
            with col15:
                # Action buttons (Approve, Decline)
                if st.button(f"Approve", key=f"approve_{event_id}"):
                    handle_event_action(event_id, "approve")
                if st.button(f"Decline", key=f"decline_{event_id}"):
                    handle_event_action(event_id, "decline")

    else:
        st.markdown("No pending events to approve. :smiley: :smiley: :smiley:")
BASIC_ADMIN_PASSWORD = st.secrets.user.pass1
password = st.text_input("Enter Admin Password", type="password")
if password == BASIC_ADMIN_PASSWORD:
    # Main Code Block for Handling Tabs
    # Fetch events based on status
    approved_events = get_events("Approved")
    pending_events = get_events("Pending")
    declined_events = get_events("Declined")

    # Tab to switch between managing approved and pending events
    tab1, tab2, tab3 = st.tabs(["Manage Approved Events", "Approve Pending Events", "Manage Declined Events"])

    with tab1:  # Manage Approved Events Tab
        st.write("Manage Approved Events")
        display_event_table_with_buttons(approved_events, "Approved")

    with tab2:  # Approve Pending Events Tab
        st.write("Approve Pending Events")
        display_pending_events_table(pending_events)

    with tab3:  # Manage Declined Events Tab
        st.write("Manage Declined Events")
        display_event_table_with_buttons(declined_events, "Declined")
