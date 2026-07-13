# 🛂 Access Control Scanner Challenge
#
# 1. Create a set of revoked badge numbers.
# 2. Create two empty lists: "approved" and "denied".
# 3. Start a loop to collect visitor info:
#    - Ask for the visitor's name (or type "done" to finish).
#    - If the name is "done", exit the loop.
#    - Otherwise, ask for their badge number.
#    - Check if the badge is revoked:
#        • If revoked: add the name to "denied" and display "ACCESS DENIED".
#        • If not: add the name to "approved" and display "ACCESS GRANTED".
# 4. Print the final "Access Summary" for "✅ Approved Visitors" & "⛔️ Denied Visitors":
#    - Sort both lists alphabetically.
#    - Display the total number of approved and denied visitors.

revoked_badges = {"X123", "B789", "Z999"}

approved = []
denied = []

while True:
    name = input("Please Enter the visitor's name (or type 'done' to finish).")

    if name.lower() == "done":
       break
    
    badge = input("Enter badge number: ").strip().upper()

    if badge in revoked_badges:
        denied.append(name)
        print(f"[ACCESS DENIED] {name} - Revoked badge")
    else:
        approved.append(name)
        print(f"[ACCESS GRANTED] {name}")

print("===== Access Summary =====")

print("✅ Approved Visitors:")
for person in sorted(approved):
  print(f" - {person}")

print("⛔️ Denied Visitors:")
for person in sorted(denied):
  print(f" - {person}")

print(f"Total Approved: {len(approved)}")
print(f"Total Denied: {len(denied)}")
