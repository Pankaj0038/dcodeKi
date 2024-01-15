def binary_to_text(binary_string):
    binary_values = binary_string.split()
    text_result = ''.join(chr(int(bin_val, 2)) for bin_val in binary_values)
    return text_result

def string_to_binary(input_string):
    binary_representation = ' '.join(format(ord(char), '08b') for char in input_string)
    #print("These are binary represent.",binary_representation)
    return binary_representation

def xor_binary_strings(binary_str1, binary_str2):
    result = ''
    for bit1, bit2 in zip(binary_str1, binary_str2):
        #print(bit1,bit2)
        result += '1' if bit1 != bit2 else '0'
        #print("result is",result)
    return result

def encode(s,key):
     
    #ignore
    #letters_array = []
    #key_array = []
    #for char in s:
        #letters_array.append(char)
    #print("")
    #flag = 0
    #Reading the array backwards, so that we can separate the key and text part
    #for i in range(len(letters_array)- 1, -1, -1):
        #if letters_array[i].isdigit():
            #pass
        #elif letters_array[i] == " ":
            #key_array = letters_array[(i+1):]
            #key = int(''.join(key_array))
            #letters_array = letters_array[:(i)]
            #flag = 1
            #break
    #performing the final steps
    #text = ''.join(letters_array)


    if key == "":
        key = 10 #Default Key
        print("No Key is given, hence default key - 10 is being used")

    key = int(key)
    print("key is:",key)

    # Converting text and key into binary
    text_binary = string_to_binary(s)
    key_binary = format(key, '08b')
    print("key_bin is:",key_binary)

    result_fina = []
    # XOR each binary letter with the key separately
    for char in text_binary.split():
        result_binary = ''.join(xor_binary_strings(char, key_binary))
        result_fina.append(result_binary)
    
    result_fina = ' '.join(result_fina)
    print("Result after XOR:", result_fina)

    b2t = binary_to_text(result_fina)
    print("Result after binary to text conversion is :", b2t)
    return(b2t)



if __name__ == '__main__':
    b = input("Enter a text to decode[Format:(Text Key)]: ")
    k = input("Enter Key")
    print(encode(b,k))

