import tkinter as tk
from tkinter import messagebox, scrolledtext


animal_data = {
    "panda": {
        "name": "Giant Panda",
        "scientific_name": "Ailuropoda melanoleuca",
        "features": "Black-and-white fur, round face, gentle demeanor.",
        "habitat": "Mountainous forests in central China.",
        "diet": "Mainly bamboo (99%), sometimes small rodents or birds.",
        "lifespan": "20 years in the wild, up to 30 in captivity.",
        "size": "Up to 1.9 meters long, weighing 70–100 kg.",
        "fun_fact": "They spend up to 14 hours a day eating bamboo!"
    },
    "lion": {
        "name": "Lion",
        "scientific_name": "Panthera leo",
        "features": "Large cats with a mane (in males), muscular build.",
        "habitat": "Savannas, grasslands, and open woodlands in Africa.",
        "diet": "Carnivorous – mostly zebras, wildebeest, and other ungulates.",
        "lifespan": "10–14 years in the wild, up to 20 in captivity.",
        "size": "1.5 to 2.5 meters long, males weigh 150–250 kg.",
        "fun_fact": "Lions are the only cats that live in groups (prides)."
    },
    "elephant": {
        "name": "Elephant",
        "scientific_name": "Loxodonta africana / Elephas maximus",
        "features": "Trunk, tusks, huge ears, and thick grey skin.",
        "habitat": "Forests, savannas, and grasslands in Africa and Asia.",
        "diet": "Herbivorous – grasses, fruits, bark, and roots.",
        "lifespan": "60–70 years.",
        "size": "Up to 4 meters tall, weigh 4,000–7,000 kg.",
        "fun_fact": "Elephants can recognize themselves in mirrors!"
    },
    "giraffe": {
        "name": "Giraffe",
        "scientific_name": "Giraffa camelopardalis",
        "features": "Extremely long neck, long legs, spotted coat.",
        "habitat": "African savannas and open woodlands.",
        "diet": "Leaves, fruits, and flowers from tall trees.",
        "lifespan": "20–25 years.",
        "size": "Up to 5.5 meters tall, weigh around 800–1,200 kg.",
        "fun_fact": "Their neck has only 7 bones — same as humans!"
    },
    "tiger": {
        "name": "Tiger",
        "scientific_name": "Panthera tigris",
        "features": "Orange coat with black stripes, muscular body.",
        "habitat": "Forests, grasslands, and mangroves in Asia.",
        "diet": "Carnivorous – deer, wild boar, and buffalo.",
        "lifespan": "10–15 years in the wild.",
        "size": "Up to 3.3 meters long, 220–300 kg.",
        "fun_fact": "No two tigers have the same stripe pattern."
    }
}

def get_animal_info(animal):
    animal = animal.lower()
    if animal in animal_data:
        data = animal_data[animal]
        return (
            f"Name: {data['name']}\n"
            f"Scientific Name: {data['scientific_name']}\n"
            f"Features: {data['features']}\n"
            f"Habitat: {data['habitat']}\n"
            f"Diet: {data['diet']}\n"
            f"Lifespan: {data['lifespan']}\n"
            f"Size: {data['size']}\n"
            f"Fun Fact: {data['fun_fact']}"
        )
    else:
        return "Sorry, I don't have information on that animal yet. Try another one!"

def search_animal():
    animal = entry.get().strip()
    if not animal:
        messagebox.showwarning("Input Error", "Please enter an animal name.")
        return
    info = get_animal_info(animal)
    text_area.config(state='normal')
    text_area.delete(1.0, tk.END)
    text_area.insert(tk.INSERT, info)
    text_area.config(state='disabled')

root = tk.Tk()
root.title("Animal Info Chatbot")
root.geometry("500x450")
root.resizable(False, False)

label = tk.Label(root, text="Enter Animal Name:", font=("Arial", 12))
label.pack(pady=10)


entry = tk.Entry(root, font=("Arial", 14), width=30)
entry.pack(pady=5)

search_btn = tk.Button(root, text="Get Info", command=search_animal, font=("Arial", 12), bg="#4CAF50", fg="white")
search_btn.pack(pady=10)

text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, font=("Arial", 11), width=60, height=15, state='disabled')
text_area.pack(padx=10, pady=10)

root.mainloop()