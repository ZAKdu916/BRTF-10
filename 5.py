import time 

CODE_SECRET = "12345"

def brute_force():
    for i in range(100000):
        tentative = f"{i:05}"
        print(f"Essai : {tentative}", end="\r")
        time.sleep(0.01)
        if tentative == CODE_SECRET:
            print(f"\n✅ Code trouvé : {tentative}")
            break 

brute_force()
