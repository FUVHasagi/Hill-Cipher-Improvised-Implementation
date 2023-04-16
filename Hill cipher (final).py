import numpy as np

def init(n):
    # Initialize a matrix size nxn
    A = np.zeros((n,n))
    return A


def inputmatrix(A,n):
    # Input data for a matrix
    for i in range(0,n):
        for j in range(0,n):
            print('A[',i,',',j,']=')
            A[i,j] = input()


def check_and_add(string,n):
    # Making a string with the length appropriate
    while len(string)%n !=0:
        string = string + ' '
    string = string + ' '
    return string


def conv_n_char_to_vector(string,n):
    #turn n char in the string into a vector of numbers
    A = np.zeros((n,1))
    for i in range(0,n,1):
        A[i,0] = ord(string[i])
    return A


def real_encoding(ordistr,A,n):
    # The core of the encoding process
    # Input a string, the key matrix and the size
    # Output the encoded string
    k = int(len(ordistr)/n)
    a = list()
    for i in range(0,k,1):
        temp_str = ordistr[n*i:(n*i+n)]
        temp_mat = conv_n_char_to_vector(temp_str,n)
        temp_mat = A@temp_mat
        for j in range(0,n,1):
            a.append(str(int(temp_mat[j])))
            # Chuyển từ matrix sang list
    result = '_'.join(a)
    return result


def encoding():
    # Call this procedure when the user want to encode a message
    print('Enter a string to be encoded (No Vietnamse signs is better but not required):')
    ordi = input()
    print('Enter the level of the Hill cipher n =')
    n = int(input())
    ordi = check_and_add(ordi,n)
    key = init(n)
    print('Enter the entries in the key matrix:')
    inputmatrix(key,n)
    print('Your key matrix is \n',key)
    #Checking the matrix invertible or not so that we can have a key matrix that can be use for decoding again
    while  np.linalg.det(key) == 0:
        print('Your matrix key is not invertible. Please enter another key')
        inputmatrix(key,n)
        print('Your key matrix is \n',key)
        #For the user to have a look again at the key
    result_str = real_encoding(ordi,key,n)
    print('Your result string is: \n',result_str)


def check_and_remove(code,n):
    #check and remove the redundant numbers in the "wrong" code that cannot be translated back to original
    while code.count('_')%n != (n-1):
        code = code[:-1]


def conv_n_list_elements_to_vector(code_list,n):
    #convert a n elements list to vector (used during decoding)
    A = np.zeros((n,1))
    for i in range(0,n,1):
        A[i,0] = int(code_list[i])
    return A


def real_decoding(code_string,A,n):
    # The core of the encoding process
    # Input a string, the key matrix and the size
    # Output the encoded string
    code_list = code_string.split('_')
    #Turn the sequence numbers from the encoded string which are separated by a "_" character into a list
    k = int(len(code_list)/n)
    a = ""
    for i in range(0,k,1):
        temp_list = code_list[n*i:(n*i+n)]
        temp_mat = conv_n_list_elements_to_vector(temp_list,n)
        temp_mat = A@temp_mat
        for j in range(0,n,1):
            a = a + chr(int(round(float(temp_mat[j]))))
            # Decoding the number in a composition matrix to a string then add it into the string
    return a


def decoding():
    # Call this procedure when the user want to decode a message
    print('Enter a string coded by the program: ')
    coded_message = input()
    print('Enter the level of the Hill cipher n =')
    n = int(input())
    key = init(n)
    # the encoding message must have a divisible number of numbers
    if coded_message.count('_') % n != (n-1):
        print('This code message ',coded_message.count('_') % n+1," last digits can't be decode so will be lost")
        check_and_remove(coded_message,n)
    print('Enter the entries in the key matrix:')
    inputmatrix(key,n)
    ans = ''
    while ans != '1' or ans != '2':
        print('This is the: \n 1. Coding key, or \n2. Decoding key')
        ans = input('My choose is: ')
        if ans == '1':
            key = np.linalg.inv(key)
            break
        elif ans == '2':
            break
        else:
            print('You have enter an invalid value please try again')
    result = real_decoding(coded_message,key,n)
    print("The original message is:  ")
    print(result)


def key_cracking(known_string,coded_list,n):
    source_mat = init(n)
    end_mat = init(n)
    for i in range(0,n,1):
        temp_vec1 = conv_n_char_to_vector(known_string[n*i:n*(i+1)],n)
        temp_vec2 = conv_n_list_elements_to_vector(coded_list[n*i:n*(i+1)],n)
        for j in range(0,n,1):
            source_mat[j,i] = temp_vec1[j,0]
            end_mat[j,i] = temp_vec2[j,0]
    key_matr = source_mat@np.linalg.inv(end_mat)
    return key_matr


def cracking():
    print('Enter a string coded by the program: ')
    coded_message = input()
    print('Enter the level of the Hill cipher n =')
    n = int(input())
    while coded_message.count('_') <= n*n:
        print('Your the message must be larger than ',n*n,' numbers to crack, retype your message or choose another one please: ')
        coded_message = input()
    if coded_message.count('_') % n != (n-1):
        print('This code message ',coded_message.count('_') % n+1," last digits can't be decode so will be lost")
        check_and_remove(coded_message)
    print('Enter the already ',n*n,'known first digits:')
    known_str = input()
    # The number of numbers in the code must be a number divisible by n
    while len(known_str) != n*n:
        print("Your string don't have the right number (",n*n,") of characters please try again:")
        known_str = input()
    code_list = coded_message.split('_')
    key = key_cracking(known_str,code_list,n)
    result = real_decoding(coded_message,key,n)
    print("The key matrix is:","\n", np.linalg.inv(key))
    print('The original message is :')
    print(result)


#Main stream
en = ''
while en != '1' or en != '2' or en != '3':
    print('***Welcome to my Hill cipher encoding and decoding program.***\n')
    print('For the encoding please press 1 and enter. Then enter your message and the entries in the key matrix.')
    print('For the decoding please press 2 and enter. Then enter your encoded message, the entries in the key matrix, and choose whether this is the encoding key or the decoding key.')
    print('For the cracking please press 3 and enter. Then enter your encoded message and the known digits in the original string')
    en = input()
    if en == '1':
        encoding()
        break
    elif en == '2':
        decoding()
        break
    elif en == '3':
        cracking()
        break
    else:
        print('You have entered an invalid value please try again')