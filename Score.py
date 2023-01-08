def add_score():
    text_open = open('difficulty.txt')
    diff = text_open.readline()
    difficulty = (int(diff))
    score = int((difficulty * 3) +5)
    current_score = open('Scores.txt')
    current_sc = current_score.readline()
    current = (int(current_sc))
    newscore = score + current
    scoretxt = open('Scores.txt', mode='w')
    scoretxt.write(str(newscore))
    scoretxt.close()
    return ""

add_score()