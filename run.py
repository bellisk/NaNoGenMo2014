from nano.novel import things, segments

if __name__ == "__main__":
    # Generate characters
    person = things.Person()
    print segments.describe_character(person)
