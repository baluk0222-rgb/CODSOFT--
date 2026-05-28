# IMAGE CAPTIONING - BEGINNER HUMAN LOGIC (NO AI / NO DL)

# -----------------------------------
# STEP 1: SIMULATED IMAGE FEATURES
# (In real AI, CNN extracts features)
# Here we manually assume keywords
# -----------------------------------

image_keywords = {
    "img1": ["dog", "grass", "outdoor"],
    "img2": ["car", "road", "city"],
    "img3": ["food", "plate", "table"],
    "img4": ["child", "ball", "park"],
    "img5": ["beach", "sea", "sun"]
}

# -----------------------------------
# STEP 2: CAPTION DATABASE
# (Like rule-based NLP system)
# -----------------------------------

captions = {
    "dog": "A dog is playing happily in the grass.",
    "car": "A car is moving on a busy road in the city.",
    "food": "Delicious food is served on a plate.",
    "child": "A child is playing in the park.",
    "beach": "A beautiful beach with sea and sunshine."
}

# -----------------------------------
# STEP 3: GENERATE CAPTION FUNCTION
# -----------------------------------

def generate_caption(image_id):

    keywords = image_keywords.get(image_id, [])

    caption_list = []

    for word in keywords:
        if word in captions:
            caption_list.append(captions[word])

    # -----------------------------------
    # STEP 4: FINAL OUTPUT LOGIC
    # -----------------------------------

    if len(caption_list) == 0:
        return "No caption available for this image."

    return " | ".join(caption_list)

# -----------------------------------
# STEP 5: TEST SYSTEM
# -----------------------------------

print("IMAGE CAPTIONING SYSTEM (BEGINNER VERSION)\n")

for img in image_keywords:
    print("Image:", img)
    print("Caption:", generate_caption(img))
    print()