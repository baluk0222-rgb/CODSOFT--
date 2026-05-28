# MOVIE GENRE PREDICTION - PURE HUMAN LOGIC (NO ML LIBRARIES)

# -----------------------------------
# STEP 1: SIMPLE TRAINING DATA
# -----------------------------------

data = [
    ("action", "hero fight war save city battle weapons"),
    ("romance", "love couple meet college relationship emotional"),
    ("comedy", "funny friends joke laugh road trip comedy"),
    ("thriller", "murder mystery detective crime investigation case"),
    ("sci-fi", "alien space future robot technology earth invasion")
]

# -----------------------------------
# STEP 2: USER INPUT (MOVIE PLOT)
# -----------------------------------

plot = input("Enter movie plot: ").lower().split()

# -----------------------------------
# STEP 3: SIMPLE MATCHING LOGIC
# -----------------------------------

genre_scores = {
    "action": 0,
    "romance": 0,
    "comedy": 0,
    "thriller": 0,
    "sci-fi": 0
}

# Compare input words with training words
for genre, text in data:
    words = text.split()

    for word in plot:
        if word in words:
            genre_scores[genre] += 1

# -----------------------------------
# STEP 4: FIND BEST MATCH
# -----------------------------------

best_genre = None
max_score = 0

for genre in genre_scores:
    if genre_scores[genre] > max_score:
        max_score = genre_scores[genre]
        best_genre = genre

# -----------------------------------
# STEP 5: OUTPUT RESULT
# -----------------------------------

if max_score == 0:
    print("Cannot detect genre clearly. Try better input.")
else:
    print("Predicted Genre:", best_genre)