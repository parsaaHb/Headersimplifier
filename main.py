# main.py
import tkinter as tk
from tkinter import messagebox, scrolledtext
from fetching import get_request_headers

# Enhanced header dictionary
header_info = {
    "User-Agent": {
        "explanation": "Identifies the client making the request (e.g., browser, Python script).",
        "common_values": [
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/XX.X.X.X Safari/537.36",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 Safari/605.1.15",
            "python-requests/2.32.5",
            "curl/7.79.1"
        ]
    },
    "Accept-Encoding": {
        "explanation": "Lists compression methods the client supports.",
        "common_values": [
            "gzip, deflate",
            "br",
            "compress",
            "*"
        ]
    },
    "Accept": {
        "explanation": "Tells the server what content types the client can understand.",
        "common_values": [
            "*/*",
            "text/html",
            "application/json",
            "image/webp,image/apng,*/*"
        ]
    },
    "Connection": {
        "explanation": "Controls whether the network connection stays open or closes.",
        "common_values": [
            "keep-alive",
            "close"
        ]
    }
}

# HTTP method explanations
method_explanations = {
    "GET": "GET requests retrieve data from a server. This is the most common method for fetching webpages.",
    "POST": "POST requests send data to a server, often to submit forms or upload data.",
    "PUT": "PUT requests update data on a server.",
    "DELETE": "DELETE requests remove data from a server.",
    "HEAD": "HEAD requests retrieve only headers, without the response body.",
    "OPTIONS": "OPTIONS requests ask the server which methods are allowed on a resource.",
    "PATCH": "PATCH requests apply partial modifications to a resource."
}

def fetch_headers():
    url = url_entry.get().strip()
    
    if not url:
        messagebox.showerror("Error", "Please enter a URL.")
        return
    
    try:
        method, reqheader = get_request_headers(url)
        
        # Clear text area
        text_area.config(state=tk.NORMAL)
        text_area.delete(1.0, tk.END)
        
        # Show HTTP method + explanation
        method_expl = method_explanations.get(method, "This is an HTTP method used for the request.")
        text_area.insert(tk.END, f"Method: {method}\n → {method_expl}\n\n")
        
        for key, value in reqheader.items():
            info = header_info.get(key)
            if info:
                explanation = info["explanation"]
                common_values = ", ".join(info["common_values"])
                text_area.insert(tk.END, f"{key}: {value}\n → {explanation}\n → Common values: {common_values}\n\n")
            else:
                text_area.insert(tk.END, f"{key}: {value}\n → No explanation available.\n\n")
        
        text_area.config(state=tk.DISABLED)
    
    except Exception as e:
        messagebox.showerror("Error", f"Could not fetch headers:\n{e}")


root = tk.Tk()
root.title("Request Headers Viewer")
root.geometry("650x450")
root.configure(bg="#f0f0f0")  


url_frame = tk.Frame(root, bg="#f0f0f0")
url_frame.pack(pady=5)

url_label = tk.Label(url_frame, text="Enter URL:", font=("Courier", 10), fg="#000000", bg="#f0f0f0")
url_label.pack(side=tk.LEFT, padx=5)

url_entry = tk.Entry(url_frame, width=50, font=("Courier", 10))
url_entry.pack(side=tk.LEFT, padx=5)

fetch_button = tk.Button(url_frame, text="Start ", command=fetch_headers, font=("Courier", 10))
fetch_button.pack(side=tk.LEFT, padx=5)


text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=80, height=20, font=("Courier", 10))
text_area.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
text_area.config(state=tk.DISABLED)

# Run UI
root.mainloop()
