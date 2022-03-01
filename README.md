### Welcome to the Sprookjesgenerator (nl)

Fairy Tale generator in the Dutch language (*)

'SprookjesGenerator' (Dutch) is a Fairytale generator. In a way it's my attempt to learn the python language and also to understand ML. At it's core it can be used as a 'copilot' for writing stories within the classical fairytale genre. It's goal is it to create meaningfull stories that can be used as a source and inspiration for writing.

Now it's possible to create generated female male and citynames run main.py for more explanations

Basically i have a lot of issues with this program. Started too soon and in hindsight looks like it's better to make Some adjustments. for now i put hte project on ice. focus is on 'Taaldoos' which is a set of tools that can manipulate dutch sentences.

the idea is it to generate sentences in a limited contex like for instance :

man walk street man falls grond woman climbs tree etc...

Al these sentences are true and with a space of for instance 10^3 possibilities 10 verbs and 10 nouns it's very limited. phase 2 is it to train an Ai... after that recurring on a greater set with more nouns and verbs. However al nouns and in a certain sense verbs are low abstract.

for instance 'The Idea' is a noun but the abstractness is too great for the set.

phase 3 will incorporate more abstract nouns and prepositions. The whole system is orientated on the Dutch language (because of reasons). And also it seems to me that LSTM networks preform better when context given is more accurate than just plugging characters. I expect that training takes less time if input is more organized in the above described. However this also needs more supervision. Eventually the system must be able to write stories with a limited context than make completely sense. (;)

Ray Koster