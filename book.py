import tkinter as tk
import tkinter.messagebox
import webbrowser


class Book:
	def __init__(self, root):
		root.title("Address Book")


		self.add_var = tk.StringVar()
		self.name_var = tk.StringVar()
		self.num_var = tk.StringVar()
		self.email_var = tk.StringVar()
		self.to = tk.StringVar()
		self.fr = tk.StringVar()

		### Frames
		entry_frame = tk.Frame(root)
		entry_frame.grid(row=0, column=0)

		button_frame = tk.Frame(root)
		button_frame.grid(row=1, column=0)

		list_names_frame = tk.Frame(root)
		list_names_frame.grid(row=2, column=0)

		###

		### Setting up of email button and map button
		email = tk.Button(entry_frame, text="send email" ,bg="orange")
		email.grid(row=3, column=4)
		email.bind("<Button-1>", self.to_email)

		map_but = tk.Button(entry_frame, text=" map" ,bg="orange")
		map_but.grid(row=1, column=4, sticky=tk.W)
		map_but.bind("<Button-1>", self.to_map)

		###

		### Setting up of all labels and entry boxes
		name = tk.Label(entry_frame, text="Name", padx=10, pady=10, fg="blue")
		name.grid(row=0, column=0, sticky='E')

		address = tk.Label(entry_frame, text="Address", padx=10, pady=10, fg="blue")
		address.grid(row=1, column=0, sticky='E')

		phone = tk.Label(entry_frame, text="Phone", padx=10, pady=10, fg="blue")
		phone.grid(row=2, column=0, sticky='E')

		email = tk.Label(entry_frame, text="Email", padx=10, pady=10, fg="blue")
		email.grid(row=3, column=0, sticky='E')

		en_name = tk.Entry(entry_frame, textvariable=self.name_var)
		en_name.grid(row=0, column=1)

		en_address = tk.Entry(entry_frame, textvariable=self.add_var)
		en_address.grid(row=1, column=1)

		en_phone = tk.Entry(entry_frame, textvariable=self.num_var)
		en_phone.grid(row=2, column=1)

		en_email = tk.Entry(entry_frame, textvariable=self.email_var)
		en_email.grid(row=3, column=1)

		save = tk.Button(button_frame, text="Save", padx=10, pady=10, fg="green")
		save.grid(row=0, column=0)
		save.bind("<Button-1>", self.save)

		delete = tk.Button(button_frame, text="Delete", padx=10, pady=10, fg="red")
		delete.grid(row=0, column=1)
		delete.bind("<Button-1>", self.delete)

		clear = tk.Button(button_frame, text="Clear", padx=10, pady=10)
		clear.grid(row=0, column=2)
		clear.bind("<Button-1>", self.clear)

		view_con = tk.Button(list_names_frame, text="View Contact information", padx=10, pady=10, fg="red")
		view_con.grid(row=3, column=0)
		view_con.bind("<Button-1>", self.view_contact)
		###

		### List box setup
		label1 = tk.Label(list_names_frame, text="List of available contacts:", fg="blue")
		label1.grid(row=0, column=0, padx=10, pady=4)

		self.list_box = tk.Listbox(list_names_frame, selectmode="EXTENDED")
		self.list_box.grid(row=2, column=0)

		yscroll = tk.Scrollbar(list_names_frame, orient=tk.VERTICAL)
		self.list_box['yscrollcommand'] = yscroll.set
		yscroll['command'] = self.list_box.yview

		yscroll.grid(row=2, column=0, sticky=tk.E, rowspan=2)
		### Fill list box with names

		file2 = open("File1.txt", "r")
		x = file2.readlines()
		file2.close()
		for i in x:
			i = i.split(",")
			name = i[0]
			self.list_box.insert(1, name)


	def save(self, event):
		data_file2 = open("File1.txt", "r")
		read = data_file2.readlines()
		data_file2.close()
		data_file = open("File1.txt", "w")
		
		if len(self.add_var.get().strip()) == 0 or len(self.num_var.get().strip()) == 0 or len(
				self.email_var.get().strip()) == 0 or len(self.name_var.get().strip()) == 0:
			tk.messagebox.showinfo("Not saved", "Please complete all details.")
		else:
			wir = "{0},{1},{2},{3}\n".format(self.name_var.get().rstrip(), self.add_var.get().rstrip(), self.num_var.get().rstrip(),
				self.email_var.get().rstrip())
			x = self.name_var.get()
			for name in read:
				name2 = name.split(",")
				name2 = name2[0]
				if x == name2:
					answer = tk.messagebox.askquestion("Warning", "Conatact already Exists. Are you sure you want to replace with new info?")
					if answer == "yes":
						data_file.write(wir)
						return None
					else:
						return None

			data_file.write(wir)
			tk.messagebox.showinfo("Save", "Saved")
			self.clear(event)
			self.list_box.insert(1, x)
			
			

	def delete(self, event):
		answer = tkinter.messagebox.askquestion("Warning!", "Are you sure you want to delete?")
		x2 = self.list_box.get(tk.ACTIVE)
		count = 0
		if answer == "yes":
			try:
				if self.list_box.get(tk.ACTIVE) != "":
					self.list_box.delete(self.list_box.curselection())
					data_file = open("File1.txt", "r+")
					file = data_file.readlines()
					data_file.close()
					write_file = open("File1.txt", "w")
					for i in file:
						x = i.split(",")
						x = x[0]
						if x == x2:
							if count == 0:
								tk.messagebox.showinfo("File", "Deleted")
								count += 1
								continue
						else:
							write_file.write(i)
					write_file.close()
				else:
					tk.messagebox.showinfo("Error", "Please select contact to delete.")
			except:
				tk.messagebox.showinfo("Error", "Please select contact to delete.")


	def clear(self, val):
		self.add_var.set("")
		self.name_var.set("")
		self.num_var.set("")
		self.email_var.set("")


	def view_contact(self, event):
		file = open("File1.txt", "r")
		x = file.readlines()
		file.close()
		select = self.list_box.get(tk.ACTIVE)
		for i in x:
			if select in i:
				i = i.split(",")
				self.name_var.set(i[0])
				self.add_var.set(i[1])
				self.num_var.set(i[2])
				self.email_var.set(i[3])


	def to_map(self, event):
		address = self.add_var.get()
		if len(address) == 0:
			tk.messagebox.showinfo("Error", "Please enter an address.")
			return None
		address = address.split(' ')
		final = ""
		for i in address:
			i = i+"+"
			final += i
		final = final.rstrip("+")
		send = webbrowser.open("https://www.google.co.za/maps/place/"+final)
		

	def to_email(self, event):
		email_win = tk.Tk()
		email_win.title("Email")

		info_frame = tk.Frame(email_win)
		info_frame.grid(row=0, column=0)

		new_frame = tk.Frame(email_win)
		new_frame.grid(row=1, column=0)

		message_frame = tk.Frame(email_win)
		message_frame.grid(row=2, column=0)

		message = tk.Label(message_frame, text="Enter message")
		message.grid(row=0, column=0)

		message_entry = tk.Entry(message_frame)
		message_entry.grid(row=1, column=0)

		send = tk.Button(message_frame, text="Send", fg="red")
		send.grid(rowspan=2)


		from_label = tk.Label(info_frame, text="From:")
		from_label.grid(row=0, column=0, sticky=tk.W)

		to_label = tk.Label(new_frame, text="To:   {}".format(self.email_var.get()))
		to_label.grid(row=0, column=0, sticky=tk.W, pady=10)

		### Entries
		from_entr = tk.Entry(info_frame, textvariable=self.fr)
		from_entr.grid(row=0, column=1, sticky=tk.W)
		###






win = tk.Tk()
x = Book(win)
win.mainloop()
