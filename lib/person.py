class Person:
    # Person can talk
    def talk(self):
        print("Hello World!")

    # Person can walk
    def walk(self):
        print("The person is walking.")


# Example usage (optional)
if __name__ == "__main__":
    alice = Person()
    alice.talk()  # Hello World!
    alice.walk()  # The person is walking.
