# TerminalGemini
A handy tool to use Gemini in terminal in Linux.

USAGE:

STEP 1: Open Terminal --> Place your downloaded files at Desktop. Type in terminal--> cd Desktop
STEP 2: Type in terminal --> python -m venv jarvis_files. Then type --> chmod +x heygpt
STEP 3: Type in terminal -->  python jarvisfiles/bin/activate. Then type in --> "pip install google-generativeai"
STEP 4: Type in terminal --> echo $SHELL (It will tell you which commands to use ahead)
STEP 5: Type in terminal --> nano ~/.bashrc OR nano ~/.zshrc. At end of file, add --> "export PATH=$HOME/Desktop:$PATH" (including Double Quotation marks). Press Ctrl+x, then hit y and then hit enter.
STEP 6: Go to Google AI Studio (https://aistudio.google.com/).  Sign In.
STEP 7: On left top, click get API key. Then on new page that opened, click Create API Key. Click on text box and choose "My First Project". Hit generate and copy it somewhere safe. (DO NOT SHARE THIS KEY WITH ANYONE)
STEP 8: Open Jarvis.py file and put your key in Line 25. (Within the double quotation marks.)
STEP 9: Now simply type heygpt in terminal and hit enter.
Step 10: Enter your question and hit enter.
Step 11: Enter  's' for short answer 
                'n' for normal answer
                'e' for long and elaborated answer
                then hit enter and get your response ;)
