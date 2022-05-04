import random

def magic_eight_ball():
    response = input("Welcome! I am your Magic 8 Ball. \n What is your question?\n(Type a YES or NO question for an answer or type 'quit' to exit)\n")
    list = ['It is certain', 'It is decidedly so', 'Without a doubt', 'Yes definitely', 'You may rely on it', 'As I see it, yes', 'Most likely', 'Outlook good', 'Yes', 'Signs point to yes', 'Reply hazy, try again', 'Ask me again later', 'Better not tell you now', 'Cannot predict now', 'Concentrate and ask again', 'Don\'t count on it', 'My reply is no', 'My sources say no', 'Outlook not so good', 'Very doubtful']

    
    if response == 'quit':
        print('Thanks for playing!')
    else:
        print(random.choice(list),'\n')
        magic_eight_ball()

magic_eight_ball()