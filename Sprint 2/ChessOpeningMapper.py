import pandas as pd
import pytrie

import zipfile

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

    def create_trie(self, df, opening_column='name', moves_column='plies'):
        """
        Create a Trie structure from the DataFrame using pytrie.
        """
        self.trie = pytrie.StringTrie()
        for _, row in df.iterrows():
            self.trie[row[moves_column]] = row[opening_column]

    def map_opening_moves(self, moves_sequence):
        """
        Map the opening moves of a game to an opening name using pytrie.
        """
        if self.trie is None:
            raise ValueError("Trie has not been created. Call create_trie() first.")
        
        moves = ' '.join([move for move in moves_sequence.split() if not move.endswith('.')])
        try:
            # Find the longest prefix that matches the moves
            return self.trie.longest_prefix_value(moves, default="Unknown Opening")
        except KeyError:
            return "Unknown Opening"

    
    def process_game_data(self, game_data, max_plies=36):
        move_columns = [f'Move_ply_{i+1}' for i in range(max_plies)]
        selected_moves_df = game_data[move_columns].copy()

        def create_move_sequence(row):
            moves = row.dropna().tolist()  # Drop NaN values and convert to list
            return ' '.join(moves)

        selected_moves_df['move_sequence'] = selected_moves_df.apply(create_move_sequence, axis=1)
        return selected_moves_df

    def get_opening_name_from_game(self, game_data):
        selected_moves_df = self.process_game_data(game_data)
        selected_moves_df['opening_name'] = selected_moves_df['move_sequence'].apply(self.map_opening_moves)
        return selected_moves_df
    
    @staticmethod
    def load_openings():

        file_list = ['..\\Chess Pattern Recognition\\a.tsv', '..\\Chess Pattern Recognition\\b.tsv', '...\\Chess Pattern Recognition\\c.tsv','.\\Chess Pattern Recognition\\d.tsv', '..\\Chess Pattern Recognition\\e.tsv']
        mapper = ChessOpeningMapper()
        merged_df = mapper.merge_tsv_files(file_list)
        return mapper.split_pgn_to_columns(merged_df)
    
    @staticmethod
    def unzip_game_data(zip_path, extract_to='.'):
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(extract_to)

    @staticmethod
    def load_game_data( zip_path, extracted_file_name):
        game_data = pd.read_csv(extracted_file_name)
        return game_data

#Example usage of the class
if __name__ == "__main__":
    # Create an instance of the ChessOpeningMapper
    mapper = ChessOpeningMapper()
    
    # Load opening moves and create Trie
    opening_moves = ChessOpeningMapper.load_openings()
    print(opening_moves.head())
    print(opening_moves.columns)
    mapper.create_trie(opening_moves)

    # Path to the zipped game data file
    game_data_zip_path = 'Chess Pattern Recognition\\chessdata.zip'
    extracted_file_name = 'chessdata.csv'  # The CSV file within the zip

    # Unzip the game data
    ChessOpeningMapper.unzip_game_data(zip_path=game_data_zip_path)

    # Load the game data from the extracted CSV file
    game_data = ChessOpeningMapper.load_game_data(zip_path=game_data_zip_path,extracted_file_name=extracted_file_name)

    # Get opening names from the game data
    result_df = mapper.get_opening_name_from_game(game_data)
    print(result_df.head())