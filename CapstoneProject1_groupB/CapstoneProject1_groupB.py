import time

# Define a function to sort high scores
def scoreSort(entry):
    return entry["score"]

# High Scores
highScores = [
    {"score": 180, "Name": "Billy"},
    {"score": 90, "Name": "Tommy"},
    {"score": 150, "Name": "Ronny"},
    {"score": 60, "Name": "Timmy"},
    {"score": 80, "Name": "Jimmy"}
]

# Sort high scores
highScores = sorted(highScores, key=scoreSort)

# Define Quiz Questions & Answers
quizQs = [
    # Question 1
    {
        "question": "What year was the Premier League founded?\nA: 1992 B: 1985\n",
        "answer": "A",
        "questionMed": "C: 1993 D: 1999\n",
        "questionHard": "E: 2005 F: 1995\n"
    },
    # Question 2
    {
        "question": "Who has won the most Premier League titles?\nA: Chelsea B: Manchester United\n",
        "answer": "B",
        "questionMed": "C: Liverpool D: Manchester City\n",
        "questionHard": "E: Arsenal F: Chelsea\n"
    },
    # Question 3
    {
        "question": "Who holds the record for most Premier League hat-tricks?\nA: Alan Shearer B: Wayne Rooney\n",
        "answer": "A",
        "questionMed": "C: Erling Haaland D: Didier Drogba\n",
        "questionHard": "E: Harry Kane F: Thierry Henry\n"
    },
    # Question 4
    {
        "question": "Who holds the record for most Premier League wins as a manager?\nA: Jose Mourinho B: Sir Alex Ferguson\n",
        "answer": "B",
        "questionMed": "C: Pep Guardiola D: Harry Redknapp\n",
        "questionHard": "E: Arsene Wenger F: Jurgen Klopp\n"
    },
    # Question 5
    {
        "question": "Who holds the record for most Premier League red cards?\nA: Patrick Vieira B: Roy Keane\n",
        "answer": "A",
        "questionMed": "C: Duncan Ferguson D: Joey Barton\n",
        "questionHard": "E: John Terry F: Vinnie Jones\n"
    },
    # Question 6
    {
        "question": "What is the highest number of goals scored by a single player in a Premier League season?\nA: 31 B: 34\n",
        "answer": "B",
        "questionMed": "C: 29 D: 36\n",
        "questionHard": "E: 28 F: 38\n"
    },
    # Question 7
    {
        "question": "Which team has conceded the fewest goals in a single Premier League season?\nA: Chelsea B: Manchester City\n",
        "answer": "A",
        "questionMed": "C: Liverpool D: Arsenal\n",
        "questionHard": "E: Manchester United F: Tottenham Hotspur\n"
    },
    # Question 8
    {
        "question": "Who has scored the fastest hat-trick in Premier League history?\nA: Sadio Mane B: Robbie Fowler\n",
        "answer": "B",
        "questionMed": "C: Luis Suarez D: Thierry Henry\n",
        "questionHard": "E: Sergio Aguero F: Michael Owen\n"
    },
    # Question 9
    {
        "question": "Which team won the first Premier League title?\nA: Manchester United B: Arsenal\n",
        "answer": "A",
        "questionMed": "C: Blackburn Rovers D: Chelsea\n",
        "questionHard": "E: Liverpool F: Leeds United\n"
    },
    # Question 10
    {
        "question": "Who is the youngest goalscorer in Premier League history?\nA: James Vaughan B: Michael Owen\n",
        "answer": "A",
        "questionMed": "C: Wayne Rooney D: Raheem Sterling\n",
        "questionHard": "E: Federico Macheda F: Francis Jeffers\n"
    },
    # Question 11
    {
        "question": "Which team has won the most consecutive Premier League matches?\nA: Manchester City B: Liverpool\n",
        "answer": "B",
        "questionMed": "C: Chelsea D: Manchester United\n",
        "questionHard": "E: Arsenal F: Tottenham Hotspur\n"
    },
    # Question 12
    {
        "question": "Who is the oldest player to score in the Premier League?\nA: Teddy Sheringham B: Ryan Giggs\n",
        "answer": "A",
        "questionMed": "C: Alan Shearer D: David Beckham\n",
        "questionHard": "E: Zlatan Ibrahimovic F: Paolo Maldini\n"
    },
    # Question 13
    {
        "question": "Which player has the most appearances in the Premier League?\nA: Gareth Barry B: Ryan Giggs\n",
        "answer": "A",
        "questionMed": "C: Frank Lampard D: Steven Gerrard\n",
        "questionHard": "E: John Terry F: Paul Scholes\n"
    },
    # Question 14
    {
        "question": "Who has won the Premier League Golden Boot the most times?\nA: Thierry Henry B: Alan Shearer\n",
        "answer": "B",
        "questionMed": "C: Cristiano Ronaldo D: Harry Kane\n",
        "questionHard": "E: Sergio Aguero F: Luis Suarez\n"
    },
    # Question 15
    {
        "question": "Which goalkeeper has kept the most clean sheets in Premier League history?\nA: Petr Cech B: David De Gea\n",
        "answer": "A",
        "questionMed": "C: Edwin van der Sar D: Joe Hart\n",
        "questionHard": "E: Thibaut Courtois F: Alisson Becker\n"
    },
    # Question 16
    {
        "question": "Who is the only player to have scored a hat-trick in the Premier League, FA Cup, and UEFA Champions League final?\nA: Lionel Messi B: Cristiano Ronaldo\n",
        "answer": "B",
        "questionMed": "C: Robert Lewandowski D: Neymar\n",
        "questionHard": "E: Luis Suarez F: Fernando Torres\n"
    },
    # Question 17
    {
        "question": "Which player has the most assists in a single Premier League season?\nA: Kevin De Bruyne B: Thierry Henry\n",
        "answer": "A",
        "questionMed": "C: Mesut Ozil D: Cesc Fabregas\n",
        "questionHard": "E: David Silva F: Ryan Giggs\n"
    },
    # Question 18
    {
        "question": "Who is the youngest manager to win the Premier League?\nA: Andre Villas-Boas B: Jose Mourinho\n",
        "answer": "B",
        "questionMed": "C: Pep Guardiola D: Jurgen Klopp\n",
        "questionHard": "E: Antonio Conte F: Roberto Mancini\n"
    },
    # Question 19
    {
        "question": "Which team has won the most FA Cup titles?\nA: Manchester United B: Arsenal\n",
        "answer": "B",
        "questionMed": "C: Chelsea D: Liverpool\n",
        "questionHard": "E: Tottenham Hotspur F: Everton\n"
    },
    # Question 20
    {
        "question": "Who is the only player to have scored in every minute of a Premier League match?\nA: Sergio Aguero B: Jamie Vardy\n",
        "answer": "A",
        "questionMed": "C: Harry Kane D: Mohamed Salah\n",
        "questionHard": "E: Thierry Henry F: Alan Shearer\n"
    },
]

