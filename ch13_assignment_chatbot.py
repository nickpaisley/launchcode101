class Chatbot:
    """ An object that can engage in rudimentary conversation with a human. """

    def __init__(self, name,):
        self.name = name
        self.bored = False

    def greeting(self):
        """ Returns the Chatbot's way of introducing itself. """
        return "Hello, my name is " + self.name

    def response(self, prompt_from_human):
        """ Returns the Chatbot's response to something the human said. """
        return "It is very interesting that you say: '" + prompt_from_human + "'"


# TODO define a class called BoredChatbot
#A bored chatbot has a short attention span. 
# When the human says something that is longer than 20 characters, 
# it should respond by saying: “zzz... Oh excuse me, I dozed off reading your essay.”

class BoredChatbot(Chatbot):

    def response(self, prompt_from_human):
        if len(prompt_from_human) > 20:
            return "zzz... Oh excuse me, I dozed off reading your essay."
        else:
            return "It is very interesting that you say: '" + prompt_from_human + "'"


#make a chatbot
sally = BoredChatbot("Sally")
#introduce the chatbot and allow the user to say something. 
human_message = "testlskdfslkdfjsldkfjsldkfjsldkfj"
#respond to the user
print(sally.response(human_message))
