# %%
### Merge and Map Chess Openings

# Import libraries
import pandas as pd
from io import StringIO


# %%
#tsv data
a=pd.read_csv('a.tsv', sep='\t')
b=pd.read_csv('b.tsv', sep='\t')
c=pd.read_csv('c.tsv', sep='\t')
d=pd.read_csv('d.tsv', sep='\t')
e=pd.read_csv('e.tsv', sep='\t')

tsv_data= a,b,c,d,e

merged_df = pd.concat(tsv_data, ignore_index=True)

# %%
merged_df.head()

# %%


opening_moves = merged_df

def split_pgn_to_columns(df, pgn_column='pgn'):
    max_plies = 0
    split_data = []
    plies_list = []

    # Split each PGN into individual plies and find the maximum number of plies
    for pgn in df[pgn_column]:
        moves = [move for move in pgn.split() if not move.endswith('.')]
        split_data.append(moves)
        plies_list.append(" ".join(moves))  # Join moves into a single string for 'plies' column
        max_plies = max(max_plies, len(moves))
    
    # Add 'plies' column to the DataFrame
    df['plies'] = plies_list

    # Create new columns for each ply
    columns = {f'Move_ply_{i+1}': [] for i in range(max_plies)}

    # Assign moves to corresponding columns
    for moves in split_data:
        for i in range(max_plies):
            if i < len(moves):
                columns[f'Move_ply_{i+1}'].append(moves[i])
            else:
                columns[f'Move_ply_{i+1}'].append(None)
    
    # Add new columns to the DataFrame
    for col_name, col_values in columns.items():
        df[col_name] = col_values

    return df

# Apply the function
opening_moves = split_pgn_to_columns(opening_moves)

print(opening_moves.head())


# %%
print(opening_moves['plies'])

# %%
class TrieNode:
    def __init__(self):
        self.children = {}
        self.opening_name = None

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, moves, opening_name):
        node = self.root
        for move in moves:
            if move not in node.children:
                node.children[move] = TrieNode()
            node = node.children[move]
        node.opening_name = opening_name
    
    def search(self, moves):
        node = self.root
        last_opening_name = None
        for move in moves:
            if move in node.children:
                node = node.children[move]
                if node.opening_name:
                    last_opening_name = node.opening_name
            else:
                break
        return last_opening_name

# %%
trie = Trie()
for index, row in opening_moves.iterrows():
    opening = row['name']
    plies = row['plies'].split()
    trie.insert(plies, opening)

# %%
game_data = pd.read_csv('C:\\Users\\clancyam\\OneDrive - University of South Australia\\2024\\SP4\\Capstone Project\\Code\\Mapping Openings\\chessdata.csv')

# %%
game_data = pd.DataFrame(game_data)

# %%
# Select the first 36 move columns as the largest opening definition consists of 18 moves
move_columns = [f'Move_ply_{i+1}' for i in range(36)]
selected_moves_df = game_data[move_columns].copy()

# Concatenate moves into a single sequence for each game
def create_move_sequence(row):
    moves = row.dropna().tolist()  # Drop NaN values and convert to list
    return ' '.join(moves)

selected_moves_df['move_sequence'] = selected_moves_df.apply(create_move_sequence, axis=1)

# Function to get the opening name from a sequence of moves
def get_opening_name(moves):
    return trie.search(moves.split())

# Apply the function to get the opening names
selected_moves_df['opening_name'] = selected_moves_df['move_sequence'].apply(get_opening_name)

# Print the DataFrame with the move sequences and identified openings
print(selected_moves_df[['move_sequence', 'opening_name']])
selected_moves_df['opening_name'] = selected_moves_df['move_sequence'].apply(get_opening_name)


# %%


# %%



