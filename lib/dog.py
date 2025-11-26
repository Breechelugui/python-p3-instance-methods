class Dog:
    # Dog can bark
    def bark(self):
        print("Woof!")

    # Dog can sit
    def sit(self):
        print("The dog is sitting.")


# Example usage (optional, only for manual testing)
if __name__ == "__main__":
    fido = Dog()
    fido.bark()  # Woof!
    fido.sit()   # The dog is sitting.

    snoopy = Dog()
    snoopy.bark()  # Woof!
    snoopy.sit()   # The dog is sitting.
