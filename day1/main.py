def lowercase(text: str):
    """Takes the text and turns it into lowercase if needed."""
    return text.lower()


if __name__ == "__main__":
    test_text = "Ala Ma KoTa"
    print(f"lowercase({test_text}) = {lowercase(test_text)}")