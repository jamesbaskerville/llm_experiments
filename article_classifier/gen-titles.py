import ollama
import re
import json

genPrompt = lambda x: f'Give me ten article titles in an array as strings. Each should be related to the field of {x} and describe a specific phenomenon or occurrence within that field. Titles should seem to be from either newspaper articles or blog-style posts like Medium or Substack. Please make the titles as realistic as possible. Return only a single array with ten titles.'

categories = ['science', 'technology', 'politics', 'sports', 'economy']

prompts = [genPrompt(c) for c in categories]
numPrompts = len(prompts)

allTitles = []

def saveToCSV(titles):
  try:
    csvContent = '\n'.join([','.join(title) for title in titles])
    filename = 'titles.csv'
    with open(filename, 'w', encoding="utf-8") as f:
      f.write("text,label\n")
      f.write(csvContent)
    print(f'CSV file {filename} has been created with {len(titles)} titles')
  except:
    print(titles)
    print('Failed to write to file')


matcher = re.compile(r'\[[^\]]*\]', re.MULTILINE)
for i in range(300):
  category = categories[i % numPrompts]
  prompt = prompts[i % numPrompts]
  # print('prompt: ', prompt)
  output = ollama.chat(
    model="gemma2:2b",
    messages=[{ 'role': 'user', 'content': prompt }],
    format="json",
  )

  titles = []

  # print(output['message']['content'])

  jsonArrayMatch = re.search(r'\[[^\]]*\]', output['message']['content'], re.MULTILINE)
  if (jsonArrayMatch):
    try:
      titles = json.loads(jsonArrayMatch.group())
      # print(titles)
    except Exception as error:
      print('Failed to parse JSON array from response:', error)

    allTitles += zip(titles, [category] * len(titles))
  else:
    print('No JSON match')

  print(f'Generated {len(allTitles)} article titles')
  
  if (len(allTitles) > 3000):
    break

# print(allTitles)

saveToCSV(allTitles)