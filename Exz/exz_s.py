'''Трекер активності
Створіть програму для відстеження щоденної активності користувача (наприклад, кількість кроків, витрачені калорії).
Користувачі можуть вводити свої дані та переглядати історію своєї активності.
Програма повинна мати можливість відображати статистику активності за вибраний період.'''


# import tkinter as tk
# from tkinter import messagebox
# from datetime import datetime
# import pandas as pd
# import matplotlib.pyplot as plt
# from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
#
# class ActivityTracker:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Activity Tracker")
#
#         self.activity_data = []
#         self.create_widgets()
#
#     def create_widgets(self):
#         # Entry for entering daily activity
#         self.activity_entry = tk.Entry(self.root, width=10)
#         self.activity_entry.grid(row=0, column=0, padx=10, pady=10)
#
#         # Entry for entering weight
#         self.weight_entry = tk.Entry(self.root, width=10)
#         self.weight_entry.grid(row=0, column=1, padx=10, pady=10)
#
#         # Button to submit daily activity
#         submit_button = tk.Button(self.root, text="Submit Activity", command=self.submit_activity)
#         submit_button.grid(row=0, column=2, padx=10, pady=10)
#
#         # Text widget to display activity log
#         self.log_text = tk.Text(self.root, width=40, height=10)
#         self.log_text.grid(row=1, column=0, columnspan=3, pady=10)
#
#         # Button to view history
#         history_button = tk.Button(self.root, text="View History", command=self.view_history)
#         history_button.grid(row=2, column=0, columnspan=3, pady=10)
#
#         # Entry for entering date for viewing statistics
#         self.date_entry = tk.Entry(self.root, width=10)
#         self.date_entry.insert(0, datetime.now().strftime("%Y-%m-%d"))  # Set default value to current date
#         self.date_entry.grid(row=3, column=0, padx=10, pady=10)
#
#         # Button to view statistics for a selected period
#         stats_button = tk.Button(self.root, text="View Statistics", command=self.view_statistics)
#         stats_button.grid(row=3, column=1, padx=10, pady=10)
#
#         # Button to visualize data
#         visualize_button = tk.Button(self.root, text="Visualize Data", command=self.visualize_data)
#         visualize_button.grid(row=3, column=2, padx=10, pady=10)
#
#     def submit_activity(self):
#         try:
#             activity_value = float(self.activity_entry.get())
#             weight_value = float(self.weight_entry.get())
#         except ValueError:
#             messagebox.showerror("Error", "Please enter valid numerical values for activity and weight.")
#             return
#
#         current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#         log_entry = {"Value": activity_value, "Weight": weight_value, "Date": current_date}
#         self.activity_data.append(log_entry)
#
#         # Update the log display
#         self.update_log_display()
#
#         messagebox.showinfo("Success", f"Activity recorded successfully.")
#
#     def view_history(self):
#         history_text = "\n".join([f"{entry['Value']} units, Weight: {entry['Weight']} kg - {entry['Date']}" for entry in self.activity_data])
#         if not history_text:
#             history_text = "No activity recorded yet."
#         messagebox.showinfo("Activity History", history_text)
#
#     def view_statistics(self):
#         selected_date = self.date_entry.get()
#         try:
#             activity_date = pd.to_datetime(selected_date, format="%Y-%m-%d")
#         except ValueError:
#             messagebox.showerror("Error", "Please enter a valid date (YYYY-MM-DD) for statistics.")
#             return
#
#         df = pd.DataFrame(self.activity_data)
#         mask = (df['Date'] >= activity_date) & (df['Date'] < activity_date + pd.to_timedelta('1 day'))
#
#         selected_data = df.loc[mask]
#
#         if selected_data.empty:
#             messagebox.showinfo("Statistics", f"No data available for {selected_date}.")
#         else:
#             statistics_text = f"Statistics for {selected_date}:\n"
#             statistics_text += f"Total activity: {selected_data['Value'].sum()} units\n"
#             statistics_text += f"Average activity: {selected_data['Value'].mean()} units\n"
#             statistics_text += f"Average weight: {selected_data['Weight'].mean()} kg\n"
#             messagebox.showinfo("Statistics", statistics_text)
#
#     def visualize_data(self):
#         if not self.activity_data:
#             messagebox.showinfo("Information", "No data available for visualization.")
#             return
#
#         df = pd.DataFrame(self.activity_data)
#
#         try:
#             df['Date'] = pd.to_datetime(df['Date'])
#         except ValueError:
#             messagebox.showerror("Error", "Error converting 'Date' to datetime.")
#             return
#
#         # Plotting using pandas
#         fig, ax = plt.subplots(figsize=(8, 4))
#         df.plot(x='Date', y='Value', kind='bar', ax=ax, rot=45)
#         ax.set_title('Activity Visualization')
#         ax.set_xlabel('Date')
#         ax.set_ylabel('Value')
#
#         # Embedding the plot in Tkinter
#         canvas = FigureCanvasTkAgg(fig, master=self.root)
#         canvas_widget = canvas.get_tk_widget()
#         canvas_widget.grid(row=4, column=0, columnspan=3, pady=10)
#
#
#     def update_log_display(self):
#         # Clear the text widget
#         self.log_text.delete(1.0, tk.END)
#
#         # Insert each log entry into the text widget
#         for entry in self.activity_data:
#             log_entry = f"{entry['Value']} units, Weight: {entry['Weight']} kg - {entry['Date']}\n"
#             self.log_text.insert(tk.END, log_entry)
#
# if __name__ == "__main__":
#     root = tk.Tk()
#     app = ActivityTracker(root)
#     root.mainloop()


