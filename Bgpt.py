from tkinter import *
import requests
from io import BytesIO
import pandas as pd
from PIL import Image, ImageTk
from io import BytesIO
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import re
import csv
import tkinter as tk

# Load the CSV file
df = pd.read_csv("database_quote.csv")

# Define the TF-IDF vectorizer
vectorizer = TfidfVectorizer()

# Compute the TF-IDF matrix
tfidf_matrix = vectorizer.fit_transform(df['Prompt'].values.astype('U'))

# Define regular expressions to match variations of "kill", "murder", and "homicide"
kill_regex = re.compile(r"\b(kill(?:s|ed|ing)?)\b", re.IGNORECASE)
murder_regex = re.compile(r"\b(murder(?:s|ed|ing)?)\b", re.IGNORECASE)
homicide_regex = re.compile(r"\b(homicide(?:s|d)?)\b", re.IGNORECASE)
regex_appearance = re.compile(r'\b(fat|ugly|beauty|weight|look|tall|short)\b', re.IGNORECASE)
suicide_regex = re.compile(r'\bsuicid(e|al|e\s*thoughts?)\b', re.IGNORECASE)
work_regex = re.compile(r'\b(work|working|job|career|lazy|laziness|study|studying|studious)\b', re.IGNORECASE)
gender_regex = re.compile(r'\b(gay|lesbian|bisexual|transgender|queer|LGBTQ|gender fluid)\b', re.IGNORECASE)


