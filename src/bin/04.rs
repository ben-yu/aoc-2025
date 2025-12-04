advent_of_code::solution!(4);

pub fn part_one(input: &str) -> Option<u64> {

    let grid: Vec<Vec<char>> = input.lines()
        .map(|line| line.chars().collect())
        .collect();

    let adj_pos: Vec<(isize, isize)> = vec![(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)];

    let mut accessible_rolls = 0;

    for (r, row) in grid.iter().enumerate() {
        for (c, &cell) in row.iter().enumerate() {
            if cell == '@' {
                let mut adj_rolls = 0;
                for (dr, dc) in &adj_pos {
                    let next = (r.checked_add_signed(*dr), c.checked_add_signed(*dc));

                    match (next.0, next.1) {
                        (Some(x), Some(y)) => {
                            if x < grid.len() && y < grid[0].len() {
                                if grid[x][y] == '@' {
                                    adj_rolls += 1;
                                }
                            }
                        },
                        (None, _) => (),
                        (_, None) => (),
                    }
                }

                if adj_rolls < 4 {
                    accessible_rolls += 1;
                }
            }
        }
    }

    Some(accessible_rolls)
}

pub fn part_two(input: &str) -> Option<u64> {
    let mut grid: Vec<Vec<char>> = input.lines()
        .map(|line| line.chars().collect())
        .collect();

    let adj_pos: Vec<(isize, isize)> = vec![(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)];

    let mut removed_rolls = 0;

    loop {
        let mut remove_positions : Vec<(usize, usize)> = Vec::new();
        for (r, row) in grid.iter().enumerate() {
            for (c, &cell) in row.iter().enumerate() {
                if cell == '@' {
                    let mut adj_rolls = 0;
                    for (dr, dc) in &adj_pos {
                        let next = (r.checked_add_signed(*dr), c.checked_add_signed(*dc));

                        match (next.0, next.1) {
                            (Some(x), Some(y)) => {
                                if x < grid.len() && y < grid[0].len() {
                                    if grid[x][y] == '@' {
                                        adj_rolls += 1;
                                    }
                                }
                            },
                            (None, _) => (),
                            (_, None) => (),
                        }
                    }

                    if adj_rolls < 4 {
                        remove_positions.push((r,c));
                        removed_rolls += 1;
                    }
                }
            }
        }

        // mark positions as removed
        for pos in &remove_positions {
            grid[pos.0][pos.1] = 'x';
        }

        if remove_positions.is_empty() {
            break;
        }
    }

    Some(removed_rolls)
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_part_one() {
        let result = part_one(&advent_of_code::template::read_file("examples", DAY));
        assert_eq!(result, Some(13));
    }

    #[test]
    fn test_part_two() {
        let result = part_two(&advent_of_code::template::read_file("examples", DAY));
        assert_eq!(result, Some(43));
    }
}
