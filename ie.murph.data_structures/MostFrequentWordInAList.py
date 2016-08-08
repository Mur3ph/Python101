from collections import Counter

text = "A compiler is a computer program (or a set of programs) that transforms source code written in a programming language " \
       "(the source language) into another computer language (the target language), with the latter often having a binary form " \
       "known as object code.[1] The most common reason for converting source code is to create an executable program. " \
       "The name compiler is primarily used for programs that translate source code from a high-level programming language " \
       "to a lower level language (e.g., assembly language or machine code). If the compiled program can run on a computer " \
       "whose CPU or operating system is different from the one on which the compiler runs, the compiler is known as a " \
       "cross-compiler. More generally, compilers are a specific type of translator."

words = text.split()
print(words)

counter = Counter(words)
top_three_occuring_words = counter.most_common(3)
print(top_three_occuring_words)