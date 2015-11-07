dict = ["GEEKS", "FOR", "QUIZ", "GO"]

def is_word(word):
    if word in dict:
        return True
    else:
        return False

def find_word(boggle):
    row = len(boggle)
    col = len(boggle[0])
    visited = [[False] * col for r in range(row)]
    for i in range(row):
        for j in range(col):
            word = []
            search_word(boggle,visited,word,i,j,row,col)

def search_word(boggle,visited,word,i,j,row,col):

    # Appendd the current cell char to the word
    word.append(boggle[i][j])

    # Mark the current cell as visited
    visited[i][j] = True

    # Check if the current word is present in dictionary
    if is_word(''.join(word)):
        print(''.join(word))

    # Traverse all the  8 possibilities from the current cell
    # The posible cell are: (i,j+1),(i,j-1),(i+1,j),(i-i,j),(i+1,j+1),(i+1,j-1)
    #(i-1,j+1),(i-1,,j-1)

    m = i - 1
    while m <= i+1 and m < row:
        n = j - 1
        while n <= j+1 and n < col:
            if (m >= 0 and n >= 0 and not visited[m][n]):
                search_word(boggle,visited,word,m,n,row,col)
            n += 1
        m += 1

   # Set the current cell as not visited so it can be used to form
   # word from different cell
    visited[i][j] = False
    word.pop()

boggle = [['G','I','Z'],
          ['U','E','K'],
          ['Q','S','E']
        ]

find_word(boggle)
