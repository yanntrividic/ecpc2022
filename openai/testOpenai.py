import openai
import openaiSetup

# list engines
engines = openai.Engine.list()

# print the first engine's id
#print(engines.data[0].id)

prompt = "Continue the following sentence and make it a paragraph: Eh da wont bethere wadoo..."

# # create a completion
# completion_ada = openai.Completion.create(engine="ada", prompt="Génère-moi de la glossolalie.")
# completion_curie = openai.Completion.create(engine="curie", prompt="Génère-moi de la glossolalie.")
# completion_babbage = openai.Completion.create(engine="babbage", prompt="Génère-moi de la glossolalie.")
# completion_davinci = openai.Completion.create(engine="davinci", prompt="Generate some topline.")
# instruct_davinci = openai.Completion.create(engine="davinci-instruct-beta", prompt=prompt)
instruct_curie = openai.Completion.create(engine="curie-instruct-beta", prompt=prompt)


# # print the completion
# print("completion_ada:", completion_ada.choices[0].text)
# print("completion_curie:", completion_curie.choices[0].text)
# print("completion_babbage:", completion_babbage.choices[0].text)
#print("instruct_davinci:", instruct_davinci.choices[0].text)
print("instruct_curie:", instruct_curie.choices[0].text)