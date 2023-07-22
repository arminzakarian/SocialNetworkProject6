# CHAPTER 8
# CASCADING IN SOCIAL NETWORKS
# IMPORTIMG LIBRARIES
import random
# INITIALIZE GRAPH PARAMETERS
num_nodes = 10000
out_degree = 10
# INITIALIZE VOTER PREFERENCES
support_you = [0, 2, 4, 6]
support_rival = [1, 3, 5, 7]
undecided = [8, 9]
# CREATE AN ADJACENCY LIST
graph = {i: [] for i in range(num_nodes)}
for i in range(num_nodes):
    friends = random.sample(range(num_nodes), out_degree)  # Randomly select out_degree friends for each node
    graph[i] = friends
voter_preferences = {}
for node_id in range(num_nodes):
    last_digit = node_id % 10
    if last_digit in support_you:
        voter_preferences[node_id] = 'You'
    elif last_digit in support_rival:
        voter_preferences[node_id] = 'Rival'
    else:
        voter_preferences[node_id] = 'Undecided'
# Determine initial support for each candidate
support_you_count = sum(1 for pref in voter_preferences.values() if pref == 'You')
support_rival_count = sum(1 for pref in voter_preferences.values() if pref == 'Rival')
undecided_count = num_nodes - support_you_count - support_rival_count
print("Initial support:")
print("You:", support_you_count)
print("Rival:", support_rival_count)
print("Undecided:", undecided_count)
# Simulate the live stream and persuade voters within the range 3000-3099
funding = 9000
cost_per_10_voters = 1000
voters_to_persuade = min(funding // cost_per_10_voters, 10)  # Calculate the number of voters to persuade based on available funding
persuaded_voters = set(range(3000, 3000 + voters_to_persuade * 10))
for voter_id in persuaded_voters:
    voter_preferences[voter_id] = 'You'
# Determine updated support after the live stream
support_you_count = sum(1 for pref in voter_preferences.values() if pref == 'You')
support_rival_count = sum(1 for pref in voter_preferences.values() if pref == 'Rival')
print("\nSupport after the live stream:")
print("You:", support_you_count)
print("Rival:", support_rival_count)
# Simulate the decision-making process for 10 days (10 iterations)
for iteration in range(10):
    updates = {}  # Store the updates for the current iteration
    for node_id in range(num_nodes):
        if voter_preferences[node_id] == 'Undecided':
            support_you_friends = 0
            support_rival_friends = 0

            # Count the number of friends supporting each candidate
            for friend_id in graph[node_id]:
                friend_preference = voter_preferences[friend_id]
                if friend_preference == 'You':
                    support_you_friends += 1
                elif friend_preference == 'Rival':
                    support_rival_friends += 1

            # Update the voter's preference based on the majority support among friends
            if support_you_friends > support_rival_friends:
                updates[node_id] = 'You'
            elif support_rival_friends > support_you_friends:
                updates[node_id] = 'Rival'
            else:
                # When there is a tie, assign support alternately
                if iteration % 2 == 0:
                    updates[node_id] = 'You'
                else:
                    updates[node_id] = 'Rival'

    # Apply the updates simultaneously
    for node_id, preference in updates.items():
        voter_preferences[node_id] = preference

# Count the final number of supporters for each candidate
support_you_count = sum(1 for pref in voter_preferences.values() if pref == 'You')
support_rival_count = sum(1 for pref in voter_preferences.values() if pref == 'Rival')
print("\nFinal support before the election:")
print("You:", support_you_count)
print("Rival:", support_rival_count)
# Simulate the election day (11th day)
votes_you = support_you_count + len(persuaded_voters)
votes_rival = support_rival_count
print("\nElection Results:")
print("Votes for You:", votes_you)
print("Votes for Rival:", votes_rival)
margin_of_victory = abs(votes_you - votes_rival)
if votes_you > votes_rival:
    print("\nCongratulations! You win the election by", margin_of_victory, "votes.")
elif votes_rival > votes_you:
    print("\nUnfortunately, your rival wins the election by", margin_of_victory, "votes.")
else:
    print("\nThe election results in a tie.")
print("Problem 52 Results by Armin Zakarian")