🤖 AI Virtual Career Counsellor


An intelligent virtual assistant designed to help users explore potential career paths based on their interests and skills. Built with Rasa for conversational AI and Streamlit for an interactive web interface, this counsellor provides instant, personalized career guidance.

✨ Features
Interactive Chat Interface: A user-friendly and responsive chat application powered by Streamlit.
Natural Language Understanding (NLU): Leverages Rasa's NLU capabilities to understand user queries about their career interests.
Dynamic Career Recommendations: Provides tailored suggestions for various fields, including:
Technology: Software Developer, Data Scientist, Cybersecurity Analyst, Web Developer.
Arts & Design: Graphic Designer, Animator, Content Creator, Fine Artist.
Commerce & Business: Financial Analyst, Accountant, Marketing Manager, Business Consultant.
Psychology: Psychologist, Counselor, Social Worker, HR Specialist.
Healthcare: Doctor, Nurse, Medical Researcher, Public Health Professional.
Action Server Integration: Custom actions in Rasa allow for structured responses and more complex logic beyond simple text replies.
🚀 How to Run
This project is set up for easy deployment and development using GitHub Codespaces, providing a consistent and ready-to-go environment.

1. Open in Codespaces
The quickest way to get started is to click the "Code" button on this GitHub repository page, navigate to the "Codespaces" tab, and select "Create codespace on main."

(The Codespaces environment is pre-configured to automatically install necessary dependencies and set up the Rasa project via the .devcontainer/postCreateCommand.)

2. Start Services in Separate Terminals
Once your Codespace has fully loaded and initialized, you'll need to run three separate services for the application to function. Open three distinct terminal windows (Terminal > New Terminal in VS Code) and run the following commands in each:

Terminal 1: Rasa Action Server
This server executes the custom actions defined in actions/actions.py (e.g., providing career recommendations).

Bash

rasa run actions
Terminal 2: Rasa Core & NLU Server
This is the main Rasa server that handles natural language understanding, dialogue management, and communicates with the action server.

Bash

rasa run --enable-api --cors "*" --endpoints endpoints.yml
Terminal 3: Streamlit Frontend
This starts the web application that provides the chat interface.

Bash

streamlit run app.py
3. Access the Application
Once the Streamlit server starts, a new tab should automatically open in your browser, displaying the chat interface. If it doesn't, you can typically access it via the "Ports" tab in Codespaces (usually on port 8501).

Optional: Accessing Rasa from Outside Codespaces (via ngrok)
If you need to expose your Rasa server (running on port 5005) to a public URL (e.g., for testing with other services or demonstrating outside Codespaces):

Install ngrok (if not already present) and authenticate:
Sign up for a free ngrok account at dashboard.ngrok.com/signup.
Copy your authtoken from your ngrok dashboard.
In a Codespaces terminal, run:
Bash

ngrok config add-authtoken YOUR_ACTUAL_AUTHTOKEN_HERE
Start ngrok tunnel:
In a new terminal (keep your Rasa and Streamlit servers running), execute:
Bash

ngrok http 5005
ngrok will provide a public HTTPS forwarding URL (e.g., https://xxxx-xx-xxx-xxx-xxx.ngrok-free.app).
Update RASA_API_URL: If you are connecting from a deployed Streamlit app, you will need to update the RASA_API_URL in app.py to this ngrok URL, then commit and redeploy your Streamlit app.
💡 How to Interact
Start a conversation by typing your career interests or general greetings. The bot is designed to understand various ways you might express your preferences.

Example Inputs:

"Hi there!"
"I'm interested in programming and software development."
"What kind of careers are there in art and design?"
"I'm really good with numbers and business concepts."
"Tell me about psychology as a career."
"What about healthcare jobs?"
"Can you recommend something for me?"
"Thank you!"
"Bye"
🔮 Future Enhancements
Given more time, here are some potential improvements for the AI Virtual Career Counsellor:

Expanded Career Database: Integrate more diverse career paths and sub-specialties.
Deeper Recommendation Logic: Incorporate user skills, educational background, and preferences for more personalized advice.
External API Integration: Connect to job boards (e.g., LinkedIn API), educational platforms (e.g., Coursera API), or industry data sources for real-time insights.
User Profiles: Allow users to save their conversations, preferences, and recommended paths.
Multilingual Support: Extend the bot's capabilities to support different languages.
Interview Preparation/Skill Development Tips: Offer next steps for pursuing a recommended career.
📸 Screenshot
(Consider adding a screenshot of your running Streamlit app here for quick visual understanding!)
(Example: You can place your image file in an assets folder.)

🙏 Acknowledgements
This project was built with the power of open-source tools:

Rasa: For building robust conversational AI assistants.
Streamlit: For turning Python scripts into interactive web apps.
GitHub Codespaces: For a cloud-based, consistent development environment.
ngrok: For securely exposing local development servers to the internet.