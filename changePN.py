import tkinter as tk

# one idea is to change 111bb to the number that is actually interesting to change

# all places

import tkinter as tk

fields = 'SWLM', 'SWP1', 'SWP2', 'SWCE'


class PnMan:
    def __init__(self):
        self.field = ""
        self.text = ""
        self.texts = []

    def main(self, fields):
        root = tk.Tk()
        ents = self.makeform(root, fields)
        root.bind('<Return>', (lambda event, e=ents: self.fetch(e)))
        b1 = tk.Button(root, text='Show',
                       command=(lambda e=ents: self.fetch(e)))
        b1.pack(side=tk.LEFT, padx=5, pady=5)
        b2 = tk.Button(root, text='Quit', command=root.quit)
        b2.pack(side=tk.LEFT, padx=5, pady=5)
        root.mainloop()

        tk.mainloop()

        print(self.texts)

        # change the json file
        a_file = open("new_json_file.json", 'a')
        with open('Customer_PNs_Cfg.json', 'r') as file:
            content = file.read()

            replaced = content.replace("wow", "")  # assign to new value!!
            a_file.write(replaced)

    def fetch(self, entries):
        for entry in entries:
            field = entry[0]
            text = entry[1].get()
            print('%s: "%s"' % (field, text))

    def makeform(self, root, fields):
        entries = []
        for field in fields:
            row = tk.Frame(root)
            lab = tk.Label(row, width=15, text=field, anchor='w')
            ent = tk.Entry(row)
            row.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)
            lab.pack(side=tk.LEFT)
            ent.pack(side=tk.RIGHT, expand=tk.YES, fill=tk.X)
            entries.append((field, ent))
        return entries


if __name__ == "__main__":
    pn_man = PnMan()
    pn_man.main(fields)
