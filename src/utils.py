import sys
import re

def graceful_shutdown(signal_num, frame):
    print("\nПолучен сигнал завершения, программа корректно завершится...")
    sys.exit(0)

def validate_link(link):
    regexp = re.compile(r"^https://www\.flashscorekz\.com/match/[A-Za-z0-9]+/#/match-summary$")

    if regexp.match(link):
        return True
    else:
        return False