
class Klocki:
    def multiplication_tables(n):
        s = ""
        for i in range(1,n+1):
            for k in range(1,n+1):
                if i == k:
                    s += f"{1}\t"
                else: 
                    s += f"{0}\t"
            s += '\n'
        return(s)


    def genrate_text(file_name:str,content:str):
        file_name = file_name + ".txt"
        with open(file_name, "w") as text_file:
            text_file.write(content)


multiplication_data = Klocki.multiplication_tables(10)


Klocki.genrate_text("multiplication_tables", multiplication_data)