import tkinter as tk
from tkinter import messagebox
from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class ActivityTracker:
    def __init__(self, root):
        self.root = root
        self.root.title("Activity Tracker")
        self.activity_data = []
        self.create_widgets()

    def create_widgets(self):
        self.activity_entry = self.create_entry(0, 0)
        self.weight_entry = self.create_entry(0, 1)

        self.create_button("Submit Activity", self.submit_activity, 0, 2)
        self.log_text = self.create_text(1, 0, 3)

        self.date_entry = self.create_entry(3, 0)

        self.create_button("View History", self.view_history, 2, 0, 3)
        self.create_button("View Statistics", self.view_statistics, 3, 1)
        self.create_button("Visualize Data", self.visualize_data, 3, 2)

    def create_label(self, text, row, column):
        label = tk.Label(self.root, text=text)
        label.grid(row=row, column=column, padx=10, pady=10)
        return label

    def create_entry(self, row, column):
        entry = tk.Entry(self.root, width=10)
        entry.grid(row=row, column=column, padx=10, pady=10)
        return entry

    def create_button(self, text, command, row, column, columnspan=1):
        button = tk.Button(self.root, text=text, command=command)
        button.grid(row=row, column=column, columnspan=columnspan, padx=10, pady=10)

    def create_text(self, row, column, rowspan):
        text_widget = tk.Text(self.root, width=40, height=10)
        text_widget.grid(row=row, column=column, columnspan=rowspan, pady=10)
        return text_widget

    def submit_activity(self):
        try:
            activity_value = float(self.activity_entry.get())
            weight_value = float(self.weight_entry.get())
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numerical values for activity and weight.")
            return

        current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = {"Value": activity_value, "Weight": weight_value, "Date": current_date}
        self.activity_data.append(log_entry)

        self.update_log_display()
        messagebox.showinfo("Success", f"Activity recorded successfully.")

    def view_history(self):
        history_text = self.format_history_text()
        messagebox.showinfo("Activity History", history_text)

    def view_statistics(self):
        selected_date = self.date_entry.get()
        try:
            activity_date = pd.to_datetime(selected_date, format="%Y-%m-%d")
        except ValueError:
            messagebox.showerror("Error (YYYY-MM-DD)")
            return

        df = pd.DataFrame(self.activity_data)
        mask = (df['Date'] >= activity_date) & (df['Date'] < activity_date + pd.to_timedelta('1 day'))

        selected_data = df.loc[mask]

        if selected_data.empty:
            messagebox.showinfo("Statistics", f"No data available for {selected_date}.")
        else:
            statistics_text = self.format_statistics_text(selected_data)
            messagebox.showinfo("Statistics", statistics_text)

    def visualize_data(self):
        if not self.activity_data:
            messagebox.showinfo("Information", "No data available for visualization.")
            return

        df = pd.DataFrame(self.activity_data)

        try:
            df['Date'] = pd.to_datetime(df['Date'])
        except ValueError:
            messagebox.showerror("Error", "Error converting 'Date' to datetime.")
            return

        fig, ax = plt.subplots(figsize=(8, 4))
        df.plot(x='Date', y='Value', kind='bar', ax=ax, rot=45)
        ax.set_title('Activity Visualization')
        ax.set_xlabel('Date')
        ax.set_ylabel('Value')

        canvas = FigureCanvasTkAgg(fig, master=self.root)
        canvas_widget = canvas.get_tk_widget()
        canvas_widget.grid(row=4, column=0, columnspan=3, pady=10)

    def update_log_display(self):
        self.log_text.delete(1.0, tk.END)
        history_text = self.format_history_text()
        self.log_text.insert(tk.END, history_text)

    def format_history_text(self):
        return "\n".join([f"{entry['Value']} units, Weight: {entry['Weight']} kg - {entry['Date']}" for entry in self.activity_data]) or "No activity recorded yet."

    def format_statistics_text(self, selected_data):
        return f"Statistics for {selected_date}:\n" \
               f"Total activity: {selected_data['Value'].sum()} units\n" \
               f"Average activity: {selected_data['Value'].mean()} units\n" \
               f"Average weight: {selected_data['Weight'].mean()} kg\n"


if __name__ == "__main__":
    root = tk.Tk()
    app = ActivityTracker(root)
    root.mainloop()
