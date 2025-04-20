import os
import google.generativeai as genai

genai.configure(api_key=os.environ["GEMINI_API_KEY"])

def upload_to_gemini(path, mime_type=None):
  file = genai.upload_file(path, mime_type=mime_type)
  print(f"Uploaded file '{file.display_name}' as: {file.uri}")
  return file

# Create the model
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 65536,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-2.5-pro-preview-03-25",
  generation_config=generation_config,
)

# TODO Make these files available on the local file system
# You may need to update the file paths
files = [
  upload_to_gemini("image.png", mime_type="image/png"),
  upload_to_gemini("image.png", mime_type="image/png"),
  upload_to_gemini("image.png", mime_type="image/png"),
  upload_to_gemini("image.png", mime_type="image/png"),
]

chat_session = model.start_chat(
  history=[
    {
      "role": "user",
      "parts": [
        files[0],
        files[1],
        files[2],
        files[3],
        "please transcribe those hooks into a list",
      ],
    },
    {
      "role": "model",
      "parts": [
        "Here's my thought process for transcribing the TikTok hook formats from the provided images:\n\n1.  **Understand the Goal:** The user wants a transcribed list of the \"40 Viral TikTok Hook Formats (pt2)\" shown in the four screenshots. The output should be a clean, readable list.\n\n2.  **Examine the Input:** I have four images showing a numbered list in what appears to be a notes app (likely Apple Notes based on the UI). The title indicates \"40 Viral TikTok Hook Formats (pt2)\". The list items are numbered from 1 to 39, followed by a smiley face drawing. This implies either the title meant *around* 40, or the 40th item is missing/cut off, or perhaps the drawing is meant to be the 40th item (unlikely for a list of *formats*). I'll transcribe what's visible (1-39).\n\n3.  **Transcription Strategy:**\n    *   Go through each image sequentially.\n    *   Read each numbered item carefully.\n    *   Type out the text exactly as it appears, including capitalization, punctuation, and bracketed placeholders `[like this]`.\n    *   Maintain the original numbering.\n    *   Pay attention to potential OCR errors if I were an OCR tool, but since I'm analyzing the image directly, I need to be accurate in reading.\n    *   Handle line breaks within a single list item if they exist (none seem significant here).\n\n4.  **Execution (Item by Item):**\n\n    *   **Image 1:**\n        *   Title: \"40 Viral TikTok Hook Formats (pt2)\" - Include this at the top.\n        *   1. `6 STEPS TO [GETTING ANYONE TO BUY ANYTHING FROM YOU]` - Looks correct. Note the ALL CAPS.\n        *   2. `First day as a [housekeeper]... I wasn't ready for THIS` - Correct. Note the ellipsis and ALL CAPS 'THIS'.\n        *   3. `[US] citizens:` - Correct. Note the brackets and colon.\n        *   4. `oh so NOW you're learning [mandarin]` - Correct. Note lowercase 'oh', ALL CAPS 'NOW', brackets.\n        *   5. `Bro is living in 2050 [* 700 pages in 10 minutes !?]` - Correct. Note the asterisk, spacing, punctuation inside brackets.\n        *   6. `Day 247 of trying to get [Joe Jonas to stop copying my BeReals...]` - Correct. Note the ellipsis inside brackets.\n        *   7. `can someone tell me [what i'm supposed to do in this situation]` - Correct. Note lowercase 'can', contraction, brackets.\n        *   8. `Who needs an [elevator boy] when you can have an [elevator pengu]` - Correct. Note the apparent typo 'pengu' instead of 'penguin'. Transcribe as shown.\n        *   9. `Damm i've been [running] wrong my whole life` - Correct. Note 'Damm', lowercase 'i've', brackets.\n        *   10. `5 TIPS to [travel low cost]` - Correct. Note ALL CAPS 'TIPS', brackets.\n        *   11. `Best AI Tools [For Students]` - Correct. Note capitalization, brackets.\n\n    *   **Image 2:**\n        *   12. `Coolest [wedding] idea ever!` - Correct. Note capitalization, brackets, exclamation mark.\n        *   13. `This will change your [life]` - Correct. Note brackets. *Self-correction: Wait, the image doesn't show brackets around 'life'. Re-read.* Ah, yes, no brackets. Correction: `This will change your life!`\n        *   14. `[COSTCO PRICING] SECRETS` - Correct. Note ALL CAPS in brackets and 'SECRETS'.\n        *   15. `[ISHOWSPEED] TRIES [DEADLIFTING]` - Correct. Note ALL CAPS in brackets.\n        *   16. `[Morning] routine to [build good habits]` - Correct. Note capitalization in the first bracket, lowercase in the second.\n        *   17. `is your [relationship]?` - Correct. Note lowercase 'is', brackets, question mark.\n        *   18. `Your daily reminder that you [deserve better than your ex]` - Correct. Note brackets.\n        *   19. `got a [headache/migraine]? try this.` - Correct. Note lowercase 'got', brackets with slash, question mark, lowercase 'try', period.\n        *   20. `Me [showing up to school] like I didn't [just get an hour of sleep the night before]` - Correct. Note capitalization, brackets.\n        *   21. `Did you know [dog toys can collect bacteria, yeast, mold & dirt? ]` - Correct. Note capitalization, brackets, ampersand, question mark inside brackets, trailing space inside brackets.\n        *   22. `Do you really still [edit your stories like this?]` - Correct. Note capitalization, brackets, question mark inside brackets.\n        *   23. `I wasted so much time [editing stories like this]` - Correct. Note capitalization, brackets.\n        *   24. `Another [laptop life hack] I guarantee you` - Correct. Note capitalization, brackets. (Text below is cut off but belongs to the next item or is just notes).\n\n    *   **Image 3:**\n        *   (Item 24 continuation seems irrelevant to the list format itself)\n        *   25. `Secrets your [teachers] don't want you to know` - Correct. Note capitalization, brackets.\n        *   26. `10 years of using a [male owned period app] and just found this...` - Correct. Note brackets, ellipsis.\n        *   27. `STOP [DRAGONS AREN'T REAL]` - Correct. Note ALL CAPS 'STOP', ALL CAPS inside brackets.\n        *   28. `Crazy fact of the day: [Tea is made with the water infusion of leaves]` - Correct. Note capitalization, colon, brackets.\n        *   29. `5 questions you should ask [your boyfriend]` - Correct. Note brackets.\n        *   30. `[dyson] is terrible` - Correct. Note lowercase inside brackets.\n        *   31. `How did I not know about this` - Correct. Note capitalization.\n        *   32. `life without [snap] >>>` - Correct. Note lowercase 'life', brackets, greater-than signs.\n        *   33. `want to [get hired] before [the summer]? This is what you have to do:` - Correct. Note lowercase 'want', brackets, question mark, capitalization, colon.\n        *   34. `I'm never using [google scholar for literature review] again after this` - Correct. Note contraction, brackets with lowercase content.\n        *   35. `best websites/ai for [research]` - Correct. Note lowercase 'best', slash, brackets.\n        *   36. `I was struggling to find [research papers]` - Correct. Note capitalization, brackets. (Text below is cut off).\n\n    *   **Image 4:**\n        *   36. (Repeated/Continued - already transcribed) `I was struggling to find [research papers]`\n        *   37. `All these [people] and none of them know about this:` - Correct. Note capitalization, brackets, colon. *Self-correction: Re-read.* Ah, no colon at the end. Correction: `All these [people] and none of them know about this`\n        *   38. `[polls] that are guaranteed to make you [laugh]` - Correct. Note lowercase in brackets.\n        *   39. `I don't think [colour analysis] makes any difference` - Correct. Note contraction, brackets with lowercase content.\n        *   (Smiley face drawing - Ignore for the list transcription).\n\n5.  **Final Review:** Read through the transcribed list (1-39) one more time, comparing it against the images to ensure accuracy in text, capitalization, punctuation, and bracket usage. Check for any missed items or typos. Everything looks good.\n\n6.  **Format the Output:** Present the transcribed text as a clean, numbered list as requested by the user. Add the title from the image.",
        "Okay, here is the transcribed list of the 39 TikTok hook formats from the images:\n\n**40 Viral TikTok Hook Formats (pt2)**\n\n1.  6 STEPS TO [GETTING ANYONE TO BUY ANYTHING FROM YOU]\n2.  First day as a [housekeeper]... I wasn't ready for THIS\n3.  [US] citizens:\n4.  oh so NOW you're learning [mandarin]\n5.  Bro is living in 2050 [* 700 pages in 10 minutes !?]\n6.  Day 247 of trying to get [Joe Jonas to stop copying my BeReals...]\n7.  can someone tell me [what i'm supposed to do in this situation]\n8.  Who needs an [elevator boy] when you can have an [elevator pengu]\n9.  Damm i've been [running] wrong my whole life\n10. 5 TIPS to [travel low cost]\n11. Best AI Tools [For Students]\n12. Coolest [wedding] idea ever!\n13. This will change your life!\n14. [COSTCO PRICING] SECRETS\n15. [ISHOWSPEED] TRIES [DEADLIFTING]\n16. [Morning] routine to [build good habits]\n17. is your [relationship]?\n18. Your daily reminder that you [deserve better than your ex]\n19. got a [headache/migraine]? try this.\n20. Me [showing up to school] like I didn't [just get an hour of sleep the night before]\n21. Did you know [dog toys can collect bacteria, yeast, mold & dirt? ]\n22. Do you really still [edit your stories like this?]\n23. I wasted so much time [editing stories like this]\n24. Another [laptop life hack] I guarantee you\n25. Secrets your [teachers] don't want you to know\n26. 10 years of using a [male owned period app] and just found this...\n27. STOP [DRAGONS AREN'T REAL]\n28. Crazy fact of the day: [Tea is made with the water infusion of leaves]\n29. 5 questions you should ask [your boyfriend]\n30. [dyson] is terrible\n31. How did I not know about this\n32. life without [snap] >>>\n33. want to [get hired] before [the summer]? This is what you have to do:\n34. I'm never using [google scholar for literature review] again after this\n35. best websites/ai for [research]\n36. I was struggling to find [research papers]\n37. All these [people] and none of them know about this\n38. [polls] that are guaranteed to make you [laugh]\n39. I don't think [colour analysis] makes any difference",
      ],
    },
  ]
)

response = chat_session.send_message("INSERT_INPUT_HERE")

print(response.text)