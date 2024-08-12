import base64
import tkinter as tk
from tkinter import messagebox

def text_to_base64(text):
    try:
        base64_encoded = base64.b64encode(text.encode('utf-8')).decode('utf-8')
        return base64_encoded
    except Exception as e:
        return f"인코딩 오류: {e}"
def base64_to_text(base64_string):
    try:
        padded_string = base64_string + '=' * ((4 - len(base64_string) % 4) % 4)
        decoded_text = base64.b64decode(padded_string).decode('utf-8', errors='replace')
        return decoded_text
    except Exception as e:
        return f"디코딩 오류: {e}"
def handle_encoding():
    text = text_entry.get("1.0", tk.END).strip()
    if not text:
        messagebox.showwarning("입력 오류", "인코딩할 텍스트를 입력하세요.")
        return
    
    base64_string = text_to_base64(text)
    result_entry.delete("1.0", tk.END)
    result_entry.insert(tk.END, base64_string)
def handle_decoding():
    base64_string = text_entry.get("1.0", tk.END).strip()
    if not base64_string:
        messagebox.showwarning("입력 오류", "디코딩할 Base64 문자열을 입력하세요.")
        return
    
    decoded_text = base64_to_text(base64_string)
    result_entry.delete("1.0", tk.END)
    result_entry.insert(tk.END, decoded_text)
def handle_batch_encoding():
    text = text_entry.get("1.0", tk.END).strip()
    if not text:
        messagebox.showwarning("입력 오류", "인코딩할 텍스트를 입력하세요.")
        return
    
    base64_string = text_to_base64(text)
    result_entry.delete("1.0", tk.END)
    result_entry.insert(tk.END, base64_string)
    text_entry.delete("1.0", tk.END)
    text_entry.insert(tk.END, base64_string)
def handle_batch_decoding():
    base64_string = text_entry.get("1.0", tk.END).strip()
    if not base64_string:
        messagebox.showwarning("입력 오류", "디코딩할 Base64 문자열을 입력하세요.")
        return
    
    decoded_text = base64_to_text(base64_string)
    result_entry.delete("1.0", tk.END)
    result_entry.insert(tk.END, decoded_text)
    text_entry.delete("1.0", tk.END)
    text_entry.insert(tk.END, decoded_text)
root = tk.Tk()
root.title("Base64 인코더/디코더")
text_label = tk.Label(root, text="인코딩할 텍스트 또는 디코딩할 Base64 입력:")
text_label.pack(pady=5)
text_entry = tk.Text(root, height=25, width=90)
text_entry.pack(pady=5)
result_label = tk.Label(root, text="결과:")
result_label.pack(pady=5)
result_entry = tk.Text(root, height=25, width=90)
result_entry.pack(pady=5)
encode_button = tk.Button(root, text="일반 인코딩", command=handle_encoding)
encode_button.pack(pady=5)

decode_button = tk.Button(root, text="일반 디코딩", command=handle_decoding)
decode_button.pack(pady=5)

batch_encode_button = tk.Button(root, text="연속 인코딩", command=handle_batch_encoding)
batch_encode_button.pack(pady=5)

batch_decode_button = tk.Button(root, text="연속 디코딩", command=handle_batch_decoding)
batch_decode_button.pack(pady=5)

root.mainloop()
