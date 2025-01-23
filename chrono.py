import threading


def start_global_timer(limit):
    """Lance un timer global pour le test."""
    global time_expired
    time_expired = False

    def timer_function():
        global time_expired
        time_expired = True
        print("\nTemps total écoulé ! Le test est terminé.")

    timer = threading.Timer(limit, timer_function)
    timer.start()
    return timer


def time_limit(prompt, limit):
    """Obtenir une réponse dans un délai donné."""
    timer = threading.Timer(limit, print, args=["\nTemps écoulé pour cette question!"])
    timer.start()
    try:
        answer = input(prompt)
    except:
        answer = None
    timer.cancel()
    return answer