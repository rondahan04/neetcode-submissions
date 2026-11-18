class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        columns = defaultdict(set)
        boxes = defaultdict(set)
        for row in range(9):
            for column in range(9):
                current_number = board[row][column]
                if current_number == ".":
                    continue
                box_num = (row // 3) * 3 + (column // 3)
                if (
                    current_number in rows[row]
                    or current_number in columns[column]
                    or current_number in boxes[box_num]
                ):  # if already appears somwhere
                    return False
                # reached here need to add it to the set thats a new number
                rows[row].add(current_number)
                columns[column].add(current_number)
                boxes[box_num].add(current_number)

        return True
