import tkinter as tk
import csv

def read_table_from_csv(file_path):
    table = []
    with open(file_path, 'r') as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            if len(row) >= 2:  # Check if the row has at least 2 columns
                table.append((row[0], row[1]))
    return table

def perform_search():
    # Clear the output text window
    output_text.delete('1.0', tk.END)

    # Get the text from the input text window
    text = input_text.get('1.0', tk.END)

    # Perform search based on the table
    for search_term, output in table:
        if search_term in text:
            output_text.insert(tk.END, output + '\n')

# Read the table from CSV file
table = read_table_from_csv('E:\\czarny\\OneDrive\\OneDrive - Ingram Micro\\dane\\data.csv')

# Create the main window
window = tk.Tk()
window.title('Text Search')

# Create the input text window
input_text = tk.Text(window, height=10, width=50)
input_text.pack()

# Create the output text window
output_text = tk.Text(window, height=10, width=50)
output_text.pack()

# Create the search button
search_button = tk.Button(window, text='Search', command=perform_search)
search_button.pack()

# Start the GUI event loop
window.mainloop()
