# Lesson 41
# 1 point - A, E, I, O, U, L, N, S, T, R.
# 2 points - D, G.
# 3 points - B, C, M, P.
# 4 points - F, H, V, W, Y.
# 5 points - K.
# 8 points - J, X.
# 10 points - Q, Z.
word_list = ['apple', 'orange', 'cat', 'difficult', 'beautiful', 'lesson', 'python', 'exciting']

def score(words):
    result = 0
    for j in range(len(words)):
        curr_word = str(words[j]) 
        curr_score = 0
        for i in range(len(curr_word)): 
            if curr_word[i] == 'a' or curr_word[i] == 'e' or curr_word[i] == 'i' or curr_word[i] == 'o' or curr_word[i] == 'u' or curr_word[i] == 'l' or curr_word[i] == 'n' or curr_word[i] == 's' or curr_word[i] == 't' or curr_word[i] == 'r':
                curr_score += 1
            elif curr_word[i] == 'd' or curr_word[i] == 'g':
                curr_score += 2
            elif curr_word[i] == 'b' or curr_word[i] == 'c' or curr_word[i] == 'm' or curr_word[i] == 'p':
                curr_score += 3
            elif curr_word[i] == 'f' or curr_word[i] == 'h' or curr_word[i] == 'v' or curr_word[i] == 'w' or curr_word[i] == 'y':
                curr_score += 4
            elif curr_word[i] == 'k':
                curr_score += 5
            elif curr_word[i] == 'j' or curr_word[i] == 'x':
                curr_score += 6
            elif curr_word[i] == 'q' or curr_word[i] == 'z':
                curr_score += 7
            if curr_score >= result:
                result = curr_score
    return result

print(f" the largest score is {score(word_list)}")
