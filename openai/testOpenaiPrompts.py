import openai
openai.api_key = "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"
completion = openai.Completion.create(
  engine="curie",
  n=1,
  max_tokens=30,
  stop=["\n"],
  prompt="mccrae said though is tied boom it's so good debate it and they say that guy is a crate if we can beat i kind",
  temperature=0.1,
  top_p=1,
  presence_penalty=0,
  frequency_penalty=0,
  echo=True,
)

choice = completion["choices"][0]
print("[choice object]", choice)
print("[choice text]", choice.text)

