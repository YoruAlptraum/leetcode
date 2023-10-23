def truncateSentence(s: str, k: int) -> str:
    arr = s.split(' ')
    return ' '.join(arr[:k])

if __name__ == "__main__":
    cases = [
        [{'s': "Hello how are you Contestant", 'k':4},"Hello how are you"],
        [{'s': "What is the solution to this problem", 'k':4},"What is the solution"],
        [{'s': "chopper is not a tanuki", 'k':5},"chopper is not a tanuki"]
    ]
    for c in cases:
        print('passed' if truncateSentence(c[0]['s'],c[0]['k']) == c[1] else 'failed')
