import time 

CODE_SECRET = "1"

def brute_force():
    for i in range(10):
        tentative = f"{i:01}"
        print(f"Essai : {tentative}", end="\r")
        time.sleep(0.01)
        if tentative == CODE_SECRET:
            print(f"\n✅ Code trouvé : {tentative}")
            break 

brute_force()
