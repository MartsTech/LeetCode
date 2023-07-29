class Solution:
    # O(n) time | O(n) space
    def getHint(self, secret: str, guess: str) -> str:
        bulls = 0
        cows = 0
        secrets = {}
        guesses = {}
        for idx in range(len(guess)):
            if guess[idx] == secret[idx]:
                bulls += 1
            else:
                if guess[idx] in secrets and secrets[guess[idx]] > 0:
                    cows += 1
                    secrets[guess[idx]] -= 1
                else:
                    guesses[guess[idx]] = guesses.get(guess[idx], 0) + 1
                if secret[idx] in guesses and guesses[secret[idx]] > 0:
                    cows += 1
                    guesses[secret[idx]] -= 1
                else:
                    secrets[secret[idx]] = secrets.get(secret[idx], 0) + 1
        return f"{bulls}A{cows}B"