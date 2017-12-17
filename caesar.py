import cs50
import sys

def main():
    if(len(sys.argv) != 2):
            sys.exit("That input was incorrect!  Please rerun and try again.")
    a = int(sys.argv[1]);
    print ("plaintext: ", end = "");
    message = cs50.get_string();
    encryptedMessage = [];
    while(len(message) > 0):
        if(message[0] == " "):
            encryptedMessage = encryptedMessage + " ";
            message = message+1;
        else:
            length = len(encryptedMessage);

            n = -1;

            if (message[0] >= 'A' and message[0] <= 'Z'):
                alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
                p = alphabet.find(message[0]);

                if (p):
                    n = p - alphabet;

                n = (n+a)%26;
                encryptedMessage[length] = alphabet[n];
            elif (message[0] >= 'a' and message[0] <= 'z'):
                alphabet = "abcdefghijklmnopqrstuvwxyz";
                p = alphabet.find(message[0]);

                if (p):
                    n = p - alphabet;

                n = (n+a)%26;
                encryptedMessage[length] = alphabet[n];

            encryptedMessage[length+1] = '\0';
            message = message+1;

    print ("ciphertext: %s", encryptedMessage);