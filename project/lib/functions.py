#! /usr/bin/python3

class WordsModifications:
    def doubleName(self, original_words, final_doc, words_number, created_number):
        initial_word = 0
        while int(created_number) < int(words_number):
            a = str(original_words[initial_word])
            b = str(original_words[created_number])

            password = (str(a).strip("\n") + str(b).strip("\n"))
            final_doc.write(password + "\n")

            password = (str(a).strip("\n").lower() + str(b).strip("\n").lower())
            final_doc.write(password + "\n")

            password = (str(a).strip("\n").lower() + str(b).strip("\n").upper())
            final_doc.write(password + "\n")

            password = (str(a).strip("\n").upper() + str(b).strip("\n").lower())
            final_doc.write(password + "\n")

            password = (str(a).strip("\n").upper() + str(b).strip("\n").upper())
            final_doc.write(password + "\n")

            created_number = created_number + 1
            if int(created_number) == int(words_number):
                created_number = 0
                initial_word = initial_word + 1
                if int(initial_word) == int(words_number):
                    break

    def originalWords(self, original_words, final_doc, words_number, created_number):
        while int(created_number) < int(words_number):
            if int(created_number) < int(words_number):
                password = str(original_words[created_number].strip("\n"))
                final_doc.write(password + "\n")

                password = str(original_words[created_number].strip("\n").lower())
                final_doc.write(password + "\n")

                password = str(original_words[created_number].strip("\n").upper())
                final_doc.write(password + "\n")

                password = str(original_words[created_number].strip("\n"))
                final_doc.write(password[::-1] + "\n")

                password = str(original_words[created_number].strip("\n").lower())
                final_doc.write(password[::-1] + "\n")

                password = str(original_words[created_number].strip("\n").upper())
                final_doc.write(password[::-1] + "\n")

                created_number = created_number + 1

                if int(created_number) == int(words_number):
                    break


class WordmasterApresentation:
    def banner(self):
        print("""

    ██╗    ██╗ ██████╗ ██████╗ ██████╗     ███╗   ███╗ █████╗ ███████╗████████╗███████╗██████╗
    ██║    ██║██╔═══██╗██╔══██╗██╔══██╗    ████╗ ████║██╔══██╗██╔════╝╚══██╔══╝██╔════╝██╔══██╗
    ██║ █╗ ██║██║   ██║██████╔╝██║  ██║    ██╔████╔██║███████║███████╗   ██║   █████╗  ██████╔╝
    ██║███╗██║██║   ██║██╔══██╗██║  ██║    ██║╚██╔╝██║██╔══██║╚════██║   ██║   ██╔══╝  ██╔══██╗
    ╚███╔███╔╝╚██████╔╝██║  ██║██████╔╝    ██║ ╚═╝ ██║██║  ██║███████║   ██║   ███████╗██║  ██║
     ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝╚═════╝     ╚═╝     ╚═╝╚═╝  ╚═╝╚══════╝   ╚═╝   ╚══════╝╚═╝  ╚═╝


    """)
