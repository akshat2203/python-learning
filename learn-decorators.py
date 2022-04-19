from datetime import datetime


def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")

    return wrapper


def say_whee():
    print("Whee!")


say_whee = my_decorator(say_whee)
say_whee()


# todo : improve for advance level
def log_datetime(func):
    """Log the date and time of a function"""

    def wrapper():
        print(f'Function: {func.__name__}\nRun on: {datetime.today().strftime("%Y-%m-%d %H:%M:%S")}')
        print(f'{"-" * 30}')
        func()

    return wrapper


@log_datetime
def daily_backup():
    print('Daily backup job has finished.')


daily_backup()
