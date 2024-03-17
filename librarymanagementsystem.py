import tkinter as tk
from tkinter import ttk, messagebox

class Library:
    def __init__(self):
        self.books = {
            '1': {'title': 'Python Programming', 'author': 'John Smith', 'status': 'available'},
            '2': {'title': 'Introduction to Java', 'author': 'Emily Brown', 'status': 'available'},
            '3': {'title': 'Data Structures and Algorithms', 'author': 'David Lee', 'status': 'unavailable'}
        }
        self.logged_in_user = None

    def update_book_display(self):
        popup = tk.Toplevel()
        popup.title("All Books")
        popup.geometry("600x400")
        popup.configure(bg="#f0f0f0")  # Set background color

        tree = ttk.Treeview(popup, columns=("ID", "Title", "Author", "Status"), show="headings")
        tree.heading("ID", text="ID")
        tree.heading("Title", text="Title")
        tree.heading("Author", text="Author")
        tree.heading("Status", text="Status")

        for book_id, book_info in self.books.items():
            status_text = "Available" if book_info['status'] == 'available' else "Unavailable"
            bg_color = "#90EE90" if book_info['status'] == 'available' else "#FFA07A"
            tree.insert("", "end", values=(book_id, book_info['title'], book_info['author'], status_text), tags=(bg_color,))

        tree.tag_configure("#90EE90", background="#90EE90")
        tree.tag_configure("#FFA07A", background="#FFA07A")
        tree.pack(expand=True, fill=tk.BOTH)

    def add_book(self, book_id, title, author):
        if book_id not in self.books:
            self.books[book_id] = {'title': title, 'author': author, 'status': 'available'}
            messagebox.showinfo('Success', f'Book "{title}" by {author} added successfully!')
            self.update_book_display()
        else:
            messagebox.showerror('Error', 'Book with the same ID already exists.')

    def remove_book(self, book_id):
        if book_id in self.books:
            del self.books[book_id]
            messagebox.showinfo('Success', f'Book with ID {book_id} removed successfully!')
            self.update_book_display()
        else:
            messagebox.showerror('Error', 'Book not found.')

    def issue_book(self, book_id):
        if book_id in self.books:
            if self.books[book_id]['status'] == 'available':
                self.books[book_id]['status'] = 'unavailable'
                messagebox.showinfo('Success', f'Book with ID {book_id} issued successfully!')
            else:
                messagebox.showerror('Error', 'Book is not available for issue.')
        else:
            messagebox.showerror('Error', 'Book not found.')

    def return_book(self, book_id):
        if book_id in self.books:
            if self.books[book_id]['status'] == 'unavailable':
                self.books[book_id]['status'] = 'available'
                messagebox.showinfo('Success', f'Book with ID {book_id} returned successfully!')
            else:
                messagebox.showerror('Error', 'Book is already available.')
        else:
            messagebox.showerror('Error', 'Book not found.')

    def show_book_details(self):
        total_books = len(self.books)
        available_books = sum(1 for book in self.books.values() if book['status'] == 'available')
        issued_books = total_books - available_books

        popup = tk.Toplevel()
        popup.title("Book Details")
        popup.geometry("300x150")
        popup.configure(bg="#f0f0f0")  # Set background color

        label_total = tk.Label(popup, text=f"Total Books: {total_books}", bg="#f0f0f0")
        label_total.pack()

        label_available = tk.Label(popup, text=f"Available Books: {available_books}", bg="#f0f0f0")
        label_available.pack()

        label_issued = tk.Label(popup, text=f"Issued Books: {issued_books}", bg="#f0f0f0")
        label_issued.pack()

def add_book_clicked():
    book_id = add_book_id_entry.get()
    title = add_book_title_entry.get()
    author = add_book_author_entry.get()
    library.add_book(book_id, title, author)

def remove_book_clicked():
    book_id = remove_book_id_entry.get()
    library.remove_book(book_id)

def issue_book_clicked():
    book_id = issue_book_id_entry.get()
    library.issue_book(book_id)

