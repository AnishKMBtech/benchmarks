import streamlit as st
import matplotlib.pyplot as plt
import networkx as nx

# Set page title
st.set_page_config(page_title="User-Task Automation Flowchart", page_icon=":robot_face:")

# Display title
st.title("User-Task Automation Flowchart using Language Model, Vision Model, and PyAutoGUI")

# Function to generate flowchart using networkx
def create_flowchart():
    G = nx.DiGraph()

    # Define the flowchart nodes
    nodes = [
        "User Input via Web Interface",
        "Language Model Task Interpretation",
        "Vision Model (OpenCV / OmniParser)",
        "Action Mapping and Collaboration Between Models",
        "Execution with PyAutoGUI",
        "Verification of Task Completion",
        "Feedback to Language Model",
        "Display Output to User",
        "Logging & Monitoring"
    ]

    # Add nodes to the graph
    G.add_nodes_from(nodes)

    # Define the flow between the nodes (edges)
    edges = [
        ("User Input via Web Interface", "Language Model Task Interpretation"),
        ("Language Model Task Interpretation", "Vision Model (OpenCV / OmniParser)"),
        ("Vision Model (OpenCV / OmniParser)", "Action Mapping and Collaboration Between Models"),
        ("Action Mapping and Collaboration Between Models", "Execution with PyAutoGUI"),
        ("Execution with PyAutoGUI", "Verification of Task Completion"),
        ("Verification of Task Completion", "Feedback to Language Model"),
        ("Feedback to Language Model", "Display Output to User"),
        ("Display Output to User", "Logging & Monitoring")
    ]

    # Add edges to the graph
    G.add_edges_from(edges)

    # Set node positions using spring layout
    pos = nx.spring_layout(G, seed=42)

    # Plot the graph
    plt.figure(figsize=(10, 8))
    nx.draw(G, pos, with_labels=True, node_size=3000, node_color="skyblue", font_size=10, font_weight="bold", edge_color="gray")
    plt.title("User-Task Automation Flowchart")
    st.pyplot()

# Display the flowchart
create_flowchart()

# Display the task steps with descriptions
st.subheader("Process Description")
st.write("""
### 1. User Input via Web Interface:
- The user navigates to a website where the task automation system is deployed.
- The user enters a task description in natural language (e.g., "Click the Submit button on the form").
- The language model integrated with the web interface processes the user's input.

### 2. Language Model Task Interpretation:
- The language model breaks down the task description into specific operations or goals.
- It identifies target UI components and actions, such as clicking buttons or typing text into input fields.

### 3. Vision Model (OpenCV / OmniParser):
- The vision model analyzes the screen or video feed to detect relevant UI components.
- It locates elements like buttons, input fields, and images.
- The model uses techniques such as object detection and image segmentation for accurate UI element detection.

### 4. Action Mapping and Collaboration Between Models:
- The language model identifies the task's action (e.g., clicking the Submit button).
- The vision model provides the exact coordinates or location of UI components.
- The models collaborate to ensure the task's action corresponds to a valid UI component detected by the vision model.

### 5. Execution with PyAutoGUI:
- The system uses PyAutoGUI to simulate the required actions (e.g., clicking or typing).
- The language model and vision model work together to simulate user interaction.

### 6. Verification of Task Completion:
- After executing the task, the vision model verifies the outcome (e.g., detecting confirmation messages or updated forms).
- The vision model checks for visual cues to confirm success or failure.

### 7. Feedback to Language Model:
- Based on the visual verification, the vision model sends feedback to the language model.
- The system updates the task status (success or failure) and decides whether to retry or confirm success.

### 8. Display Output to User:
- The system displays the final outcome (success or failure) to the user via the web interface.

### 9. Logging & Monitoring:
- Each action and decision is logged for debugging and optimization purposes.
- The system can track failures, retries, and task completion for future analysis.
""")

# Add a note for users
st.write("This flowchart and description outline the process for automating user tasks using advanced models like Language, Vision, and PyAutoGUI.")
