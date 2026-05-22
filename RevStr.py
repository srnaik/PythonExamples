
# Inheriting str class
class RevSstr(str):
    def __str__(self):
        return self[::-1] # Override __str__ method and reverse the string


def main():
    hello = RevSstr('Hello, World!')
    print(hello)

if __name__ == '__main__': main()