def return_book_clicked():
    book_id = return_book_id_entry.get()
    library.return_book(book_id)

library = Library()

root = tk.Tk()
root.title("Library Management System")
root.geometry("600x500")
root.configure(bg="#f0f0f0")  # Set background color

# Title
title_label = tk.Label(root, text="Library Management System", font=("Helvetica", 20, "bold"), bg="#f0f0f0")
title_label.pack(pady=20)

# Add Book Frame
add_book_frame = tk.LabelFrame(root, text="Add Book", font=("Helvetica", 14), bg="#f0f0f0")
add_book_frame.pack(pady=20, padx=20, fill="both", expand="yes")

add_book_id_label = tk.Label(add_book_frame, text="Book ID:", bg="#f0f0f0")
add_book_id_label.grid(row=0, column=0)
add_book_id_entry = tk.Entry(add_book_frame)
add_book_id_entry.grid(row=0, column=1)

add_book_title_label = tk.Label(add_book_frame, text="Title:", bg="#f0f0f0")
add_book_title_label.grid(row=1, column=0)
add_book_title_entry = tk.Entry(add_book_frame)
add_book_title_entry.grid(row=1, column=1)

add_book_author_label = tk.Label(add_book_frame, text="Author:", bg="#f0f0f0")
add_book_author_label.grid(row=2, column=0)
add_book_author_entry = tk.Entry(add_book_frame)
add_book_author_entry.grid(row=2, column=1)

add_book_button = tk.Button(add_book_frame, text="Add Book", command=add_book_clicked, bg="#6495ED", fg="white")
add_book_button.grid(row=3, columnspan=2, pady=10)

# Remove Book Frame
remove_book_frame = tk.LabelFrame(root, text="Remove Book", font=("Helvetica", 14), bg="#f0f0f0")
remove_book_frame.pack(pady=20, padx=20, fill="both", expand="yes")

remove_book_id_label = tk.Label(remove_book_frame, text="Book ID:", bg="#f0f0f0")
remove_book_id_label.grid(row=0, column=0)
remove_book_id_entry = tk.Entry(remove_book_frame)
remove_book_id_entry.grid(row=0, column=1)

remove_book_button = tk.Button(remove_book_frame, text="Remove Book", command=remove_book_clicked, bg="#DC143C", fg="white")
remove_book_button.grid(row=1, columnspan=2, pady=10)

# Issue Book Frame
issue_book_frame = tk.LabelFrame(root, text="Issue Book", font=("Helvetica", 14), bg="#f0f0f0")
issue_book_frame.pack(pady=20, padx=20, fill="both", expand="yes")

issue_book_id_label = tk.Label(issue_book_frame, text="Book ID:", bg="#f0f0f0")
issue_book_id_label.grid(row=0, column=0)
issue_book_id_entry = tk.Entry(issue_book_frame)
issue_book_id_entry.grid(row=0, column=1)

issue_book_button = tk.Button(issue_book_frame, text="Issue Book", command=issue_book_clicked, bg="#32CD32", fg="white")
issue_book_button.grid(row=1, columnspan=2, pady=10)

# Return Book Frame
return_book_frame = tk.LabelFrame(root, text="Return Book", font=("Helvetica", 14), bg="#f0f0f0")
return_book_frame.pack(pady=20, padx=20, fill="both", expand="yes")

return_book_id_label = tk.Label(return_book_frame, text="Book ID:", bg="#f0f0f0")
return_book_id_label.grid(row=0, column=0)
return_book_id_entry = tk.Entry(return_book_frame)
return_book_id_entry.grid(row=0, column=1)

return_book_button = tk.Button(return_book_frame, text="Return Book", command=return_book_clicked, bg="#FF8C00", fg="white")
return_book_button.grid(row=1, columnspan=2, pady=10)

# View Books Button
view_books_button = tk.Button(root, text="View Books", font=("Helvetica", 16), command=library.update_book_display, bg="#6495ED", fg="white")
view_books_button.pack()

root.mainloop()
