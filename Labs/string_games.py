#Jeanna Shellenberger Section 061
def rev(text):
    return text[::-1]


def revNums(text):
    nums = ''
    reverse = ''
    digit = False
    count = 0
    for letter in text:
        try:
            num = int(letter)
            nums += letter
            reverse += letter
            digit = True
        except Exception:
            if digit:
                reverse = reverse.replace(nums, rev(nums))
                nums = ''
            reverse += letter
            digit = False
        if count == len(text) - 1 and digit:
            reverse = reverse.replace(nums, rev(nums))
        count += 1
    return reverse


if __name__ == "__main__":
    print('Welcome to Digit Flipper')
    message = input('Enter Some Text:\n')
    print('Revised String:')
    print(revNums(message))
