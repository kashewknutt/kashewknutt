import time

def printinmotion(text):
    for i in range(0, len(text)):
        print(text[i], end='', flush=True)
        time.sleep(0.1)
    print()

if __name__ == "__main__":
    printinmotion("Hello Techies!!")
    printinmotion("Welcome to my world :P")
