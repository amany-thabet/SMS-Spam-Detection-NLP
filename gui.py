import tkinter as tk
import pickle

# ==============================
# Load models
# ==============================
nb_model = pickle.load(open("nb.pkl", "rb"))
log_model = pickle.load(open("log.pkl", "rb"))
svm_model = pickle.load(open("svm.pkl", "rb"))
rf_model = pickle.load(open("rf.pkl", "rb"))
knn_model = pickle.load(open("knn.pkl", "rb"))

vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

# ==============================
# Prediction function
# ==============================
def predict(model, text):
    text_vec = vectorizer.transform([text])
    result = model.predict(text_vec)[0]
    return "Spam" if result == 1 else "Ham"

# ==============================
# Button Function
# ==============================
def process_text():
    text = input_text.get("1.0", tk.END)

    result1.set(predict(nb_model, text))
    result2.set(predict(log_model, text))
    result3.set(predict(svm_model, text))
    result4.set(predict(rf_model, text))
    result5.set(predict(knn_model, text))

# ==============================
# GUI
# ==============================
root = tk.Tk()
root.title("SMS Spam Detection")
root.geometry("600x400")

# Input
tk.Label(root, text="Input:").pack(anchor="w", padx=10)
input_text = tk.Text(root, height=4)
input_text.pack(fill="x", padx=10)

# Button
tk.Button(root, text="Process", command=process_text, bg="lightblue").pack(pady=10)

# Results
result1 = tk.StringVar()
result2 = tk.StringVar()
result3 = tk.StringVar()
result4 = tk.StringVar()
result5 = tk.StringVar()

def create_row(label, var):
    frame = tk.Frame(root)
    frame.pack(fill="x", padx=10, pady=3)
    
    tk.Label(frame, text=label, width=15).pack(side="left")
    tk.Entry(frame, textvariable=var).pack(fill="x", expand=True)

create_row("Naive Bayes:", result1)
create_row("Logistic Reg:", result2)
create_row("SVM:", result3)
create_row("Random Forest:", result4)
create_row("KNN:", result5)

root.mainloop()