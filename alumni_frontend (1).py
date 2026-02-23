import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector


# -------- DATABASE CONNECTION --------

conn = mysql.connector.connect(
    host="localhost",
    user="root",          # change if needed
    password="anushka",      # change mysql password
    database="AlumniDB"
)

cursor = conn.cursor()


# -------- MAIN WINDOW --------

root = tk.Tk()
root.title("Alumni Management System")
root.geometry("900x600")
root.configure(bg="lightblue")


# -------- VARIABLES --------

name_var = tk.StringVar()
email_var = tk.StringVar()
phone_var = tk.StringVar()
year_var = tk.StringVar()
dept_var = tk.StringVar()
job_var = tk.StringVar()
company_var = tk.StringVar()
search_var = tk.StringVar()


# -------- FUNCTIONS --------

def add_alumni():

    try:

        sql = """INSERT INTO Alumni
        (name,email,phone,passing_year,
        department_id,job_title,company)

        VALUES(%s,%s,%s,%s,%s,%s,%s)
        """

        values = (
            name_var.get(),
            email_var.get(),
            phone_var.get(),
            year_var.get(),
            dept_var.get(),
            job_var.get(),
            company_var.get()
        )

        cursor.execute(sql, values)
        conn.commit()

        messagebox.showinfo("Success","Alumni Added")

        view_data()

    except Exception as e:

        messagebox.showerror("Error",str(e))


def view_data():

    cursor.execute("SELECT * FROM Alumni")

    rows = cursor.fetchall()

    table.delete(*table.get_children())

    for row in rows:
        table.insert("",tk.END,values=row)



def delete_alumni():

    selected = table.focus()

    if selected == "":
        messagebox.showwarning("Warning","Select Record")
        return

    data = table.item(selected)

    alumni_id = data["values"][0]

    cursor.execute(
        "DELETE FROM Alumni WHERE alumni_id=%s",
        (alumni_id,)
    )

    conn.commit()

    view_data()



def update_alumni():

    selected = table.focus()

    if selected == "":
        messagebox.showwarning("Warning","Select Record")
        return

    alumni_id = table.item(selected)["values"][0]

    sql = """UPDATE Alumni

    SET name=%s,
    email=%s,
    phone=%s,
    passing_year=%s,
    department_id=%s,
    job_title=%s,
    company=%s

    WHERE alumni_id=%s
    """

    values = (

        name_var.get(),
        email_var.get(),
        phone_var.get(),
        year_var.get(),
        dept_var.get(),
        job_var.get(),
        company_var.get(),
        alumni_id
    )

    cursor.execute(sql,values)

    conn.commit()

    messagebox.showinfo("Updated","Record Updated")

    view_data()



def select_record(event):

    selected = table.focus()

    data = table.item(selected)

    row = data["values"]

    if row:

        name_var.set(row[1])
        email_var.set(row[2])
        phone_var.set(row[3])
        year_var.set(row[4])
        dept_var.set(row[5])
        job_var.set(row[6])
        company_var.set(row[7])



def search_alumni():

    keyword = search_var.get()

    sql = """
    SELECT * FROM Alumni
    WHERE name LIKE %s
    """

    cursor.execute(sql,('%'+keyword+'%',))

    rows = cursor.fetchall()

    table.delete(*table.get_children())

    for row in rows:

        table.insert("",tk.END,values=row)



# -------- FORM --------

frame = tk.Frame(root,bg="lightblue")
frame.pack(pady=10)


labels = [

("Name",name_var),
("Email",email_var),
("Phone",phone_var),
("Passing Year",year_var),
("Department ID",dept_var),
("Job Title",job_var),
("Company",company_var)

]

for i,(text,var) in enumerate(labels):

    tk.Label(frame,
    text=text,
    bg="lightblue",
    font=("Arial",11,"bold")).grid(row=i,column=0,padx=10,pady=5)

    tk.Entry(frame,
    textvariable=var,
    width=30).grid(row=i,column=1)



# -------- BUTTONS --------

btn_frame = tk.Frame(root,bg="lightblue")
btn_frame.pack()

tk.Button(btn_frame,
text="Add",
command=add_alumni,
bg="green",
fg="white",
width=10).grid(row=0,column=0,padx=5)

tk.Button(btn_frame,
text="Update",
command=update_alumni,
bg="orange",
fg="white",
width=10).grid(row=0,column=1,padx=5)

tk.Button(btn_frame,
text="Delete",
command=delete_alumni,
bg="red",
fg="white",
width=10).grid(row=0,column=2,padx=5)

tk.Button(btn_frame,
text="View All",
command=view_data,
bg="blue",
fg="white",
width=10).grid(row=0,column=3,padx=5)



# -------- SEARCH --------

search_frame = tk.Frame(root,bg="lightblue")
search_frame.pack(pady=10)

tk.Entry(search_frame,
textvariable=search_var,
width=30).grid(row=0,column=0)

tk.Button(search_frame,
text="Search Name",
command=search_alumni).grid(row=0,column=1)



# -------- TABLE --------

columns = (

"id","name","email","phone",
"year","dept","job","company"

)

table = ttk.Treeview(
root,
columns=columns,
show="headings",
height=10
)

for col in columns:

    table.heading(col,text=col.upper())
    table.column(col,width=100)

table.pack(fill="both",expand=True)

table.bind("<ButtonRelease-1>",select_record)


view_data()

root.mainloop()
