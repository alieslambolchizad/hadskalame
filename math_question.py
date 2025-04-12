import random
import threading
import time
from inputimeout import inputimeout, TimeoutOccurred

score = 0
question_count = 0
op = ['+', '-', '*']

def countdown(seconds, stop_event):
    for i in range(seconds, 0, -1):
        if stop_event.is_set():
            return
        print(f"\r⏳ {i} seconds left... ", end="")
        time.sleep(1)
    if not stop_event.is_set():
        print("\r⏰ Time's up! ")

while question_count < 5:
    num1 = random.randint(1, 9)
    num2 = random.randint(1, 9)
    select_op = random.choice(op)
    print(f'\n{num1} {select_op} {num2} = ?')

    if select_op == '+':
        result = num1 + num2
    elif select_op == '-':
        result = num1 - num2
    else:
        result = num1 * num2

    stop_event = threading.Event()
    timer_thread = threading.Thread(target=countdown, args=(30, stop_event))
    timer_thread.start()

    try:
        user_input = inputimeout(prompt='\nEnter your answer: ', timeout=30)
        stop_event.set()
        user_choice = int(user_input)
        if user_choice == result:
            print("✅ Correct!")
            score += 1
        else:
            print(f"❌ Wrong! Correct answer: {result}")
            if score > 0:
                score -= 1

    except TimeoutOccurred:
        print("\n🚫 Time is up and no answer was given.")
        if score > 0:
            score -= 1
    except ValueError:
        print("⛔ Invalid input!")

    question_count += 1
    timer_thread.join()

print(f"\n🎯 Quiz finished! Your final score: {score}")