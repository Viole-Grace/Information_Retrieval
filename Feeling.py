from collections import OrderedDict as OD
import math
def get_emotion(s):
	s.lower()
	disgust=["revulsion", "repugnance", "aversion", "distaste", "abhorrence", "loathing", "detestation", "odium", "execration", "horror"]
	sad = ["unhappy", "sorrowful", "dejected", "regretful", "depressed", "downcast", "miserable", "downhearted", "down", "despondent", "despairing", "disconsolate", "out of sorts", "desolate", "bowed down", "wretched", "glum", "gloomy", "doleful", "dismal", "blue", "melancholy", "melancholic", "low-spirited", "mournful", "woeful", "woebegone", "forlorn", "crestfallen", "broken-hearted", "heartbroken", "inconsolable", "grief-stricken"]
	trust = ["confidence", "belief", "faith", "sureness", "certainty", "certitude", "assurance", "conviction", "credence", "reliance"]
	anger = ["annoyance", "vexation", "exasperation", "crossness", "irritation", "irritability", "indignation", "pique", "displeasure", "resentment", "rage", "fury", "wrath", "outrage", "temper", "road rage", "air rage", "irascibility", "ill temper", "dyspepsia", "spleen", "ill humour", "tetchiness", "testiness", "waspishness","aggravation", "ire", "choler", "bile"]
	surprise = ["shock","out of the blue", "thunderbolt", "bombshell", "revelation", "source of amazement", "rude awakening", "eye-opener", "shocker", "whammy"]
	anticipation = ["expectation", "prediction", "forecast", "prolepsis","expectancy", "hope", "hopefulness","excitement", "suspense"]
	fear = ["error", "fright", "fearfulness", "horror", "alarm", "panic", "agitation", "trepidation", "dread", "consternation", "dismay", "distress", "anxiety", "worry", "angst", "unease", "uneasiness", "apprehension", "apprehensiveness", "nervousness", "nerves", "timidity", "disquiet", "disquietude", "discomposure", "unrest", "perturbation", "foreboding", "misgiving", "doubt", "suspicion","the creeps", "the willies", "the heebie-jeebies", "the shakes", "the collywobbles", "jitteriness", "twitchiness", "butterflies" ,"funk", "blue funk", "worriment","inquietude"]

	if s in set(disgust):
		return "disgust", list(set(disgust))
	if s in set(sad):
		return "sad", list(set(sad))
	if s in set(trust):
		return "trust", list(set(trust))
	if s in set(anger):
		return "anger", list(set(anger))
	if s in set(surprise):
		return "surprise", list(set(surprise))
	if s in set(anticipation):
		return "anticipation", list(set(anticipation))
	if s in set(fear):
		return "fear", list(set(fear))