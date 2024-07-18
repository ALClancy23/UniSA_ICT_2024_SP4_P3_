import pandas as pd
import datrie

class ChessOpeningMapper:
    def __init__(self):
        self.trie = None

    def merge_tsv_files(self, file_list):
        """
        Merge multiple TSV files into a single DataFrame.
        """
        dataframes = [pd.read_csv(file, sep='\t') for file in file_list]
        merged_df = pd.concat(dataframes, ignore_index=True)
        return merged_df

    def split_pgn_to_columns(self, df, pgn_column='pgn'):
        """
        Split PGN into individual moves and create new columns for each ply.
        """
        max_plies = 0
        split_data = []

        for pgn in df[pgn_column]:
            moves = [move for move in pgn.split() if not move.endswith('.')]
            split_data.append(moves)
            max_plies = max(max_plies, len(moves))
        
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

        # Add a column for all plies concatenated
        df['plies'] = [' '.join(moves) for moves in split_data]

        return df

    def create_trie(self, df, opening_column='opening', moves_column='plies'):
        """
        Create a Trie structure from the DataFrame.
        """
        self.trie = datrie.Trie(ranges=[chr(i) for i in range(32, 127)])
        for _, row in df.iterrows():
            self.trie[row[moves_column]] = row[opening_column]

    def map_opening_moves(self, moves_sequence):
        """
        Map the opening moves of a game to an opening name.
        """
        if self.trie is None:
            raise ValueError("Trie has not been created. Call create_trie() first.")
        
        moves = ' '.join([move for move in moves_sequence.split() if not move.endswith('.')])
        opening_name = self.trie.longest_prefix(moves)
        return self.trie[opening_name] if opening_name in self.trie else None

#Example usage (uncomment to test)
if __name__ == "__main__":
    file_list = ['/a.tsv', '/b.tsv', '/c.tsv']  # Replace with your file paths
    mapper = ChessOpeningMapper()

    # Merge TSV files
    merged_df = mapper.merge_tsv_files(file_list)
    
    # Create the Trie structure
    merged_df = mapper.split_pgn_to_columns(merged_df)
    mapper.create_trie(merged_df)

    # Example moves sequence
    moves_sequence = "1. Nh3 d5 2. g3 e5 3. f4"
    
    # Map opening moves to opening name
    opening_name = mapper.map_opening_moves(moves_sequence)
    print(f"Opening Name: {opening_name}")
