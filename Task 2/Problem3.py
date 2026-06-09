from codeop import compile_command
pattern = input("Enter DNA String:")
compilement = {"A":"T",
               "T":"A",
               "C":"G",
               "G":"C"
               }
               reverse_complement = ""
               for i in range(len(pattern) -1, -1, -1):
                reverse_complement += complement
