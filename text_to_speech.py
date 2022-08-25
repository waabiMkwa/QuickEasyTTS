import pyttsx3,os



def sound_text_to_speech(text,_read_aloud=False):
    """
    Converts text to speech
    """

    full_text = ""

    audio_reader = pyttsx3.init()
    audio_reader.setProperty('rate', 155)

    lines = text.split('\n')
    # eliminate empty lines
    lines = [line for line in lines if line]
    print("Beginning to speak...")

    for line in lines:
        print(line)
        full_text += line + "\n"
        if _read_aloud:
            audio_reader.say(line)
            audio_reader.runAndWait()
    
    print("Finished speaking.\nSaving to file...")
    audio_reader.save_to_file(full_text, "output.mp3")
    audio_reader.runAndWait()
    print("Saved to file.")

def select_txt_file():
    """
    Selects a text file to convert to speech.
    Displays the files in the directory, and asks the user to select one.
    Returns the selected file.
    """
    print("Select a text file to convert to speech.")
    print("Files in the directory:")
    files = {}
    count = 0
    for file in os.listdir():
        if file.endswith(".txt"):
            print(str(count) + ": " + file)
            
            files[count] = file
            count += 1
    
    while True:
        try:
            choice = int(input("Enter the number of the file: "))
            if choice in files:
                return files[choice]
            else:
                print("Invalid choice.")
        except ValueError:
            print("Invalid choice.")
        
    
def main():
    """
    Main function.
    """
    file = select_txt_file()
    # open as utf-8 to avoid encoding errors
    with open(file, 'r', encoding='utf-8') as f:
        text = f.read()
    
    print("Converting to speech...")
    try:
        sound_text_to_speech(text)
    except UnicodeDecodeError:
        print("UnicodeDecodeError. Trying once more.")
        # to handle the error when the text is not in utf-8, we convert it to utf-8
        text = text.encode('utf-8')
        sound_text_to_speech(text)
    input("\n\tText to speech complete. Press enter to exit...")


if __name__ == "__main__":
    main()
    