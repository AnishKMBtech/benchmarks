import streamlit as st

# Set page title
st.set_page_config(page_title="User-Task Automation Flowchart", page_icon=":robot_face:")

# Display title
st.title("User-Task Automation Flowchart using Language Model, Vision Model, and PyAutoGUI")

# Flowchart in SVG format (you can create it externally and embed or use it inline)
flowchart_svg = """
<svg xmlns="http://www.w3.org/2000/svg" width="600" height="600">
  <rect x="20" y="20" width="200" height="50" fill="lightblue" />
  <text x="120" y="50" font-size="16" text-anchor="middle" fill="black">User Input via Web Interface</text>
  
  <rect x="20" y="100" width="200" height="50" fill="lightgreen" />
  <text x="120" y="130" font-size="16" text-anchor="middle" fill="black">Language Model Task Interpretation</text>
  
  <rect x="20" y="180" width="200" height="50" fill="lightyellow" />
  <text x="120" y="210" font-size="16" text-anchor="middle" fill="black">Vision Model (OpenCV / OmniParser)</text>
  
  <rect x="20" y="260" width="200" height="50" fill="lightcoral" />
  <text x="120" y="290" font-size="16" text-anchor="middle" fill="black">Action Mapping and Collaboration</text>
  
  <rect x="20" y="340" width="200" height="50" fill="lightgray" />
  <text x="120" y="370" font-size="16" text-anchor="middle" fill="black">Execution with PyAutoGUI</text>
  
  <rect x="20" y="420" width="200" height="50" fill="lightpink" />
  <text x="120" y="450" font-size="16" text-anchor="middle" fill="black">Verification of Task Completion</text>
  
  <rect x="20" y="500" width="200" height="50" fill="lightseagreen" />
  <text x="120" y="530" font-size="16" text-anchor="middle" fill="black">Feedback to Language Model</text>
  
  <rect x="300" y="100" width="200" height="50" fill="lightskyblue" />
  <text x="400" y="130" font-size="16" text-anchor="middle" fill="black">Display Output to User</text>
  
  <rect x="300" y="180" width="200" height="50" fill="lightgoldenrodyellow" />
  <text x="400" y="210" font-size="16" text-anchor="middle" fill="black">Logging & Monitoring</text>

  <!-- Lines to connect boxes -->
  <line x1="120" y1="70" x2="120" y2="100" stroke="black" stroke-width="2" />
  <line x1="120" y1="150" x2="120" y2="180" stroke="black" stroke-width="2" />
  <line x1="120" y1="230" x2="120" y2="260" stroke="black" stroke-width="2" />
  <line x1="120" y1="310" x2="120" y2="340" stroke="black" stroke-width="2" />
  <line x1="120" y1="390" x2="120" y2="420" stroke="black" stroke-width="2" />
  <line x1="120" y1="470" x2="120" y2="500" stroke="black" stroke-width="2" />
  <line x1="400" y1="150" x2="400" y2="100" stroke="black" stroke-width="2" />
  <line x1="400" y1="230" x2="400" y2="180" stroke="black" stroke-width="2" />
</svg>
"""

# Display the SVG Flowchart
st.markdown(flowchart_svg, unsafe_allow_html=True)

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
