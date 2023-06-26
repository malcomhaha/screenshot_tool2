# main.py

import tkinter as tk
from tkinter import filedialog
import image_processing
import chatgpt

# Store the last user input for continuing the conversation
last_user_input = ""

def process_screenshot():
    # Pop up the file selection dialog
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])

    # If the user selects a file
    if file_path:
        # Extract text from the screenshot
        extracted_text = image_processing.extract_text_from_image(file_path)

        # # Clear the text box content
        # text_box.delete(1.0, tk.END)

        # Insert the extracted text into the text box
        text_box.insert(tk.END, extracted_text)

        # Generate a response using ChatGPT
        reply = chatgpt.generate_response(extracted_text)

        # Insert the ChatGPT response into the text box
        text_box.insert(tk.END, '\n\nChatGPT: ' + reply)

        # Update the last user input
        global last_user_input
        last_user_input = extracted_text

def continue_conversation():
    # Get the last user input from the text box
    user_input = text_box.get("end-1c linestart", tk.END)

    # Generate a response using ChatGPT
    reply = chatgpt.generate_response(user_input)

    # Insert the ChatGPT response into the text box
    text_box.insert(tk.END, '\n\nChatGPT: ' + reply)

# Create the window
window = tk.Tk()

# Set the window title
window.title("MALCOM的截图拾取文字然后问GPT小工具")

# Set the window size
window.geometry("400x400")

# Create the "Process Screenshot" button
button_screenshot = tk.Button(window, text="选一张比较清楚的文字截图", command=process_screenshot)
button_screenshot.pack(pady=10)

# Create the "Continue Conversation" button
button_continue = tk.Button(window, text="和ChatGPT继续对话", command=continue_conversation)
button_continue.pack(pady=10)

# Create the text box
text_box = tk.Text(window, height=100, width=100)
text_box.pack(pady=10)

# Enter the main event loop
window.mainloop()
