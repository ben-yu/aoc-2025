advent_of_code::solution!(3);

pub fn part_one(input: &str) -> Option<u64> {
    let mut sum = 0;
    for line in input.lines() {
        let mut batteries :Vec<u32> = line.chars()
            .map(|c| c.to_digit(10).unwrap())
            .collect();
        let mut res = 0;
        // Find largest digit that isn't the last element
        if let Some((index, &max_value)) = batteries[..batteries.len()-1]
            .iter()
            .enumerate()
            .max_by(|(idx_a, val_a), (idx_b, val_b)| {
                // Compare values first
                match val_a.cmp(val_b) {
                    std::cmp::Ordering::Equal => idx_b.cmp(idx_a), // If values are equal, compare indices
                    other => other,                               // Otherwise, use the value comparison
                }
            })
        {
            //println!("Maximum element: {}", max_value);
            //println!("Index of maximum element: {}", index);
            let sub_slice = &batteries[index+1..];
            let next_max_value = sub_slice.iter().max().unwrap();
            res = max_value * 10 + next_max_value;
        }
        //println!("{}", res);
        sum += res;
    }

    Some(sum as u64)
}

pub fn part_two(input: &str) -> Option<u64> {
    let mut sum = 0;
    for line in input.lines() {
        let batteries :Vec<u32> = line.chars()
            .map(|c| c.to_digit(10).unwrap())
            .collect();
        let mut res = vec![];
        let mut last_index = 0;
        let mut sub_slice = &batteries[..];
        for i in (0..12).rev() {
            // Find largest digit that isn't in the last i elements
            let start_idx = last_index;
            let end_idx = batteries.len() - i;
            sub_slice = &batteries[start_idx..end_idx];
            //println!("{:?}", sub_slice);
            if let Some((index, max_value)) = sub_slice
                .iter()
                .enumerate()
                .max_by(|(idx_a, val_a), (idx_b, val_b)| {
                    // Compare values first
                    match val_a.cmp(val_b) {
                        std::cmp::Ordering::Equal => idx_b.cmp(idx_a), // If values are equal, compare indices
                        other => other,                               // Otherwise, use the value comparison
                    }
                })
            {
                // index is relative to the slice
                last_index = start_idx + index + 1;
                //println!("{}", last_index);
                res.push(max_value.to_string());
            }

        }
        println!("{:?}", res);
        sum += res.join("").parse::<u64>().unwrap();
    }

    Some(sum as u64)
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_part_one() {
        let result = part_one(&advent_of_code::template::read_file("examples", DAY));
        assert_eq!(result, Some(357));
    }

    #[test]
    fn test_part_one_real_input() {
        let result = part_one("2112332342532272232223275313233436223321233437135331262264123523352223532764132713226233262613423352\n");
        assert_eq!(result, Some(77));
    }

    #[test]
    fn test_part_two() {
        let result = part_two(&advent_of_code::template::read_file("examples", DAY));
        assert_eq!(result, Some(3121910778619));
    }
}