def send_message():
    prev_prompt = None
    prev_response = None
    feedback = False

    user_input = input_field.get().lower()
    input_field.delete(0, tk.END)
    user_message_label = tk.Label(chatbot_dialogue_content, text=user_input, bg="#e1f5fe", fg="#000000",
                                  wraplength=360, justify=tk.RIGHT, relief=tk.RAISED, padx=10, pady=10,
                                  borderwidth=1, highlightthickness=1, highlightbackground="#000000")
    user_message_label.pack(anchor=tk.E, padx=10, pady=5)

    # Evaluate Message

    if user_input.lower() == 'exit':
        quote = "Chatbot: Goodbye!"
        chatbot_response_label = tk.Label(chatbot_dialogue_content, text=quote, bg="#f2f2f2", fg="#000000",
                                          wraplength=360, justify=tk.LEFT, relief=tk.RAISED, padx=10, pady=10,
                                          borderwidth=1, highlightthickness=1, highlightbackground="#000000")
        chatbot_response_label.pack(anchor=tk.W, padx=10, pady=5)

    # Check if the user input matches any of the regular expressions
    elif kill_regex.search(user_input):
        # Respond with the pre-defined response for "kill"
        quote = "Chatbot: He who sees the Supreme Lord equally present everywhere does not degrade himself by his behavior. It is important to take responsibility for your actions and seek forgiveness."
        chatbot_response_label = tk.Label(chatbot_dialogue_content, text=quote, bg="#f2f2f2", fg="#000000",
                                          wraplength=360, justify=tk.LEFT, relief=tk.RAISED, padx=10, pady=10,
                                          borderwidth=1, highlightthickness=1, highlightbackground="#000000")
        chatbot_response_label.pack(anchor=tk.W, padx=10, pady=5)

    elif murder_regex.search(user_input):
        # Respond with the pre-defined response for "murder"
        quote = "Chatbot: Violence is never a solution. It's important to promote peace and understanding among all beings."
        chatbot_response_label = tk.Label(chatbot_dialogue_content, text=quote, bg="#f2f2f2", fg="#000000",
                                          wraplength=360, justify=tk.LEFT, relief=tk.RAISED, padx=10, pady=10,
                                          borderwidth=1, highlightthickness=1, highlightbackground="#000000")
        chatbot_response_label.pack(anchor=tk.W, padx=10, pady=5)

    elif homicide_regex.search(user_input):
        # Respond with the pre-defined response for "homicide"
        quote = "Chatbot: The value of human life is sacred. It's important to respect and protect the lives of others."
        chatbot_response_label = tk.Label(chatbot_dialogue_content, text=quote, bg="#f2f2f2", fg="#000000",
                                          wraplength=360, justify=tk.LEFT, relief=tk.RAISED, padx=10, pady=10,
                                          borderwidth=1, highlightthickness=1, highlightbackground="#000000")
        chatbot_response_label.pack(anchor=tk.W, padx=10, pady=5)

    elif regex_appearance.search(user_input):
        # Respond with the pre-defined response for appearance-related queries
        quote = "Chatbot: Remember that true beauty comes from within. It's important to love and accept yourself just as you are."
        chatbot_response_label = tk.Label(chatbot_dialogue_content, text=quote, bg="#f2f2f2", fg="#000000",
                                          wraplength=360, justify=tk.LEFT, relief=tk.RAISED, padx=10, pady=10,
                                          borderwidth=1, highlightthickness=1, highlightbackground="#000000")
        chatbot_response_label.pack(anchor=tk.W, padx=10, pady=5)

    elif suicide_regex.search(user_input):
        # Respond with the pre-defined response for suicide-related queries
        quote = "Chatbot: I'm really sorry to hear that you're feeling this way. Remember that there are people who care about you and want to help. Please reach out to a helpline or a trusted person in your life."
        chatbot_response_label = tk.Label(chatbot_dialogue_content, text=quote, bg="#f2f2f2", fg="#000000",
                                          wraplength=360, justify=tk.LEFT, relief=tk.RAISED, padx=10, pady=10,
                                          borderwidth=1, highlightthickness=1, highlightbackground="#000000")
        chatbot_response_label.pack(anchor=tk.W, padx=10, pady=5)

    elif work_regex.search(user_input):
        # Respond with the pre-defined response for work-related queries
        quote = "Chatbot: It's important to find a balance between work and personal life. Remember to take breaks, prioritize self-care, and seek support when needed."
        chatbot_response_label = tk.Label(chatbot_dialogue_content, text=quote, bg="#f2f2f2", fg="#000000",
                                          wraplength=360, justify=tk.LEFT, relief=tk.RAISED, padx=10, pady=10,
                                          borderwidth=1, highlightthickness=1, highlightbackground="#000000")
        chatbot_response_label.pack(anchor=tk.W, padx=10, pady=5)

    elif gender_regex.search(user_input):
        # Respond with the pre-defined response for gender-related queries
        quote = "Chatbot: Gender identity is personal and unique to each individual. It's important to respect and support everyone's right to self-identify."
        chatbot_response_label = tk.Label(chatbot_dialogue_content, text=quote, bg="#f2f2f2", fg="#000000",
                                          wraplength=360, justify=tk.LEFT, relief=tk.RAISED, padx=10, pady=10,
                                          borderwidth=1, highlightthickness=1, highlightbackground="#000000")
        chatbot_response_label.pack(anchor=tk.W, padx=10, pady=5)

    else:
        # Compute the TF-IDF vector of the user input
        user_tfidf = vectorizer.transform([user_input])

        # Compute the cosine similarity between the user input and the prompts
        cosine_similarities = cosine_similarity(user_tfidf, tfidf_matrix)

        # Get the index of the most similar prompt
        max_index = np.argmax(cosine_similarities)

        # Get the corresponding response
        prompt = df.iloc[max_index]['Prompt']
        response = df.iloc[max_index]['Response']

        # Print the response
        quote = "Chatbot:" + response

        chatbot_response_label = tk.Label(chatbot_dialogue_content, text=quote, bg="#f2f2f2", fg="#000000",
                                          wraplength=360, justify=tk.LEFT, relief=tk.RAISED, padx=10, pady=10,
                                          borderwidth=1, highlightthickness=1, highlightbackground="#000000")
        chatbot_response_label.pack(anchor=tk.W, padx=10, pady=5)

        # Ask for feedback
        chatbot_response_label = tk.Label(chatbot_dialogue_content,
                                          text="Chatbot: Are you satisfied with the response? (yes/no): ", bg="#f2f2f2",
                                          fg="#000000",
                                          wraplength=360, justify=tk.LEFT, relief=tk.RAISED, padx=10, pady=10,
                                          borderwidth=1, highlightthickness=1, highlightbackground="#000000")
        chatbot_response_label.pack(anchor=tk.W, padx=10, pady=5)

        def first_yes():
            # Continue with the next prompt
            user_message_label = tk.Label(chatbot_dialogue_content, text="Yes", bg="#e1f5fe", fg="#000000",
                                          wraplength=360, justify=tk.RIGHT, relief=tk.RAISED, padx=10, pady=10,
                                          borderwidth=1, highlightthickness=1, highlightbackground="#000000")
            user_message_label.pack(anchor=tk.E, padx=10, pady=5)
            prev_prompt = prompt
            prev_response = response

        def first_no():
            # Get the second most similar prompt
            user_message_label = tk.Label(chatbot_dialogue_content, text="No", bg="#e1f5fe", fg="#000000",
                                          wraplength=360, justify=tk.RIGHT, relief=tk.RAISED, padx=10, pady=10,
                                          borderwidth=1, highlightthickness=1, highlightbackground="#000000")
            user_message_label.pack(anchor=tk.E, padx=10, pady=5)
            cosine_similarities[0][max_index] = -1
            second_max_index = np.argmax(cosine_similarities)
            second_max_sim = cosine_similarities[0][second_max_index]
            second_response = df.iloc[second_max_index]['Response']
            second_prompt = df.iloc[second_max_index]['Prompt']

            # Print the second response
            chatbot_response_label = tk.Label(chatbot_dialogue_content, text="Chatbot:" + second_response, bg="#f2f2f2",
                                              fg="#000000",
                                              wraplength=360, justify=tk.LEFT, relief=tk.RAISED, padx=10, pady=10,
                                              borderwidth=1, highlightthickness=1, highlightbackground="#000000")
            chatbot_response_label.pack(anchor=tk.W, padx=10, pady=5)

            # Update the variables for prompt and response
            prev_prompt = second_prompt
            prev_response = second_response

            # Ask for feedback again
            chatbot_response_label = tk.Label(chatbot_dialogue_content,
                                              text="Chatbot: Are you satisfied with the response? (yes/no): ",
                                              bg="#f2f2f2", fg="#000000",
                                              wraplength=360, justify=tk.LEFT, relief=tk.RAISED, padx=10, pady=10,
                                              borderwidth=1, highlightthickness=1, highlightbackground="#000000")
            chatbot_response_label.pack(anchor=tk.W, padx=10, pady=5)

            def second_yes():
                user_message_label = tk.Label(chatbot_dialogue_content, text="Yes", bg="#e1f5fe", fg="#000000",
                                              wraplength=360, justify=tk.RIGHT, relief=tk.RAISED, padx=10, pady=10,
                                              borderwidth=1, highlightthickness=1, highlightbackground="#000000")
                user_message_label.pack(anchor=tk.E, padx=10, pady=5)

                chatbot_response_label = tk.Label(chatbot_dialogue_content,
                                                  text="Chatbot: Glad you found us to be helpful.",
                                                  bg="#f2f2f2", fg="#000000",
                                                  wraplength=360, justify=tk.LEFT, relief=tk.RAISED, padx=10, pady=10,
                                                  borderwidth=1, highlightthickness=1, highlightbackground="#000000")
                chatbot_response_label.pack(anchor=tk.W, padx=10, pady=5)

                # Continue with the next prompt

            def second_no():
                user_message_label = tk.Label(chatbot_dialogue_content, text="No", bg="#e1f5fe", fg="#000000",
                                              wraplength=360, justify=tk.RIGHT, relief=tk.RAISED, padx=10, pady=10,
                                              borderwidth=1, highlightthickness=1, highlightbackground="#000000")
                user_message_label.pack(anchor=tk.E, padx=10, pady=5)
                # Store the prompt and response in the CSV file
                with open("feedback.csv", mode="a", newline='', encoding='utf-8') as file:
                    writer = csv.writer(file)
                    writer.writerow([user_input, prev_response])

                chatbot_response_label = tk.Label(chatbot_dialogue_content,
                                                  text="Chatbot: I apologize for the inconvenience. Let's move on to the next prompt.",
                                                  bg="#f2f2f2", fg="#000000",
                                                  wraplength=360, justify=tk.LEFT, relief=tk.RAISED, padx=10, pady=10,
                                                  borderwidth=1, highlightthickness=1, highlightbackground="#000000")
                chatbot_response_label.pack(anchor=tk.W, padx=10, pady=5)

            syes = tk.Button(window, text='Yes', command=second_yes)
            sno = tk.Button(window, text='No', command=second_no)
            syes.pack(side=tk.LEFT)  # pack starts packing widgets on the left
            sno.pack(side=tk.RIGHT)  # and keeps packing them to the next place available on the left
            syes.after(3000, lambda: yes.destroy())
            sno.after(3000, lambda: no.destroy())

        yes = tk.Button(window, text='Yes', command= first_yes)
        no = tk.Button(window, text='No', command= first_no)
        yes.pack(side=tk.LEFT)  # pack starts packing widgets on the left
        no.pack(side=tk.RIGHT)  # and keeps packing them to the next place available on the left
        yes.after(3000, lambda: yes.destroy())
        no.after(3000, lambda: no.destroy())

    canvas.yview_moveto(1.0)






