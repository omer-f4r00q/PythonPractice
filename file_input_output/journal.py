def add_entry(text):
    with open("my_journal.txt", "a") as file:
        file.write(f"{text}\n")
    print("Entry saved.")


def view_journal():
    print("---Journal Entries---")
    try:
        with open("my_journal.txt", "r") as file:
            for line in file:
                print(f"{line.strip()}")
    except FileNotFoundError:
        print("Journal is empty.")


if __name__ == "__main__":
    add_entry("Today I learned File I/O.")
    add_entry("But something unusual happened, i had already done the write, append and read modes and done a log_events task.")
    add_entry("In this task I had to record the logs with the timestamp using the datetime module.")
    add_entry("I successfully did the task and also the bonus challenge.")
    add_entry("Then gemini pro was teaching me about how we can iterate over the file object, which is a more memory efficient way.")
    add_entry("I was about to ask him a few questions and suddenly the tab got closed and the memory was lost!")
    add_entry("Then I had to open the tab again and do the whole thing again and here I am now..")
    add_entry("Yo Gemini!, should I send you my log.app task too? What do you say?")

    view_journal()