# Welcome Message
print("Welcome to Capstone Quiz Master, the ultimate quiz game that will test your knowledge!\n"
      "With 20 questions of varying difficulty, this game is designed for players of all backgrounds.\n"
      "There are three difficulty ratings: Easy, Medium, and Hard. Each question has a point value: Easy (5 points), "
      "Medium (8 points), and Hard (10 points).\n"
      "To answer a question please type the Letter next to the answer. E.g. if the answer was C: 200 then type 'C'.\n"
      "Think you can conquer Capstone Quiz Master? Gather your friends, family, or fellow trivia enthusiasts and let the challenge begin!\n"
      "Show off your knowledge, aim for high scores, and become the ultimate quiz master!\n")

# Play again status
playAgain = "yes"

# While loop for the quiz
while playAgain.lower() == "yes":
    userName = input("Please enter your name: ")
    userDifficulty = input("Please enter your difficulty: Easy, Medium or Hard ")

    correctAnswers = 0
    playerScore = 0

    # Loop through the questions
    for i in range(20):
        if userDifficulty.lower() == "easy":
            answer = input("\n" + quizQs[i]["question"])
        elif userDifficulty.lower() == "medium":
            answer = input("\n" + quizQs[i]["question"] + quizQs[i]["questionMed"])
        elif userDifficulty.lower() == "hard":
            answer = input("\n" + quizQs[i]["question"] + quizQs[i]["questionMed"] + quizQs[i]["questionHard"])

        start_time = time.time()  # Start the timer
        elapsed_time = 0

        while elapsed_time < 30:  # 30 seconds timer
            elapsed_time = time.time() - start_time
            if elapsed_time >= 30:
                print("\nTime's up!\n")
                break

        if elapsed_time < 30:  # If time hasn't run out
            if answer.lower() == quizQs[i]["answer"].lower():
                print("\nCongratulations that is correct!\n")
                correctAnswers += 1
                if userDifficulty.lower() == "easy":
                    playerScore += 5
                elif userDifficulty.lower() == "medium":
                    playerScore += 8
                elif userDifficulty.lower() == "hard":
                    playerScore += 10
            else:
                print("\nThat is incorrect!\n")

    # Display score and leaderboard
    print(f"You scored {correctAnswers} out of 20.\n")

    if playerScore > highScores[0]["score"]:
        print("Congratulations you made it onto the Leaderboard!\n")
        highScores[0]["Name"] = userName
        highScores[0]["score"] = playerScore
        highScores = sorted(highScores, key=scoreSort)

    print("LeaderBoard:")
    for i, score in enumerate(highScores[::-1]):
        print(f"{i+1} Place = {score['Name']}: {score['score']}")

    # Ask if the player wants to play again
    playAgain = input("\nWould you like to play again? (Yes or No): ")

# Thank you message
if playAgain.upper() == "NO":
    print("\nThank you for Playing!")