# Create the main window
window = tk.Tk()
window.title("BHAGVATGITA GPT")
window.geometry("850x638")

# Load the background image
background_image = Image.open("grunge-pop-art-comic-versus.png")
background_photo = ImageTk.PhotoImage(background_image)

# Create a label for the background image
background_label = tk.Label(window, image=background_photo)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Create a frame for the header
header_frame = tk.Frame(window, bg="#f9a825")
header_frame.place(relx=0.2, rely=0, relwidth=0.7, relheight=0.1)

# Load and resize the header image
header_image = Image.open("hello.jpg")
header_image = header_image.resize((125, 125), Image.ANTIALIAS)
header_photo = ImageTk.PhotoImage(header_image)

# Create a label for the header image
header_image_label = tk.Label(header_frame, image=header_photo, bd=0)
header_image_label.pack(side=tk.LEFT, padx=10, pady=10)

# Create a label for the header text
header_text = tk.Label(header_frame, text="KRISHNA", fg="#ffffff", font=("MONO SPACE", 16, "bold"), bg="#f9a825")
header_text.pack(side=tk.LEFT, padx=10, pady=10)

# Create a frame for the chatbot dialogue
chatbot_dialogue = tk.Frame(window, bg="#f2f2f2")
chatbot_dialogue.place(relx=0.2, rely=0.1, relwidth=0.7, relheight=0.8)

