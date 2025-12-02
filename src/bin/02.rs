advent_of_code::solution!(2);

pub fn part_one(input: &str) -> Option<u64> {
    let mut sum: u64 = 0;
    let id_ranges: Vec<&str> = input.split(',').collect();
    for id_range in id_ranges {
        let range: Vec<&str> = id_range.split('-').collect();
        //println!("{:?}", range);
        let lower_bound = range[0].trim().parse::<u64>().unwrap();
        let upper_bound = range[1].trim().parse::<u64>().unwrap();
        for i in lower_bound..upper_bound+1 {
            if invalid_id(i) {
                //println!("{}", i);
                sum += i;
            }
        }
    }

    Some(sum)
}

pub fn part_two(input: &str) -> Option<u64> {
    let mut sum: u64 = 0;
    let id_ranges: Vec<&str> = input.split(',').collect();
    for id_range in id_ranges {
        let range: Vec<&str> = id_range.split('-').collect();
        //println!("{:?}", range);
        let lower_bound = range[0].trim().parse::<u64>().unwrap();
        let upper_bound = range[1].trim().parse::<u64>().unwrap();
        for i in lower_bound..upper_bound+1 {
            if invalid_id_pt2(i) {
                //println!("{}", i);
                sum += i;
            }
        }
    }

    Some(sum)
}

fn invalid_id(id: u64) -> bool {
    let s: Vec<char> = id.to_string().chars().collect();
    // odd digits
    if s.len() % 2 != 0 {
        return false;
    }

    for i in 0..s.len()/2 {
        if s[i] != s[i+s.len()/2] {
            return false;
        }
    }

    return true;
}

fn invalid_id_pt2(id: u64) -> bool {
    let s: String = id.to_string();
    if s.len() == 1 {
        return false;
    }

    // repeated substring trick - but search from offset of 1. concat string with itself so it's
    // easier to search
    let dup_s = [s.clone(), s.clone()].concat();
    let index: Option<usize> = dup_s[1..].find(&s).map(|i| i + 1);
    match index {
        Some(i) => {
            return i < s.len();
        },
        None => {
            return false;
        },
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_part_one() {
        let result = part_one(&advent_of_code::template::read_file("examples", DAY));
        assert_eq!(result, Some(1227775554));
    }

    #[test]
    fn test_part_two() {
        let result = part_two(&advent_of_code::template::read_file("examples", DAY));
        assert_eq!(result, Some(4174379265));
    }
}