# Create a vertical scrollbar
scrollbar = tk.Scrollbar(chatbot_dialogue)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Create a canvas to contain the chatbot dialogue and attach the scrollbar
canvas = tk.Canvas(chatbot_dialogue, bg="#f2f2f2", yscrollcommand=scrollbar.set)
canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
scrollbar.config(command=canvas.yview)

# Create a frame to hold the chatbot dialogue content
chatbot_dialogue_content = tk.Frame(canvas, bg="#f2f2f2")
canvas.create_window((150, 0), window=chatbot_dialogue_content, anchor=tk.NW)

# Configure the canvas to resize when the window size changes
chatbot_dialogue_content.bind("<Configure>", lambda event: canvas.configure(scrollregion=canvas.bbox("all")))

# Create a label for the chatbot introduction
intro_label = tk.Label(chatbot_dialogue_content,
                       text="Chatbot: Hello! I am a chatbot based on the teachings of Bhagavad Gita. Ask me anything!",
                       bg="#f2f2f2", fg="#000000", wraplength=360, justify=tk.LEFT, relief=tk.RAISED, padx=10,
                       pady=10, borderwidth=1, highlightthickness=1, highlightbackground="#000000")
intro_label.pack(anchor=tk.W, padx=10, pady=5)

# Create a frame for the footer
footer_frame = tk.Frame(window, bg="#f2f2f2")
footer_frame.place(relx=0.2, rely=0.9, relwidth=0.7, relheight=0.05)

# Create an input field for the user to enter messages
input_field = tk.Entry(footer_frame, bg="#ffffff", fg="#000000", relief=tk.RAISED, borderwidth=1)
input_field.pack(side=tk.LEFT, padx=10, pady=5, fill=tk.BOTH, expand=True)

# Create a button to send the user message
send_button = tk.Button(footer_frame, text="Send", bg="#00bcd4", fg="#ffffff", relief=tk.RAISED, borderwidth=0,
                        command=send_message)
send_button.pack(side=tk.RIGHT, padx=10, pady=5)

# Start the main event loop
window.mainloop()
